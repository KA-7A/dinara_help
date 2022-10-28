base_stip_size = 5000

def middle_result(session_dict: dict, optional: int = 1):
    average_mark = 0
    for item in session_dict:
        average_mark += session_dict[item]
    average_mark /= len(session_dict)
    if 3.5 <= average_mark < 4.5:
        return base_stip_size * optional
    elif 4.5 <= average_mark <= 5:    # А в чем разница? Странная формулировка.
        return base_stip_size * optional
    else:
        return ("стипендия не выплачивается")

def test():
    session_dict = {"матан": 4, "информатика": 5}
    print(middle_result(session_dict))
    session_dict["биология"] = 2
    print(middle_result(session_dict))
    session_dict["биология2"] = 2
    print(middle_result(session_dict))
    session_dict["тесты"] = 5
    print(middle_result(session_dict, 10))

if __name__ == "__main__":
    test()