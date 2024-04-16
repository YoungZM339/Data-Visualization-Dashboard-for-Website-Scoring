# Data-Visualization-Dashboard-for-Website-Scoring

[![License](https://img.shields.io/github/license/youngzm339/Data-Visualization-Dashboard-for-Website-Scoring)](https://github.com/youngzm339/Data-Visualization-Dashboard-for-Website-Scoring/blob/master/LICENSE)
[![Issues](https://img.shields.io/github/issues/youngzm339/Data-Visualization-Dashboard-for-Website-Scoring)](https://github.com/youngzm339/Data-Visualization-Dashboard-for-Website-Scoring/issues)
[![Stars](https://img.shields.io/github/stars/youngzm339/Data-Visualization-Dashboard-for-Website-Scoring)](https://github.com/youngzm339/Data-Visualization-Dashboard-for-Website-Scoring)

![Data Visualization Dashboard for Website Scoring](/docs/imgs/readme_cover.jpeg)

README of supported languages: [English](./README.md) | [简体中文](./docs/README-zh_CN.md)

## Introduction

The Data Visualization Dashboard for Website Scoring is a project aimed at visually displaying website scoring data through charts, graphs, and data visualizations. This dashboard allows users to intuitively understand the scoring of different websites, helping them make better decisions and optimize website performance. The project will provide intuitive and easy-to-understand data visualizations to help users quickly grasp website scoring trends and key metrics.

## Features

### User Control

![User Control](/docs/imgs/login.jpg)

### Upload & Analysis

![Upload & Analysis](/docs/imgs/process.jpg)

### Visualization Dashboard

![Visualization Dashboard](/docs/imgs/LargeScreenDisplay.jpg)

## Deployment Guide

### Frontend

- Install dependencies with `npm install`
- Configure the base URL for backend requests in `frontend/api.js`
- Run `npm run dev` (for testing environment only) or `npm run build`

### Backend

- Install dependencies with `pip install -r requirements.txt`
- Configure MySQL database for algorithm computation results in `backend\web_scoring\algorithms\algorithm.py` and `backend\web_scoring\algorithms\views.py`
- Initialize SQLite databases for user management and algorithm task control using `backend\web_scoring\manage.py migrate`
- Run the server with `backend\web_scoring\manage.py runserver` (for testing environment only)

## Development Guide

The `frontend` directory contains frontend code using Vue, Axios, VueRouter, Vuex (for frontend JavaScript framework support), ECharts, DataV, ElementUI (for component UI support).

The `backend` directory contains backend code using Django (for backend web application framework support), Django REST Framework (for RESTful API support), Simple JWT (for user authentication support).

The `docs` directory contains documentation.
