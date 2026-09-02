# 2026年8月具身模型、世界模型与真实评测更新

> 作者：Damon Li
> 更新日期：2026年9月2日
> 核验口径：优先使用论文原文、官方项目页、官方 GitHub、Hugging Face / ModelScope 与公司官网；微信公众号文章仅作为线索与出处追溯，不将未经一手来源证实的主张视为事实。

本专题归档 2026 年 7—8 月新增的具身基础模型、世界动作模型（World-Action Model, WAM）、人形机器人真实评测、开源 VLA 研究与仿真平台资料。内容将**论文证据**、**官方产品披露**与**未公开信息**分开处理，便于后续复核、复现与持续更新。

## 文档导航

| 文档 | 聚焦对象 | 可用资源 |
| :--- | :--- | :--- |
| [7.10 LingBot 与 FabriVLA](./7.10-lingbot-and-fabrivla-2026.md) | LingBot-VLA 2.0、LingBot-VA 2.0、FabriVLA 与 FabriGym | 论文、GitHub、Hugging Face、ModelScope、官方技术页 |
| [7.11 世界动作模型](./7.11-world-action-models-2026.md) | Khora、GEN-1.5、Dyna-2 | 论文、项目页、官方研究博客、演示页 |
| [7.12 人形 VLA 与真实硬件评测](./7.12-humanoid-vla-and-real-robot-evaluation.md) | UniBot-V1、Unitree G1、QUAR-VLA、Humanoid-VLA、CARP、VLA-Adapter、TrajBooster、OpenWBC | 赛事、提交规范、代码、模型页、项目主页 |
| [7.13 世界模型与具身仿真资源图谱](./7.13-world-models-and-simulators-resource-map.md) | World Models、Dreamer、MuZero、JEPA、IRIS、Genie、GAIA、DIAMOND、Genesis、Isaac Lab、MuJoCo、Habitat、AI2-THOR | 论文、开源基线、框架与基准入口 |
| [7.14 Xiaomi-Robotics-1 VLA](./7.14-xiaomi-robotics-1-vla-2026.md) | Xiaomi-Robotics-1、100K+ 小时 UMI 预训练、自动语言标注、RoboCasa365 SOTA | 论文、项目页 |
| [7.15 VLA 架构创新](./7.15-vla-architecture-innovations-2026.md) | NebulaVLA（双频+GESTURE-7）、AtVLA（自适应视觉细化）、Semantic Anchoring、Cross-View Action Consistency | 论文 |
| [7.16 VLA 后训练与 RL 微调](./7.16-vla-post-training-rl-2026.md) | ExToken（结构化探索）、Z-1（GRPO for flow-based VLA）、DEED（零售场景部署） | 论文 |
| [7.17 机器人世界模型](./7.17-world-models-for-robotics-2026.md) | Robot-Factored World Models、RoboWorld（神经仿真评估）、GeniWorld（可泛化交互世界模型） | 论文、项目页 |
| [7.18 人形世界动作模型](./7.18-humanoid-world-models-2026.md) | ω-0（latent predictive WAM + ω-HOME 数据集）、GigaBrain-WBC-0.5（行为世界模型） | 论文 |
| [7.19 VLA 训练范式与评测基准突破](./7.19-vla-training-paradigm-breakthroughs-2026.md) | Recap/π*0.6、OpenVLA-OFT、latent action 预训练、离散扩散/流匹配动作解码、HybridVLA、RoboDojo、LIBERO-PRO/Plus、RoboArena、AutoEval、vla-eval | 论文、OpenReview、官方博客（B 级标注） |
| [7.20 τ₀-VLA：世界模型引导测试时计算](./7.20-tau0-vla-world-model-guided-ttc-2026.md) | 分层子任务搜索、执行记忆、world-model-guided TTC、40 维掩码流匹配 | 论文、官方 GitHub、模型卡与示例数据；高层组件未完整公开 |
| [7.21 Lumo-2：潜在世界—动作模型](./7.21-lumo2-latent-world-action-alignment-2026.md) | latent world dynamics、三阶段动作预对齐、BAR 动作解码 | 技术报告与公司项目页；代码、权重和完整数据未公开 |
| [7.22 XCoT-VLA：可执行思维链驾驶 VLA](./7.22-xcot-vla-executable-cot-driving-2026.md) | 紧凑 Reason–Action token、确定性 FFN 路由、flow-matching 轨迹 | 预印本；相邻 X-World 为公司披露；代码/权重未核验 |
| [7.23 具身 MoE：VLA 与世界模型](./7.23-moe-for-vla-and-world-models-2025-2026.md) | AdaMoE-VLA 动作专家；Worldscape-MoE 异构控制 | 两篇预印本；AdaMoE 代码为 MIT，Worldscape 资源未核验 |
| [7.24 Masked Visual Actions 统一世界模型](./7.24-masked-visual-actions-unified-world-model-2026.md) | 像素空间动作掩码、前向 rollout、逆向动作生成 | 预印本、项目页、Apache-2.0 代码与权重入口 |
| [7.25 VLA/世界模型综述阅读图谱](./7.25-vla-world-model-survey-reading-map-2026.md) | VLA、世界模型、广义具身 AI 与 VLN 的边界 | 综述与资源入口；已撤稿 VLN 条目明确排除为主依据 |
| [7.26 PSG-JEPA：物理状态锚定](./7.26-psg-jepa-physical-state-grounding-2026.md) | static/dynamic grounding、JEPA latent 可辨识性、规划与真机操作 | 预印本、项目页、官方代码；数据依赖 LeWM/OGBench 路径 |
| [7.27 物理仿真器与世界模型](./7.27-simulators-and-world-models-survey-2025.md) | 显式仿真、学习型 dynamics、MPC 与 sim-to-real 的互补性 | 预印本 v3、Apache-2.0 资源仓；综述非统一实现 |
| [7.28 VA/VLA/WM/WAM：术语与闭环分类](./7.28-va-vla-wm-wam-taxonomy-2026.md) | 条件策略、预测动态、Cascaded/Joint WAM、Video-Action 消歧 | VLA 论文、WAM 预印本、LingBot-VA/2.0 论文与 Apache-2.0 代码；VA 非统一标准术语 |
| [7.29 Pointing-VLA：类型化空间读出](./7.29-pointing-vla-typed-spatial-grounding-2026.md) | 点、功能接触热图与视觉轨迹；OFG-PICK / Pointing-PLACE 执行合约 | 预印本；Embodied-R1.5 的代码/模型可用；Pointing-VLA 自身独立权重与训练 artifact 未发现 |
| [7.30 GlanceWAM：异步测试时想象](./7.30-glancewam-asynchronous-test-time-imagination-2026.md) | 异步 lookahead latent、3-class Prefix-LM、staleness-robust flow matching | 预印本、MIT 代码、21 GB 数据/权重 bundle 与模拟评测脚本；真机结果未见 |
| [7.31 Facet-0：动作—力矩预测的精密装配 VLA](./7.31-facet0-contact-rich-precision-manipulation-2026.md) | joint action–wrench flow matching、Action–Wrench Critic、contact-selective RL、受界局部适配 | 预印本、NTU/PINE 项目页、Apache-2.0 模型与 CC-BY-4.0 数据；训练代码未发现 |

## 证据等级

| 等级 | 说明 | 本专题中的处理方式 |
| :--- | :--- | :--- |
| A | 可公开访问的论文原文、开源仓库、数据/模型托管页或官方技术文档 | 可引用机制、实验与下载方式，并给出直接链接。 |
| B | 公司官方博客、新闻稿或赛事官方页面 | 作为公司披露或赛事规则记录，不等同于同行评审结论。 |
| C | 微信公众号、自媒体或转述页面 | 仅保留为线索来源；若无法得到 A/B 级交叉证实，会在“待核验”中标注。 |

## 关联的输入资料

本专题新增追溯了用户提供的 τ₀-VLA、Lumo-2、VLA-Perf、Patch Policy、Science Robotics 系统案例以及 Tesla/FSD/Optimus 相关的九篇微信公众号入口。通用溯源台账位于 [`researches/2026-08-wechat-source-followup/`](../../../researches/2026-08-wechat-source-followup/README.md)；Tesla 产业主张因适合独立的产业信息核验，归入 [`researches/2026-08-industry-platforms-claims/`](../../../researches/2026-08-industry-platforms-claims/README.md)。

本轮新增 PSG-JEPA、物理仿真器—世界模型综述及人类视频到 VLA 综述三项公众号线索；来源台账位于 [`researches/2026-08-wechat-embodied-source-followup-0825/`](../../../researches/2026-08-wechat-embodied-source-followup-0825/README.md)，其中人类视频主题归入第 5 章模仿学习。

本次新增 VA/VLA/WM/WAM 术语分类文档；其输入线索和来源链位于 [`researches/2026-08-wechat-embodied-source-followup-0827/`](../../../researches/2026-08-wechat-embodied-source-followup-0827/README.md)。同批“全模态具身数据”主题归入第 5 章。

本轮对近期权威论文与官方项目的增量扫描补充了 Pointing-VLA 与 GlanceWAM；候选筛选、来源等级、排除的单一来源条目及跨章节索引位于 [`researches/2026-08-authoritative-embodied-incremental-scan/`](../../../researches/2026-08-authoritative-embodied-incremental-scan/README.md)。

本轮默认更新已按 P1 固定合集和注册表权威入口完成增量扫描，补充 Facet-0；其来源、深蓝具身智能合集扫描记录、TrAct/UniArmL1 等观察候选与跨章节导航位于 [`researches/2026-09-default-embodied-incremental-scan/`](../../../researches/2026-09-default-embodied-incremental-scan/README.md)。

## 更新建议

后续新增内容应优先补充正式论文版本、可复现实验脚本、模型权重许可与真实硬件评测协议。对于仅有企业博客的模型，应在取得同行评审论文或开源资源前继续标记为“官方披露，尚待独立复核”。
