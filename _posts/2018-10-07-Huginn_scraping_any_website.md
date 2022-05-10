---
layout:       post
title:        "RSS 进阶篇：Huginn - 真·为任意网页定制 RSS 源（PhantomJs 抓取）"
subtitle:     ""
date:         2018-10-7
author:       "Benson"
header-img:   img/post-bg-20180108.jpg
header-mask:  0.3
catalog:      true
categories:
    - 自动化
tags:
    - Huginn
    - rss
---
烧制网页 RSS 源，主要有**FEED43**和**Huginn**两种方法。

1. FEED43：简单免费，六小时抓取一次，每次抓取 20 条静态页面。
2. Huginn：自由度高，可设定**抓取频率、内容结构、js 结果、输出样式**等；需要搭建服务器，学习 Huginn 抓取规则。

微信有各类屏蔽措施，可以尝试[wechat-feeds](https://wechat.privacyhide.com/)抓取。

## **Huginn 准备工作**

1. 准备一台 Debian/Ubuntu 环境的服务器
2. 按[Qi 大的攻略](https://wzfou.com/huginn/)搭建 Huginn，也可以直接看[Huginn 官方搭建攻略](https://github.com/huginn/huginn/blob/master/doc/manual/installation.md)

准备工作完成后，我们已经可以使用 Huginn 抓取页面了。但很多网站都是用 JS 加载动态内容，需要通过 **PhantomJs Cloud** 抓取页面 JS 缓存。

————

## Huginn + PhantomJs Cloud 全网页抓取

### 一、Phantom Js Cloud API key 获取

注册 [PhantomJs Cloud](https://phantomjscloud.com/) ,然后将 API key 保存在 Huginn 的 Credentials 中。免费版每天限制抓取 500 次页面，需求不大可建立多个账号使用不同 API key，足够个人使用。
![](http://tc.seoipo.com/20181006010447.png)

新建 Huginn 任务组 Scenario「国内应急新闻」，抓取链接 <http://www.cneb.gov.cn/guoneinews/>

![](http://tc.seoipo.com/20181008131549.png)

### 二、Phantom Js Cloud Agent 抓取页面缓存

   *Name: 国内应急新闻 #1 获取 JS 缓存*
   *Schedule: Every 1h*
![](http://tc.seoipo.com/20181008111704.png)

### 三、WebsiteAgent 获取页面详情

   *Name: 国内应急新闻 #2 抓取全页*
   *Schedule: Every 1h*
![](http://tc.seoipo.com/20181008112658.png)

### 四、css path 路径获取

1. 使用火狐浏览器打开抓取页面
2. 按下`F12`, 然后点击 *Developer Tools* 左上角的*检查指针*
![](http://tc.seoipo.com/20181008114911.png)
3. 选中要抓取的部分
![](http://tc.seoipo.com/20181008113925.png)
4. 回到 *Developer Tools* 窗口，右键选中的蓝色部分，获取 css path、Xpath。这里以 css path 为例。
![](http://tc.seoipo.com/20181008114207.png)
5. 处理 css path 路径

```css
html body div.area.areabg1 div.area-half.right div.tabBox div.tabContents.active table tbody tr td.red a
```

css path 原始路径过长，删去不带 `.` 或 `#` 的节点（节点间以空格“ ”分割），并删去每个节点在 `.` 或 `#`前的第一个标签，得到：

```css
.area.areabg1 .area-half.right .tabBox .tabContents.active .red a
```

前半部分对节点定位无用，继续省略（比如：中国上海，省略掉中国，大家也知道上海在哪）

```css
.tabContents.active .red a
```

**非常规情况处理**：
a. 有些路径中的**节点带空格**，如`<div class="packery-item article">`,路径中的空格由`.`代替，截取为`.packery-item.article`
b. 当抓取**多种 css path 规则**时，用逗号，分割

```css
"css": ".focus-title .current a , .stress h2 a",
```

### 五、DataOutputAgent 导出 RSS

   *Name: 国内应急新闻 #3 排序生成 RSS*
   **Propagate immediately*: Yes*

![](http://tc.seoipo.com/20181008130943.png)

回到 Scenarios，点击最后一步的 Actions - Show ，复制导出的 xml 链接 `http://xxx.xxxxxx/users/1/web_requests/xxx/xxxx.xml`

![](http://tc.seoipo.com/20181008131059.png)

详细设置的使用文件-[百度网盘下载](https://pan.baidu.com/s/1JdsFkLN9kczR9C92tKi83A)

其他问题，查看官方说明-[PhantomJs Cloud 英文使用攻略](https://github.com/huginn/huginn/wiki/Browser-Emulation-Using-PhantomJs-Cloud)

## RSS 合集

汇总 RSS 永久订阅链接，feeds 均通过 RSSHub 和 Huginn 制作。如果有兴趣自己制作 RSS，可查看以下教程。

- [RSS 入门篇：FEED43&FeedEx-为静态网页定制 RSS 源](https://newzone.top/p/2017-04-22-RSS_FEED43_FeedEx/)

- [RSS 进阶篇：Huginn - 真·为任意网页定制 RSS 源（PhantomJs 抓取）](https://newzone.top/p/2018-10-07-Huginn_scraping_any_website/)

- [RSS 速成篇：RSSHub 捡现成的轮子](https://newzone.top/p/2019-04-01-RSSHub_noob/)

- [RSS 速成篇 2：RSSHub 自部署](https://newzone.top/p/2020-03-25-RSSHub_on_vps/)

- [RSS 完结篇：节省千元服务费，RSSHub、Huginn 转移 NAS](https://newzone.top/p/2021-10-23-NAS_with_RSSHub_and_Huginn/)

- [RSS 汇总篇：RSS 永久链接合集，拒绝 RSS 失效](https://newzone.top/p/2022-03-17-rss_persistent_link_collection)
