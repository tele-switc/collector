# 📰 每日外刊精选 - Daily Foreign Media Collection

自动收集并展示全球顶级媒体文章的GitHub项目，每天早上8点自动更新！

## ✨ 功能特点

- 🤖 **全自动运行**：使用GitHub Actions每天早上8点自动收集
- 🌍 **六大顶级媒体**：连线、经济学人、科学美国人、大西洋月刊、纽约时报、华尔街日报
- 🎨 **精美界面**：现代化响应式设计，支持手机和电脑浏览
- 🔍 **智能去重**：自动过滤重复文章
- 📅 **历史存档**：从2025年开始的所有文章永久保存
- 🚀 **零成本部署**：完全基于GitHub，无需服务器

## 🛠️ 一键部署指南

### 第一步：Fork这个仓库

1. 点击本页面右上角的 **Fork** 按钮
2. 选择你的GitHub账号
3. 等待Fork完成

### 第二步：启用GitHub Pages

1. 进入你Fork后的仓库
2. 点击 **Settings**（设置）
3. 在左侧菜单找到 **Pages**
4. 在 **Source** 下拉菜单选择 **Deploy from a branch**
5. 在 **Branch** 下拉菜单选择 **main**
6. 文件夹选择 **/ (root)**
7. 点击 **Save** 保存

### 第三步：启用GitHub Actions

1. 点击仓库的 **Actions** 标签
2. 如果看到提示，点击 **"I understand my workflows, go ahead and enable them"**
3. 找到 **Collect Daily Articles** workflow
4. 点击 **Enable workflow**

### 第四步：创建初始数据文件夹

1. 回到仓库主页
2. 点击 **Create new file**
3. 在文件名输入框输入：`data/articles.json`
4. 在文件内容输入：`[]`
5. 点击 **Commit new file**

### 第五步：手动运行一次（可选）

1. 进入 **Actions** 标签
2. 选择 **Collect Daily Articles**
3. 点击右侧的 **Run workflow**
4. 点击绿色的 **Run workflow** 按钮
5. 等待运行完成（约2-3分钟）

### 第六步：访问你的网站

1. 等待5-10分钟让GitHub Pages生效
2. 访问：`https://[你的用户名].github.io/[仓库名]/`
3. 例如：`https://yourname.github.io/news-aggregator/`

## 📁 项目结构

```
.
├── .github/
│   └── workflows/
│       └── collect-articles.yml    # GitHub Actions工作流
├── data/
│   └── articles.json               # 文章数据存储
├── index.html                      # 网站主页
├── collector.py                    # 文章收集脚本
├── requirements.txt                # Python依赖
└── README.md                       # 本文档
```

## ⚙️ 配置说明

### 修改收集时间

编辑 `.github/workflows/collect-articles.yml` 文件中的cron表达式：

```yaml
schedule:
  - cron: '0 0 * * *'  # UTC时间0点 = 北京时间早上8点
```

### 添加或删除媒体源

编辑 `collector.py` 文件，在相应的收集函数中添加或删除RSS源。

### 自定义网站样式

编辑 `index.html` 文件中的CSS样式部分。

## 📊 数据格式

文章数据以JSON格式存储在 `data/articles.json`：

```json
[
  {
    "id": "abc12345",
    "source": "wired",
    "title": "文章标题",
    "url": "https://...",
    "summary": "文章摘要...",
    "image": "https://...",
    "date": "2025-01-01",
    "collected_at": "2025-01-01T08:00:00"
  }
]
```

## 🔧 故障排除

### GitHub Actions没有运行？

1. 确保Actions已启用
2. 检查 `.github/workflows/collect-articles.yml` 文件格式是否正确
3. 查看Actions标签页的错误日志

### 网站无法访问？

1. 确保GitHub Pages已正确配置
2. 等待5-10分钟让配置生效
3. 检查仓库是否为公开（Public）

### 没有收集到文章？

1. 手动运行一次Action查看日志
2. 某些RSS源可能暂时无法访问
3. 检查 `requirements.txt` 中的依赖是否都已安装

## 📈 后续优化建议

- [ ] 添加文章全文提取功能
- [ ] 增加文章分类和标签
- [ ] 添加阅读统计
- [ ] 支持更多媒体源
- [ ] 添加邮件订阅功能
- [ ] 实现文章翻译功能

## 📝 许可证

MIT License - 自由使用和修改

## 🤝 贡献

欢迎提交Issues和Pull Requests！

## 💬 联系方式

如有问题，请在Issues中提出。

---

**注意**：本项目仅用于个人学习和研究，收集的文章版权归原作者所有。请勿用于商业用途。
