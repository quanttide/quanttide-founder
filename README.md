# 量潮创始人第二大脑

基于认知科学记忆分类框架的组织知识库。

## 核心框架

**记忆分类框架**是本项目的元理论，定义了组织知识管理的认知基础。

### 陈述型记忆 - 九宫格模型

| | 事件类 | 语义类 | 自我类 |
|------|--------|--------|--------|
| **过去** | `archive/` Archive<br>工作归档 | `tutorial/` Tutorial<br>基础教程 | History<br>发展历程 |
| **现在** | `journal/` Journal<br>工作日志<br>（原始事件记录） | `report/` Report<br>工作报告<br>（日报总结） |  Brochure<br>宣传册 |
| **未来** | `profile/` Profile<br>工作档案 | `essay/` Essay<br>工作札记 | Roadmap<br>发展蓝图 |

### 程序型记忆五层体系

| 层次 | 英文名称 | 中文名称 | 法律隐喻 | 子模块 | 说明 |
|------|----------|----------|----------|--------|------|
| L1 | Paper | 工作论文 | 立法原理 | `paper/` | 系统总结归纳基本原理与方法论，无直接约束力 |
| L2 | Usecase | 工作案例 | 精选判例 | `usercase/` | 来源于具体实践案例的积累与复用 |
| L3 | Handbook | 工作手册 | 权威汇编 | `handbook/` | 对实践和原理的系统化整理 |
| L4 | Specification | 工程标准 | 程序性法律 | `specification/` | 系统性程序规范，具有约束力 |
| L5 | Bylaw | 工作章程 | 宪法 | `meta/bylaw/` | 规定基本原则与权责划分 |

**事实源**：`paper/meta/memory.md`

## 目录

```
quanttide-founder/
├── archive/         # 过去-事件类：工作归档
├── essay/           # 未来-语义类：工作札记
├── handbook/        # 权威法理：工作手册
├── journal/         # 现在-事件类：工作日志
├── paper/           # 立法原理：工作论文
├── platform/        # 技术平台
├── profile/         # 未来-事件类：工作档案
├── report/          # 现在-语义类：工作报告
├── specification/   # 程序性法律：工程标准
├── usercase/        # 判例法：工作案例
├── tutorial/        # 过去-语义类：基础教程
├── meta/            # 元信息（自我映射）
├── AGENTS.md        # Agent 工作指南
├── CONTRIBUTING.md  # 贡献指南
└── README.md        # 项目说明
```

## 常用命令

### 子模块初始化

```bash
git submodule update --init --recursive
```
