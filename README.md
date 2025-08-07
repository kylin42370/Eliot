# Do I Dare Disturb - Blog Website

一个采用2013年博客风格设计的Streamlit网站，专注于2000-2013年人权新闻研究。

## 作者
**Measured Silence** - 专注于数字时代人权研究的作者

## 功能特点

- 🎨 2013年经典博客设计风格
- 📝 三篇关于人权新闻的研究文章
- 🏷️ 标签分类系统
- �� 响应式设计
- 📅 文章归档功能
- 💬 互动留言系统

## 文章内容

1. **The Whisperers: Voices from the Digital Shadows (2000-2005)**
   - 探讨早期互联网上的个人声音
   - 分析数字记忆的保存

2. **Between the Lines: The Unwritten History of Digital Resistance (2006-2009)**
   - 研究数字抵抗的无声历史
   - 分析记忆保存者的角色

3. **The Quiet Revolution: When Silence Became a Form of Speech (2010-2013)**
   - 沉默如何成为一种表达
   - 数字见证的新形式

## 安装和运行

### 本地运行

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行网站：
```bash
streamlit run 网站.py
```

3. 在浏览器中打开显示的本地地址（通常是 http://localhost:8501）

### 部署到Streamlit Cloud

1. 将代码推送到GitHub仓库
2. 在Streamlit Cloud中连接仓库
3. 设置主文件为 `网站.py`
4. 部署会自动使用 `requirements.txt` 中的依赖

## 技术栈

- **Streamlit** - Web应用框架
- **HTML/CSS** - 自定义样式
- **Python** - 后端逻辑
- **JSON** - 留言数据存储

## 设计特色

- 复古博客风格设计
- 渐变标题背景
- 卡片式文章布局
- 侧边栏分类导航
- 引用块样式
- 互动留言系统

## 留言功能

- 用户可以输入姓名和留言内容
- 留言数据持久化保存
- 显示最近10条留言
- 支持匿名留言

## 部署注意事项

- 使用最新的Streamlit版本
- 移除了Pillow依赖以避免兼容性问题
- 留言数据保存在本地JSON文件中

## 版权信息

© 2013 Measured Silence. All rights reserved.

这个博客献给那些敢于打破沉默的人们。 