# 2025年世界模型最新研究补充报告

**作者**: Damon Li  
**日期**: 2026年1月6日  
**来源**: [AwesomeWorldModels](https://github.com/Li-Zn-H/AwesomeWorldModels)

---

## 1. 引言

世界模型（World Models）作为具身智能的核心技术之一，在2025年取得了突破性进展。本报告基于对`AwesomeWorldModels`仓库中2025年最新研究成果的深度调研，重点分析了**DreamerV3**、**FOUNDER**和**WMP**等代表性工作，旨在揭示世界模型的技术前沿和发展趋势。

---

## 2. DreamerV3: 通用控制的里程碑

**论文**: Mastering diverse control tasks through world models  
**发表**: Nature 2025  
**核心贡献**: 提出第三代Dreamer算法，是**首个在超过150个不同任务上超越专用算法的通用强化学习算法**，使用单一配置无需调参。

### 2.1. 技术创新

1. **鲁棒性技术**: 基于**归一化、平衡和变换**，使算法能在不同领域稳定学习。
2. **Symlog预测**: 处理不同量级的信号，对奖励和值函数使用symlog变换。
3. **自由比特 (Free Bits)**: 避免退化解，将动力学损失和表示损失裁剪到1 nat以下。
4. **想象训练**: 在潜在空间中想象未来轨迹，无需访问中间图像即可预测45帧。

### 2.2. 里程碑成就

- **Minecraft钻石挑战**: 首个无需人类数据从零开始在Minecraft中收集钻石的算法。
- **Nature顶刊发表**: 标志着世界模型方法的成熟。

### 2.3. 对具身智能的意义

- **通用性突破**: 证明单一算法可以处理多样化具身任务。
- **数据效率**: 通过想象训练减少与环境的实际交互。
- **开放世界能力**: 展示了处理复杂开放环境的潜力。

---

## 3. FOUNDER: 基础模型与世界模型的融合

**论文**: Grounding Foundation Models in World Models for Open-Ended Embodied Decision Making  
**会议**: ICML 2025  
**核心贡献**: 将**基础模型（LLM/VLM）植根于世界模型**中，实现开放式具身决策。

### 3.1. 核心创新：时间距离奖励 (Temporal Distance Reward)

**问题**: GenRL等早期方法使用余弦相似度作为奖励，导致**奖励黑客**问题（如智能体在原地“跑步”）。

**解决方案**: FOUNDER提出**时间距离奖励函数 (TempD)**，利用时间距离作为奖励，增强时间感知，避免奖励黑客。

### 3.2. 技术架构

1. **三阶段学习范式**: 世界模型学习 → 连接器学习 → 行为学习。
2. **状态表示**: 使用**确定性状态 + 随机状态**的组合，捕捉历史信息和当前观察。
3. **深层语义对齐**: 相比GenRL的视觉层面对齐，FOUNDER实现了更深层次的任务语义对齐。

### 3.3. 对具身智能的意义

- **开放式决策**: 支持基于自然语言/视频的开放式任务指定。
- **跨域泛化**: 实现跨具身、跨视角泛化。
- **基础模型集成**: 为将大模型能力引入具身智能提供有效范式。

---

## 4. WMP: 视觉腿式运动的突破

**论文**: World Model-based Perception for Visual Legged Locomotion  
**会议**: ICRA 2025  
**核心贡献**: 提出**世界模型感知 (WMP)** 框架，在A1机器人上实现了**迄今为止最佳的穿越性能**。

### 4.1. 技术优势

**问题**: 传统Teacher-Student框架存在信息差距，限制学生策略性能。

**解决方案**: WMP构建环境的世界模型，直接基于世界模型学习策略，实现**端到端学习**。

### 4.2. 关键发现

- **Sim2Real能力**: 虽然完全在仿真中训练，世界模型能够对**真实世界轨迹做出准确预测**。
- **超越专用方法**: 在多种挑战性地形（间隙、攀爬、爬行、倾斜）上超越现有最佳方法。

### 4.3. 对具身智能的意义

- **视觉腿式运动新范式**: 为视觉引导的腿式运动提供新思路。
- **Sim2Real新思路**: 通过世界模型实现有效的仿真到现实迁移。
- **端到端学习**: 简化训练流程，提升最终性能。

---

## 5. 2025年世界模型技术趋势总结

1. **通用性与鲁棒性**: 以DreamerV3为代表，追求单一配置解决多样化任务。
2. **与基础模型融合**: 以FOUNDER为代表，将大模型的语义理解能力与世界模型的动态预测能力结合。
3. **端到端学习**: 以WMP为代表，抛弃复杂的两阶段训练，追求更自然的端到端学习范式。
4. **Sim2Real能力增强**: 世界模型成为连接仿真与现实的关键桥梁。
5. **新架构探索**: 以GLAM为代表，探索Mamba等新架构在世界模型中的应用。

---

## 6. 参考文献

1. Hafner, D., Pasukonis, J., Ba, J., & Lillicrap, T. (2025). Mastering diverse control tasks through world models. *Nature, 640*(647–653).
2. [FOUNDER Project Page](https://sites.google.com/view/founder-rl)
3. [WMP Project Page](https://wmp-loco.github.io/)
4. [AwesomeWorldModels GitHub Repository](https://github.com/Li-Zn-H/AwesomeWorldModels)
