---
name: product-requirement
description: 把 `qtfounder-lab` 本地账本里的需求差按主题整理进 `data/profile/product/requirement/`，建立持久档案，归档完成后清理本地缓存。当用户要汇总或归档澄清账本、按主题整理需求差、或清理本地缓存时使用。
---

# 产品需求归档

本地账本是缓存：逐条记录、随归档清空。`data/profile/product/requirement/` 是持久档案：一主题一档、长期保留。归档就是把这个方向走完——读账本，分类成主题档，校验落盘，再清掉缓存。

## 前置

账本位置按下面顺序取，取到即止：

1. `QTFOUNDER_LAB_DATA`（临时隔离时才设）；
2. 开发版：`<lab 仓>/src/cli/data/`；
3. 发布版：`$XDG_DATA_HOME/qtfounder-lab`，未设则 `~/.local/share/qtfounder-lab`。

目标仓是 `data/profile`（`quanttide-profile-of-founder`），档在 `product/requirement/`。先把 profile 仓 `git pull`，再看 `product/index.md` 里已有哪些主题。

## 分类验收标准

产品需求与协作差分开放：换个产品就不成立的（做什么、给谁、分几层交付）写成产品档放 `product/` 顶层，一产品一档；`requirement/` 只收与 AI 协作的差。刚归档的那三条已按此写成 `product/novel-preference-library.md`。

- 主题来自「实际做了什么」这一列，不是来自任务名、日期或工具。同一件事下的多条差，`actual` 归一化后同键的归一类。
- 主题名是协作维度上的短语（如「输出形态与篇幅」「边界与范围」「验收与收尾」），不是命令名、不是产品模块名。
- 已存在的主题档优先归入；确实新类型才新增档，并在 `product/index.md` 的表格里登记一行。
- 一个主题一档，档名用英文 slug（与 `think/`、`work/` 一致）。
- 每条记录都要进档案：单次出现进「观察」档，不留在缓存里。

## 主题档结构

```markdown
# 主题名

> 来源：澄清账本（`clarify.json`）中 `actual` 归为同一类的记录，涉及 `clr_xxx`、`clr_yyy`；状态：观察 / 类型 / 规则；已归档。

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

状态三档照抄 `think/` 的分层习惯：出现 1 次只算观察，≥2 次才算类型，落了规则升为规则。

## 流程

1. 读账本：`clarify.json` 的全部记录与 `rules.md` 的规则原文。
2. 按 `actual` 归一化键聚成簇，算出每簇次数与涉及记录。
3. 与 `product/requirement/` 既有档比对：能归入的归入，不能的才新增。
4. 逐档改写，不是追加：更新状态、差的一句话、记录明细、提示词、规则节。同一档里同一记录只出现一次。
5. 同步 `product/index.md` 的表格与 profile 仓 `CHANGELOG.md` 的 `[Unreleased]`。
6. 提交并推送 profile 仓，再更新 `data/profile` 子模块指针。缓存清理只在这一步成功之后做。
7. 清缓存，见下节。
8. 汇报：归档了哪些主题、写了几条记录、删了几条缓存；有记录没能归类就单独说。

## 清缓存

先校验，再删除。顺序不能反。

**校验**：对账本里每条 `clr_` id，在 `product/requirement/*.md` 里搜一次，必须都能搜到。搜不到的那条留在缓存，不删，并在汇报里点名。

**删除**：把已归档的记录从 `clarify.json` 移除；全部归档时直接写回空库：

```bash
printf '{\n  "requirements": []\n}\n' > "$LEDGER"
```

删完再读一次，确认 `requirements` 为空；`rules.md` 一个字都不动——那是用户自己的规则文件，不是缓存。

**后果要说清**：缓存删掉就没有第二份，档案成为唯一副本；去重也不再依赖账本，以后遇到同类差，比对档案里的主题与提示词。

## 边界

- 不改 `rules.md`：规则文本永远是用户原话，这里只读。
- 不生成规则：只呈现「该用的提示词」和已落库的规则。
- 不按日期切档、不按命令切档。
- 没有成功写进档案并推送，就绝不删缓存。

## 排错

账本读不到，多半是已经清空过：直接看 `product/requirement/` 与 `product/index.md`，不要重建缓存。归类时拿不准的，先归入最接近的既有档并在记录里保留原话，下次归档再拆。
