import streamlit as st
import requests

st.title("💱 환율 계산기 (KRW · USD · EUR)")

# --- 환율 가져오기 함수 ---
def get_rate(base="USD"):
    url = f"https://open.er-api.com/v6/latest/{base}"
    response = requests.get(url)
    data = response.json()

    if data.get("result") != "success":
        st.error(f"API 오류 발생: {data}")
        return None

    return data["rates"]

# --- 변환 함수 ---
def convert(amount, from_currency, to_currency):
    rates = get_rate(from_currency)
    if rates is None:
        return None

    if to_currency not in rates:
        st.error(f"{to_currency} 환율 정보를 찾을 수 없습니다!")
        return None

    return amount * rates[to_currency]

# --- UI 구성 ---
st.subheader("환율 변환하기")

amount = st.number_input("금액을 입력하세요", min_value=0.0, format="%.2f")
from_currency = st.selectbox("변환할 통화", ["USD", "KRW", "EUR"])
to_currency = st.selectbox("목표 통화", ["USD", "KRW", "EUR"])

if st.button("변환하기"):
    result = convert(amount, from_currency, to_currency)
    if result is not None:
        st.success(f"➡ {amount} {from_currency} = {result:,.2f} {to_currency}")

