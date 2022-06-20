---
layout: post
title: "小狼毫 3 分钟入门及进阶指南"
subtitle: ""
date: 2020-11-27
author: "Benson"
header-img: img/post-bg-20180108.jpg
header-mask: 0.3
catalog: true
categories:
  - 工具
tags:
  - 小狼毫
  - 输入法
---

常年使用搜狗输入法，备份时发现搜狗词库高达 27 万条，其中 99% 的内容是垃圾词条，即使偶尔输入过一次的内容也被输入法记录。更可怕的是，这次词库无法从云端删除，只要你输入过一次，搜狗就永远记住了。

这哪里是输入法，根本是个**键盘记录器**。

之后尝试各类输入法，百度、讯飞、手心等依旧是键盘记录器，影子输入法开源但不够稳定，谷歌拼音停止更新，微软拼音词库收录慢且难以转移。唯有小狼毫开源，且方便多设备同步词库。

官网下载：<https://github.com/rime/weasel/releases/download/0.14.3/weasel-0.14.3.0-installer.exe>

国内搬运：<https://wwi.lanzoui.com/iDyF4pdzmni>

安装时建议不要修改用户文件夹位置，后续定制输入法容易出错。

安装完成后，右键点击任务栏小狼毫图标，选「输入法设定」，只勾选一个「朙月拼音·简化字」，再选一个喜欢的皮肤就好。

现在已经可以正常使用小狼毫输入法了。如果想要更完美的输入法，可以继续查看进阶指南。进阶前，右键点击任务栏小狼毫图标，选「用户文件夹」，新建 `luna_pinyin_simp.custom.yaml`(此方案为「朙月拼音·简化字」)。

## 进阶指南

**官方文档**：[定制指南](https://github.com/rime/home/wiki/CustomizationGuide)、[文件配置说明](https://github.com/rime/home/wiki/RimeWithSchemata#rime-%E4%B8%AD%E7%9A%84%E6%95%B8%E6%93%9A%E6%96%87%E4%BB%B6%E5%88%86%E4%BD%88%E5%8F%8A%E4%BD%9C%E7%94%A8)、[emoji 集成](https://github.com/rime/rime-emoji)、[模糊音设置](https://github.com/rime/home/wiki/CustomizationGuide#%E6%A8%A1%E7%B3%8A%E9%9F%B3)

[**同步用户资料**](https://github.com/rime/home/wiki/UserGuide#%E5%90%8C%E6%AD%A5%E7%94%A8%E6%88%B6%E8%B3%87%E6%96%99)：

打开用户文件夹中的`installation.yaml`，将设备名称`installation_id`从长字符串修改为方便识别的名称，并在文件最下方添加`sync_dir: 'D:\Sync\RIME'`，此处为用户资料同步位置。

注意：

- 同步文件夹路径中不能出现中文。
- 打字习惯会保存在`<词典名>.userdb.txt`、`<词典名>.userdb.kct.snapshot`，还原时手工导入词典。

**扩充词库**：[自定义短语](https://gist.github.com/lotem/5440677)、[Rime 擴充詞庫](https://github.com/rime-aca/dictionaries)

如果要兼具英文联想、网络流行语、成语、俗语等，可使用下列词库

- BetterRime 词库：[https://github.com/Chernfalin/better-rime-dict](https://github.com/Chernfalin/better-rime-dict)
- SuperRime 拓展词库：[https://github.com/Chernfalin/SuperRimeDict](https://github.com/Chernfalin/SuperRimeDict)

SuperRime 词库 > BetterRime 词库 > Rime 擴充詞庫，词库越大错误收录越多，按需选择词库。解压后，修改`luna_pinyin.extended.dict.yaml`，选择启用词库范围。`mysymbols.yaml`对全角和半角符号都做了优化，有问题的话可以按自己需求修改。

不建议安装「四叶草」等集成方案，而推荐以「朙月拼音·简化字」为基础定制你自己的输入法。这样即使出现 bug 也不会对你的输入法设置产生过大影响。小狼毫的魅力就在于定制、可控。

**手动更新**：下载 [librime](https://github.com/rime/librime/releases)，替换小狼毫目录内 的 rime.dll 就可完成手动更新。

librime 是 rime 输入法的核心库，小狼毫长久未更新，只能用此临时替代更新。

**指定程序中默认英文输入**： `.\weasel.custom.yaml` 中加入下列代码

```yaml
patch:
  app_options/windowsterminal.exe: # 程序名字全用小寫字母
    ascii_mode: true
  app_options/powershell.exe:
    ascii_mode: true
  app_options/code.exe:
    ascii_mode: true
  app_options/putty.exe:
    ascii_mode: true
  app_options/listary.exe:
    ascii_mode: true
```

## 双拼方案

为提高效率，继续折腾，开始使用**小鹤双拼**。

1. 官方配置库：<https://github.com/rime/rime-double-pinyin>。其中收录了自然码双拼、智能 ABC 双拼、小鹤双拼、MSPY 双拼、拼音加加双拼。
2. 小鹤双拼配置：将官方配置库中的 [double_pinyin_flypy.schema.yaml](https://github.com/rime/rime-double-pinyin/blob/master/double_pinyin_flypy.schema.yaml) 下载到用户文件夹。设置好后，右键点击任务栏小狼毫图标，选「输入法设定」，只勾选一个「小鹤双拼」。默认方案为繁体，可使用按键 F5 (部分版本是 F4)，将配置默认为简体。

如需双拼中实现自定义短语，可参考[小狼毫自定义短语-Rime-双拼](https://blog.csdn.net/neninee/article/details/83692270)。如果设定后，无法使用简体输入，将`double_pinyin_flypy.schema.yaml` 中的 filters 模块转移到 translators 模块上方。或者直接使用我的配置包。

## 常见问题

- **开机后，输入法不能输出中文？**

  需手动打开程序文件夹中的`WeaselServer.exe`即可，默认位置为`C:\Program Files (x86)\Rime\weasel-0.14.3\WeaselServer.exe`。不要手动将`WeaselServer.exe`设为开机启动，否则程序容易报错。
  不愿手动启动，可以使用 [WeaselServerAutostart](https://github.com/rockbenben/rime-WeaselServer) 脚本工具。将脚本放置于小狼毫「程序文件夹」内，并生成桌面快捷方式。将快捷方式移动至开机启动目录，Win10 默认位置为`%AppData%\Microsoft\Windows\Start Menu\Programs\Startup`。脚本国内下载：[https://wwx.lanzoux.com/if3znkka01g](https://wwx.lanzoux.com/if3znkka01g)

- **将用户文件夹置为同步文件夹，提示`有错误，请查看日志%TEMP%\rime.weasel.*.INFO`？**

  不要将用户文件夹完整置为同步文件夹，会导致进程冲突，日志中有提示`另一个程序正在使用此文件，进程无法访问`。出错后，关闭任务管理器中的`WeaselServer.exe`进程，然后重新执行小狼毫算法服务。

- **中文输入法的候选框闪烁，无法显示候选词？**

  排除键盘硬件问题，拔除或更换键盘，确认问题是否复现。Word 2016 下候选框闪烁参考 [issue 228](https://github.com/rime/weasel/issues/228)。

- **打错了字，之后就总在前排出现，如何删除错误「上屏」的词？**

  将选字光标移到要删除的词组上，再按下 Shift+Delete 或 Control+Delete。

- **官方文档中的`%APPDATA%\Rime`是用户文档吗？为什么有时位置不同？**

  `%APPDATA%\Rime`是小狼毫默认的用户文档。如果在安装时修改了用户文档位置，右键点击任务栏小狼毫图标，选「用户文件夹」，会出现当前的位置，所有文档只需在这里修改。

- **emoji 按教程设置，但始终无法显示？**

  暂无解决方法。官方文档、三种集成词库都试过了，同样无法显示。特殊字符可使用 SuperRime 词库的 symbol 输出。

- **SuperRime 词库安装后，无法完整触发特殊符号？**

  SuperRime 词库自带的标点及特殊表情设置有问题。在`luna_pinyin_simp.custom.yaml`植入以下代码。

  ```
  patch:
  #标点及特殊表情
  'punctuator/import_preset': mysymbols
  'recognizer/patterns/punct': "^/([a-z]+|[0-9])$"
  ```

### **参考资料**

- [30 分钟搞定 自由输入法 RIME 简明配置指南](https://www.jianshu.com/p/296bba666604)
- [小狼毫 RIME 输入法配置](https://www.dazhuanlan.com/2019/10/06/5d995d43e4432/)
- [Rime 输入法—鼠须管 (Squirrel) 词库添加及配置](https://www.jianshu.com/p/cffc0ea094a7)
- [四叶草拼音输入方案](https://github.com/fkxxyz/rime-cloverpinyin)
- [小狼毫 [rime_win][眀月拼音] 简单配置方法](https://blog.csdn.net/qq_42204675/article/details/86422450)
- [小狼毫自定义短语-Rime-双拼](https://blog.csdn.net/neninee/article/details/83692270)
