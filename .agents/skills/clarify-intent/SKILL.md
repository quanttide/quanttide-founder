---
name: clarify-intent
description: 当用户在跟 AI 协作中察觉「不对劲」、要记一次澄清、或要复盘已攒的差并立成规则时使用；落地调用 qtfounder-lab 的命令行。
---

# 澄清意图

把一句「不对劲」变成一条记录和一段能粘回对话的话，同一类差重复出现时提示立成规则。命令是 `qtfounder-lab`（与正式版 `qtfounder` 区分），契约见 lab 仓 `src/cli/docs/api-references/`。

## 规则

- **只在用户召唤时做**。用户没说「不对劲 / 停一下 / 记一下这次」就不主动记，不猜意图，不做情绪检测。
- **两问必须落到具体行为**。答得笼统（「它就是不行」）追问一次「举它刚才那句话或那个动作」；追问后仍笼统，就记用户实际说的那句，不替它编。
- **规则文本永远是用户的话**。工具与 agent 都不代写规则，只把候选顶到用户面前，点头后才落库。
- **数据目录固定，不按 cwd 散落**。所有命令前先 `export QTFOUNDER_LAB_DATA=${QTFOUNDER_LAB_DATA:-$HOME/.local/share/qtfounder-lab}`——CLI 默认落 `./data/`，换目录跑就会各存一份。
- 输出给用户的是提示词原文（`prompt` 字段），不是让它自己去组织语言。

## 前置

```bash
export QTFOUNDER_LAB_DATA=${QTFOUNDER_LAB_DATA:-$HOME/.local/share/qtfounder-lab}
command -v qtfounder-lab || cargo install --offline --path \
  "$HOME/repos/quanttide/defaults/quanttide-founder/examples/quanttide-founder-lab/src/cli"
```

## 工作流

### 1. 两问

先问「你原本以为它知道 / 会做什么？」，再问「它实际做了什么？」。两问答完即可，不要先分类这是偏差还是意图。

### 2. 记一条，拿回提示词

一次把整条记录走 stdin，`--json` 拿结构化结果：

```bash
qtfounder-lab work clarify --stdin --json <<'JSON'
{"before":"我以为它知道我要能直接跑的代码","actual":"给了五段解释加伪代码","prompt":""}
JSON
```

`prompt` 留空时按两问拼模板；也可直接把已经写好的那段话放进 `prompt`。要新开一件事加 `"task":"<一句话>"`，不加就挂到最近一件事上。

把返回的 `prompt` 原文给用户，并说明「可以直接粘回对话」。若 `deduplicated` 为 true，说明这条之前记过，只提示、不重复记账。

### 3. 看有没有够格的候选

```bash
qtfounder-lab work intent --json
```

找当前 intent 的 `candidates`：`count ≥ 2` 即同一类差已重复。有候选就问一句「这类差第 N 次了，要不要立成一条规则？」——**等用户给文本**，不要替它写。

### 4. 用户点头才落规则

```bash
qtfounder-lab work clarify --rule "<用户原话>"
```

落库后回一句：写进了哪个文件、这一批重复差已标为处理过。`rules.md` 由用户自己保管，下次开工前给 AI 看。

## 示例

```text
用户：/clarify-intent，它又在给我写一大堆

agent：你原本以为它知道 / 会做什么？
用户：我要的是能直接用的短结论，三行以内
agent：它实际做了什么？
用户：先讲了两大段背景才给答案

agent：（跑 clarify --stdin）
       我原以为「我要的是能直接用的短结论，三行以内」。
       它实际做了「先讲了两大段背景才给答案」。
       请按我原以为的重做一遍，把这两条当约束。
       —— 这段可以直接粘回对话。

agent：（跑 intent --json，发现同类差 ×2）
       这类差第 2 次了，要不要立成一条规则？你给一句话。
用户：先结论后细节，除非我明确要展开
agent：（跑 clarify --rule "先结论后细节，除非我明确要展开"）已写进 rules.md。
```

## 排错

错误一律是 JSON、写在 stderr，退出码三档：

| 码 | 含义 | 常见原因 |
|----|------|---------|
| 0 | 成功（含去重） | — |
| 2 | 用法错 | `--stdin` 少 `before`/`actual`/`prompt`；`--task` 与 `--rule` 同给；`--rule` 文本为空；无可挂的意图（没给 `task` 而库里还没有任何意图） |
| 3 | 未找到 | `--id` 指向的意图不存在 |
