---
name: summarize-intent
description: 当用户要汇总澄清账本、把攒下的「和 AI 协作的差」归档、或按主题整理那些差时使用；产出去向是 `quanttide-profile-of-founder` 的 `code/intent/`，一主题一档。
---

# 汇总澄清需求

把澄清账本（`qtfounder-lab` 的 `clarify.json` + `rules.md`）里攒下的差，按**主题**提炼成档案，落到 profile 仓的 `code/intent/`。账本是逐条记录，档案是提炼后的类型——两者分工不能混。

## 前置

账本位置按下面顺序取，取到即止：

1. `QTFOUNDER_LAB_DATA`（临时隔离时才设）；
2. 开发版：`<lab 仓>/src/cli/data/`；
3. 发布版：`$XDG_DATA_HOME/qtfounder-lab`，未设则 `~/.local/share/qtfounder-lab`。

目标仓：`data/profile`（`quanttide-profile-of-founder`），分区 `code/`，档在 `code/intent/`。先把 profile 仓 `git pull`，再看 `code/index.md` 里已有哪些主题。

## 分类验收标准

- **主题来自「实际做了什么」这一列**，不是来自任务名、日期或工具。同一件事下的多条差，`actual` 归一化后同键的归一类。
- 主题名是协作维度上的短语（如「输出形态与篇幅」「边界与范围」「验收与收尾」），不是命令名、不是产品模块名。
- 已存在的主题档优先归入；确实新类型才新增档，并在 `code/index.md` 的表格里登记一行。
- 一个主题一档，档名用英文 slug（与 `think/`、`work/` 一致）。

## 主题档结构

```markdown
# 主题名

> 来源：澄清账本（`clarify.json`）中 `actual` 归为同一类的记录，涉及 `clr_xxx`、`clr_yyy`；状态：观察 / 类型 / 规则。

**状态：观察。**（出现 1 次）/ **类型**（≥2 次）/ **规则**（已落 `rules.md`）

## 差

一句话说清这一类差是什么：原以为 X，实际 Y。

## 记录

- `clr_xxx`（req_xxx，日期）：原以为 …… / 实际 ……

## 该用的提示词

> 可复用的那句，取自记录里的 `prompt` 或由它归并，仍用第一人称。

## 规则

已落库的规则原话（`rules.md` 那一行）；未立就写「未立」。
```

状态三档照抄 `think/` 的分层习惯：出现 1 次只算**观察**，≥2 次才算**类型**，落了规则升为**规则**。

## 流程

1. 读账本，按 `actual` 归一化键聚成簇，算出每簇次数与涉及记录。
2. 与 `code/intent/` 既有档比对：能归入的归入，不能的才新增。
3. 逐档改写（不是追加）：更新状态、差的一句话、记录明细、提示词、规则节。同一档里同一记录只出现一次。
4. 改了哪些档就同步 `code/index.md` 的表格与 `CHANGELOG.md` 的 `[Unreleased]`。
5. 提交推送：profile 仓 → `data/profile` 子模块指针 → 主仓 → 根仓。

## 边界

- **不改账本**：`clarify.json` 与 `rules.md` 只读。要修记录用 `code clarify --revise`，删记录才手改文件。
- **不生成规则**：规则文本永远是用户原话；这里只呈现「该用的提示词」和已落库的规则。
- **不搬原文**：档案收提炼后的类型与那句提示词，原始每条以 `clr_` id 指回账本；单次出现、不成类型的差留在账本，不进档案。
- 不按日期切档、不按命令切档。
