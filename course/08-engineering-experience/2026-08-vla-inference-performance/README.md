# 2026 年 8 月：VLA 推理性能与部署工程专题

> 作者：Damon Li
> 更新日期：2026年8月23日

VLA 的工程可用性由模型、视觉上下文、动作块、网络、硬件、调度和机器人执行器共同决定。本专题以 VLA-Perf 的 Roofline 分析为入口，强调将理论上界与实机 profile、闭环控制质量和安全预算一起使用。

## 文档导航

- [8.3 VLA-Perf：从 Roofline 模型到机器人 VLA 的部署决策](./8.3-vla-perf-inference-engineering-2026.md)
- [8.4 DriveVLA-M0：故障记忆增强与测试时适配](./8.4-drivevla-m0-failure-aware-memory-2026.md)
  - 将自动驾驶 VLA 的检索、TTT 额外开销、NAVSIM 评测与真实车辆端到端时延边界分开审计。

## 使用边界

VLA-Perf 可以快速筛选架构—硬件—网络的设计空间，但不测量任务成功率、接触质量、传感器采集、OS 抖动或执行器迟滞。任何生产部署都应把其预测视为可达上界，并以目标机器人上的真实 trace 复核。DriveVLA-M0 的 26.44 ms 仅是 NAVSIM 中测试时训练反向传播的额外开销，不能作为完整车端时延或机器人 VLA 通用延迟结论。
