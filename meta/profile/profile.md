# Profile

本目录是 quanttide-founder 元仓库的数据定义中心。

**事实源**：[contract.yaml](./contract.yaml)

## 记忆建模

语义定义见 `semantics`

- **陈述型记忆（九宫格）**：`semantics.declarative.grid`
- **程序型记忆（五层）**：`semantics.procedural.levels`
- **事实源**：`docs/paper/meta/memory.md`

## 子模块

数据定义见 `data.submodules`

- 修改子模块配置请编辑 `contract.yaml`
- 脚本读取位置：`contract.yaml#data.submodules`
- Schema 约束：`contract.yaml#models.submodule`

## Release

数据定义见 `data.releases`

- 修改 Release 信息请编辑 `contract.yaml`
- 版本规范：`contract.yaml#quality.versioning`
- 发布后需同步更新 `meta/IDENTITY.md`

## 仓库结构

规范定义见 `quality`

- **必填文件**：`quality.files.required`
- **可选文件**：`quality.files.optional`
- **命名规范**：`quality.naming`
- **标准文件结构**：`docs/handbook/asset/repo.md`