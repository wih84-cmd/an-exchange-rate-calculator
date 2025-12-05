import requests

def get_rate(base="USD"):
    """exchangerate.host API에서 환율 가져오기"""
    url = f"https://api.exchangerate.host/latest?base={base}"
    response = requests.get(url)
    data = response.json()
    return data["rates"]

def convert(amount, from_currency, to_currency):
    """환율 변환"""
    rates = get_rate(from_currency)
    return amount * rates[to_currency]

def main():
    print("=== 환율 계산기 (KRW, USD, EUR) ===")
    amount = float(input("금액을 입력하세요: "))
    from_currency = input("변환할 통화 (KRW / USD / EUR): ").upper()
    to_currency = input("목표 통화 (KRW / USD / EUR): ").upper()

    result = convert(amount, from_currency, to_currency)
    print(f"\n➡ {amount} {from_currency} = {result:,.2f} {to_currency}")

if __name__ == "__main__":
    main()
