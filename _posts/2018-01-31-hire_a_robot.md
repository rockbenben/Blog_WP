---
layout: post
title: "雇个机器人帮你干活"
subtitle: ""
date: 2018-01-31 22:51:00
author: "Benson"
header-img: img/post/wallhaven-586105.jpg
header-mask: 0.3
catalog: true
categories:
  - 自动化
tags:
  - Huginn
  - rss
---

> 机器人会取代你工作！
> 计算云会取代你工作！
> AI 会取代你的工作！

我相信科技终究有一天会消灭所有工作，但我们这代人的无奈就是很难等到这一天。

作为懒人、宅男，等不及了怎么办？

既然还没被取代，那就**雇个机器人帮你干活**！

我每天第一件事是去各个网站看热门新闻、行业资料。以前是用 RSS，但 RSS 被视为落后，越来越多的网站不再提供 RSS 源。离开 RSS，我就一直没找到更合适的方法去将内容聚合起来，不得不在一个个网站间疲于奔命，逐渐不再看内容。

> RSS(Really Simple Syndication) 是一种描述和同步网站内容的格式，是使用最广泛的 XML 应用。简易信息聚合（也叫聚合内容）是一种 RSS 基于 XML 标准，在互联网上被广泛采用的内容包装和投递协议。

- [ ] 增加 `Alfred` 搜索

**直到遇到了我的第一个机器人雇员 [Huginn](https://github.com/huginn/huginn)**

> Huginn 是一个可以创建为你在线执行自动化任务的系统。Huginn 可以读取网页，监测事件并且执行符合你需求的动作。Huginn 通过 agents 创建并执行任务（事件流）。你可以将它看作是一个运行在你自己服务器上的 IFTTT 或 Zapier。

Huginn 帮我将所有信息聚合成 RSS，24 小时帮我获取我要的内容。

- [网易热门新闻](http://news.163.com/rank)：抓取网易顶贴最多的 100 条新闻
- [百度实时热点](http://top.baidu.com/buzz?b=1)：实时更新每天的百度热点
- [果壳网](https://www.guokr.com/)：果壳首页推荐，官方更新速度较慢，刚好可以了解些奇思妙想
- 工作类：梅花、SocialBeta、数英网、艾瑞网
