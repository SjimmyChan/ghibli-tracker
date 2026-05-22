import streamlit as st
import json
import os

st.set_page_config(page_title="吉卜力新品情報", page_icon="🌿")
st.title("吉卜力公園新品情報站 🌿")

if os.path.exists('data.json'):
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for item in data:
        st.markdown(f"### {item['title']}")
        st.caption(f"來源: {item['category']} | 日期: {item['published']}")
        st.link_button("前往查看", item['link'])
        st.divider()
else:
    st.info("資料正在初始化中...")