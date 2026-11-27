# Round 2 — School 2: ARCHITECTUS「筑云者」

*Feature War gladiator — 路线：平台真实感（push 即部署 · 零配置探测 · 域名 HTTPS · 指标面板 · 进程模型）*

---

**ARCHITECTUS「筑云者」**

**【出战宣言】**
硬核的奇观化只有一条路：把工程链路变成评委指尖的仪式。我不演示云——评委亲手 push，投影上滚过真实构建日志，绿灯亮起，容器复活。别人演云，我筑云；Heroku 怎么行为，我的黑板就怎么行为。这份「真」，是 24 小时内唯一无法伪造的护城河。

**【TABLE STAKES】**
- **git push 即部署**：bare repo 当 remote，post-receive hook 串起构建→容器→上线，commit 链 `git log` 当场可验——别人按按钮演，我们按协议真。
- **零配置框架探测**：扫 composer.json / package.json / 静态文件，规则表自动产出 Dockerfile 与进程拓扑——别人手写配置，我们生成配置。
- **自定义域名 + HTTPS**：预铸 wildcard 证书 + 路由器 DNS override，`*.cloud.lan` 离线照样亮绿锁。
- **指标面板**：直采容器 CPU/内存/请求量，1s WebSocket 推送——真采样曲线，非假动画。
- **日志流**：容器 stdout 汇聚成终端瀑布，可 grep、可暂停。
- **Procfile 进程模型**：web/worker/cron 一行声明，一键拉起。

**【SIGNATURE MOVES】**

**「THREE-SECOND LIFT」三秒起飞**
评委亲手敲 `git push demo main`，终端吐出构建日志瀑布，3 秒内域名亮锁、容器绿灯。别的队做「部署按钮」，我们做部署协议——hook、构建队列、健康门，一条不敢断的真链路。hook + build 是真工程；「3 秒」靠预烤镜像层把冷启动伪装成热启动（包装）。Demo 时刻：键盘在他手里，震撼也在他手里。

**「POLYGLOT RADAR」闻栈识码**
把 PHP、Node、静态三个仓库拖进同一入口，平台盲发探测、自动生成正确 Dockerfile 与拓扑。别队只敢演一个 happy-path 栈，识别器是平台内功。规则表是真逻辑，「盲发」是仪式感包装。Demo：三屏齐鸣，多栈同时起飞。

**「GREEN GATE」绿门**
新版本不直接接流量：探活通过才切流，失败拒之门外。自动回滚人人会喊，但「何谓健康、何时切流」的门控才是工程判断力。健康检查 + 门控全真，蓝绿目录结构简单可靠。Demo：投毒版被绿门拦下，流量纹丝不动——KILLSTREAK 的死亡戏，靠这道门才有重力。

**「SCALE SLIDER」扩容滑块**
评委亲手拖 1→5，容器块实时增减、负载均分、压测曲线应声起伏。扩容最像「云」，但没真实现的人绝不敢让观众拖。compose replicas 真实现，压测脚本打本机。Demo：弹性具象成一次拖拽。

**【KILL SHOT】**
让评委亲手 `git push`，三秒绿灯——全场只有这一刻，「云」从展品变成他掌中之物。点名放话：KILLSTREAK 的尸体必须躺进我绿的容器才吓人，CHRONOS 的时间线必须卷我真实的日志才有纵深，FURIOSA 的剧场必须踩在我的钢筋上才立得住——没有筑云者，三位全是纸糊布景。观众投给指尖那 3 秒。

**【RISK REPORT】**
最大风险：真实 docker build 在现场被磁盘、镜像层、网络命名拖进泥潭——「真」最贵。对策：镜像与依赖 12 月 3 日预烤入库；构建失败自动降级为「预制层 + 差异层」模式，界面全链路不变、观众无感；CI 里已跑通的 Docker 纪律原样搬进 LAN。真东西早该在 CI 里绿着——我们只是把它搬上舞台。
