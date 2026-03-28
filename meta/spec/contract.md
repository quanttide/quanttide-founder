# 契约规范

本文件定义数据契约（contract.yaml）的编写标准。

## 格式

YAML 文件，命名为 `contract.yaml`。

## 必须章节

```yaml
dataContractSpecification: 0.9.3  # 规范版本
id: <仓库标识>
info:                             # 元信息
  title: <标题>
  version: <契约版本>
  description: <描述>
  owner: <所有者>

models: <数据模型定义>
data: <实际数据>
```

## 可选章节

```yaml
semantics: <语义定义>             # 分类框架
quality: <质量约束>               # 命名、版本、文件约定
```

## 版本规范

- 契约版本（info.version）：遵循语义化版本
- 规范版本（dataContractSpecification）：跟随上游标准

## 数据模型

每个模型定义必须包含：

```yaml
models:
  <name>:
    description: <描述>
    type: object | array
    items|properties: <字段定义>
```

字段定义必须包含：
- `type`：数据类型
- `description`：字段说明

可选：
- `required`：必填字段列表
- `pattern`：正则约束
- `enum`：枚举值

## 数据章节

`data` 是事实源。所有引用此契约的文档都应指向此章节。

## 命名约定

- 契约文件：`contract.yaml`
- 说明文件：`contract.md`（handbook 层级）
- 契约目录：`meta/profile/`