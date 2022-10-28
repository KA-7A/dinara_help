
def is_in_mkb_list():
    MKB_list = [s for s in input("Введите список МКБ кодов -> ").split()]   # читаем список МКБ кодов
    MKB_code = input("Введите МКБ код для поиска ->")                       # Получаем Х код
    codes = []
    for i in range(len(MKB_list)):          # Идём по списку кодов
        if MKB_code == MKB_list[i][1:]:     # Проверяем, равен ли X коду из списка
            codes.append(i)                 # Если совпадает, то добавляем индекс
    if len(codes) == 0:                     # Проверяем равенство длины выходного списка индексов нулю
        print("Отсутствуют")
        return
    print(len(codes))                       # Печатаем длину списка
    print("Список индексов: ",codes)        # Печатаем сам список
    return 
    
if __name__ == "__main__":
    is_in_mkb_list()