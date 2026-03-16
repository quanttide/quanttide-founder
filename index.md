# QuantTide Founder 组织知识库

基于认知科学记忆分类框架的九宫格模型，构建组织共同记忆体系。

## 建模思想

### 记忆分类框架

本项目采用认知科学中**陈述型记忆**与**程序型记忆**的分类体系，将组织知识划分为两大类型：

| 类型 | 回答的问题 | 知识特征 |
|------|-----------|---------|
| 陈述型记忆 | "是什么" | 关于事实、事件和知识的记录 |
| 程序型记忆 | "怎么做" | 关于方法、规范和流程的积累 |

### 九宫格模型

将组织知识按**类型维度**与**时间维度**交织，形成九宫格：

| | 事件类 | 语义类 | 自我类 |
|------|--------|--------|--------|
| **过去** | Archive（工作归档） | Handbook（工作手册） | Profile（个人档案） |
| **现在** | Journal（工作日志） | Report（工作报告） | Essay（工作札记） |
| **未来** | Specification（工程标准） | Platform（技术平台） | Roadmap（发展蓝图） |

**三个类型维度**：

- **事件类**：回答"我们要做什么"——关于行动和任务的记录
- **语义类**：回答"我们相信什么"——关于方法和规范的积累
- **自我类**：回答"我们是谁"——关于身份与认同的知识

**三个时间维度**：

- **过去**：已完成的履约，奠定组织连续性
- **现在**：正在履行的约定，保障实时协作
- **未来**：将要履行的承诺，提供方向指引

### 程序型记忆五层体系

参考英国法律体系实践，程序型记忆分为五个层次：

| 层次 | 比喻 | 说明 |
|------|------|------|
| Usercase | 判例法 | 来源于具体实践案例的积累与复用 |
| Handbook | 习惯法 | 来源于人与人协作时的经验总结 |
| Essay | 学术论文 | 系统总结归纳基本原理与方法论 |
| Specification | 成文法 | 对协作进行明确约束与规范 |
| Platform | 宪法 | 规定基本原则与技术架构 |

## 子模块

本仓库为元仓库（meta-repo），通过 Git 子模块管理独立文档仓库。

```bash
git submodule update --init --recursive
```

### 陈述型记忆

| 子模块 | 定位 | 仓库 |
|--------|------|------|
| Archive | 过去的事件类——工作归档 | quanttide-archive-of-founder |
| Journal | 现在的事件类——工作日志 | quanttide-journal-of-founder |
| Report | 现在的语义类——工作报告 | quanttide-report-of-founder |
| Profile | 过去的自我类——个人档案 | quanttide-profile-of-founder |
| Essay | 现在的自我类——工作札记 | quanttide-essay-of-founder |

### 程序型记忆

| 子模块 | 定位 | 仓库 |
|--------|------|------|
| Handbook | 过去的语义类——工作手册 | quanttide-handbook-of-founder |
| Specification | 未来的语义类——工程标准 | quanttide-specification-of-founder |
| Platform | 未来的语义类——技术平台 | quanttide-platform-of-founder |
| Usecase | 程序型记忆——工作案例 | quanttide-usercase-of-founder |

## 使用指南

### 选择合适的子模块

根据你要记录的知识类型和时间维度，选择对应的子模块：

1. **记录具体工作** → Journal（日志）或 Report（报告）
2. **总结方法经验** → Handbook（手册）或 Usecase（案例）
3. **制定规范标准** → Specification（规范）
4. **梳理身份认同** → Essay（札记）或 Profile（档案）
5. **归档历史资料** → Archive（归档）

### 协作原则

- **最小干预**：仅记录必要信息，不过度复杂化
- **原子提交**：每次提交独立完整，便于追溯
- **及时同步**：定期推送更新，保持团队信息一致

## 相关文档

- [README](./README.md) - 项目概述与构建命令
- [CONTRIBUTING](./CONTRIBUTING.md) - 提交流规范与发布流程
