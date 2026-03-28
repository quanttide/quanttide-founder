# Contract 的归宿

## 现象

今天经历了一次有意思的文件迁移：

```
profile.md → spec/contract.md → handbook/contract.md
```

三分钟内，同一个文件从"档案"升级为"标准"，又降级为"手册"。

## 问题

Handbook 和 Specification 的边界是什么？

## 更深的问题

在讨论边界之前，先要问：contract.yaml 是什么？

答案是：它既不是 spec，也不是 handbook。它是一个**数据实例**。

三个东西是不同层次：

| 文件 | 层次 | 内容 |
|------|------|------|
| `contract.yaml` | 数据 | 这个仓库的具体契约 |
| `handbook/contract.md` | 手册 | 如何使用这个契约 |
| `spec/contract.md` | 标准 | 契约应该怎么写（元规则） |

## 理清

**Specification** 不是"有约束力的文件"，而是"定义规则的规则"。

- contract.yaml 定义了子模块应该有什么字段 → 这是契约
- spec/contract.md 定义了所有仓库的契约应该怎么写 → 这是标准

Specification 是元层。它是关于契约的契约，关于规则的规则。

**Handbook** 是对具体实践的解释。它告诉你怎么做，但不告诉你为什么必须这样做。

## 回到迁移

contract.md 最初在 profile/ 下，这是对的——它是对这个仓库契约的说明。

尝试放到 spec/ 是错的，因为它没有定义元规则，只是解释了一个具体文件。

最终落到 handbook/ 是对的。它是"关于这个契约的使用手册"。

## 结论

这次迁移的价值不在于找到正确位置，而在于发现了一个空缺：

我们有契约（contract.yaml），有手册（handbook/contract.md），但没有标准（spec/contract.md）。

**spec/contract.md 应该存在**，它应该定义：
- 契约的 Schema 格式
- 必须包含哪些章节
- 版本号规范
- 跨仓库的一致性要求

这是下一步要做的事。