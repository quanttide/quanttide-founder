# 子模块列表

本文件记录 quanttide-founder 仓库中所有子模块的详细信息。

## 子模块列表

| 子模块 | 路径 | 定位 | 描述 |
|--------|------|------|------|
| **archive** | `docs/archive/` | 过去-事件类 | 工作归档 |
| **essay** | `docs/essay/` | 未来-语义类 | 工作札记 |
| **handbook** | `docs/handbook/` | 程序型-习惯法 | 工作手册 |
| **journal** | `docs/journal/` | 现在-事件类 | 工作日志 |
| **paper** | `docs/paper/` | 程序型-权威法理 | 工作论文 |
| **platform** | `src/thera/` | 程序型-宪法 | 技术平台 |
| **profile** | `docs/profile/` | 未来-事件类 | 工作档案 |
| **report** | `docs/report/` | 现在-语义类 | 工作报告 |
| **specification** | `docs/specification/` | 程序型-成文法 | 工程标准 |
| **usercase** | `docs/usercase/` | 程序型-判例法 | 工作案例 |
| **tutorial** | `docs/tutorial/` | 过去-语义类 | 工作教程 |

## 目录结构

```
quanttide-founder/
├── src/
│   └── thera/       # 技术平台
├── docs/            # 文档（给人类读）
│   ├── archive/      # 过去-事件类：工作归档
│   ├── essay/        # 未来-语义类：工作札记
│   ├── handbook/     # 程序型-习惯法：工作手册
│   ├── journal/      # 现在-事件类：工作日志
│   ├── paper/        # 程序型-权威法理：工作论文
│   ├── profile/      # 未来-事件类：工作档案
│   ├── report/       # 现在-语义类：工作报告
│   ├── specification/ # 程序型-成文法：工程标准
│   ├── tutorial/    # 过去-语义类：工作教程
│   └── usercase/    # 程序型-判例法：工作案例
├── meta/            # 元信息（给AI读）
├── AGENTS.md        # Agent 工作指南
├── CONTRIBUTING.md  # 贡献指南
└── README.md        # 项目说明
```

## 版本约定

- 各子模块独立版本管理
- 主仓库不设版本，仅追踪子模块引用
- Meta 目录由 AI 自动维护

## 工作流程优化

### 工作流程原则
- **原子提交**：每次提交独立完整
- **验证优先**：修改后运行验证
- **文档同步**：代码变更同步更新文档

### 子模块分类原则
- **陈述型记忆**：按时间分类（过去/现在/未来）
- **程序型记忆**：按法律隐喻分类（立法原理/精选判例/权威汇编/程序性法律/宪法）
- **九宫格模型**：事件类、语义类、自我类的交叉分类
