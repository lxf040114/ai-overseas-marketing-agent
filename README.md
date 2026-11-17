# AI 出海营销助手

一个用 AI 串起「找客户 → 联系 → 写方案 → 交付 → 复盘」的出海营销助手 Demo，帮助出海营销服务商高效锁定「可能需要出海营销服务的 AI 企业」，并用一个模拟客户案例走完五环节闭环。

## 产品思路

出海营销服务商最痛的环节不是「做营销」，而是「找到对的人、让对的人愿意聊」。传统做法靠买名单、人工筛选、逐条写开发信，效率低且缺乏针对性。

本助手把这条链交给 AI：从一批候选 AI 企业中，按 ICP（理想客户画像）自动打分排序、给出「为什么」的理由，再生成个性化开发信、撰写服务方案、拆解交付任务，最后用数据复盘并反馈优化——形成「分析 → 联系 → 方案 → 交付 → 复盘 → 再分析」的闭环。

## 运营方式

- **输入**：候选 AI 企业池（官网、融资、产品、出海信号等结构化信息）；
- **流程**：潜客分析（打分排序）→ 潜客联系（开发信 + 跟进节奏）→ 方案撰写 → 执行交付（任务 + 样例）→ 数据复盘（改进）；
- **真实场景**：企业数据可接入公开数据源 / CRM，开发信经人工确认后发送，复盘结果回写 ICP 权重与话术，实现自改进。

## 技术实现

- **Demo 形态**：Streamlit 五页签应用，每页签对应一个环节；
- **打分模型**：五维加权（产品适配 25% / 出海信号 25% / 预算 20% / 触达 15% / 时机 15%），总分由代码实时计算；
- **数据**：全部为模拟数据（Python 内嵌），不接真实 CRM、不真实发送邮件；
- **可扩展**：真实场景可将静态内容替换为 LLM API 调用（LiteLLM 统一接入），并用 LangGraph 编排五环节 Agent。

## AI 工具使用说明

| AI 工具 | 用于环节 | 具体用途 |
|---------|---------|---------|
| ChatGPT / Claude | 环节 1–5 | 方案设计、ICP 定义推演、开发信 / 方案 / 文案生成、复盘分析 |
| Codex | Demo 开发 | 生成 Streamlit 应用代码、打分逻辑实现 |
| Claude | 环节 4 | 交付样例（英文落地页文案）生成 |

## 运行方式

```bash
pip install streamlit
streamlit run app.py
```

## 在线部署（Streamlit Community Cloud）

代码已托管在 GitHub：https://github.com/lxf040114/ai-overseas-marketing-agent

部署三步（免费、公开应用）：

1. 打开 https://share.streamlit.io ，用 GitHub 账号登录；
2. 点右上角 **Create app** → 选 **"Yup, I have an app"**；
3. 填写 Repository `lxf040114/ai-overseas-marketing-agent`、Branch `main`、Main file path `app.py`，点 **Deploy**。

也可以点 **"Paste GitHub URL"** 直接粘贴入口文件链接：

```
https://github.com/lxf040114/ai-overseas-marketing-agent/blob/main/app.py
```

`requirements.txt` 仅依赖 streamlit，冷启动很快；部署后每次 `git push` 会自动更新线上应用。

## 目录结构

```
├── app.py              # Streamlit 主应用（5 个页签）
├── content/            # 五环节内容（Markdown）
│   ├── 01_潜客分析.md
│   ├── 02_联系内容.md
│   ├── 03_服务方案.md
│   ├── 04_任务清单.md
│   ├── 05_交付样例.md
│   └── 06_复盘报告.md
└── requirements.txt
```

## 参考项目

- `eracle/OpenOutreach` — 描述式获客 + 每条线索附「可读可反驳」的为什么；
- `zubair-trabzada/ai-sales-team-claude` — 14 skills + 5 agents 完整销售团队划分；
- `1160339764/AI_Find_Customer` — FastAPI + LangGraph + React 多 Agent 流水线；
- `Kandid-ai/AgentSDR` — 开源 AI SDR，多渠道序列化触达 + AI CRM。
