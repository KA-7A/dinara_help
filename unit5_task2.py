import random

def bigger(in_list):
    out_list = []
    if len(in_list) <= 1:   # На случай, если список пустой или содержит один элемент
        return []
    for i in range(1, len(in_list), 1):
        if in_list[i] > in_list[i-1]:
            out_list.append(in_list[i])
    # Рассматривать краевые случаи смысла нет, так как условие вполне определенное: 
    # нас интересуют только элементы, которые больше предыдущего (последнего предыдущего)
    # В случае, когда у нас одинаковые элементы, никто не больше предыдущего и список пустой
    # Также нас не интересует первый элемент (с индексом 0), так как он не может быть больше того, чего нет
    return out_list

if __name__ == "__main__":
    m_list = []
    for i in range(10): # Заполним список случайными числами в диапазоне от -100 до 100
        m_list.append(random.randint(-100, 100))   
    new_list = bigger(m_list)
    print(new_list) 