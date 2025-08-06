import streamlit as st

# タイトル（クリックでリロード = ホームに戻る）
st.markdown("### [Author Style Analyzer](#)")

# サイドバーでn-gram選択
ngram_type = st.radio(
    "Select n-gram type:",
    ["bigram", "trigram"],
    horizontal=True
)

# テキスト入力 or ファイルアップロード
st.subheader("Upload or Paste Text")
uploaded_file = st.file_uploader("Upload .txt file", type=["txt"])
input_text = st.text_area("Or paste your text here", height=200)

# 分析開始ボタン（スタイルはCSSで後ほど追加可能）
if st.button("Start Analysis"):
    st.success(f"Analysis started with {ngram_type}")

# 分析結果表示切り替え（まだ中身はダミー）
st.subheader("Analysis Results")
tab1, tab2, tab3 = st.tabs(["Ranking", "Bar Graph", "Word Cloud"])
with tab1:
    st.write("Ranking output here...")
with tab2:
    st.write("Bar graph output here...")
with tab3:
    st.write("Word cloud output here...")
