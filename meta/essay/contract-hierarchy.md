# Contract 的归宿

## 现象

今天经历了一次有意思的文件迁移：

```
profile.md → spec/contract.md → handbook/contract.md
```

三分钟内，同一个文件从"档案"升级为"标准"，又降级为"手册"。

## 问题

Handbook 和 Specification 的边界是什么？

## 定义

按程序型记忆五层：

| 层次 | 性质 | 约束力 |
|------|------|--------|
| Specification | 程序性法律 | 强制 |
| Handbook | 权威汇编 | 建议 |

Specification 是"必须这样做"，Handbook 是"建议这样做"。

## 判断

contract.md 的内容是什么？是对 contract.yaml 的解释说明。

它定义了什么必须遵守的规则吗？没有。它只是说"数据在这里，结构在那里"。

真正的约束在 contract.yaml 本身——那个 YAML 是 Schema，是规则，是"必须"。

而 contract.md 只是告诉你怎么看这个文件。

## 结论

contract.yaml 是 Specification（它定义结构和约束）
contract.md 是 Handbook（它解释如何使用）

形式不决定层级。文件放在 spec/ 还是 handbook/，不取决于它的名字，而取决于它的内容是否具有强制约束力。

一个解释性的文档，即使命名为"标准"，本质上仍是"手册"。

## 延伸

这引出一个问题：我们的子模块里，有多少"标准"其实是"手册"？

检查清单：
- 它定义了"必须"还是"建议"？
- 违反它会导致错误还是只是不推荐？
- 它可被机器验证还是仅靠人工遵守？

如果答案偏右，它可能是 Handbook 而非 Specification。