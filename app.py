import requests

def get_rate(base="USD"):
    """open.er-api.com을 사용한 무료 환율 API"""
    url = f"https://open.er-api.com/v6/latest/{base}"
    response = requests.get(url)
    data = response.json()

    # 오류 처리
    if data.get("result") != "success":
        raise Exception(f"API 오류: {data}")

    return data["rates"]

def convert(amount, from_currency, to_currency):
    rates = get_rate(from_currency)
    
    if to_currency not in rates:
        raise Exception(f"{to_currency} 환율 정보를 찾을 수 없습니다!")

    return amount * rates[to_currency]

def main():
    print("=== 환율 계산기 (KRW, USD, EUR) ===")
    amount = float(input("금액을 입력하세요: "))
    from_currency = input("변환할 통화 (KRW / USD / EUR): ").upper()
    to_currency = input("목표 통화 (KRW / USD / EUR): ").upper()

    try:
        result = convert(amount, from_currency, to_currency)
        print(f"\n➡ {amount} {from_currency} = {result:,.2f} {to_currency}")
    except Exception as e:
        print("\n[오류 발생!]")
        print(e)

if __name__ == "__main__":
    main()
