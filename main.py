
income = 0
expenses = 0
expense_categories = {}

while True:
    print("\n===== ЛИЧНЫЙ БЮДЖЕТ =====")
    print("1. Добавить доход")
    print("2. Добавить расход")
    print("3. Показать баланс")
    print("4. Расходы по категориям")
    print("5. Самая затратная категория")
    print("6. Выход")

    choice = input("Выбери действие: ")

    if choice == "1":
        amount = float(input("Введи сумму дохода: "))
        if amount > 0:
            income += amount
            print("Доход добавлен!")
        else:
            print("Сумма должна быть больше нуля.")

    elif choice == "2":
        amount = float(input("Введи сумму расхода: "))

        if amount > 0:
            category = input("Введи категорию расхода: ")

            expenses += amount
            expense_categories[category] = expense_categories.get(category, 0) + amount

            print("Расход добавлен!")
        else:
            print("Сумма должна быть больше нуля.")

    elif choice == "3":
        balance = income - expenses
        print("Доход:", income)
        print("Расход:", expenses)
        print("Баланс:", balance)

    elif choice == "4":
        if expense_categories:
            for category, amount in expense_categories.items():
                print(category, ":", amount)
        else:
            print("Расходов пока нет.")

    elif choice == "5":
        if expense_categories:
            biggest = max(expense_categories, key=expense_categories.get)
            print("Самая затратная категория:", biggest)
            print("Сумма:", expense_categories[biggest])
        else:
            print("Расходов пока нет.")

    elif choice == "6":
        print("До свидания!")
        break

    else:
        print("Неверный выбор!")





