salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
vsego=0
ostatok=0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долг
for m in range(months):
    vsego = salary + ostatok
    if spend>=vsego:
        money_capital += spend-vsego
        ostatok=0
    else:
        ostatok=vsego-spend
    spend *= (1 + increase)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
