# 量潮创始人第二大脑

基于认知科学记忆分类框架的组织知识库。

具体分类详见 [记忆模型简介](docs/profile/meta/memory_model.md)。

## 目录

```
quanttide-founder/
├── src/
│   └── qtadmin/     # 管理后台
├── scripts/         # AI 工具脚本
├── docs/            # 文档
│   ├── archive/     # 工作归档
│   ├── essay/       # 工作札记
│   ├── journal/     # 工作日志
│   ├── profile/     # 工作简介
│   ├── roadmap/     # 工作蓝图
│   └── roadmap/     # 工作蓝图
├── meta/            # 元信息
├── AGENTS.md        # Agent 工作指南
├── CONTRIBUTING.md  # 贡献指南
└── README.md        # 项目说明
```

## 常用命令

### 子模块初始化

```bash
git submodule update --init --recursive
```

### 更新关联子模块

```bash
git submodule update --remote --merge
```
