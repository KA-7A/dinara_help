import random

def swap_min_max(in_list):
    ind_min = in_list.index(min(in_list))   # получаем из списка индекс минимального элемента списка
    ind_max = in_list.index(max(in_list))   # аналогично
    tmp = in_list[ind_max]                  # меняем местами
    in_list[ind_max] = in_list[ind_min]
    in_list[ind_min] = tmp


if __name__ == "__main__":
    m_list = []
    for i in range(10): # Заполним список случайными числами в диапазоне от -100 до 100
        m_list.append(random.randint(-100, 100))  
    print(m_list)
    swap_min_max(m_list)
    print(m_list) 
