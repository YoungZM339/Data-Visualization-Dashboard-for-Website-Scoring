# 用于网站评分的数据可视化仪表盘

[![License](https://img.shields.io/github/license/youngzm339/Data-Visualization-Dashboard-for-Website-Scoring)](https://github.com/youngzm339/Data-Visualization-Dashboard-for-Website-Scoring/blob/master/LICENSE)
[![Issues](https://img.shields.io/github/issues/youngzm339/Data-Visualization-Dashboard-for-Website-Scoring)](https://github.com/youngzm339/Data-Visualization-Dashboard-for-Website-Scoring/issues)
[![Stars](https://img.shields.io/github/stars/youngzm339/Data-Visualization-Dashboard-for-Website-Scoring)](https://github.com/youngzm339/Data-Visualization-Dashboard-for-Website-Scoring)

![Data Visualization Dashboard for Website Scoring](/docs/imgs/readme_cover.jpeg)

README of supported languages: [English](/README.md) | [简体中文](/docs/README-zh_CN.md)

## 简介

用于网站评分的数据可视化仪表盘是一个旨在通过图表、图形和数据可视化来直观显示网站评分数据的项目。该仪表盘让用户直观地了解不同网站的评分，帮助他们做出更好的决策并优化网站性能。该项目将提供直观易懂的数据可视化，帮助用户快速把握网站评分趋势和关键指标。

## 特点

### 用户控制

![User Control](/docs/imgs/login.jpg)

### 上传与分析

![Upload & Analysis](/docs/imgs/process.jpg)

### 可视化仪表盘

![Visualization Dashboard](/docs/imgs/LargeScreenDisplay.jpg)

## 部署指南

### 前端

- 安装依赖`npm install`
- 配置`frontend/api.js`中请求后端的 baseURL
- `npm run dev`（仅供测试环境）/`npm run build`

### 后端

- 安装依赖`pip install -r requirements.txt`
- 配置算法计算结果的 MySQL 数据库（`backend\web_scoring\algorithms\algorithm.py`和`backend\web_scoring\algorithms\views.py`）
- 初始化用户管理和算法任务控制的 SQLite 数据库(`backend\web_scoring\manage.py migrate`)
- `backend\web_scoring\manage.py runserver`（仅供测试环境）

## 二次开发指南

`frontend` 目录下存放着前端代码，技术栈采用 Vue Axios VueRouter Vuex（前端 JavaScript 框架支持），ECharts、DataV、ElementUI （组件库 UI 支持）

`backend` 目录下存放着后端代码，技术栈采用 Django（后端 Web 应用框架支持）， Django REST Framework（RESTful API 支持），Simple JWT（用户鉴权支持）

`docs`目录下存放着文档
