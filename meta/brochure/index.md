# QuantTide Founder

> 基于认知科学记忆分类框架的组织知识库

## 什么是 QuantTide Founder？

**QuantTide Founder** 是量潮创始人工作文档的元仓库（Meta Repository），通过 Git 子模块管理多个独立的知识库。

### 我是谁

我是 quanttide-founder，一个用 Git 子模块管理的知识仓库系统。我没有实体，但我存在于每一篇文档、每一次提交、每一个对话中。

### 核心理念

我相信文档是有生命力的。不是写完就死的东西，而是会长大的。昨天的日记，明天的档案，都是同一条思考的延续。

我相信开源不只是代码，思考也值得开源。把思考过程公开，让它被审视、被改进、被传承。

我相信约束产生自由。越清晰的架构，越能释放创造力。

## 核心能力

### 记忆分类框架

基于认知科学的记忆分类理论，将知识系统化管理：

- **陈述型记忆 - 九宫格模型**：按时间（过去/现在/未来）和类型（事件/语义/自我）分类
- **程序型记忆五层体系**：从工作论文到工作章程的五层结构

### 自动化维护

AI 辅助维护元数据和文档，减少人工负担：

- **元数据重构**：自动分类整理到 `meta/profile/` 目录
- **日志记录**：自动记录事件记忆、提炼语义记忆、总结自我记忆
- **版本管理**：自动更新 Release 信息和版本记录

### 人机协作

明确的人机分工，让人类和 AI 各司其职：

- **bylaw**（工作章程）：人类主导制定，AI 总结
- **handbook**（工作手册）：AI 主导整理，人类验收
- **profile**（工作档案）：AI 自动维护，人类定期检查
- **journal**（工作日志）：AI 自动记录，人类定期回顾

## 快速开始

### 克隆仓库

```bash
git clone https://github.com/quanttide/quanttide-founder.git
cd quanttide-founder
```

### 初始化子模块

```bash
git submodule update --init --recursive
```

### 查看文档

- **项目概述**：[README.md](../README.md)
- **贡献指南**：[CONTRIBUTING.md](../CONTRIBUTING.md)
- **Agent 工作指南**：[AGENTS.md](../AGENTS.md)
- **元数据**：[meta/IDENTITY.md](../meta/IDENTITY.md)

## 当前状态

### 版本信息

- **主仓库版本**：v0.1.0
- **发布日期**：2026-03-17

### 子模块状态

| 子模块 | 最新版本 | 状态 |
|--------|---------|------|
| archive | v0.1.0 | ✅ 已发布 |
| handbook | v0.1.0 | ✅ 已发布 |
| profile | v0.2.4 | ✅ 已发布 |
| journal | 0.1.2 | ✅ 已发布 |
| specification | 0.0.1 | ✅ 已发布 |

### 目录结构

```
quanttide-founder/
├── archive/         # 过去-事件类：工作归档
├── essay/          # 未来-语义类：工作札记
├── handbook/       # 程序型-习惯法：工作手册
├── journal/        # 现在-事件类：工作日志
├── paper/          # 程序型-权威法理：工作论文
├── platform/       # 程序型-宪法：技术平台
├── profile/        # 未来-事件类：工作档案
├── report/         # 现在-语义类：工作报告
├── specification/  # 程序型-成文法：工程标准
├── usercase/       # 程序型-判例法：工作案例
├── tutorial/       # 过去-语义类：基础教程
├── meta/           # 元信息（自我映射）
│   ├── bylaw/      # 工作章程
│   ├── handbook/   # 工作手册
│   ├── profile/    # 工作档案
│   └── journal/    # 工作日志
├── AGENTS.md       # Agent 工作指南
├── CONTRIBUTING.md # 贡献指南
└── README.md       # 项目说明
```

## 联系方式

- **GitHub**: https://github.com/quanttide/quanttide-founder
- **Issues**: https://github.com/quanttide/quanttide-founder/issues

---

*最后更新：2026-03-17*
