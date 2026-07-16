# Website Scoring Dashboard

网站评分数据可视化原型。项目使用 Django REST 后端处理上传和任务记录，使用 Vue 2、Element UI、ECharts 和 DataV 展示网站体验指标、大屏看板和优化建议。

## 功能范围

- JWT 登录与用户相关接口。
- 数据上传和处理任务。
- 任务记录和结果查看。
- 网站体验仪表盘。
- 大屏数据展示。
- 静态优化建议页面。

## 指标展示

前端组件覆盖用户体验、跳出率、加载/网络反馈、输入延迟、点击/页面错误、白屏以及总分/平均分等指标。具体字段、计算口径和数据质量以后台算法与实际数据源为准。

## 技术栈

- 后端：Django 5、Django REST Framework、Simple JWT、pandas、PyMySQL。
- 前端：Vue 2、Vue CLI、Element UI、ECharts、DataV。

## 本地开发

后端：

    cd backend/web_scoring
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

前端：

    cd frontend
    npm install
    npm run dev

在运行迁移或任务前，必须先审阅并配置自己的数据库、数据查询来源、跨域策略和服务地址。仓库中的占位或开发设置不应直接连接生产数据。

## 结果使用边界

仪表盘分数和优化建议是对接入数据的可视化与算法输出，不是通用的网站性能认证。使用结果做业务或技术决策前，应核验：

- 指标定义和时间窗口；
- 数据采集完整性；
- 样本代表性；
- 算法/规则版本；
- 与原始日志或监控系统的一致性。

## 许可证

请参阅仓库中的 LICENSE 文件。