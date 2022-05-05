---
layout:       post
title:        "直播完全攻略：从直播小白到网红达人"
subtitle:     "小白如何开直播？"
date:         2021-03-26
author:       "Benson"
header-img:   img/post-bg-20180108.jpg
header-mask:  0.3
catalog:      true
categories:
    - 工具
tags: 
    - 直播
---
直播已经成为最强大的传播方式，是个不错的尝试。本文会从硬件、软件、技巧三方面，让你迅速直播入门，开始自己的直播之旅。

## 直播硬件

直播设备主要有为视频采集（摄像头）、音频采集（收音话筒）、稳定器（三脚架）。

### 摄像头

视频采集可使用桌面摄像头、手机、微单相机。

桌面摄像头价格为 50～1000 元不等，但实际效果没太大区别。个人体验罗技 C930 后，发现画面模糊不清晰，反馈给客服，得知画质不清是桌面摄像头的通病。不管是几十的廉价摄像头还是上千的罗技 c1000，它们**实际像素多为 200 万**。各类宣传中高于 200 万的像素是软件放大的结果，画质没有本质性改变。推荐个人用户选择 100 元自动变焦摄像头即可。桌面摄像头搭配三角架角度更佳，建议购买时注意**摄像头是否有三脚架接口**。

手机一般为室外直播使用。如果没有桌面摄像头，又希望使用电脑直播，可以参考 NDI、IP Webcam 教程，将手机充当桌面摄像头。

- 不推荐：国内大多使用无他伴侣，但实际应用中问题多多。手机摄像头容易与直播应用断开 (10 分钟)，摄影角度难以控制，无法使用 facerig 等变脸应用，无法长时间直播 (2 小时)。
- NDI 最为稳定，可自由调节拍摄参数，为商业收费应用，安卓手机测试可用[调试 APK](https://wwe.lanzoup.com/iQCMh00b946b)。刚打开 NDI 应用，不会马上连接，等待 NDI 应用周边出现绿框或红框时，才可以正常链接视频。
- **IP Webcam** 推流，稳定性一般，免费版足够个人使用，点击下载 [IP Webcam APK](https://wwz.lanzouf.com/iT6pH01tj7yb)。IP Webcam 设置网页将流质量调整至 90%，能有效减少卡顿。IP camera 耗电低，适合手机长时间直播，支持视频与浏览器等方式。
  - OBS 场景 - 来源 - 视频源，「输入」项中填入 IP Webcam 视频地址，例如`http://192.168.2.234:8080/video`。
  - OBS 场景 - 来源 - 添加浏览器，「URL」项中填入 IP Webcam 浏览器全屏地址，例如 `http://192.168.2.234:8080/jsfs.html`。注意：浏览器退流，容易出现闪屏。

微单相机能达到真正的高清直播，索尼、佳能均有配套软件连接。唯一的缺点是价格偏高，配上镜头的微单直播方案，通常需要 2 万，建议有微单的人使用此方案。

### 收音话筒

话筒价格从 10 元到几千元不等。低价麦克风存在收音范围窄、不清晰、多噪音等问题，适合新人测试使用。如果对收音效果有要求的话，推荐声卡和话筒搭配使用。声卡 + 话筒预算需 1000+ 元，市面上几百元的山寨声卡还不如直接使用手机收音。

### 三脚架

三脚架价位为 10～500 元不等，效果无明显区别，按预算选择。桌面三角架高度选择 55cm 足够。

### 补光灯

柔光灯、环形灯适合露脸主播，对颜值提升巨大。

如果带眼镜的话，环形灯会使镜片会出现光圈，影响视野。推荐近视用户，在上方放置小型补光灯代替环形灯。

## 直播软件

### OBS 直播

最流行的直播软件是[OBS](https://obsproject.com/)，这是一款开源免费软件。市面上大部分直播软件都基于 OBS。

OBS 可对直播界面进行重加购和美化，如对多个摄像头进行取景，添加文字、窗口、媒体采集等。市面有成熟的直播美化插件，如[跨播](https://console.kuabo.cn/widgets?id=20)、[智能云插件](http://zbmate.com/)。

直播界面模糊，需将`文件－设置－输出－串流 - 视频比特率`设为 4000-6000 Kbps，`文件－设置－视频`中的输出分辨率确保与基础分辨率一致，游戏直播将`常用 FPS 值 (帧率)`从 30 调整到 60 。

如果电脑配置超过 5 年，可考虑使用两台主机 (PC、手机均可)，NDI 双机推流，避免卡顿。

**常用滤镜：**

- 色度键：一般是在抠绿幕的时候用到这个滤镜，通过关键的颜色我们可以将特定的颜色抠成透明，例如将绿幕背景抠掉，换成更有趣的背景。
- 色彩校正：通过调整伽玛度、对比度、亮度、饱和度等信息调整摄像头的显示效果。
- 裁剪/填充：对来源的显示进行裁剪，剪去多余的部分。
- 增益：当麦克风声音过大或过小时，可以通过增益滤镜调整音量，但是不宜设置数值过大，容易造成声音失真。
- 噪音阈值：当背景有噪音时，可以通过设置噪音阈值控制，但是并不是传统意义上的降噪，只能解决部分问题。

![色度键滤镜一键抠图](http://tc.seoipo.com/20210328235013.gif)

**[常用插件](https://obsproject.com/forum/resources/categories/obs-studio-plugins.6/)：**

- [StreamFX](https://github.com/Xaymar/obs-StreamFX/releases)：支持更多的信号源、滤镜和转场效果，如：模糊滤镜
- [OBS Shaderfilter](https://obsproject.com/forum/resources/obs-shaderfilter.775/)：文字图片特效滤镜
- [virtualcam](https://obsproject.com/forum/resources/obs-virtualcam.949/)：能让来源单独输出虚拟摄像头，仅支持横屏场景，在竖屏中使用会奔溃
- [NDI](https://obsproject.com/forum/resources/obs-ndi-newtek-ndi%E2%84%A2-integration-into-obs-studio.528/) : 局域网视频无线传输技术 NDI 插件
- [multi-rtmp](https://github.com/sorayuki/obs-multi-rtmp)：OBS 多地址推流，同时在多个平台上进行直播
- [Asynchronous Source Duplication](https://obsproject.com/forum/resources/asynchronous-source-duplication.1483/)：复制来源以同时作用多个场景，复制源间会有延迟
- [VLC](https://www.videolan.org/vlc/)：非插件，但安装 VLC 64 位后，才能使用「VLC 视频源」(播放列表)

**进阶插件**：

- [Advanced Scene Switcher](https://obsproject.com/forum/resources/advanced-scene-switcher.395/)：使用 "宏 "来自动完成各种任务，按条件切换场景、来源
- [Move transition](https://obsproject.com/forum/resources/move-transition.913/)：记录来源的位置变化，生成元素移动的动画效果。如，视频演讲时，相机从右下移动到中央。
- [Transition Table](https://obsproject.com/forum/resources/transition-table.1174/)：场景切换效果，设定不同场景间的切换规则
- [Source Dock](https://obsproject.com/forum/resources/source-dock.1317/)：为单独场景或来源建立控制栏，能小窗口预览场景
- [Source Copy](https://obsproject.com/forum/resources/source-copy.1261/)：更方便地复制、保存场景设置
- [Scene Collection Manager](https://obsproject.com/forum/resources/scene-collection-manager.1434/)：自动备份场景，防止误操作
- [Audio Monitor](https://obsproject.com/forum/resources/audio-monitor.1186/)：将来源声音输出给指定设备播放，方便单独调节音量，能让主播与观众听到不同的音频效果
- [Downstream Keyer](https://obsproject.com/forum/resources/downstream-keyer.1254/)：切换场景时，置顶指定场景
- [Multi Source Effect](https://github.com/norihiro/obs-multisource-effect)：滤镜效果？
- [Teleport](https://github.com/fzwoch/obs-teleport)：NDI 替代品，局域网设备推流到直播
- [spectralizer](https://github.com/univrsal/spectralizer)：音频频谱，用滤镜「图像掩码」的「混合图层」给频谱遮罩滤镜
- [obs-websocket](https://obsproject.com/forum/resources/obs-websocket-remote-control-obs-studio-from-websockets.466/)：远程控制插件
- transition matrix 过渡矩阵
- scrab 截图
- lower third in html/css 文字运动特效
- input overlay 输入显示
- motion-effect 动画效果
- reply source 回放控制
- advanced scene switcher 高级场景切换器
- PTZ controller PTZ 摄影机云台控制器
- [Animated captions](https://obsproject.com/forum/resources/animated-captions-with-obs-controller-and-a-preview-function.1407/)：自定义弹幕功能，无漂浮弹幕，适用较少
- [Background Removal](https://github.com/royshil/obs-backgroundremoval)：无绿幕移除背景，需搭配神经网络环境

**使用技巧：**

1. 来源使用窗口采集时，窗口不能最小化，否则窗口会卡住不同步。
2. 不同界面切换可使用 OBS 的工作室模式，避免让观众看到不完整的直播画面。
3. OBS 场景 - 来源 - 混音器，右键点击调整「高级音频属性」。默认音频为「关闭监听」，音频仅直播间观众输出，主播听不到。仅监听 (输出静音)：主播能听到，但观众只能通过主播话筒的收音听到，音量会特别小。监听并输出：主播和观众都能直接听到，但如果主播开了话筒，话筒音量容易被该音频盖住，无法听清。修改音量或使用滤镜并不能降低输出音频音量。

### 小葫芦弹幕助手

国内直播推荐搭配[小葫芦弹幕助手](https://www.obsapp.com/apps/danmupro/)，可以显示网友的互动、打赏，尤其适合游戏直播。

如果无需在直播界面中显示弹幕，建议不要安装小葫芦弹幕插件。安装弹幕助手后，会影响 OBS 窗口捕获功能，无法抓取基于 Electron 的应用界面。如果窗口捕捉黑屏，删除`C:\Program Files\obs-studio\obs-plugins\64bit`目录内的`CalabashDanmuPlugin.dll`、`CalabashWinCapture.dll`、`ObssDanmuInfo.dll`，重启 OBS 即可恢复。但当下次使用弹幕助手时，这三个文件会自动安装，黑屏问题复现，只能重新删除指定文件。

小葫芦直播助手是基于 OBS 再开发的直播软件，集成了 OBS 和弹幕助手的功能，适合新手使用。进阶使用推荐 OBS + 小葫芦弹幕助手。

### YY 开播 (美颜)

OBS 美颜需借助第三方插件，这里用的是 YY 开播。

YY 开播调用摄像头摄像，完成美颜。然后 OBS 调用 YY 开播视频源，完成视频剪辑和人像抠图。下次启动 OBS，软件会自动调用 YY 开播，无需另外配置。

**注意**：YY 开播中除美颜外，不用开启虚拟背景、虚拟形象等功能，否则直播中的画面背景无法透明化。运动中不要开美颜，延时严重。

## 直播娱乐

### 虚拟主播

如果不想录脸或原声直播，可以搭配应用 MorphVOX Pro(变音)、facerig(变脸)、prprlive(变脸)，但对效果不要报太大希望，娱乐就好。

MorphVOX Pro、神舌等软件变声器对使用者的语气要求较高。我尝试了淘宝的精调，调整后效果依旧无法仿真。店家发来语气教程意义不大，初学者很难入门，硬件变声器效果类似，过于机器人，不推荐。

facerig 通过对五官的动作捕捉，让卡通脸的表情进行同步变化，不能对头部以下的部分进行捕捉和同步。facerig 在百度的首个搜索结果是虚假官网，不要在上面进行购买，直接去 Steam 购买即可。直播中，facerig 需打开「切换广播」，否则 obs 中的窗口会显示黑屏。

![facerig 演示图](http://tc.seoipo.com/20210329092154.gif)

prprlive 是国内的变脸软件，基础版免费，同样在 steam 销售，都可以试下。变脸软件会占用较高的 cpu，建议电脑在 5 年内。

### 动态背景

直播中场景比较单调，建议增加些动态背景。使用带绿幕的视频画面，就可以单独展示所需要的动态素材。

除了动态视频，还可以借助类虚拟主播技术，达到交互效果。

[Bongo Cat Mver](https://d.appinn.com/bongo-cat-mver/) 实时同步键盘与鼠标状态，增加直播趣味性。如果使用全键盘同步，注意打乱映射内容，防止泄漏隐私。

## 直播技巧

1. 选题
    - 最新热点：热榜话题、新品发布等；**看到热点直接开始，用现有内容来做，抢黄金流量时间**；
    - 热门问题：关注、互动较多；
    - 系列直播：知识娱乐化。
2. 命题：关键词搜索站内热门问答，参考标题。**直播准备 15－20 分钟话题，然后循环说**。没人的话，也别停，否则进入流量会变少。
3. 环境：环境灯光要亮；灯光要在脸部前方。
4. 时间：选择白天等冷门时间，**长期并固定时间直播，稳定开播频次与时间段**。新人直播有流量扶持，初期没有观众也要坚持开播。直播保持 2.5 小时以上，电商保持 3.5 小时以上才会有官方稳定推流。
5. 直播预告：开播前一定要先发预告
    - 提前发布视频，在直播前二至三小时发布预告视频，可以有机会让更多观众通过视频进入到直播间看到你；
    - 开播页添加特色信息，在每场开播时，一定要记得在开播页上提前设置好封面标题并勾选定位，优质有特色的封面能够提升观众对直播间的点击欲望，但应尽量选择本人或和内容相关的图片作为封面；
    - 打开定位，将会有更多的同城观众看到你的直播间对直播间提升流量是非常有好处的。如果你不知道什么是好的封面标题可以多参考其他观众较多的直播间。
6. 互动：主动互动，时常口播；直面镜头，展现自我。
    - 暖场：开场前 10 - 15 分钟可先与用户互动，等人多了再正式开始
    - 有新观众进入直播间时，要主动欢迎
    - 有意识地引导用户关注、互动
    - 要「读出」用户的弹幕，再做出回答
    - 及时感谢礼物
7. 直播间优化方向
    - 保持长时间和持续开播
    - 优化直播标题 + 直播封面 + 直播间背景
    - 多参与直播平台的官方活动
    - 多使用直播道具，适当购买直播推流产品
    - 多拍优质短视频引流

### 直播定位

以下内容主要摘录自知乎直播官方建议，新主播可参考使用。

```
快速入门一个新领域的捷径：市场调研和自我定位，也就是观察头部主播、找到对标主播。

换位思考：
* 你喜欢哪类型的直播？喜欢谁的直播？为什么？每个主播至少列出 3 个吸引你的点
* 你不喜欢哪种直播？为什么？
* 如果是你做直播，你希望是什么样的？你的底线是什么？有什么顾虑？顾虑和目标比起来，孰轻孰重？

自我认知：
* 我是谁：我的职业/身份是什么
* 面向谁：目标用户画像：性别、年龄、兴趣、收入、消费能力、性格特征等
* 我能提供什么：核心竟争力：陪伴？专业知识？丰富经验？渠道资源？
* 解决目标用户什么问题：排遣寂寞？选购答疑？
```

刚开始直播，会存在很多疑问和顾虑，效果也不会有多好。但要勇敢去尝试新事物，只有不断开拓，我们的人生才会有更多的可能性。
