#  Поскольку в задании не сказано, что такое "слово", будем считать, что 
# слово -- это подстрока, которая находится в начале или в конце строки, и отделена
# от остальной строки пробелом, либо отделена от строки пробелами с обеих сторон. 
# При этом в слове пробелов не содержится.
# 
# Иначе говоря, мы не рассатриваем случаи, когда слова могут быть разделены чем-то, кроме пробелов

def main(filename):
    with open(filename, "r", encoding="utf-8") as file: # Открываем файл
        string_list = file.readlines()                  # Читаем все строки из файла
    words = []                                          # Делаем список строк в файле (пока пустой)
    for string in string_list:                          # Рассматриваем каждую строку из файла:
        words += string.split("\n")[0].split(" ")       # Добавляем к списку слов разделенную на слова строку
    max_len = len(max(words, key = len))                # Получаем длину самого длинного слова
    for word in words:                                  # Смотрим все слова в списке
        if len(word) == max_len:                        # Если слово имеет ту же длину, что и максимальное
            print(word)                                 # Печатаем его

if __name__ == "__main__":
    filename = input("Введите название файла -> ")
    main(filename)