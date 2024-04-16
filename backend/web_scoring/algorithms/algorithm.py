import re, json
import time

import numpy as np
import json
import pandas as pd
import pymysql


# 定义读取和处理HTML文件数据的函数
def read_data(path):
    with open(path, 'r', encoding='utf8', errors='ignore') as file:
        a = json.load(file)
        df =pd.DataFrame(a['data'])
    return df


def algorithm_process(file_list):
    # 初始化一个空的DataFrame
    df = pd.DataFrame()
    df['user_activity_score'] = 0  # 同样假设满分10分
    # 循环读取文件并合并到DataFrame
    for i in file_list:  # 替换为实际路径
        df1 = read_data(i)
        print(i, len(df1))
        df = pd.concat([df, df1], ignore_index=True)

    p1 = []
    for i in range(len(df['interactionAttr'])):  # 典表明页面访问期间信息
        p1.append({'interactionAttr_' + key: value for key, value in
                   pd.DataFrame(df['interactionAttr'][i]).loc['value', :].to_dict().items()})
    p2 = []
    for i in range(len(df['performanceAttr'])):  # 有关网页性能和用户交互的一些信息
        p2.append({'performanceAttr_' + key: value for key, value in
                   pd.DataFrame(df['performanceAttr'][i]).loc['value', :].to_dict().items()})
    p3 = []
    for i in range(len(df['pageAttr'])):  # 包含了有关用户访问网页的信息
        p3.append({'pageAttr_' + key: value for key, value in
                   pd.DataFrame(df['pageAttr'][i]).loc['value', :].to_dict().items()})
    df = pd.concat([df, pd.DataFrame(p1), pd.DataFrame(p2), pd.DataFrame(p3), ], axis=1, )
    df = df.sort_values('pageAttr_clientCreateTs').reset_index()
    df.drop('index', axis=1, inplace=True)
    from datetime import timedelta

    # 假设 df 已经正确加载和排序
    # 设置 'repeat_clicks' 和 'ptime'，以及初始分数
    df['ptime'] = pd.to_datetime(df['pageAttr'].apply(lambda x: x.get('clientCreateTs', {}).get('value', '2020-01-01')))
    df = df.sort_values('ptime')
    df['repeat_clicks'] = df['interactionAttr'].apply(
        lambda x: (x if isinstance(x, dict) else json.loads(x)).get('repeatClick', False))
    df['user_experience_score'] = 100

    # 设置冷却时间阈值
    cooldown_period = timedelta(seconds=2)  # 这里设置为2秒

    # 初始化上一个重复点击时间
    last_repeat_click_time = None

    # 逐行更新评分
    for index, row in df.iterrows():
        # 首先，确保行中相关字段不为空
        if pd.notnull(row['repeat_clicks']) and pd.notnull(row['ptime']):
            # 如果当前行是重复点击
            if row['repeat_clicks']:
                # 如果这是我们遇到的第一个重复点击，或者这次点击与上次重复点击的时间间隔小于冷却期
                if last_repeat_click_time is None or (row['ptime'] - last_repeat_click_time) <= cooldown_period:
                    # 减少分数，同时确保'user_experience_score'不为空
                    if pd.notnull(row['user_experience_score']):
                        df.at[index, 'user_experience_score'] = max(0, row['user_experience_score'] - 2)
                # 更新最后一次重复点击的时间
                last_repeat_click_time = row['ptime']
            else:
                # 如果当前行不是重复点击，重置上一个重复点击时间
                last_repeat_click_time = None
        else:
            # 如果'repeat_clicks'或'ptime'为空，则保持'user_experience_score'不变
            # 注意：您可以根据需要在这里设置默认得分，或者做其他处理
            df.at[index, 'user_experience_score'] = row.get('user_experience_score')

    # 计算跳出率和用户活跃度得分
    for index, row in df.iterrows():
        # 首先判断'interactionAttr'是否存在且可以解析
        if pd.notnull(row['interactionAttr']):
            interaction_data = json.loads(row['interactionAttr']) if isinstance(row['interactionAttr'], str) else row[
                'interactionAttr']

            # 确保相关字段存在且值为数值类型
            page_duration = interaction_data.get('pageDuration', {}).get('value', None)
            stay_time = interaction_data.get('stayTime', {}).get('value', None)
            page_active_duration = interaction_data.get('pageActiveDuration', {}).get('value', None)

            # 计算跳出率得分，确保page_duration是有效的数字
            if page_duration is not None and page_duration <= 10000:
                df.at[index, 'bounce_rate_score'] = 0  # 标记为跳出
            else:
                df.at[index, 'bounce_rate_score'] = 100  # 不是跳出，则保持满分

            # 计算用户活跃度得分，确保stay_time和page_active_duration是有效的数字
            if stay_time is not None and page_active_duration is not None and stay_time > 10000 and page_active_duration > 10000:
                df.at[index, 'user_activity_score'] = 100  # 用户活跃
            else:
                df.at[index, 'user_activity_score'] = 0  # 用户不活跃
        else:
            # 如果'interactionAttr'字段不存在或不可解析，则跳过这一行的得分计算
            df.at[index, 'bounce_rate_score'] = None  # 可以设为None或保持原值
            df.at[index, 'user_activity_score'] = None  # 可以设为None或保持原值

    # 计算页面加载速度
    for index, row in df.iterrows():
        # 确保'desc'字段非空
        if pd.notnull(row['desc']):
            desc = row['desc']
            if 'PerformanceGood' in desc:
                df.at[index, 'loading_speed_score'] = 100
            elif 'PerformanceNeedsImprovement' in desc:
                df.at[index, 'loading_speed_score'] = 50
            elif 'PerformancePoor' in desc:
                df.at[index, 'loading_speed_score'] = 0  # 修改: 应避免使用负分
            else:
                df.at[index, 'loading_speed_score'] = None  # 如果desc不包含已知的性能描述，则设置为None
        else:
            df.at[index, 'loading_speed_score'] = None  # 'desc'为空，得分未知

    # 根据反馈时间间隔计算得分的函数
    def calculate_feedback_score(feedbackInterval):
        # 确保feedback_interval是有效的数值
        if feedbackInterval is not None:
            if feedbackInterval < 100:
                return 100  # 少于100ms得满分
            elif 100 <= feedbackInterval <= 300:
                # 介于100ms到300ms之间，线性减分
                return round(100 - ((feedbackInterval - 100) / 200 * 100), 2)  # 分数线性减少
            else:
                return 0  # 大于300ms得0分
        else:
            return None  # feedback_interval为空，得分未知

    # 解析 performanceAttr 中的数据并计算网络反馈得分
    for index, row in df.iterrows():
        # 直接从DataFrame获取 'feedbackInterval' 的值
        feedbackInterval = row.get('feedbackInterval', None)  # 使用 .get 避免 KeyError
        # 计算并设置 'network_feedback_score'
        df.at[index, 'network_feedback_score'] = calculate_feedback_score(feedbackInterval)

    def calculate_fid_score(fid):
        # 确保fid是有效的数值
        if fid is not None:
            if fid < 100:
                return 100  # 小于100ms得满分
            elif 100 <= fid < 300:
                # 介于100ms到300ms之间，从100分线性减少到60分
                return round(100 - ((fid - 100) / (300 - 100) * 40), 2)  # 分数线性减少
            elif 300 <= fid < 500:
                # 介于300ms到500ms之间，从60分线性减少到0分
                return round((500 - fid) / (500 - 300) * 60, 2)
            else:
                return 0  # 大于等于500ms得0分
        else:
            return None  # fid为空，得分未知

    # 解析 performanceAttr 中的数据并计算首次输入延迟得分
    for index, row in df.iterrows():
        # 首先检查是否存在'interactionAttr'，并且可正确解析
        # 计算首次输入延迟得分
        for index, row in df.iterrows():
            if pd.notnull(row['performanceAttr_firstInputDelay']):
                # 直接使用列值，不需要再次解析JSON
                first_input_delay = row['performanceAttr_firstInputDelay']
                df.at[index, 'first_input_delay_score'] = calculate_fid_score(first_input_delay)
            else:
                # 如果数据不存在，则设为None
                df.at[index, 'first_input_delay_score'] = None

    # 初始化点击错误得分列，并计算
    # 假定我们已有点击错误计数的逻辑（您需要根据您的数据结构调整这一部分）
    for index, row in df.iterrows():
        # 假定错误计数保存在performanceAttr字段下的consoleErrors中
        if pd.notnull(row['performanceAttr']):
            performance_data = json.loads(row['performanceAttr']) if isinstance(row['performanceAttr'], str) else row[
                'performanceAttr']
            if 'consoleErrors' in performance_data and 'value' in performance_data['consoleErrors']:
                console_errors = performance_data['consoleErrors'].get('value', 0)  # 默认为0错误
                # 根据错误数量减分，每个错误扣5分
                df.at[index, 'click_error_score'] = max(0, 100 - console_errors * 5)
            else:
                df.at[index, 'click_error_score'] = 100  # 如果没有错误信息，默认满分
        else:
            df.at[index, 'click_error_score'] = 100  # 如果performanceAttr缺失或无效，也默认满分

    # 解析数据并计算点击错误得分
    for index, row in df.iterrows():
        # 初始化得分为None，以处理无效或缺失数据的情况
        df.at[index, 'click_error_score'] = None

        # 确保'eventName'和'performanceAttr'字段非空
        if pd.notnull(row['eventName']) and pd.notnull(row['performanceAttr']):
            # 解析eventName和performanceAttr
            event_name = row['eventName']
            performance_data = json.loads(row['performanceAttr']) if isinstance(row['performanceAttr'], str) else row[
                'performanceAttr']

            # 确保'consoleErrors'在performance_data中有效
            if 'consoleErrors' in performance_data:
                console_errors = performance_data.get('consoleErrors', {}).get('value', 0)

                # 如果事件名为ElementClick，根据consoleErrors数量计算得分
                if event_name == 'ElementClick':
                    # 出现一个错误扣五分，但确保不超过初始分数
                    score = max(0, 100 - console_errors * 5)
                    df.at[index, 'click_error_score'] = score
                else:
                    # 如果不是ElementClick事件，得满分
                    df.at[index, 'click_error_score'] = 100

    # 初始化页面加载报错得分列
    df['page_load_error_score'] = 100  # 默认满分

    # 解析数据并计算页面加载报错得分
    for index, row in df.iterrows():
        # 初始化得分为满分，以处理无效或缺失数据的情况
        df.at[index, 'page_load_error_score'] = 100  # 假设满分为100分

        # 确保'performanceAttr'字段非空并且包含所需的信息
        if pd.notnull(row['performanceAttr']):
            performance_data = json.loads(row['performanceAttr']) if isinstance(row['performanceAttr'], str) else row[
                'performanceAttr']

            # 确保'pageLoad'和'consoleErrors'字段在performance_data中有效
            if 'pageLoad' in performance_data and 'consoleErrors' in performance_data:
                page_load = performance_data.get('pageLoad', {}).get('value', None)
                console_errors = performance_data.get('consoleErrors', {}).get('value', None)

                # 如果pageload大于两秒，并且consoleErrors出现报错
                if page_load is not None and page_load > 2000 and console_errors is not None and console_errors > 0:
                    # 出现一个加载报错就扣五分，但确保不超过初始分数
                    deducted_score = min(5 * console_errors, 100)
                    df.at[index, 'page_load_error_score'] = max(0, 100 - deducted_score)

    # 初始化空白网页得分列
    df['blank_page_score'] = 100  # 默认满分

    # 解析数据并计算空白网页得分
    for index, row in df.iterrows():
        # 首先检查是否存在'interactionAttr'，并且可正确解析
        if pd.notnull(row['interactionAttr']):
            interaction_data = json.loads(row['interactionAttr']) if isinstance(row['interactionAttr'], str) else row[
                'interactionAttr']

            # 检查 'isBlank' 是否存在并且是 true 或 false
            if 'isBlank' in interaction_data:
                is_blank = interaction_data['isBlank'].get('value', False)

                # 判断页面是否为空白，如果是，则扣分
                if is_blank:
                    df.at[index, 'blank_page_score'] = max(0, 100 - 10)  # 出现空白页面扣十分
                else:
                    # 如果页面不是空白，则保持满分
                    df.at[index, 'blank_page_score'] = 100
            else:
                # 如果 'isBlank' 数据无效或不存在，则保留原有得分
                df.at[index, 'blank_page_score'] = None  # 可以设为None或保持原值
        else:
            df.at[index, 'blank_page_score'] = None  # 如果整个interactionAttr字段缺失或无效

    def calculate_total_and_average_scores(row, score_columns):
        valid_scores = [row[col] for col in score_columns if pd.notnull(row[col])]
        total_score = sum(valid_scores)
        average_score = total_score / len(valid_scores) if valid_scores else None
        return total_score, average_score

    # 更新得分列的列表，加入新的 blank_page_score
    score_columns = ['user_experience_score', 'bounce_rate_score', 'user_activity_score',
                     'loading_speed_score', 'network_feedback_score', 'first_input_delay_score',
                     'click_error_score', 'page_load_error_score', 'blank_page_score']

    # 对DataFrame的每一行应用更新后的总分和平均分计算逻辑
    for index, row in df.iterrows():
        total_score, average_score = calculate_total_and_average_scores(row, score_columns)
        df.at[index, 'total_score'] = total_score
        # 更新平均得分计算方法，避免除以零
        df.at[index, 'average_score'] = average_score if average_score is not None else None

    # 在所有得分计算完成后，将更新后的 DataFrame 保存到新的 CSV 文件中
    # output_file_path_updated = '/Users/diannao/Desktop/服务外包大赛/20240104151004_602/新建文件夹/processed_data_final.csv'
    # df.to_csv(output_file_path_updated, index=False)

    # 定义topsis分析
    def topsis_analysis(df, score_columns, weights):
        # Ensure dataframe copying to avoid SettingWithCopyWarning
        analysis_df = df[score_columns].copy()

        # Normalize each score column
        for col in score_columns:
            col_min = analysis_df[col].min()
            col_max = analysis_df[col].max()
            # Avoid division by zero by setting normalized value to 0 if col_max equals col_min
            analysis_df[col] = (analysis_df[col] - col_min) / (col_max - col_min) if col_max != col_min else 0

        # Apply weights
        for i, col in enumerate(score_columns):
            analysis_df[col] *= weights[i]

        # Calculate distances to ideal best and worst
        ideal_best = analysis_df.max()
        ideal_worst = analysis_df.min()

        squared_diff_best = (analysis_df - ideal_best) ** 2
        squared_diff_worst = (analysis_df - ideal_worst) ** 2

        # Manually compute square roots to avoid issues.
        distance_to_best = squared_diff_best.sum(axis=1).apply(lambda x: np.sqrt(x))
        distance_to_worst = squared_diff_worst.sum(axis=1).apply(lambda x: np.sqrt(x))

        # Calculate the relative closeness to the ideal solution
        relative_closeness = distance_to_worst / (distance_to_best + distance_to_worst)

        # Add the topsis score to the original dataframe
        df['topsis_score'] = relative_closeness

        return df

    # 定义分数列和权重
    score_columns = ['user_experience_score', 'bounce_rate_score', 'user_activity_score',
                     'loading_speed_score', 'network_feedback_score', 'first_input_delay_score',
                     'click_error_score', 'page_load_error_score', 'blank_page_score']

    weights = np.array([0.15, 0.10, 0.10, 0.15, 0.10, 0.10, 0.10, 0.10, 0.10])

    # 应用TOPSIS分析到DataFrame
    df = topsis_analysis(df, score_columns, weights)

    # 确保在所有得分计算完成后，再次将更新后的 DataFrame 保存到新的 CSV 文件中
    # output_file_path_updated = '/Users/diannao/Desktop/服务外包大赛/20240104151004_602/新建文件夹/processed_data_final.csv'
    # df.to_csv(output_file_path_updated, index=False)
    df['envAttr'] = df['envAttr'].apply(lambda x: str(x))
    df['interactionAttr'] = df['interactionAttr'].apply(lambda x: str(x))
    df['pageAttr'] = df['pageAttr'].apply(lambda x: str(x))
    df['performanceAttr'] = df['performanceAttr'].apply(lambda x: str(x))
    df['repeat_clicks'] = df['repeat_clicks'].astype('str')
    # df_result =df[['user_activity_score', 'desc', 'deviceGroupId', 'eventId',
    #        'eventName', 'eventTypeId', 'projectId', 'screenDirect', 'sessionId', 'userId',
    #        'interactionAttr_errorCount', 'interactionAttr_isBlank',
    #        'interactionAttr_isFirstTimeVisit', 'interactionAttr_isRefresh',
    #        'interactionAttr_pageActiveDuration', 'interactionAttr_pageDuration',
    #        'interactionAttr_timeSinceSessionStart', 'interactionAttr_textInput',
    #        'interactionAttr_textInputTime', 'interactionAttr_timeSincePageLoad',
    #        'interactionAttr_repeatClick',
    #        'interactionAttr_viewportHeightChangeRate',
    #        'interactionAttr_viewporChinaidthChangeRate',
    #        'interactionAttr_stayTime', 'interactionAttr_viewportPosition',
    #        'interactionAttr_viewportPositionPercentage',
    #        'performanceAttr_consoleErrors', 'performanceAttr_consoleInfos',
    #        'performanceAttr_consoleWarnings',
    #        'performanceAttr_largestContentfulPaint',
    #        'performanceAttr_loadingPerformance', 'performanceAttr_pageLoad',
    #        'performanceAttr_firstInputDelay',
    #        'performanceAttr_firstInteractionAction',
    #        'performanceAttr_firstInteractionPerformance',
    #        'performanceAttr_errorText', 'performanceAttr_isError',
    #        'performanceAttr_feedbackInterval', 'performanceAttr_slowNeChinaork',
    #        'pageAttr_clientCreateTs', 'pageAttr_libVersion', 'pageAttr_referrer',
    #        'pageAttr_referrerHost', 'pageAttr_sdkType', 'pageAttr_sessionId',
    #        'pageAttr_title', 'pageAttr_uri', 'pageAttr_url', 'pageAttr_urlHost',
    #        'pageAttr_urlPath', 'pageAttr_cssSelector', 'pageAttr_elementClassName',
    #        'pageAttr_elementId', 'pageAttr_elementName',
    #        'pageAttr_elementPosition', 'pageAttr_elementTargetUrl',
    #        'pageAttr_elementText', 'pageAttr_elementType', 'pageAttr_pageLength',
    #        'ptime', 'repeat_clicks', 'user_experience_score', 'bounce_rate_score',
    #        'loading_speed_score', 'network_feedback_score',
    #        'first_input_delay_score', 'click_error_score', 'page_load_error_score',
    #        'blank_page_score', 'total_score', 'average_score', 'topsis_score']]
    conn = pymysql.connect(host='CHANGE_ME_HERE', port=1181, user='CHANGE_ME_HERE', password='CHANGE_ME_HERE', database='comp_test')
    cur = conn.cursor()
    table = 'comp_test.web_data'
    try:
        sql = f"truncate table {table};"
        cur.execute(sql)
        conn.commit()
        print("清空表成功")
    except Exception as e:
        print(e)
        conn.rollback()
        print("清空表失败")
    finally:
        cur.close()
        conn.close()
    conn = pymysql.connect(host='CHANGE_ME_HERE', port=1181, user='CHANGE_ME_HERE', password='CHANGE_ME_HERE', database='comp_test')
    cur = conn.cursor()
    sql1 = f"insert into {table} values({','.join(['%s'] * len(df.columns))});"
    print(sql1)
    try:
        cur.executemany(sql1, df.replace(np.nan, None).values.tolist())
        conn.commit()
        print('成功')
    except Exception as e:
        print(e)
        conn.rollback()
        print("插入数据失败")
    finally:
        cur.close()
        conn.close()