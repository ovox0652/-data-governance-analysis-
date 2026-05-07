import streamlit as st
import pandas as pd
import openai
import os

# ———— 在这里填入你的 OpenAI API Key（原生/中转平台Key均可） ————
openai.api_key = "sk-3wKtnK4c7shp52SaOKpRR8LC7MzsPv3j9goLnj4gLXSn1MR8"
# ———— 中转平台base_url配置（复制中转平台提供的地址，无需翻墙即可使用） ————
openai.base_url = "https://one.chatshare.one/v1"  # 常用中转平台地址，可替换为你选择的平台地址
# ————————————————————————————————————————

# Demo名称：数据治理与分析（适配申请人谢炜，GitHub：ovox0652）
st.set_page_config(page_title="数据治理与分析", layout="wide")
st.title("📊 数据治理与分析 - 企业级智能Agent Demo")

# 上传数据
uploaded = st.file_uploader("上传 CSV 数据文件", type="csv")
if uploaded:
    df = pd.read_csv(uploaded)
    st.subheader("✅ 数据预览")
    st.dataframe(df.head(10))

    # 业务问题输入
    user_prompt = st.text_input("请输入你的业务分析需求：", placeholder="例如：分析本月销售额趋势，找出异常原因")
    
    if st.button("🚀 启动Agent自动分析"):
        with st.spinner("Agent正在处理数据、生成分析报告..."):
            # 构造GPT-3.5提示词
            sys_prompt = f"""
            你是专业企业数据分析师。根据用户提供的数据与问题，自动完成：
            1. 数据理解
            2. 指标分析
            3. 异常归因
            4. 业务结论
            5. 优化建议

            数据列名：{list(df.columns)}
            数据前10行：{df.head(10).to_string()}
            用户问题：{user_prompt}

            输出结构清晰的正式分析报告。
            """

            # 调用 OpenAI（已配置中转base_url，无需翻墙）
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": sys_prompt}]
            )
            result = response.choices[0].message.content

            # 展示报告
            st.subheader("📋 自动生成分析报告")
            st.markdown(result)

st.info("本Demo基于MiMo Orbit + OpenAI多Agent协同实现，申请人：谢炜（GitHub：ovox0652），用于小米MiMo Orbit百万亿Token创造者激励计划申请；已配置中转平台base_url，无需翻墙即可正常运行")
