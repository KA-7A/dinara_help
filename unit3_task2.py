def bacterias():
    # В начальный момент была 1 бактерия
    # Через минуту она разделилась на 2
    # Ещё через минуту их стало 4
    # ...
    # через N минут бактерий будет 2^N
    time = int(input("Введите время -> "))
    if time < 0:
        print("Некорректный ввод: время должно быть неотрицательно")
        return
    result = 2**time
    print(f"Количество бактерий через {time} минут равно {result}")
    pass

if __name__ == "__main__":
    bacterias()