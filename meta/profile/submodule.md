# 子模块注册表

本文档是子模块的事实源，YAML 数据同时供人类阅读和脚本读取。

```{yaml}
submodules:
  - name: thera
    path: src/thera
    category: procedural
    type: platform
    description: 技术平台，CLI 工具和自动化脚本

  - name: qtadmin
    path: src/qtadmin
    category: procedural
    type: platform
    description: 管理后台，管理和运营工具

  - name: devops
    path: packages/devops
    category: procedural
    type: platform
    description: DevOps 工具包，Python SDK 用于运维自动化

  - name: data
    path: packages/data
    category: procedural
    type: platform
    description: 数据工具包，提供多语言数据操作 SDK

  - name: archive
    path: docs/archive
    category: declarative
    grid: past-event
    description: 过去-事件类：工作归档

  - name: essay
    path: docs/essay
    category: declarative
    grid: future-semantic
    description: 未来-语义类：工作札记

  - name: handbook
    path: docs/handbook
    category: procedural
    type: customary-law
    description: 程序型-习惯法：工作手册

  - name: journal
    path: docs/journal
    category: declarative
    grid: present-event
    description: 现在-事件类：工作日志

  - name: paper
    path: docs/paper
    category: procedural
    type: authoritative-law
    description: 程序型-权威法理：工作论文

  - name: profile
    path: docs/profile
    category: declarative
    grid: present-semantic
    description: 现在-语义类：工作档案

  - name: report
    path: docs/report
    category: declarative
    grid: future-event
    description: 未来-事件类：工作报告

  - name: specification
    path: docs/specification
    category: procedural
    type: statute-law
    description: 程序型-成文法：工程标准

  - name: tutorial
    path: docs/tutorial
    category: declarative
    grid: past-semantic
    description: 过去-语义类：工作教程

  - name: usercase
    path: docs/usercase
    category: procedural
    type: case-law
    description: 程序型-判例法：工作案例

  - name: bylaw
    path: docs/bylaw
    category: procedural
    type: constitution
    description: 程序型-宪法：工作章程

  - name: history
    path: docs/history
    category: declarative
    grid: past-self
    description: 过去-自我类：发展历程
```

## 使用说明

如需修改子模块配置，请编辑上方 YAML 数据块。

脚本读取位置：`meta/profile/submodules.yaml`
