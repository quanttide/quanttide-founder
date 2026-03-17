# Meta - 元信息

本目录包含项目的元信息，用于自我映射和状态追踪。

## 目录结构

```
meta/
├── bylaw/          # 工作章程（最高优先级）
│   ├── bylaw.md    # 元章程，定义人机分工
│   ├── report.md   # 元报告章程
│   └── profile.md  # Profile 维护章程
├── handbook/       # 工作手册（次高优先级）
│   └── profile.md  # Profile 维护经验
├── profile/        # 工作档案（中等优先级）
│   ├── repo.md     # 仓库结构
│   ├── release.md  # 版本管理
│   ├── memory.md   # 记忆建模
│   └── submodule.md # 子模块管理
├── journal/        # 工作日志（基础优先级）
│   ├── README.md   # 日志说明
│   └── 2026-03-18.md
├── report/         # 工作报告（基础优先级）
│   ├── 2026-03-14.md
│   ├── 2026-03-15.md
│   ├── 2026-03-16.md
│   └── 2026-03-17.md
├── brochure/       # 宣传册
│   └── index.md    # 项目宣传册
├── tutorial/       # 使用指南
│   └── index.md    # 如何使用创始人的第二大脑
├── IDENTITY.md     # 自我映射
├── SOUL.md         # 自我认知
├── AGENTS.md       # AI 自我认知
├── TOOLS.md        # 工具清单
├── USER.md         # 用户画像
└── README.md       # 本文件
```

## 文件说明

### bylaw/ - 工作章程
- **bylaw.md**：元章程，定义人机分工规范
- **report.md**：元报告章程，定义日报/总结格式
- **profile.md**：Profile 维护章程和流程

### handbook/ - 工作手册
- **profile.md**：Profile 维护经验总结

### profile/ - 工作档案
- **repo.md**：仓库结构规范
- **release.md**：Release 列表和版本管理
- **memory.md**：记忆建模知识
- **submodule.md**：子模块列表和管理

### report/ - 工作报告（日报/总结）
- 按日期命名的日报文件
- 采用记忆分类格式（事件记忆、语义记忆、自我记忆）

### journal/ - 工作日志
- 按日期命名的工作日志
- 记录 meta 目录的日常变更和思考
- README.md：日志说明和规范

### brochure/ - 宣传册
- **index.md**：项目宣传册（自我宣传）

### tutorial/ - 使用指南
- **index.md**：如何使用创始人的第二大脑

### 根文件
- **IDENTITY.md**：仓库自我映射，包含项目状态和子模块信息
- **SOUL.md**：自我认知，包含创始人的思考和信念
- **AGENTS.md**：AI 自我认知，由 AI 自维护
- **TOOLS.md**：工具清单，记录项目中使用的开发工具
- **USER.md**：用户画像，记录用户信息和期望
- **README.md**：本文件，元信息目录说明

## 优先级体系

根据记忆分层模型，`meta/` 目录的文件优先级如下：

1. **bylaw**（最高优先级）- 工作章程
2. **handbook**（次高优先级）- 工作手册
3. **profile**（中等优先级）- 工作档案
4. **journal**（基础优先级）- 工作日志
5. **report**（基础优先级）- 工作报告

## 维护说明

- **AI 自动维护**：大部分文件由 AI Agent 自动维护
- **AI 自维护**：AGENTS.md、TOOLS.md、journal/ 由 AI 自维护
- **人类验收**：bylaw 和 handbook 文件需要人类验收确认
- **按日期更新**：report 和 journal 文件按日期自动更新
- **用户驱动更新**：USER.md 根据用户信息变化更新

## 参考文件

- [元章程](./bylaw/bylaw.md)：人机分工规范
- [记忆建模](./profile/memory.md)：记忆分类框架
- [自我映射](./IDENTITY.md)：仓库状态信息
