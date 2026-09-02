---
name: embodied-intel-updater
description: 高质量具身智能知识库增量更新与深度研究工作流。针对 GitHub 仓库 DemonDamon/embodied-intelligence-nexus，从论文、会议、官方项目页、GitHub、模型/数据集和公司研究发布中筛选、核验并归档最新进展；强制补足理论推导、实验设计、复现资源和证据边界。Use when a user asks to update, catch up, verify, deep-research, or archive recent embodied AI, VLA/VLM, world model, robot manipulation, humanoid, imitation learning, reinforcement learning, simulation, dataset, benchmark, or industrial platform developments.
---

# Embodied Intelligence Nexus Updater

将 `DemonDamon/embodied-intelligence-nexus` 更新为可追溯、可复核、适合深入学习的具身智能研究库。

## 目标与固定约定

- **仓库**：`https://github.com/DemonDamon/embodied-intelligence-nexus`
- **课程目录**：`course/01-*` 至 `course/08-*`
- **研究专题目录**：`researches/`
- **作者**：所有新增 Markdown 使用 `> 作者：Damon Li | 更新日期：YYYY年M月D日`
- **Git 身份**：`Damon Li <DemonDamon@users.noreply.github.com>`
- **资源优先级**：论文、官方项目页、官方代码/模型/数据页优先；媒体和公众号只作线索。
- **默认发现源**：当用户提出未限定来源的“更新”指令时，必须扫描 `references/wechat-discovery-sources.md` 中的 P1 固定来源；它们只用于发现候选，全部技术事实仍须回溯 A/B 级来源。

在开始前读取：

1. `references/source-registry.md`：信源等级、长期入口和发现源。
2. `references/wechat-discovery-sources.md`：固定公众号合集、默认更新触发动作、去重和台账字段；仅在“更新”“增量更新”“检查近期更新”等任务中读取。
3. `references/theory-and-experiment-rubric.md`：推导补全、实验设计和复现审计标准。

## 非协商质量规则

1. **不得用二手内容证实技术事实。** 微信公众号、媒体、知乎、CSDN、榜单和营销页只能用于发现实体；必须回溯至 A/B 级来源。
2. **不得猜测资源链接。** 未找到官方 GitHub、权重、数据集、许可证或论文时，明确写“未公开”或“未发现可核验一手来源”。
3. **不得把公司博客写成同行评审结论。** 使用“官方披露”“技术报告”“预印本”“同行评审论文”精确标注证据状态。
4. **不得只复述摘要。** 每个核心论文/报告都要补足问题设定、符号、目标函数、推导中间步骤、训练/推理流程、实验协议、失败模式和复现条件。
5. **不得直接比较不可比结果。** 任务、本体、数据、动作空间、硬件、成功定义、trial 数与安全过滤不同的结果必须分开呈现。
6. **不得将令牌写入仓库、文档、命令输出或提交历史。** 仅在当前会话配置认证；推送后清除临时凭据。

## 工作流

### Phase 0：同步、界定、输入登记与固定发现源扫描

1. 安全定位现有工作目录；若已是 Git 仓库则 `git pull --ff-only`，否则克隆仓库。不要不经检查删除目录。
2. 配置 Git 作者信息并检查 `git status`、最近提交、根目录与章节 README。
3. 从根 README、章节 README 或 Git 日志确定上次覆盖日期，设定扫描窗口。
4. **若用户提出“更新”“增量更新”“检查近期更新”而未排除公众号来源**，读取 `references/wechat-discovery-sources.md`，扫描其中全部 P1 固定合集的新增/近期可见文章；以 URL、标题和原始实体去重。用户指定时间范围、主题、文章或“只看某来源”时，按用户限制缩小范围。
5. 把用户提供的 URL、固定合集命中的文章、实验室/公司主页、论文或附件登记为临时 `research_scan_notes.md`，字段至少包括：`输入URL`、`发现时间`、`主题`、`实体`、`建议章节`、`证据等级`、`需要回溯的原始来源`。对固定公众号条目额外记录 `合集名称`。
6. 对每一个输入链接保留溯源；不要因页面受限而丢弃线索。页面被限制时，以它的标题/实体做公开检索，再标注“原页未直接访问”。

### Phase 1：广度扫描与候选筛选

同时扫描学术与工业界，但分开打分。对于默认“更新”任务，先完成 `references/wechat-discovery-sources.md` 中 P1 合集的增量扫描，再以其中识别的实体扩展至学术和工业一手来源；不要把公众号标题或正文当作筛选后的事实。

| 方向 | 检索重点 | 需要获得的原始材料 |
| :--- | :--- | :--- |
| VLA / VLM | action representation、action chunking、cross-embodiment、post-training | 论文、项目页、代码、模型卡、真实机器人协议 |
| World / Action Model | video-action、latent dynamics、planning、scaling law、multi-agent | 论文/技术报告、训练目标、数据与 rollout 评测 |
| 操作 / 灵巧手 / 人形 | bimanual、whole-body、teleoperation、force/tactile、locomotion-manipulation | 本体规格、动作空间、控制频率、真机 trials |
| IL / RL / Sim-to-Real | behavior cloning、IRL、offline RL、MPC、domain randomization | 目标函数、数据 split、仿真参数、迁移协议 |
| 数据集 / Benchmark | robot dataset、motion capture、real robot benchmark | 数据卡、许可证、下载、评分函数、排行榜版本 |
| 工具链 | simulator、Isaac、MuJoCo、LeRobot、deployment | 官方仓库、文档、版本兼容、许可证 |
| 产业 | 公司模型、硬件、产品、赛事、部署 | 公司官方技术页/公告、SDK、代码/模型/数据、正式财报或监管文件 |

对每个候选按如下阈值筛选：

| 指标 | 要求 |
| :--- | :--- |
| 相关性 | 能映射到既有 8 个课程章节或 `researches/` 专题。 |
| 新颖性 | 位于扫描窗口内，或虽较旧但新开源/新基准/新正式版本使其值得补档。 |
| 证据强度 | 至少有一个 A 级来源；仅有 C 级来源的条目仅进入待核验台账。 |
| 学习价值 | 能提供新机制、严谨实验、可复现资源、重要失败模式或长期生态影响。 |
| 可操作性 | 明确提供或明确缺少代码、模型、数据、许可证与硬件要求。 |

### Phase 2：一手来源核验

对入选条目至少核验以下来源组合：

1. **论文型工作**：论文原文 + 作者/项目页 + 官方代码或补充材料；若涉及数据/模型，再加数据卡或模型卡。
2. **开源框架**：官方仓库 + 文档 + LICENSE + release/commit 活跃度；不要仅引用第三方教程。
3. **数据集/基准**：官方项目页 + 数据集卡/下载页 + 论文或任务/评分定义。
4. **工业模型/产品**：公司官方技术页面 + 官方新闻稿/文档；若无论文或权重，显式标为“官方披露，未独立复现”。

记录每个结论的来源等级、URL、页面标题、发布日期/版本号和访问日期。对外部链接使用网页读取或浏览器阅读正文，不依据搜索摘要定论。

### Phase 3：理论推导与算法重建

对每篇关键论文，按 `references/theory-and-experiment-rubric.md` 逐项补全。最低交付为：

1. **问题设定与符号表**：明确 $o_t,s_t,a_t,\ell,e,\mathcal D$ 等变量、可观测性和训练/部署信息差。
2. **完整目标函数**：从条件概率、MLE、ELBO、Bellman、policy gradient、flow matching 或 diffusion 的基本定义推导至论文损失，说明每项的监督信号、权重、梯度和用途。
3. **训练/推理算法**：分别描述输入、输出、动作块长度、采样/去噪步数、缓存刷新、控制频率和安全后处理。必要时给出伪代码。
4. **隐含假设与反例**：讨论时空同步、相机标定、动作空间、数据覆盖、模型短视界准确性、接触物理或域差等关键假设。
5. **证据边界**：若论文未给出关键超参数、推导或证明，写“基于论文公开目标函数的补充推导”，并说明作者没有直接给出什么。

可使用如下通用骨架，但必须替换成具体工作定义：

$$
\theta^*=\arg\min_\theta\;\mathbb{E}_{(x,y)\sim\mathcal D,t\sim p(t)}
\left[\mathcal L_{\mathrm{task}}(f_\theta(x,t),y)+\lambda\mathcal L_{\mathrm{reg}}\right].
$$

### Phase 4：实验设计与复现审计

每个核心文档必须回答：

- 任务数量与成功判定是什么？是否真机、仿真或混合？
- 数据来源、规模、模态、训练/验证/测试切分和泄漏风险是什么？
- 使用哪个机器人、本体 DoF、传感器、控制频率、动作表示和坐标系？
- 基线是否具备相同数据、预算、硬件、动作空间和安全过滤？
- trial 数、随机种子、均值/标准差/置信区间、失败例和消融研究是否报告？
- 代码、权重、数据、LICENSE、环境版本、训练硬件与成本是否公开？

将结果分为“论文报告”“官方披露”“自行基于公开目标函数的推导”“待核验”。缺失信息不能用推测填补。

### Phase 5：文档与归档

1. 优先落在最贴近的课程章节；若同一主题有 3 个以上强关联文档，创建 `{YYYY-MM}-{topic}/` 子目录并先写该目录 `README.md`。
2. 父目录 README 必须新增子目录与文档链接；根目录 README 需更新入口、树结构与更新时间。
3. 文档命名使用 `{chapter}.{next-index}-{english-slug}-{year}.md`；专题子目录可以使用语义化名称。
4. 每篇技术文档采用以下模板：

```markdown
# 标题

> 作者：Damon Li | 更新日期：YYYY年M月D日
> 证据状态：同行评审论文 / 预印本 / 官方披露 / 待核验

## 1. 结论与证据等级
## 2. 问题设定、符号与假设
## 3. 方法与完整推导
## 4. 训练和推理算法
## 5. 实验设计、基线与结果
## 6. 失败模式、局限性与复现条件
## 7. 代码、模型、数据与许可证
## 8. 参考资料
```

5. 事实性陈述使用 Markdown 参考式数字引文。资源表至少列出论文、项目、代码、模型、数据、演示、许可证、硬件/环境、开放状态。
6. 图示优先用 Mermaid 解释数据流、训练闭环、推理闭环或评测协议。仅在有必要时下载/生成图片，并记录来源与相对路径。

### Phase 6：质量验收与推送

1. 使用 `scripts/validate_research_docs.py` 检查新增文档的作者、日期、必要章节、引文定义、资源链接、内部链接及未核验标记。
2. 对默认“更新”任务，确认 `references/wechat-discovery-sources.md` 中每个 P1 集合已被读取，或已在永久台账中记录访问限制、最后检查日期和可见候选数；未发现更新不能以页面加载失败为依据。
3. 执行 `git diff --check`，检查所有父级 README 链接和根目录导航。
4. 从每类资源中抽样检查论文、代码、模型、数据、基准和项目页；HTTP 反爬或登录墙不等于资源失效，应注明已由浏览器/页面验证或访问受限。
5. 临时扫描笔记不得提交。`git add` 前再次检查不包含令牌、Cookie、`.env`、下载的受限数据或个人信息。
6. 提交信息明确月份和主题，例如：`docs: add verified 2026-08 embodied research updates`。
7. 推送前确认认证已有效；使用用户提供令牌时，只在当前会话内通过安全认证配置使用，完成后清除临时环境变量与本地明文凭据。

## 验收门槛

一次更新只有满足以下条件才算完成：

- 每个核心专题至少有 2 个一手来源；如没有，明确降级为线索台账。
- 每篇核心研究文档含理论/目标函数、实验设计、复现资源和局限性，而不是仅有背景与链接。
- 所有新增文件署名 Damon Li；所有子目录均从父级 README 可达。
- 质量脚本和 `git diff --check` 通过；未公开资源与未证实量化主张均明确标注。
- 变更已提交并推送，且远端分支状态已确认。

## 测试模式

触发“测试本 Skill”时，选择至少一篇有公开论文、代码/数据或项目页的真实条目，执行 Phase 1—6 的缩小版流程。测试报告必须展示：候选筛选、原始来源回溯、一个完整目标函数推导、实验审计表、资源开放状态和质量脚本结果。若任一项缺失，先更新本 Skill 或参考标准后重测。
