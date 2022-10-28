import random

def cut_even(in_list):
    out_list = []
    for i in range(0, len(in_list), 2):
        out_list.append(in_list[i])
    out_list.sort(reverse=True)
    return out_list

if __name__ == "__main__":
    m_list = []
    for i in range(10): # Заполним список случайными числами в диапазоне от -100 до 100
        m_list.append(random.randint(-100, 100))    
    new_list = cut_even(m_list)
    print(new_list)