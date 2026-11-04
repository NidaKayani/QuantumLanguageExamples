"""Produce a loan amortization schedule with Decimal arithmetic."""

from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def monthly_payment(principal, annual_rate, months):
    r = annual_rate / 12
    if r == 0:
        return (principal / months).quantize(CENT)
    factor = (1 + r) ** months
    return (principal * r * factor / (factor - 1)).quantize(CENT, rounding=ROUND_HALF_UP)


principal = Decimal("15000")
rate = Decimal("0.065")
months = 12

payment = monthly_payment(principal, rate, months)
print(f"Loan {principal:,} at {rate:.2%} over {months} months -> payment {payment}")
print(f"{'#':>3}{'payment':>10}{'interest':>10}{'principal':>11}{'balance':>11}")

balance = principal
total_interest = Decimal("0")
for month in range(1, months + 1):
    interest = (balance * rate / 12).quantize(CENT, rounding=ROUND_HALF_UP)
    pay = payment if month < months else balance + interest
    toward_principal = pay - interest
    balance -= toward_principal
    total_interest += interest
    print(f"{month:>3}{pay:>10}{interest:>10}{toward_principal:>11}{balance:>11}")

print(f"total interest: {total_interest}")
print(f"total paid: {principal + total_interest}")

print("\npayment by term:")
for years in (1, 3, 5, 10):
    m = years * 12
    p = monthly_payment(principal, rate, m)
    print(f"  {years:>2} years: {p:>8}/month, interest {p * m - principal:>9}")
print("zero-rate loan:", monthly_payment(Decimal("1200"), Decimal("0"), 12))
