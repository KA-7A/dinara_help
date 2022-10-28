# запишем референсные значения, чтобы к ним легко можно было обращаться
from weakref import ref


reference_values = [['Hb', 120, 140], 
                    ['RBC', 3.7, 4.7], 
                    ['PLT', 180, 320],
                    ['WBC', 4, 9], 
                    ['LYM', 18,40]]

def check_values(values):
    out_str = ""
    for value, ref_value in zip(values, reference_values):              # Идем по двум спискам одновременно
        if ref_value[1] >= value:                                       # если значение ниже нижнего рефернсного 
            out_str += ref_value[0] + "," + str(value) + ", понижен\n"  # добавляем информацию об этом
        elif ref_value[2] <= value:                                     # иначе, если значение больше верхнего референсного
            out_str += ref_value[0] + "," + str(value) + ", повышен\n"  # добавляем информацию
    return out_str                                                      # возвращаем конечную строку с полной информацией


if __name__ == "__main__":
    out_str = check_values((130, 3.9, 340, 5, 16))
    print(out_str)