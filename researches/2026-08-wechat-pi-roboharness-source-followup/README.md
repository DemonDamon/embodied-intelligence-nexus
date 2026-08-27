# 两篇公众号线索：PI 产业观点与 RoboHarness 的一手来源台账

> 作者：Damon Li | 更新日期：2026年8月27日
> 归档性质：**来源台账与待升级研究记录**。两篇公众号原页只能读取标题/作者信息；技术事实仅引用下列 A/B 级来源。当前没有任何一个主题达到“论文 + 独立官方项目/代码/模型/数据 artifact”的核心技术文档门槛。

本目录保存输入线索、已确认的一手事实、可用的论文级推导和资源缺口。它不替代课程章节的完整技术文档；只有未来补齐独立项目页、代码、模型、数据卡或正式论文版本后，才会创建对应的课程/研究专题条目。

## 1. 输入、实体与最终处理

| 输入 | 公众号可读信息 | 识别实体 | 一手来源回溯 | 最终处理 |
|---|---|---|---|---|
| [链接 1](https://mp.weixin.qq.com/s/ne26faA1CxpNVu6r7NfLSg) | 《很认同PI CEO的话，具身智能可能没有Chatgpt时刻》；原创 Marilyn Liu，具身纪元 | Physical Intelligence（PI）；未能确认的 CEO 原话/访谈 | PI 官方主页、π0.7 官方技术发布 | 保留为**产业观点台账**。不将标题中的“PI CEO”或“没有 ChatGPT 时刻”当作已验证原话；不制作技术文档。 [1] [2] |
| [链接 2](https://mp.weixin.qq.com/s/SLSXAq4UGFjs-KZfJFu54Q) | 《具身智能Agent系列: 华为诺亚实验室RoboHarness——异构策略的记忆驱动编排》；原创 Ru-hulu | Huawei Noah’s Ark Lab 等作者；RoboHarness | arXiv v2/HTML 原文；Huawei Noah’s Ark Lab 官方 GitHub 组织 | 保留为**单一论文级观察候选**。技术机制和论文报告实验可查，但独立代码/项目/模型/数据 artifact 未发现。 [3] [4] [5] |

## 2. Physical Intelligence：产业观点与官方披露的边界

公众号标题表达的是“具身智能是否会出现 ChatGPT 时刻”的观点判断，而不是一个可由论文验证的技术命题。直接读取的 PI 官方主页列出 π0.7、在线 RL、长短期记忆与 π0 等多项研究发布，但主页和 π0.7 页面均未出现可归因给某位 CEO 的“可能没有 ChatGPT 时刻”原话。[1] [2] 因此，不能在知识库中把该标题改写为“PI CEO 的已证实观点”。

能被官方页支持的较窄结论是：PI 在 2026 年 4 月将 π0.7 定位为具有“step-change in generalization”的可控通用机器人基础模型，并披露其以语言、行为元数据、控制模态标签和视觉子目标等多模态 prompt 整合多机器人、人类视频与自治 episode 数据。[2] 这是**公司官方技术披露**，既不是同行评审证据，也未提供可独立下载的 π0.7 权重、训练数据、统一 benchmark 表、trial 数或统计区间。

| 可讨论内容 | 已核验事实 | 禁止外推 |
|---|---|---|
| 模型方向 | π0.7 接受标准语言，也可以使用策略、速度/质量元数据、控制模态和由轻量世界模型产生的视觉子目标。 [2] | 不可据此断言其达到通用具身智能、已跨全部机器人泛化，或已产生行业级“ChatGPT 时刻”。 |
| 数据主张 | 官方披露训练中纳入多机器人、人类视频与自治 episode，并以 prompt 中的上下文缓解不同策略/质量数据混合。 [2] | 数据规模、过滤比例、交叉本体 split、训练预算和泄漏审计未在该页面完整披露。 |
| 泛化演示 | 官方页面展示零样本家电操作、语言 coaching 与高层策略的案例。 [2] | 视频/案例不是统计 benchmark；没有对照、trial、方差与失败率不得产生定量比较。 |
| 可复现性 | 该页面链接 PDF，但本轮未核验公开权重/数据/完整训练 recipe。 | 不应把早期 π0 的开源状态迁移为 π0.7 的开源状态。 |

若未来获得原始 CEO 访谈、正式演讲视频/文字稿或 PI 官方署名声明，可在此台账追加“原话—上下文—日期—说话者”四个字段；在此之前，这一条应继续作为 C 级观点线索。

## 3. RoboHarness：论文级机制重建与证据边界

RoboHarness 的 arXiv v2 于 2026 年 7 月 28 日修订，作者名单包含 Huawei Noah’s Ark Lab 研究者。论文将异构控制系统封装成可调用的 agentic skills，并以 understanding、memory、self-evolution 三类辅助技能支持长时程任务分解、能力感知路由和策略切换。[3] [4]

令异构策略库为 $\Pi=\{\pi_1,\ldots,\pi_N\}$，全局观测空间为 $\mathcal O$、子任务空间为 $\mathcal G$。每项策略具有自己的有效输入域 $\mathcal O_i\subseteq\mathcal O$ 和可达子任务域 $\mathcal G_i\subseteq\mathcal G$。对于高层指令 $I$，系统同时求子任务序列 $\tau=(g_1,\ldots,g_T)$、策略分配 $\rho=(\pi_{k_1},\ldots,\pi_{k_T})$ 与相邻策略之间的 bridge 轨迹 $B=(b_1,\ldots,b_{T-1})$，需满足：

$$
 g_t\in\mathcal G_{k_t},\qquad o_t\in\mathcal O_{k_t},\qquad
 o_{t+1}=\operatorname{Terminal}(b_t)\in\mathcal O_{k_{t+1}}.
$$

这说明问题不只是“选择当前最强 policy”，而是同时确保下一个 policy 的输入落在其训练/可执行区域。论文的 Memory Bridge 先对任务文本和当前视觉观测做分层检索：

$$
\widetilde{\mathcal N}=
\operatorname{TopK}_{K_{\mathrm{text}}}
\cos(e_{\mathrm{text}}(g),e_{\mathrm{text}}(g(n))),
\qquad
\mathcal N=
\operatorname{TopK}_{K_{\mathrm{vis}}}
\cos(e_{\mathrm{vis}}(o),e_{\mathrm{vis}}(o(n))).
$$

从检索轨迹的相邻节点构造状态—进度样本 $(\mathbf s_{i,j},y_{i,j})$，拟合局部进度函数 $f_{\mathrm{score},t}(\mathbf s)$，并将可信交接目标限制在检索状态附近的支撑区域 $\mathcal R_{\mathrm{conf},t}$。随后 bridge 轨迹在该区域附近引导当前状态，才调用下一个 policy。[4] 上述是基于论文公开定义的补充重建；它不是在现有开源 artifact 上运行得到的复现实验。

### 论文报告的实验与不可比性

| 审计维度 | 论文报告 | 应保留的边界 |
|---|---|---|
| 研究问题 | VLA、RL policy 与 TAMP 的异构长时程零样本编排 | 论文实例不等于已对任意导航、MPC、WAM policy 全面验证 |
| 评测规模 | 摘要报告 3 个公开 benchmark、500 个定制任务、135 次真机实验 | 这些是论文作者报告；细分任务、policy 组合、成功定义和独立复现应以正文/附录为准 [3] [4] |
| 核心机制 | capability-aware decomposition/routing、multimodal execution memory、Memory Bridge | 是否有效依赖各 policy 的 memory 覆盖、视觉/文本 embedding 与状态表征可比较性 |
| 策略切换 | 论文目标是在无需联合重训练下，将状态带入下一策略的 in-distribution 区域 | 不能保证检索记忆覆盖新状态；错误桥接可能放大分布外偏移 |
| 资源 | 论文 arXiv v2 和 HTML 可访问 | 本轮未在题目/描述中发现 RoboHarness 的官方代码、权重、数据、LICENSE 或独立项目页 [3] [5] |

截至 2026 年 8 月 27 日，arXiv v2 的 Code、Data、Media 区只列出通用的 alphaXiv、CatalyzeX、DagsHub、Hugging Face 和 ScienceCast 检索服务，未列作者提供的链接；查阅 Huawei Noah’s Ark Lab 官方 GitHub 组织的公开仓库列表，也未发现名称或描述包含 RoboHarness 的仓库。[3] [5] 这只是**当前公开页面与组织列表下的时间点结论**，不等于作者私人仓库、尚未发布补充材料或未来 release 不存在。达到课程技术文档门槛的触发条件是：出现官方代码/项目/模型/数据/补充材料之一，并能与论文版本明确对应。

## 4. 后续跟踪清单

| 主题 | 下一步应核验的资料 | 升级条件 |
|---|---|---|
| PI “ChatGPT 时刻”观点 | 原始 CEO 访谈、视频、演讲文字稿或 PI 署名官方声明 | 明确说话者、原话、日期和上下文后，才可将观点作为可归因引述保存 |
| π0.7 | PDF 完整方法、权重/代码、数据卡、评测协议与统计信息 | 至少有官方技术材料及公开 artifact，且披露与 π0.7 对应 |
| RoboHarness | 作者项目页、官方 GitHub、模型/数据/补充材料、正式会议版本 | 与 arXiv 2607.18060v2 对应的第二类独立一手来源可用 |

## 5. 参考资料

[1]: https://www.pi.website/ "Physical Intelligence 官方主页：研究发布列表"
[2]: https://www.pi.website/blog/pi07 "π0.7: a Steerable Model with Emergent Capabilities，PI 官方技术发布，2026-04-16"
[3]: https://arxiv.org/abs/2607.18060 "RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning，arXiv v2，2026-07-28"
[4]: https://arxiv.org/html/2607.18060v2 "RoboHarness arXiv HTML 原文：问题定义、Memory Bridge 与实验说明"
[5]: https://github.com/huawei-noah "HUAWEI Noah's Ark Lab 官方 GitHub 组织页；访问日期 2026-08-27"
