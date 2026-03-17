# QuantTide Founder

基于认知科学记忆分类框架的组织知识库。

## 核心框架

**记忆分类框架**是本项目的元理论，定义了组织知识管理的认知基础。

### 陈述型记忆 - 九宫格模型

| | 事件类 | 语义类 | 自我类 |
|------|--------|--------|--------|
| **过去** | Archive（工作归档） | Tutorial（基础教程） | History（发展历程） |
| **现在** | Journal（工作日志） | Report（工作报告） | Brochure（宣传册） |
| **未来** | Profile（工作档案） | Essay（工作札记） | Roadmap（发展蓝图） |

### 程序型记忆五层体系

| 层次 | 英文名称 | 中文名称 | 法律隐喻 | 说明 |
|------|----------|----------|----------|------|
| L1 | Paper | 工作论文 | 立法原理 | 系统总结归纳基本原理与方法论，无直接约束力 |
| L2 | Usecase | 工作案例 | 精选判例 | 来源于具体实践案例的积累与复用 |
| L3 | Handbook | 工作手册 | 权威汇编 | 对实践和原理的系统化整理 |
| L4 | Specification | 工程标准 | 程序性法律 | 系统性程序规范，具有约束力 |
| L5 | Bylaw | 工作章程 | 宪法 | 规定基本原则与权责划分 |

**事实源**：`paper/meta/memory.md`

## 子模块

```bash
git submodule update --init --recursive
```

### 陈述型记忆 - 九宫格模型匹配

#### 过去 - 事件类
- **Archive** (`archive/`) - 工作归档
  - 仓库：`quanttide-archive-of-founder`
  - 定位：过去-事件类

#### 过去 - 语义类  
- **Tutorial** (`tutorial/`) - 基础教程
  - 仓库：`quanttide-tutorial-of-founder`
  - 定位：过去-语义类

#### 现在 - 事件类
- **Journal** (`journal/`) - 工作日志
  - 仓库：`quanttide-journal-of-founder`
  - 定位：现在-事件类
  - 说明：原始事件记录，按时间顺序记录

#### 现在 - 语义类
- **Report** (`report/`) - 工作报告
  - 仓库：`quanttide-report-of-founder`
  - 定位：现在-语义类
  - 说明：日报/总结，按记忆分类提炼

#### 现在 - 自我类
- **Brochure** (`meta/brochure/`) - 宣传册
  - 说明：项目介绍和内部使用指南

#### 未来 - 事件类
- **Profile** (`profile/`) - 工作档案
  - 仓库：`quanttide-profile-of-founder`
  - 定位：未来-事件类

#### 未来 - 语义类
- **Essay** (`essay/`) - 工作札记
  - 仓库：`quanttide-essay-of-founder`
  - 定位：未来-语义类

### 程序型记忆五层体系匹配

#### L1 - Paper (工作论文)
- **Paper** (`paper/`) - 工作论文
  - 仓库：`quanttide-paper-of-founder`
  - 法律隐喻：立法原理
  - 说明：系统总结归纳基本原理与方法论

#### L2 - Usecase (工作案例)
- **Usercase** (`usercase/`) - 工作案例
  - 仓库：`quanttide-usercase-of-founder`
  - 法律隐喻：精选判例
  - 说明：来源于具体实践案例的积累与复用

#### L3 - Handbook (工作手册)
- **Handbook** (`handbook/`) - 工作手册
  - 仓库：`quanttide-handbook-of-founder`
  - 法律隐喻：权威汇编
  - 说明：对实践和原理的系统化整理

#### L4 - Specification (工程标准)
- **Specification** (`specification/`) - 工程标准
  - 仓库：`quanttide-specification-of-founder`
  - 法律隐喻：程序性法律
  - 说明：系统性程序规范，具有约束力

#### L5 - Bylaw (工作章程)
- **Bylaw** (`meta/bylaw/`) - 工作章程
  - 说明：规定基本原则与权责划分
  - 包含：`bylaw.md`、`report.md`、`profile.md`

## 目录结构

```
quanttide-founder/
├── archive/         # 过去-事件类：工作归档
├── tutorial/        # 过去-语义类：基础教程
├── journal/         # 现在-事件类：工作日志（原始事件记录）
├── report/          # 现在-语义类：工作报告（日报总结）
├── profile/         # 未来-事件类：工作档案
├── essay/           # 未来-语义类：工作札记
├── handbook/        # 程序型-习惯法：工作手册
├── usercase/        # 程序型-判例法：工作案例
├── paper/           # 程序型-权威法理：工作论文
├── specification/   # 程序型-成文法：工程标准
├── platform/        # 程序型-宪法：技术平台
├── meta/            # 元信息（自我映射）
│   ├── bylaw/       # 工作章程
│   ├── brochure/    # 宣传册
│   ├── handbook/    # 工作手册
│   ├── journal/     # 原始事件记录
│   ├── profile/     # 工作档案
│   └── report/      # 工作报告
├── AGENTS.md        # Agent 工作指南
├── CONTRIBUTING.md  # 贡献指南
└── README.md        # 项目说明
```
