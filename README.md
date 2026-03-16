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

| 层次 | 比喻 | 说明 |
|------|------|------|
| Usecase | 判例法 | 来源于具体实践案例的积累与复用 |
| Handbook | 习惯法 | 来源于人机交互或人与人协作时的经验总结 |
| Paper | 权威法理 | 系统总结归纳基本原理与方法论 |
| Specification | 成文法 | 对人机协作进行明确约束与规范 |
| Bylaws | 宪法 | 规定基本原则与权责划分 |

**事实源**：`paper/meta/memory.md`

## 子模块

```bash
git submodule update --init --recursive
```

### 陈述型记忆

| 子模块 | 定位 | 仓库 |
|--------|------|------|
| Archive | 过去-事件类 | quanttide-archive-of-founder |
| Journal | 现在-事件类 | quanttide-journal-of-founder |
| Report | 现在-语义类 | quanttide-report-of-founder |
| Profile | 未来-事件类 | quanttide-profile-of-founder |
| Essay | 未来-语义类 | quanttide-essay-of-founder |

### 程序型记忆

| 子模块 | 定位 | 仓库 |
|--------|------|------|
| Usecase | 判例法 | quanttide-usercase-of-founder |
| Handbook | 习惯法 | quanttide-handbook-of-founder |
| Paper | 权威法理 | quanttide-paper-of-founder |
| Specification | 成文法 | quanttide-specification-of-founder |
| Platform | 宪法 | quanttide-platform-of-founder |
