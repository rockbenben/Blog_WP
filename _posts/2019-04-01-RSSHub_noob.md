---
layout:       post
title:        "RSS 速成篇：RSSHub 捡现成的轮子"
subtitle:     ""
date:         2019-04-01
author:       "Benson"
header-img:   img/post-bg-20180108.jpg
header-mask:  0.3
catalog:      true
categories:
    - 自动化
tags:
    - rss
    - RSSHub
---
RSS 使用已经介绍了 feed43 和 Huginn，但这些工具或需要学习，或需要硬件。与之相比，RSSHub 有着成熟的配置，可以直接使用。

**RSSHub** 是个开源项目，对微博、知乎、豆瓣、bilibili、Youtube 等主流网站进行 RSS 转化。我们只要访问 [RSSHub 官网](https://docs.rsshub.app/) ，上面定期更新了主流媒体的 rss 项目。
![](http://tc.seoipo.com/20190331012441.png)

### 抓取示例：bilibili 番剧

1. 打开  [RSSHub bilibili 专区](https://docs.rsshub.app/social-media.html#bilibili) ，上面能根据番剧、UP 主等定制 rss。
    ![](http://tc.seoipo.com/20190406131343.png)

2. 准备抓取番剧《盾之勇者成名录》的更新，番剧主页链接为`https://www.bilibili.com/bangumi/media/md4316482/` ，mediaid 为`4316482`。

3. 按照路由参数修改 rss 链接`https://rsshub.app/bilibili/bangumi/media/4316482`，并在 rss 阅读器中打开。
    ![](http://tc.seoipo.com/20190406134022.png)

p.s. RSSHub 使用非常简单，但现在已经太过流行，微博、知乎已经开始反爬限制，动手能力强建议走 Huginn。
