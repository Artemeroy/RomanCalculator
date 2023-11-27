# класс для арабских чисел
class Integer_A_R:
    def __init__(self, integer):
        self.integer = integer

    # перевод из арабской в римскую СС
    def arabic_roman(self, num):
        romans = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ints = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_num = ''
        for i in range(len(romans)):
            count = num // romans[i] # вычисляем количество цифр
            roman_num += ints[i] * count # добавляем цифры
            num -= romans[i] * count # вычитаем значения
        return roman_num


# класс для римских чисел
class String_R_A:
    def __init__(self, string):
        self.string = string

    # перевод из римской в арабскую СС
    def roman_arabic(self, string):
        # словарь соответствия римских цифр и числовых значений
        lexicon = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_num = 0
        for i in range(len(string)):
            # если текущий символ больше предыдущего
            if i > 0 and lexicon[string[i]] > lexicon[string[i - 1]]:
                # то вычитаем из его значения двойное значения предыдущего
                int_num += lexicon[string[i]] - 2 * lexicon[string[i - 1]]
            else:
                # иначе просто прибавляем значение текущего символа
                int_num += lexicon[string[i]]
        return int_num


# адаптер для перевода римских чисел
class Adapter_Roman_Arabic:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        converter = String_R_A(self.string)
        return str(converter.roman_arabic(self.string))


# адаптер для перевода арабских чисел
class Adapter_Arabic_Roman:
    def __init__(self, integer):
        self.integer = integer

    def __int__(self):
        converter = Integer_A_R(self.integer)
        return converter.arabic_roman(self.integer)


# функция перевода чисел
def translate(data):
    # перебор списка
    for i in data:
        # если элемент - строка
        if isinstance(i, str):
            # переводим из римского в арабское число через адаптер
            print(f"{i} -> {Adapter_Roman_Arabic(i).__str__()}")
        # если элемент - число
        elif isinstance(i, int):
            # переводим из арабского в римское число через адаптер
            print(f"{i} -> {Adapter_Arabic_Roman(i).__int__()}")

# функция вычисления выражений
def calculate(expr):
    # разбиваем выражение на числа и операцию
    nums = expr.split()
    if nums[0].isdigit():
        # арабские числа
        num1 = int(nums[0])
        num2 = int(nums[2])
        result = eval(nums[1], num1, num2)
        print(f"{expr} = {int(result)}")
    else:
        # римские числа
        num1 = String_R_A(nums[0]).roman_arabic(nums[0])
        num2 = String_R_A(nums[2]).roman_arabic(nums[2])
        result = eval(nums[1], num1, num2)

        result = int(result)
        result = Integer_A_R(result).arabic_roman(result)
        print(f"{expr} = {result}")

# вычисление операций
def eval(op, num1, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2


# меню и функции калькулятора
def functions():
    n = 0
    # сделано для повторного вывода меню после совершения действия
    while n == 0:
        print("""Меню древнеримского калькулятора:
1. Перевод чисел из римских в арабские.
2. Перевод чисел из арабских в римские.
3. Вычисление выражения.
4. Выход.""")
        print("Выберите пункт меню: ")
        x = int(input())
        if x == 1:
            translate(input("Введите римские числа через запятую: ").split(", "))
        elif x == 2:
            translate([int(n) for n in input("Введите арабские числа через запятую: ").split(", ")])
        elif x == 3:
            calculate(str(input("Введите выражение: ")))
        elif x == 4:
            print("Выход")
            break
        else:
            print("Такой функции не существует.")

functions()