def bank(X, Y):
    # Начальная сумма вклада
    amount = X
    # Процентная ставка
    rate = 0.10
    # Расчет суммы вклада за каждый год
    for _ in range(Y):
        amount += amount * rate
    return amount

initial_deposit = 10000  # Сумма вклада в рублях
years = 5  # Срок вклада в годах
final_amount = bank(initial_deposit, years)

print(f"Сумма на счету после {years} лет будет: {final_amount:.2f} рублей")
