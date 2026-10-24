---
name: meta-domain
description: 把内容从一个第二大脑迁到领域侧对应资产仓库，完成跨仓移动与逐级指针提交。两种形态：移交（default → 领域资产仓，按目标体例改写）与归档（归档站 → 领域 archive，只移动不改写）。当用户要求移交领域、归档站资源迁移、或说「从 default 到领域」时使用。
---

# 元域迁移

两侧都是第二大脑，只是域不同：一边是 default（创始人、实训基地、联盟），一边是 `domains/<领域>`。结构相同，归属不同。

迁移就是搬到对侧，再把各级指针按顺序更新。判错形态的代价不一样。该改体例的照搬过去，目标仓多一份不合体的文；该原样搬的被重写，历史对不上。

## 两种形态

**移交**：从 default 第二大脑搬进领域资产仓。内容按目标侧的体例重写，先写目标、再删源。

**归档**：从归档站搬进领域归档。只移动文件，不改内容；源侧的分层（如 `write/`）在落位时去掉。

## 路径

- default 侧：`/home/iguo/repos/quanttide/defaults/<default>/`
- 归档站：`data/archive`，即 quanttide-archive-of-founder
- 领域侧：`/home/iguo/repos/quanttide/domains/<领域>/`
- 根仓库：`/home/iguo/repos/quanttide/`

## 资产映射

两侧同名子模块一一对应：default 侧 `data/` 与 `docs/` 下有什么，领域侧就有什么，名字相同即同一类资产。十七种格各自在哪，见 [meta-category](../meta-category/SKILL.md)，这里不重复。

目标领域没有对应子模块时，先确认该领域是否承接这件资产。不承接收手前停下问用户，不要新建子模块。

## 移交

1. 定领域：读正文判断内容属于哪个领域，不看它现在住在哪个仓库。源或目标不确定时先问。
2. 定资产：按它讲什么、按什么格式维护来判，不按目录。日志按日期，档案按材料，洞察按陈述式一条，手册按规范体例，文集是散文。
3. 定位置：去 `domains/<领域>/<资产路径>/` 找具体位置。同构优先；目标目录不存在时，停下问用户新目录名，命名归用户。
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

完整案例见 `quanttide-github/docs/gallery/second-brain/default-to-domain.md`。

## 归档

已知映射如下，目标根是 `domains/<领域>/data/archive/`。

| 源 | 目标 | 落位 |
|------|------|------|
| `journal/write/**` | `<领域>/data/archive/journal/**` | 与领域归档重合，平铺落位 |
| `journal/write/fiction/**` | 归档站 `fiction/journal/**` | fiction 主题日志回迁，例外 |
| `<资产>/write/**` | `<领域>/data/archive/<资产>/**` | 去掉 `write/` 层落位 |

fiction 域资源（如 `context/write/`）不随 write 迁移，归属由用户逐次确认。

迁移前先过四项检查：

1. 双侧工作区干净，跑 `git -C <路径> status --porcelain`。目标仓库若有未推送的本地提交，确认是用户自己的再一并推送，不要 rebase 掉。
2. 全量盘点源侧：`find data/archive -type d -name write -not -path '*/.git/*'`。
3. 落位冲突：列出目标将出现的资产目录，与源文件比对，同名即停下问用户。
4. 读者扫描：`grep -rn '<资产>/write' --include='*.md'`，只改活跃文档，`CHANGELOG` 里的历史记录不改。

提交链按序执行：

1. 移动：`mv <源>/* <目标>/<资产>/`；目标资产目录不存在时直接 `mv <源> <目标>/<资产>`，整目录改名，内容不动。
2. 领域 archive：`git -C <目标> add -A`，提交 `feat: 迁入 <资产>/write`，推送 `origin main`。
3. 领域仓库指针：`git -C domains/<领域> add data/archive`，提交 `chore: update data/archive submodule`，推送。
4. 根仓库指针：`git -C /home/iguo/repos/quanttide add domains/<领域>`，提交 `chore: update domains/<领域> submodule`，推送。
5. 归档站：删源，改活跃读者文档与 `CHANGELOG` 的路径对照，提交 `refactor: 迁出 <资产>/write 至 <领域>归档`，推送。
6. 主仓库：受影响的 skill 文档单独提交，再提交 `chore: update data/archive submodule` 指针。

## 提交与 CHANGELOG

提交遵循 Conventional Commits。移交时写目标用 `docs`，删源用 `docs` 并在 `CHANGELOG` 记移除；归档时迁入用 `feat`，迁出用 `refactor`；指针一律 `chore`。

`CHANGELOG` 只记结构与位置的变动：纯路径迁移升 minor，写明新旧路径对照，跨仓库路径写全到仓库名或领域根。同批次迁移并进当次未发布的记录，已发布的不改写。

## 约束

- 迁移期间内容至少在一处；完成后源侧不留复制件。
- 先写目标、再删源，窗口里不能两边都空。
- 归档只移动文件、不改内容；移交必须改体例。两种形态不混用。
- 只改本次迁移涉及的路径。根仓库常有其他脏指针，不带别人的变更。
- 新目录、新文件名由用户定，不自造。

## 复核

两边工作区干净；目标 `index.md` 已收录，源 `index.md` 不再有它；`grep` 确认源侧无残留引用。汇报时给各级提交、迁移文件数，以及 `CHANGELOG` 是否待发版。
