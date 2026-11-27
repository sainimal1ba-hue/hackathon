# WARPLAN — HEROKILL

**PS-WEB-01 · Mini-Cloud Hosting Platform · Clash of Commits（2026-12-04/05 · VIT Chennai）**

> 一句话宣讲：**HEROKILL —— the mini-cloud you can watch die and resurrect in one click.**
> 我们建的迷你云：你亲手 push 上线、亲手毒死、再看着它在十秒内复活、拖回时间轴定格死因。

---

## 1. 战场摘要（详见 intel.md）
- 24h 线下黑客松，4–5 人战队；三段赛制：Round 0 匿名 10 页 deck（约 120–150 队存活）→ Round 1 "The Raid" 24h 构建（前 8 晋级）→ Round 2 决赛**观众投票加冕**。
- 评审六维：功能面 / 24h 可行性 / Demo 震撼力 / 差异化 / 观众缘 / 团队契合。
- 离线铁律：自家笔记本 + 路由器 LAN + 投影仪；会场 Wi-Fi 视为已死；零第三方 API、零 AI 推理、零现场交互基建。

## 2. 为什么是这道题（Round 1 裁决 46/60）
- 唯一一遭"每 1 小时都买剧场而不是买学习曲线"的题：98 个测试、CI、Docker 部署是本队日常，24 小时全花在打磨与排练。
- 全场最安静赛道：Docker 重活吓退休闲队；敢选的一半死在 container-in-container，我们用宿主 socket 绕开。
- 竞品全是"部署按钮"：死亡剧场与复活时间轴无人认领。

## 3. 核心叙事：死亡与复活
"你亲手 push 上线 → 亲手下毒 → 平台尖叫 → 自动回滚 → 容器复活 → 拖回时间轴定格死因。"

**KILL SHOT（那 60 秒）**：评委亲手毒死自己亲手部署的版本 → 红墙长鸣 → 全场齐声倒数 → 00:07 绿色脉冲复活 → playhead 回拖定格"它死于这行日志"。一只手杀，一只手赦，满场嘴喊。

## 4. 最终功能名单（Round 2 皇帝终裁，详见 round2-feature-war/emperor-verdict.md）

### 4.1 TABLE STAKES（去重九项——人人都有，我们做得更狠）
| # | 功能 | 执行要点 |
|---|---|---|
| 1 | git push 即部署 | bare repo + post-receive hook，评委亲手敲；预烤镜像层伪装热启动 |
| 2 | 零配置栈探测 | 扫 composer.json / package.json / 静态文件，规则表直出 Dockerfile + 进程拓扑 |
| 3 | 自定义域名 + HTTPS | 预铸 wildcard 证书 + 本地 DNS override，离线亮绿锁 |
| 4 | 健康检查 | 轮询 + 连续失守门限判定；心跳入时间轴 |
| 5 | 自动回滚 | 绿色镜像常驻缓存，<10 秒切回 |
| 6 | 混沌四型 | 毒代码 / 依赖爆炸 / 内存泄漏 / kill -9，全数 cgroup 笼锁 |
| 7 | 死亡记录 | exit code 验尸（137=OOM、143=SIGTERM），Death Certificate 编号入册，落 SQLite 事件流 |
| 8 | 容器状态墙 | 大字三色网格，三十米可读，1s WebSocket 推送 |
| 9 | 日志流 | stdout 瀑布可 grep，同源落事件表 |

### 4.2 SIGNATURE MOVES（五式，人无我有）
| # | 代号 | 出自 | 一句话 | demo 时刻 |
|---|---|---|---|---|
| 1 | JUDGE'S TRIGGER 评委之铳 | KILLSTREAK | 评委亲手处刑、亲手赦免 | 红灯频闪中按下复活，十秒心跳回归 |
| 2 | THREE-SECOND LIFT 三秒起飞 | ARCHITECTUS | 评委亲手 push，三秒亮锁 | 键盘在他手里，震撼也在他手里 |
| 3 | RESURRECTION WINDOW 复活倒计时 | FURIOSA | 红墙压屏全场齐喊十、九、八 | 计时定格 00:07，绿色脉冲复活 |
| 4 | SCRUB THE INCIDENT 事故拖拽 | CHRONOS | playhead 回拖，日志肉眼倒流（最小 scrubber 版） | 终端文字当众倒流，定格死因行 |
| 5 | THE ROAR 声浪处刑 | FURIOSA | 三容器编号，喊声最高者当场处决 | 投票的彩排 |

已斩：扩容滑块（后台管理系统气质）；16x 逐帧时间旅行（降级为回放附属）。第一波六学派海选亦斩：THE SÉANCE 流量重放（等于再写第二个产品）、TWIN PARADE 蓝/绿双版本（5 小时买 200ms 的无人可见）、BRANCH PREVIEW 三版本并行（台上状态翻三倍）、APP STORE 一键 starters（离题）、真随机轮盘（台上开随机之枪）、CRT 扫描线特效（截图好看，后排看不清）。完整斩杀令见 `round2-feature-war/emperor-verdict-wave1-six-schools.md`。

### 4.3 STRETCH 军械库（第 20 小时全绿才领取，按序牺牲；源自 Wave-1 六学派裁决 Tier 2）
| # | 代号 | 一句话 | 工时 |
|---|---|---|---|
| 1 | GATE OF GREEN 绿门 | 仓库自带测试套件在构建内运行，红则拒绝上线——"no green, no live" | ~4h |
| 2 | DEMO DIRECTOR MODE 导演台 | 隐藏热键逐拍跳转——彩排挂具，提前造好 | ~2h |
| 3 | GREEN MEANS LIVE 绿脉冲 | 合成流量绿色脉络随心跳明灭，回滚落地即回归 | ~3h |
| 4 | .herokill.yml 契约 | env / 健康检查 / 回滚策略声明在仓库里——复活即契约 | ~3h |
| 5 | THE CAGE 牢笼 | --cpus / --memory 硬限；现场部署死循环应用，仪表飙升变红，当场扼杀 | ~3h |

## 5. 24 小时施工序（Round 1 现场执行）
| 阶段 | 里程碑 |
|---|---|
| H0–2 | 冻结地基：事件表 schema + append-only 开机落库；四型混沌裸跑通 |
| H2–6 | 出生链：push → hook → 构建 → 绿灯 → 亮锁；镜像预烤入库 |
| H6–10 | 死亡链：注入 + 门限 + RED CODE 红灯 + Death Certificate |
| H10–14 | 复活链：绿色缓存回滚 + 状态墙 + 心跳图 |
| H14–17 | 时间轴：最小 scrubber（日志倒流 + 回放）；全量时间旅行即刻斩首 |
| H17–18 | 剧本冻结：三分钟节奏表接管；音效 / 证书 / repo 全预烤本地 |
| H18–22 | 全链彩排进 CI：含评委怯场预案、dead-man switch |
| H22–24 | 压测、备份镜像、睡眠 |

角色分工（4–5 人）：A 平台工程（hook/构建/域名，不碰 UI）· B 事件流 + 回滚引擎 · C 前端（状态墙/scrubber/剧场）· D 混沌 + 验尸引擎 · E 导演 + 评委交互 + 预烤资产（4 人时 E 并入 A）。

## 6. Demo 剧本（三分钟节奏表，FURIOSA 军规）
| 时间 | 幕 | 内容 |
|---|---|---|
| 0:00–0:15 | COLD OPEN 冷启动 | 黑场，巨幕终端一行 `$ git push`，状态墙逐格点亮 |
| 0:15–1:00 | THE HANDS 借来的手 | 评委亲手 push，日志瀑布，三秒亮锁 "deployed by 评委" |
| 1:00–1:40 | GREEN GATE 绿门 | 探活门控展示：毒版本被绿门拦截、流量纹丝不动（第一次死亡，无声） |
| 1:40–2:00 | THE MURDER 亲手下毒 | 评委按下混沌武器卡；RED CODE 红墙长鸣 |
| 2:00–2:40 | RESURRECTION 复活倒计时 | 全场齐喊十、九、八；回滚；00:07 绿色脉冲复活，计时定格 |
| 2:40–3:00 | AUTOPSY + REPLAY 验尸回放 | 宣读 Death Certificate（死于 OOM，享年 4 分 12 秒）；playhead 回拖，日志倒流定格死因行 |
| 加时 | THE ROAR 声浪处刑 | 若有 5 分钟：三容器编号，喊声最高者处决——投票彩排，终幕 |

（3 分钟版砍 THE ROAR；5 分钟版留作终幕。）

**观众互动兜底梯**：预设队友坐第三排"应征"上场 → 若全场僵住，主持人亲自按下同一套攻击（剧本零损失）→ 终极兜底：定时自尽的"拒死者"演示应用全程在状态墙上循环赴死复活（混沌面板定时注入 + 复活计数器），剧场永不停场；WS 中断 → 下一拍边界整页重载（时间轴已落库，一秒不丢）。

## 7. Round 0 十页 deck（英文，匿名提交）
| 页 | 标题 | 要点 |
|---|---|---|
| P1 | Cover — HEROKILL | "The mini-cloud you can watch die and resurrect."（匿名代号） |
| P2 | The problem | Deploying is fragile; every platform hides failure. We put failure on stage. |
| P3 | The obvious build | Push-to-deploy mini-cloud — what every clan will ship. |
| P4 | Our twist | Death & Resurrection: poison it live, watch the autopsy, resurrect in seconds. |
| P5 | Signature moves | JUDGE'S TRIGGER / THREE-SECOND LIFT / RESURRECTION WINDOW / SCRUB THE INCIDENT / THE ROAR |
| P6 | Architecture | bare repo + hook → Docker API + cgroup cages → Caddy wildcard TLS (pre-minted, offline) → WebSocket event bus → SQLite append-only timeline |
| P7 | The resurrection timeline | Every second recorded: logs, health, versions; scrub your incident like a video. |
| P8 | 24h build plan | H0–H24 phase table; CI-rehearsed failure drills; test-gated deploys. |
| P9 | Demo storyboard | The 3-minute beat table: cold open → judge's push → poison → countdown → 00:07 revival → autopsy. |
| P10 | War declaration | "You deployed it. You poisoned it. It's still standing. HEROKILL." |

## 8. 风险登记册
| 风险 | 对策 |
|---|---|
| 现场 docker build 陷泥潭 | 12 月 3 日镜像预烤入库；失败自动降级"预制层 + 差异层"，界面全链路不变、观众无感 |
| 死亡系统当场暴毙（毒不死/回滚卡壳/评委怯场） | cgroup 笼锁（内存上限 + 隔离网络）；保底绿色镜像常驻；注入失败降级 kill -9 硬杀；评委怯场主持人接刀 |
| 时间轴空白或 UI 失控 | 开机即落库（append-only 事件表）；scrubber 最小化；预烤"黄金事故"录制兜底 |
| 会场 Wi-Fi 死透 | 全链路本地：预铸 wildcard 证书 + DNS override，离线亮绿锁 |
| 剧本超时/忘词 | 第 18 小时剧本冻结、只修不添；一人专任导演；计时员 + 全幕彩排三遍 |

## 9. 六维自检（战前照镜）
- **功能面**：9 项 table stakes + 5 式独门 + 5 件 stretch 军械——满地武器。
- **24h 可行性**：全是日常栈（PHP/JS/TS + Docker + CI），每式标注真工程 / 剧场包装分层。
- **Demo 震撼力**：60 秒 KILL SHOT = 亲手处刑 + 全场倒数 + 定格验尸。
- **差异化**：死亡剧场 + 验尸叙事 + 任意秒回放——赛道内无人认领。
- **观众缘**：评委亲手参与 + 全场齐喊 + 声浪处刑（投票彩排）。
- **团队契合**：CI / 测试纪律直接变成"绿门"与部署门控。

---

*Ruled by the Emperors of Round 1 & Round 2（功能之战两波：Wave 1 六学派海选出初稿名单 → Wave 2 四学派终审定律，战史全档见 `round2-feature-war/`）; scribed into law by the war room. 下一战场：把 §7 铸成十页匿名 deck，交上 Round 0。*
