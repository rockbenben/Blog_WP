# 互联网小白

---start---
## 目录(2022年05月05日更新)
---end---

网站基于[WordPressXMLRPCTools](https://github.com/zhaoolee/WordPressXMLRPCTools)，能用 Markdown 生成博客，push 更新到 Github 后，Github Actions 自动将文章更新到 WordPress，并将 WordPres 站的文章索引更新到 Github 仓库的 README.md，供搜索引擎收录。

## 常见问题

1. 无法启动 github action，显示 git denied to github-actions[bot] 和 Process completed with exit code 128.

Setting - Code and automation - Actions - General, Workflow permissions 中开启「Read and write permissions」。

2. _post 中添加了文档，但并未在 README 中显示

文档后缀必须为「.md」，不支持 .markdown。

3. 更新文章时报错`Error: Process completed with exit code 1`。

检查服务器是否开启了防火墙，文章中含代码容易被误认木马。
