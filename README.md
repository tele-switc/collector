# collector
---
AIGC:
  Label: '1'
  ContentProducer: '001191110108MA01KP2T5U00000'
  ProduceID: '2c4ac2ec-377f-4672-89b5-2f6303028417'
  ReservedCode1: 'b39cdee1-96c1-42a7-b605-ed5662cf6c4c'
  ContentPropagator: '001191110108MA01KP2T5U00000'
  PropagateID: 'c38984a6-3181-4d30-847a-4690ef690ebc'
  ReservedCode2: '8265bfc7-7405-4865-858b-af0d73e4afe6'
---

# 外刊自动收集与展示系统

一个自动收集外刊文章并生成精美展示网站的项目。

## 功能特点

- 自动收集连线、经济学人、美国科学人、Atlantic、纽约时报和华尔街日报的文章
- 每天早上8点自动更新最新文章
- 智能去重处理，避免重复内容
- 从2025年初开始收集所有文章
- 响应式网站设计，完美支持移动端浏览
- 使用GitHub Actions实现自动化任务

## 项目结构


.
├── README.md                 # 项目说明文档
├── requirements.txt          # Python依赖包
├── .gitignore               # Git忽略文件
├── scraper/                 # 爬虫模块
│   ├── __init__.py
│   ├── config.py            # 配置文件
│   ├── models.py            # 数据模型
│   ├── database.py          # 数据库操作
│   ├── scrapers.py          # 爬虫实现
│   └── utils.py             # 工具函数
├── website/                 # 网站生成模块
│   ├── __init__.py
│   ├── generator.py         # 网站生成器
│   ├── static/              # 静态资源
│   │   ├── css/             # CSS样式
│   │   ├── js/              # JavaScript脚本
│   │   └── images/          # 图片资源
│   └── templates/           # HTML模板
│       ├── index.html       # 首页模板
│       ├── article.html     # 文章详情模板
│       └── layout.html      # 布局模板
├── data/                    # 数据存储目录
│   └── articles.db          # SQLite数据库
├── scripts/                 # 脚本目录
│   └── run_scraper.py       # 爬虫运行脚本
└── .github/                 # GitHub Actions配置
    └── workflows/
        └── scheduled_scraper.yml  # 定时任务配置


## 安装与使用

### 环境要求

- Python 3.8+
- Git

### 安装步骤

1. 克隆仓库
   bash
   git clone https://github.com/yourusername/foreign-magazines-collector.git
   cd foreign-magazines-collector
   

2. 安装依赖
   bash
   pip install -r requirements.txt
   

3. 配置爬虫
   编辑 `scraper/config.py` 文件，设置相关参数。

4. 运行爬虫
   bash
   python scripts/run_scraper.py
   

5. 生成网站
   bash
   python website/generator.py
   

### 定时任务

项目使用GitHub Actions实现定时任务，每天早上8点自动运行爬虫并更新网站。您可以在 `.github/workflows/scheduled_scraper.yml` 中修改定时设置。

## 数据库结构

项目使用SQLite数据库存储文章信息，主要包含以下表：

- `articles`: 存储文章基本信息
  - id: 文章ID
  - title: 文章标题
  - url: 文章链接
  - source: 来源网站
  - publish_date: 发布日期
  - content: 文章内容
  - summary: 文章摘要
  - created_at: 记录创建时间
  - updated_at: 记录更新时间

## 网站展示

生成的网站具有以下特点：

- 响应式设计，适配各种设备
- 按来源和日期分类展示文章
- 文章搜索功能
- 简洁美观的界面设计
- 快速加载，优化用户体验

## 贡献指南

欢迎提交Issue和Pull Request来改进项目。

## 许可证

本项目采用MIT许可证。详情请参阅LICENSE文件。

## 联系方式

如有问题或建议，请通过以下方式联系：

- 邮箱: your.email@example.com
- GitHub: https://github.com/yourusername
