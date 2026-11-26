"""Simple Python application for MIS2001 Week 11 Exercise 1 (CI/CD)."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def convert_to_cny(amount: float, currency: str) -> float:
    rates = {
        "USD": 6.9,
        "EUR": 7.5,
        "CNY": 1.0,
        "JPY": 0.05,
    }
    code = currency.upper()
    if code not in rates:
        raise ValueError(f"Unsupported currency: {currency}")
    return round(amount * rates[code], 2)


if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("100 USD in CNY =", convert_to_cny(100, "USD"))
