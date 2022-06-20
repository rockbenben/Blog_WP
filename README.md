# 互联网小白

> 盛年不重来，一日难再晨。

---start---

## 目录 (2022 年 06 月 20 日更新)

---end---

## 发布工具

[WordPressXMLRPCTools](https://github.com/zhaoolee/WordPressXMLRPCTools) 能用 Markdown 生成博客，推送更新到 Github 后，通过 Github Actions 自动将文章更新到 WordPress，并将 WordPress 网站的文章索引更新到 Github 仓库的 README.md，供搜索引擎收录。​

基于 WordPressXMLRPCTools，我做了两点修改：​

- 草稿箱：`_post`路径内新建`TEMP`文件夹，用于存放文章草稿。WordPress 推送程序会忽略`_post`子文件夹的内容，换言之，`TEMP`文件夹不会发布到 WordPress 网站。

- 文章聚合页：主目录新增`.nojekyll`，`index.html`，`_sidebar.md`文件，引入文档生成工具 docsify，将博客文章聚合在一个页面，方便快速定位和位置管理。
  示例：[https://rockbenben.github.io/Blog_WP/](https://rockbenben.github.io/Blog_WP/)

  ![](http://tc.seoipo.com/2022-05-26-20-12-56.png)

## 使用流程

1. 进入项目页面，选择 [原版](https://github.com/zhaoolee/WordPressXMLRPCTools) 或 [修改版](https://github.com/rockbenben/Blog_WP)，点击「Use this template」，复制模板文件。
2. 回到你新建的 repo，删除 \_post 文件夹中的所有文件，参照主目录下`example_article.md`的格式编辑文章。
3. 按[WordPressXMLRPCTools 安装步骤](https://github.com/zhaoolee/WordPressXMLRPCTools#%E7%94%A8github-actions%E5%86%99markdown%E6%96%87%E7%AB%A0%E8%87%AA%E5%8A%A8%E6%9B%B4%E6%96%B0%E5%88%B0wordpress)执行，如遇报错，查看下方使用问题。
4. 修改主目录下的`index.html`和`_sidebar.md`，调整 docsify 网页设置。
   - `index.html`修改 docsify 网页标题、描述和关键词。
   - `_sidebar.md`修改 docsify 网页侧边栏，加入博客文章的标题和位置。

## 使用问题

### 文章发布不成功

`_post`文件夹添加了文档，但同步后，`README.md`和 WordPress 并没更新文章。

- 文章后缀必须为「.md」，不支持「.markdown」或其他后缀格式。
- 进入 repo 页面中的`Actions`，检查最近一次的 update 是否正确。

  ![](http://tc.seoipo.com/2022-05-26-20-36-56.png)

### Error: git denied to github-actions[bot]

遇到 GitHub Actions 报错：`git denied to github-actions[bot]`或`Process completed with exit code 128`。

依次点击该 repository 的`Setting - Code and automation - Actions - General`，然后在 Workflow permissions 中开启「Read and write permissions」。

### Error: Process completed with exit code 1

遇到 GitHub Actions 报错：`Error: Process completed with exit code 1`，检查服务器是否开启了防火墙，含代码的文章容易被误认为木马。暂时关闭服务器防火墙，如 Nginx 防火墙、宝塔系统加固，可解决该问题。

### 无法覆盖更新原文章 ​

修改旧文章并同步后，WordPress 站的文章没同步修改，而是新增了一篇相同的文章。这是 WordPressXMLRPCTools 项目的 bug。项目作者 @zhaoolee 说，「**只要不改文件名，就可以通过更新 markdown，更新对应的文章内容。**」​

但我和 @clairyitinggu 在未改文件名的情况下，都没能更新对应文章内容，而是重新发布了篇新文章。如果你也遇到相同的问题，建议手动将新文章内容覆盖旧文章，然后删除新文章。​

这个 bug 可以当作是强提醒。当 WordPress 新增了旧文章，你就被提醒要在其他平台修改该文章，让文章版本保持统一。​

### WordPress 发布时间与实际不符 ​

同步文章后，WordPress 显示的文章发布时间是 GitHub push 时间，而非文章真实的发布时间。​

如果你将旧文章转移到 WordPress，文章的发布时间需在 WordPress 后台手动修改，无法在 Markdown 文件中指定 WordPress 显示的发布时间。
