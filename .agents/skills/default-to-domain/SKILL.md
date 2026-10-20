---
name: default-to-domain
description: 把一个 default（quanttide/defaults 下的创始人、实训基地、联盟等）第二大脑里属于某领域的内容，迁到 domains/<领域> 的对应资产仓库。当用户要求把日志、档案、意图、洞察、手册、规范、文集、画廊等内容从某个 default 移交领域，或说「从 default 到领域」时使用。
---

# 从 default 到领域

把一个 default 第二大脑里属于某领域的内容，迁到该领域第二大脑的对应资产仓库。适用于全部资产——日志、档案、意图、洞察、路线图、报告、参考、归档、章程、手册、规范、教程、文集、画廊、宣传册、历史、语境。

完整案例见 `quanttide-github/docs/gallery/second-brain/default-to-domain.md`。

## 路径

| 侧 | 路径 |
|----|------|
| default 侧 | `/home/iguo/repos/quanttide/defaults/<default>/` |
| 领域侧 | `/home/iguo/repos/quanttide/domains/<领域>/` |
| 根仓库 | `/home/iguo/repos/quanttide/` |

## 资产映射

两侧同名子模块一一对应：

| 资产 | 路径 |
|------|------|
| 语境 | `data/context` |
| 日志 | `data/journal` |
| 档案 | `data/profile` |
| 意图 | `data/intention` |
| 洞察 | `data/insight` |
| 路线图 | `data/roadmap` |
| 报告 | `data/report` |
| 参考 | `data/library` |
| 归档 | `data/archive` |
| 宣传册 | `data/brochure` |
| 历史 | `data/history` |
| 章程 | `docs/bylaw` |
| 手册 | `docs/handbook` |
| 案例 | `docs/gallery` |
| 文集 | `docs/essay` |
| 规范 | `docs/specification` |
| 教程 | `docs/tutorial` |

目标领域没有对应子模块时，先确认该领域是否承接这件资产；不承接收手前停下问用户，不要新建子模块。

## Steps

1. 定领域：读正文判断内容属于哪个领域，不看它现在住在哪个仓库。源 default 或目标领域不确定时先问。
2. 定资产：判断资产类型，判据是它讲什么、按什么格式维护，不按目录。日志按日期、档案按材料、洞察按陈述式条目、手册按三段式规范、文集是散文。
3. 定落点：去 `domains/<领域>/<资产路径>/` 找具体位置。同构优先；目标目录不存在时，停下问用户新目录名，命名归用户。
4. 改体例：按目标资产的写法重写，术语、标题、文件名随目标侧。不要原文照搬。
5. 写目标：在目标资产子仓库写就，同步其 `index.md` 与 `CHANGELOG.md`，提交推送。

   ```sh
   git -C <目标资产仓> add -A
   git -C <目标资产仓> commit -m "docs: 新增 <标题>"
   git -C <目标资产仓> push
   ```

6. 删源：源侧删文，同步 `index.md`、`myst.yml`、`README.md`、`CHANGELOG.md`；`CHANGELOG.md` 记入「移除」，提交推送。
7. 断链：删掉源侧指向该内容的目录项与导航项；不补跨仓库相对链接。
8. 收指针，按序执行，只 add 本路径：

   ```sh
   git -C <目标领域> add <资产路径>
   git -C <目标领域> commit -m "docs: 更新 <资产> 子模块（<标题>）"
   git -C <目标领域> push

   git -C <源default> add <资产路径>
   git -C <源default> commit -m "docs: 更新 <资产> 子模块（<标题>迁出）"
   git -C <源default> push

   git -C /home/iguo/repos/quanttide add domains/<领域> defaults/<default>
   git -C /home/iguo/repos/quanttide commit -m "chore: 更新 <领域> 与 <default> 仓库指针"
   git -C /home/iguo/repos/quanttide push
   ```

9. 复核：两边工作区干净；目标 `index.md` 收录、源 `index.md` 无此内容；`grep` 确认源侧无残留引用。

## 约束

- 迁移期间内容至少在一处；完成后源侧不留副本。
- 先写目标、再删源，窗口里不能两边都空。
- 只改本次迁移涉及的路径；根仓库常有其他脏指针，不带别人的变更。
- 新目录、新文件名由用户定，不自造。
- 提交遵循 Conventional Commits：写目标用 `docs`，删源用 `docs` 并在 CHANGELOG 记移除，指针用 `chore`。
