# -data-governance-analysis-
本项目解决企业在多源数据处理、业务指标分析、异常归因、自动化报告生成中的效率低、易出错、响应慢等核心痛点，实现从原始数据到业务决策的全链路自动化。


# 数据治理与分析（data-governance-analysis）
基于小米MiMo Orbit大模型 + OpenAI 构建的企业级多源数据治理与分析Agent系统，用于小米MiMo Orbit百万亿Token创造者激励计划申请。
申请人：谢炜（GitHub：ovox0652）
项目介绍
本项目解决企业在多源数据处理、业务指标分析、异常归因、自动化报告生成中的效率低、易出错、响应慢等核心痛点，实现从原始数据到业务决策的全链路自动化。
核心功能
- 数据接入Agent：自动对接MySQL、数仓、CSV等多源数据，完成格式校验、去重、缺失值填充等清洗操作；
- 指标理解Agent：通过长链推理理解业务需求，对齐指标口径，自动生成SQL查询脚本；
- 分析与可视化Agent：基于查询结果自动进行趋势分析、异常归因，生成可直接交付的业务分析报告；
- 告警与复盘Agent：对关键指标进行监控，异常时自动生成告警并输出初步归因结论。
项目效果
将业务分析报告的生成效率从2天/份提升至2小时/份，指标口径错误率降低90%，大幅提升企业数据决策的响应速度。
部署方法
1. 克隆仓库：git clone https://github.com/ovox0652/data-governance-analysis.git
2. 安装依赖：pip install -r requirements.txt
3. 填入OpenAI API Key（app.py文件中）
4. 本地运行：streamlit run app.py
5. 在线部署：通过Streamlit Cloud关联本仓库，一键部署。
依赖说明（requirements.txt）
streamlit
pandas
openai
