# 実行は streamlit run <python-file>

import streamlit as st
import time

# streamlit のタイトル
st.title('Streamlit 超入門')

# 'Display Image'という文字の書き出し
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Interation {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'
