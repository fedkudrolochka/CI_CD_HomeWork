DEADLINE = 20


def ask_deadline(today, homework_done):
    if type(today) is not int or not 1 <= today <= 31:
        raise ValueError("Неверное число!")

    if homework_done not in ("да", "нет"):
        raise ValueError("Введите да или нет!")

    if homework_done == "да":
        if today < DEADLINE:
            return "Михаил: Молодец!"
        elif today == DEADLINE:
            return "Михаил: Работа сдана!"
        else:
            return "Михаил: Работа сдана с опозданием!"

    if today < DEADLINE:
        return "Михаил: Сместим!"

    raise ValueError("Надо было думать раньше!")


if __name__ == "__main__":
    try:
        today = int(input("Какое сегодня число? "))
        homework_done = input("ДЗ выполнено? (да/нет): ").strip().lower()

        print(ask_deadline(today, homework_done))

    except ValueError as error:
        print(f"Ошибка: {error}")
