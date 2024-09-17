import streamlit as st

st.set_page_config(layout="wide", page_title="db exporting")
st.title("data export settings")
st.markdown("### DBから出力するデータ項目の選択画面")

st.selectbox(
    "設定するIPを選択(demo)",
    ("192.168.0.2", "192.168.0.3", "192.168.0.4")
)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Researchmap関連")
    check = st.checkbox("rmap id")

    check_list1 = [
        "所属名",
        "職名",
        "番号",
        "メールアドレス",
        "・・・"
    ]
    
    check_append1 = []
    for i in range(len(check_list1)):
        check_append1.append(st.checkbox(check_list1[i]))


with col2:
    st.header("DB関連")
    check2 = st.checkbox("研究者ID")
    check_list2 = [
        "年度",
        "学期",
        "授業科目名",
        "科目区分",
        "・・・・"
    ]
    check_append2 = []
    for i in range(len(check_list2)):
        check_append2.append(st.checkbox(check_list2[i]))

with col3:
    st.header("others")
    check3 = st.checkbox("others")
    check_list3 = ["1", "2", "3", "4", "・・"]
    check_append3 = []
    for i in range(len(check_list3)):
        check_append3.append(st.checkbox(check_list3[i]))

st.markdown("---")
st.button("設定登録")
st.button("テスト出力")
