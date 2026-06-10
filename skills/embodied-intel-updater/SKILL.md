---
name: embodied-intel-updater
description: 具身智能知识库增量更新工具。针对 GitHub 仓库 DemonDamon/embodied-intelligence-nexus 执行学术界与工业界最新进展的全局扫描、深度调研与文档落盘。Use when user requests to update, catch up, or refresh the embodied intelligence knowledge base with recent developments in robotics, VLA/VLM, manipulation, reinforcement learning, or related fields.
---

# Embodied Intelligence Nexus Updater

快速将 `DemonDamon/embodied-intelligence-nexus` 仓库的课程知识库更新至最新状态。

## 目标仓库信息

- **仓库地址**: https://github.com/DemonDamon/embodied-intelligence-nexus
- **课程目录**: `course/` 下按章节组织
- **作者署名**: Damon Li
- **Git 身份**: `Damon Li <DemonDamon@users.noreply.github.com>`

## 目录结构约定

```
course/
├── 01-robot-grasping-intro/       # 第一章：机器人抓取与操作介绍
├── 02-classical-control/          # 第二章：经典规划控制方法
├── 03-robot-vision/               # 第三章：机器人视觉方法
├── 04-deep-learning-grasping/     # 第四章：基于深度学习的抓取
├── 05-imitation-learning/         # 第五章：模仿学习
├── 06-reinforcement-learning/     # 第六章：强化学习方法
├── 07-vla-vlm-models/             # 第七章：具身智能：VLA与VLM模型
└── 08-engineering-experience/     # 第八章：工程经验和总结展望
```

## 执行工作流

### Phase 1: 环境准备

1. 克隆或拉取最新仓库：
   ```bash
   cd /home/ubuntu && rm -rf embodied-intelligence-nexus
   gh repo clone DemonDamon/embodied-intelligence-nexus
   cd embodied-intelligence-nexus
   git config user.name "Damon Li"
   git config user.email "DemonDamon@users.noreply.github.com"
   ```
2. 确认上次更新时间：查看 `README.md` 中的"更新日期"字段或 `git log --oneline -5`。
3. 确定本次扫描的时间窗口：从上次更新日期到今天。

### Phase 2: 全局扫描

对以下维度进行搜索（使用 `search` 工具，`time` 设为 `past_month` 或按需调整）：

#### 学术界扫描关键词

| 领域 | 搜索关键词示例 |
| :--- | :--- |
| VLA/VLM 模型 | `VLA model {year}`, `vision language action latest`, `embodied foundation model` |
| 世界模型 | `world model robotics`, `world action model`, `video generation robot` |
| 操作与抓取 | `robot manipulation ICRA`, `dexterous grasping latest`, `6DoF grasp learning` |
| 模仿学习 | `imitation learning robot {year}`, `behavior cloning diffusion` |
| 强化学习 | `reinforcement learning robotics`, `sim-to-real transfer {year}` |
| 具身导航 | `embodied navigation`, `mobile manipulation` |

#### 工业界扫描关键词

| 领域 | 搜索关键词示例 |
| :--- | :--- |
| 开源框架 | `LeRobot update`, `Isaac GR00T`, `open source robot framework` |
| 机器人公司 | `humanoid robot company {year}`, `Figure AI`, `1X Technologies`, `Unitree` |
| 大模型厂商 | `Google robotics`, `NVIDIA embodied AI`, `OpenAI robotics` |
| 数据集/Benchmark | `robot learning dataset`, `embodied AI benchmark`, `Open X-Embodiment` |

#### 扫描输出

将扫描结果整理为临时笔记文件 `research_scan_notes.md`，包含：
- 发现的重要进展列表（标题、来源、日期、一句话摘要）
- 按相关章节分类标注

### Phase 3: 深度调研与内容撰写

对 Phase 2 中筛选出的重要进展，逐一深度调研并撰写文档。

#### 文档命名规则

- 新增文件命名：`{章节号}.{序号}-{英文短名}-{年份}-updates.md`
- 示例：`7.10-world-models-2026-q3-updates.md`
- 序号接续该章节现有最大编号

#### 文档结构模板

```markdown
# [知识点/进展标题]

> 作者：Damon Li | 更新日期：YYYY年M月D日

## 1. 概述

[背景与动机，解决什么问题，为什么重要]

## 2. 核心技术/方法

[技术细节，架构设计，关键创新点]
[数学公式使用 LaTeX: $...$ 行内, $$...$$ 块级]

## 3. 关键成果与对比

[性能指标、与前作对比、实验结果]

## 4. 代码与资源

[开源代码链接、HuggingFace模型、数据集地址]
[如有必要提供简短代码示例]

## 5. 影响与展望

[对领域的影响，未来方向]

## 6. 参考资料

- [论文/博客/官方链接，带完整URL]
```

#### 内容质量要求

- 每篇 1000-3000 字
- 中文撰写，专业术语保留英文
- 引用需注明来源URL
- 图表优先使用 Mermaid 语法内嵌
- 代码示例优先 Python

### Phase 4: 整合与导航更新

1. 更新各章节 `README.md`，添加新文件的链接
2. 更新根目录 `README.md`：
   - 课程导航表中添加新内容链接
   - 更新"更新日期"字段为当天日期
3. 删除临时文件 `research_scan_notes.md`

### Phase 5: 提交与推送

```bash
cd /home/ubuntu/embodied-intelligence-nexus
git add .
git commit -m "feat: add YYYY-MM embodied AI updates - [简要描述]"
gh auth setup-git
git push origin main
```

## 注意事项

- 不要修改已有文档的内容，只新增文件
- 如果某个方向进展特别多（>5个重要成果），考虑创建子目录
- 推送前确认 `gh auth status` 已登录，否则需通过浏览器 device flow 认证
- 每次更新完成后，向用户报告：新增文件数、覆盖的关键进展摘要、待后续关注的方向
