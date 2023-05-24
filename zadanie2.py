try:
    S = int(input("Введите натуральную сумму чисел: "))
    P = int(input("Введите натуральное произведение этих же чисел чисел: "))
    i = 0
    if S > 0 and P > 0:
        for x in range(1, 1000):
            for y in range(1, 1000):
                if S == x + y and P == x*y:
                    i = 1
                    print(f"Первое число равно {x} и второе число равно {y}")    
    if i != 1:
        print("Вы ввели не верные значения!") 
except ValueError:
    print("Вы ввели не число!")     