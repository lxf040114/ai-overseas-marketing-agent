import streamlit as st
from pathlib import Path

st.set_page_config(page_title="AI 出海营销助手", layout="wide")

# ============ 打分模型（五维加权）与模拟数据 ============
WEIGHTS = {"适配": 0.25, "信号": 0.25, "预算": 0.20, "触达": 0.15, "时机": 0.15}

LEADS = [
    {"企业": "智影科技", "产品": "AI 视频生成工具", "融资": "B 轮",  "适配": 90, "信号": 85, "预算": 85, "触达": 90, "时机": 90},
    {"企业": "声纹智能", "产品": "AI 语音合成",   "融资": "B 轮",  "适配": 85, "信号": 72, "预算": 80, "触达": 75, "时机": 78},
    {"企业": "代码侠",   "产品": "AI 编程助手",   "融资": "C 轮",  "适配": 95, "信号": 55, "预算": 92, "触达": 50, "时机": 55},
    {"企业": "灵犀写作", "产品": "AI 写作助手",   "融资": "A 轮",  "适配": 80, "信号": 62, "预算": 65, "触达": 80, "时机": 70},
    {"企业": "绘梦 AI",  "产品": "AI 图片生成",   "融资": "天使轮", "适配": 85, "信号": 75, "预算": 35, "触达": 80, "时机": 70},
    {"企业": "客服星",   "产品": "AI 客服机器人", "融资": "A+ 轮", "适配": 75, "信号": 50, "预算": 70, "触达": 70, "时机": 60},
    {"企业": "言灵 AI",  "产品": "AI 翻译 SaaS",  "融资": "A 轮",  "适配": 70, "信号": 55, "预算": 60, "触达": 75, "时机": 65},
    {"企业": "数见 AI",  "产品": "AI 数据分析",   "融资": "pre-A", "适配": 60, "信号": 30, "预算": 40, "触达": 70, "时机": 40},
]


def calc_score(lead):
    return round(sum(lead[k] * w for k, w in WEIGHTS.items()), 1)


def build_scored_table():
    rows = []
    for lead in LEADS:
        d = dict(lead)
        d["总分"] = calc_score(lead)
        rows.append(d)
    rows.sort(key=lambda x: -x["总分"])
    return rows


SCORED = build_scored_table()

CONTENT_DIR = Path(__file__).parent / "content"


def load_md(name):
    return (CONTENT_DIR / name).read_text(encoding="utf-8")


# ============ 侧边栏 ============
st.sidebar.title("AI 出海营销助手")
st.sidebar.markdown("**命题**：找到可能需要出海营销服务的 AI 企业，用模拟客户案例串起 5 个环节。")
st.sidebar.markdown("---")
st.sidebar.markdown("**五个环节**")
st.sidebar.markdown(
    "1. 潜客分析\n"
    "2. 潜客联系\n"
    "3. 方案撰写\n"
    "4. 执行交付\n"
    "5. 数据复盘"
)
st.sidebar.markdown("---")
st.sidebar.markdown("**AI 工具使用**")
st.sidebar.markdown(
    "- 方案设计：ChatGPT / Claude\n"
    "- 代码生成：Codex\n"
    "- 文案生成：Claude"
)
st.sidebar.caption("本 Demo 全部数据为模拟数据，不真实联系客户")

# ============ 主区 ============
st.title("AI 出海营销助手")
st.caption("一个用 AI 串起「找客户 → 联系 → 写方案 → 交付 → 复盘」的出海营销助手 Demo")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["1 潜客分析", "2 潜客联系", "3 方案撰写", "4 执行交付", "5 数据复盘"]
)

with tab1:
    st.subheader("候选企业打分排序（系统按五维权重计算总分）")
    st.dataframe(SCORED, width="stretch")
    st.markdown(load_md("01_潜客分析.md"))

with tab2:
    st.markdown(load_md("02_联系内容.md"))

with tab3:
    st.markdown(load_md("03_服务方案.md"))

with tab4:
    st.markdown(load_md("04_任务清单.md"))
    st.markdown("---")
    st.markdown(load_md("05_交付样例.md"))

with tab5:
    st.markdown(load_md("06_复盘报告.md"))

st.markdown("---")
st.caption("AI 出海营销助手 Demo · 数据均为模拟 · 仅演示关键流程")
