---
layout:       post
title:        "博客探索历史－从 Markdown 到 WordPress"
subtitle:     ""
date:         2022-04-29
author:       "Benson"
header-img:   img/post-bg-20180108.jpg
header-mask:  0.3
catalog:      true
categories:
    - 博客
tags: 
    - blog
    - WordPress
---

2005 年开始博客记录。第一个平台是 MSN space，并配合短命的 Google Sidewiki 记录感想。六年后，MSN space 关闭 ，旧博客被动转移到 WordPress 托管。之后改用 Blogger，没多久就暂停博客记录。

2018 年偶尔接触到 Jekyll，被其简洁的界面和便捷性打动，博客复活。本地用 Markdown 编辑排版，同步 github 发布，博客方向则从感想记录转移到知识输出。Jekyll 体验感很好，但随着文章、分发渠道的增多，修改也愈加困难，甚至逐渐习惯只更新专栏，而博客仅发布初版。

2021 年，Jekyll 已经失去了知识记录参考的初衷，决定将博客从  Jekyll 迁移到 WordPress，文章的初次排版编辑依旧使用 Markdown。
![](http://tc.seoipo.com/20210128124408.png)

但是，很快 WordPress 的糟糕编辑体验让我再次转移。这次的新平台是 Notion，界面美，编辑方便，支持在线页面，几乎是完美的博客模板。但是，Notion 不支持原生 md，国内访问速度成迷。这些使得 Notion 更适合个人分享使用，不适合作为主力分发渠道。

2022 年，晃了一圈后，博客平台再度更改。

分发平台过多，导致一篇文章需要修 N 次。

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

`_post`路径内新建`TEMP`文件夹，用于放置文章草稿，推送程序不会推送`_post`子文件夹中的 md 文件，不会同步到 WordPress。

## 常见问题

1. 无法启动 github action，显示`git denied to github-actions[bot]`和`Process completed with exit code 128`。

    依次点击该 repository 的 Setting - Code and automation - Actions - General，然后在 Workflow permissions 中开启「Read and write permissions」。

2. `_post`中添加了文档，但并未在 README 中显示

    文档后缀必须为「.md」，不支持 .markdown。

3. 更新文章时报错`Error: Process completed with exit code 1`。

    检查服务器是否开启了防火墙，文章中含代码容易被误认木马。

## 本地管理 md 文章

本地修改最大的问题是，标题不能

用飞书多维表格保存本地 md 文章的标题、本地位置、链接和封面。借助 RunAny 的「一键直达」功能，点击表格中的「本地位置」，即可用默认编辑器打开 md 文件。
![](http://tc.seoipo.com/2022-05-06-12-43-36.png)

表格切换为「画册视图」，达到 90% 的 Notion 视觉效果。
![](http://tc.seoipo.com/2022-05-06-12-28-41.png)
