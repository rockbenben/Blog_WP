---
layout:       post
title:        "－从 Markdown 到 WordPress"
subtitle:     "18 年博客探索总结"
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

2018 年，偶然接触到 Jekyll，被其简洁的界面和便捷性打动，重新恢复了博客记录。**博客方向从感想记录转变到知识整理输出**。

Jekyll 方案：**首先在本地用 Markdown 编辑排版，然后同步到 github 发布，最后以 Markdown 格式手动分发到各个渠道**。一开始这套方案的体验感特别好，可随着文章和分发渠道的增多，多平台的文章修改和管理变得愈加困难。慢慢地，我习惯在本地 Markdown 上只编辑文章初稿，后期更新则直接在外部平台上修改。

2021 年，Jekyll 方案带来的多版本问题彻底爆发，连我自己都分不清哪个版本才是全新。博客偏离了知识记录参考的初衷。为保持版本统一，博客从 Jekyll 迁移到 WordPress，准备以 WordPress 作为全平台标准版。

![Jekyll 博客](http://tc.seoipo.com/20210128124408.png?imageMogr2/thumbnail/!40p)

但很快，WorPress 方案被放弃了。原因除了 WordPress 糟糕的编辑体验外，更重要的是，当时我遇到了 Notion。

Notion 界面美观，编辑方便，支持对外展示，能导出为 Markdown、HTML 文件。

然而，打脸总是来得很快，没有哪个平台是完美的。Notion 不支持同步本地 markdown 内容，图床不能在站外使用，国内访问速度成谜。这令 **Notion 更适合个人分享，而不适合充当博客网站**。

2022 年，由于疫情被封控在家两个月。时间多了，开始尝试新的博客方案。

新的博客要求：界面美观，本地管理，一键同步。

## 博客方案

最初，我幻想着修改一篇文章同步到多个平台，但找了许久也没有合适的。网上所谓的一键分发软件，实际上是通过网页操作来完成发布，并不能自动修改更新。

剔除掉这类不现实的想法后，新的博客方案以 Markdown 版本为主，自动同步 WordPress，最后手动同步主要分发平台。「一键同步」，只能做到一键同步 github 和 WordPress 平台。

**最终方案**如下：

1. 初稿：Markdown 本地编辑，使用七牛云自建图床。
2. 发布：同步本地 Markdown 文本，自动发布，保持主力平台内容最新。
3. 管理：本地更新修改 Markdown 文件，docsify 页面整合文本内容，博客后台管理文章版本。
4. 订阅：用户能通过 RSS、邮件或微信订阅内容。

## 发布工具：WordPressXMLRPCTools

本地用 Markdown 编辑好文章后，同步到 github，然后通过 [WordPressXMLRPCTools](https://github.com/zhaoolee/WordPressXMLRPCTools) 发布到 WordPress 站点。

WordPressXMLRPCTools 能用 Markdown 生成博客，push 更新到 Github 后，Github Actions 自动将文章更新到 WordPress，并将 WordPres 站的文章索引更新到 Github 仓库的`README.md`，供搜索引擎收录。

基于 WordPressXMLRPCTools，我做了两点修改：

1. 草稿箱：`_post`路径内新建`TEMP`文件夹，用于存放文章草稿。WordPress 推送程序会忽略`_post`子文件夹的内容，换言之，`TEMP`文件夹不会发布到 WordPress 网站。

2. 文章聚合页：主目录新增`.nojekyll`，`index.html`，`_sidebar.md`文件，引入文档生成工具 docsify，将博客文章聚合在一个页面，方便快速定位和位置管理。
   示例：<https://rockbenben.github.io/Blog_WP/> 或 <https://docs.newzone.top/>

   ![](http://tc.seoipo.com/2022-05-26-20-12-56.png)

### 使用流程

1. 进入[项目页](https://github.com/rockbenben/Blog_WP)，点击「Use this template」，复制模板文件。
2. 回到你新建的 repo，删除 _post 文件夹中的所有文件。
3. 按[WordPressXMLRPCTools 安装步骤](https://github.com/zhaoolee/WordPressXMLRPCTools#%E7%94%A8github-actions%E5%86%99markdown%E6%96%87%E7%AB%A0%E8%87%AA%E5%8A%A8%E6%9B%B4%E6%96%B0%E5%88%B0wordpress)执行，如遇报错，查看下列方法解决。
4. 如果使用修改版的话，修改主目录中的`index.html`和`_sidebar.md`文件。
   * `index.html`可修改网页名称和备注。
   * `_sidebar.md`可修改网页侧边栏内容，引入博客文章的名称和位置。

### 使用问题

1. `_post`文件夹添加了文档，但同步后，`README.md`和 WordPress 并没有添加文章。这是哪里出了问题？

   * 文章后缀必须为「.md」，不支持「.markdown」或其他后缀格式。
   * 进入 repo 页面中的`Actions`，检查最近一次的 update 是否正确。

      ![](http://tc.seoipo.com/2022-05-26-20-36-56.png)

2. GitHub Actions 报错：`git denied to github-actions[bot]`和`Process completed with exit code 128`，如何解决？

   依次点击该 repository 的`Setting - Code and automation - Actions - General`，然后在 Workflow permissions 中开启「Read and write permissions」。

3. GitHub Actions 报错：`Error: Process completed with exit code 1`，如何解决？

   检查服务器是否开启了防火墙，含代码的文章容易被误认为木马。暂时关闭服务器防火墙，如 Nginx 防火墙、宝塔系统加固，可解决该问题。

4. 修改旧文章并同步后，WordPress 站的文章没同步修改，而是新增了一篇相同的文章。如何默认覆盖原文章？

   这是 WordPressXMLRPCTools 项目的 bug。项目作者 @zhaoolee 说，「只要不改文件名，就可以通过更新 markdown，更新对应的文章内容。」

   但我和 @clairyitinggu 在未改文件名的情况下，都被新增了文章而非覆盖。如果遇到该情况，建议手动将新文章内容覆盖旧文章，并删除新文章。

   可以把它当是个强提醒，当 WordPress 上新增了文章，就提醒自己需要在其他平台修改该文章，让版本统一更容易。

5. 同步文章后，WordPress 显示的文章发布时间是 github push 时间，而非文章真实的发布时间。如何在 Markdown 文件中指定 WordPress 显示的发布时间？

   如果你将旧文章转移到 WordPress，文章的发布时间需在 WordPress 后台手动修改。

## 本地管理 Markdown 文章

文章发布完成后，需要对本地文章进行整理。之前的 Windows 默认管理方案，存在 3 个问题：

1. 资源管理器的视觉效果非常难看。
2. Markdown 文件名称不能展示关键信息，较难定位文档。文章越多，管理越困难。
3. 无法对文章内容进行本地检索，只能通过文件名称猜测内容。

![难以管理的本地文档](http://tc.seoipo.com/2022-05-30-19-00-15.png)

### 飞书文档管理

视觉和文章关键信息，为解决这几个问题，我用飞书多维表格保存本地 Markdown 文章的标题、本地位置、链接和封面。

![飞书表格视图](http://tc.seoipo.com/2022-05-06-12-43-36.png)

将表格切换为「画册视图」，文档管理界面达到 90% 的 Notion 视觉效果。

![飞书画册视图](http://tc.seoipo.com/2022-05-06-12-28-41.png)

接下来，我们借助 [RunAny](https://github.com/hui-Zz/RunAny) 的「一键直达」功能，点击表格中的「本地位置」，即可使用默认编辑器打开 md 文件。

```ini
;将 Runany 主目录下的 RunAny.ini 文件内的「编辑」模块替换为下方命令
-编辑(&Edit)
 --编程|cmd bat md ahk html js css json
 vscode|Code.exe
 --文本|txt ini
 notepad++.exe
```

### docsify 管理文本

借助 [docsify](https://docsify.js.org/#/)，我们能对所有文章内容进行全文检索，并在单一页面进行管理。

在项目目录中打开终端，执行命令 `docsify serve` 即可生成网页，默认管理链接为 `http://localhost:3000/#/`。

![docsify 本地运行](http://tc.seoipo.com/2022-05-30-20-03-19.png)

如果你设置了 Github Pages，项目会默认启动 docsify，方便检索博客全文内容。管理页面链接取决于你的 Github 设置，比如我的用户名是`rockbenben`，项目名是`Blog_WP`，docsify 管理页面就是 <https://rockbenben.github.io/Blog_WP/>。

## 其他发布工具

「原生 md」指修改 markdown 文件即可更新博客平台。

* github：原生 md，支持自定义
* WordPress：不支持原生 md
* Notion：
* [竹白](https://zhubai.love/)：Newsletter，微信订阅，支持付费订阅
* [Substack](https://substack.com/)：Newsletter，支持付费订阅

## 后续

博客方案

比如 2021 年初写了 KeePass，但后面直接忘了，直到这次修改管理方式，才发现这篇在草稿箱待了一年半的稿子。最近出稿速度大增，也都跟这有关。
