import re
from typing import List


def clean_strings(str_list: List[str]) -> List[str]:
    # Зададим паттерн подстроки минимум с 2 буквами русского алфавита
    pattern = r'[а-яёА-ЯЁ].*[а-яёА-ЯЁ]'
    # Пройдемся циклом по списку и добавим в финальный список только те, в которых есть подстрока с 2 русскими буквами
    clean_list = [ln for ln in str_list if re.search(pattern, ln)]
    return clean_list


def main():
    # Готовый список для проверки (расскоментировать):
    # inp_list = ['мапкgyweпрыvhs', 'gyuhie', 'ыhdhs', 'ghjdщvhedb', 'vhbejdжж', 'bhdejyфghjeыdbh']

    # Если вы хотите проверить на своих строках через инпут
    inp_list = []
    while True:
        line = input()
        if line == '':
            break
        else:
            inp_list.append(line)

    # Вывод результата
    print(clean_strings(inp_list))


if __name__ == '__main__':
    main()
