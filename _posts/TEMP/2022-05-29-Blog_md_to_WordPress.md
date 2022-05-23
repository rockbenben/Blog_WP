---
layout:       post
title:        "博客探索－从 Markdown 到 WordPress"
subtitle:     ""
date:         2022-05-29
author:       "Benson"
header-img:   img/post-bg-20180108.jpg
header-mask:  0.3
catalog:      true
categories:
    - 博客
tags: 
    - blog
    - github
    - WordPress
---
## 博客探索

2005 年，开始用博客记录感想，发布在 MSN space 平台和短命的 Google Sidewiki 上。六年后，MSN space 关闭 ，博客被自动转移到 WordPress 托管。之后改用 Blogger，没多久就暂停了博客。

2018 年，偶然接触到 Jekyll，被其简洁的界面和便捷性打动，重新复活了博客。首先在本地用 Markdown 编辑排版，然后同步到 github 发布，最后以 Markdown 格式手动分发到各个渠道。博客方向则从感想记录转移到知识输出。Jekyll 方案的初期体验特别好。但是，随着文章和分发渠道的增多，多平台的文章修改和管理变得愈加困难。慢慢的，只有文章草稿在 Markdown 上编辑，而更新只针对一两个主要平台。

2021 年，Jekyll 方案带来的多版本问题彻底爆发，连我自己都分不清哪个版本才是全新。博客偏离了知识记录参考的初衷。为保持版本统一，博客从 Jekyll 迁移到 WordPress，准备以 WordPress 作为全平台标准版。
![](http://tc.seoipo.com/20210128124408.png)

但是很快，WorPress 方案被放弃了。原因除了 WordPress 糟糕的编辑体验外，更重要的是，当时我遇到了心中完美的博客平台 —— Notion。

Notion 界面美观，编辑方便，支持对外展示，可便捷导出为 markdown、html 多种格式。可 Notion 不支持本地 markdown 同步内容，国内访问速度成谜。这令 Notion 更适合个人分享，不适合作为博客网站。

2022 年，由于疫情被封控在家两个月。时间多了，开始尝试新的博客方案。

## 博客方案

1. 初稿：Markdown 编辑。
2. 发布：同步本地 Markdown 文本，自动发布，保持主力平台内容最新。
3. 管理：本地管理 Markdown 文件，博客后台管理文章版本。
4. 订阅：用户能通过 RSS、邮件或微信订阅更新。

至于，一篇文章同步修改多个平台的理想，大概率是不会出现了。目前没发现哪个平台提供了文章 API，网上所谓的分发软件也都是通过隐藏的网页操作完成，并不能实现一键修改更新。

目前的博客方案，依旧是以 Markdown 版本为主，自动同步 WordPress，手动更新几个主要平台。

新方案在修改后，不能自动同步 WordPress，但会在平台上新增文章，提醒哪些文章更新了需要在其他平台修改，让版本统一更容易。

## 发布平台

「原生 md」指修改 markdown 文件即可更新博客平台。

* github：原生 md，支持自定义
* WordPress：不支持原生 md
* Notion：
* [竹白](https://zhubai.love/)：Newsletter，微信订阅，支持付费订阅
* [Substack](https://substack.com/)：Newsletter，支持付费订阅

## github 同步到 WordPress

WordPressXMLRPCTools 能用 Markdown 生成博客，push 更新到 Github 后，Github Actions 自动将文章更新到 WordPress，并将 WordPres 站的文章索引更新到 Github 仓库的 README.md，供搜索引擎收录。

安装步骤查看[WordPressXMLRPCTools 项目页](https://github.com/zhaoolee/WordPressXMLRPCTools)，如遇报错，按下列方法解决。

1. `_post`路径内新建`TEMP`文件夹，用于存放文章草稿，推送程序不会推送`_post`子文件夹内的 md 文件，也就不会发布到 WordPress 网站。
2. 主目录新增`.nojekyll`，`index.html`，`_sidebar.md`文件，引入 docsify，将发布文章聚合在网页中，方便快速定位和位置管理。

## 常见问题

1. 无法启动 github action，显示`git denied to github-actions[bot]`和`Process completed with exit code 128`。

   依次点击该 repository 的 Setting - Code and automation - Actions - General，然后在 Workflow permissions 中开启「Read and write permissions」。

2. 更新文章时报错`Error: Process completed with exit code 1`。

   检查服务器是否开启了防火墙，文章中含代码容易被误认木马，比如宝塔的 Nginx 防火墙。

3. `_post`中添加了文档，但并未在 README 中显示

   文档后缀必须为「.md」，不支持 .markdown。

4. 修改文章后，WordPress 站的文章不会同步更新，反而会新增一篇文章。

   这是 WordPressXMLRPCTools 的 bug，作者反馈会自动覆盖，但大家都反馈覆盖失败。暂时只能手动将新文章内容覆盖旧文章，并删除新文章。

5. WordPress 默认时间是 push 时间，而非文章发布时间。

   如果发布旧文章，时间需到 WordPress 后台修改。

## 本地管理 markdown 文章

本地管理文章存在大量问题，

1. 资源管理器的视觉效果难看；
2. 文章数量增多后，管理越来越困难；
3. markdown 文件名称不能展示关键信息，较难定位文档。

**飞书管理方案**
用飞书多维表格保存本地 md 文章的标题、本地位置、链接和封面。借助 RunAny 的「一键直达」功能，点击表格中的「本地位置」，即可用默认编辑器打开 md 文件。

![](http://tc.seoipo.com/2022-05-06-12-43-36.png)

表格切换为「画册视图」，达到 90% 的 Notion 视觉效果。

![](http://tc.seoipo.com/2022-05-06-12-28-41.png)

比如 2021 年初写了 KeePass，但后面直接忘了，直到这次修改管理方式，才发现这篇在草稿箱待了一年半的稿子。
