try:
    n = int(input("Введите число: "))
    count = 0
    while 2 ** count <= n:
        print(count)
        count += 1
except ValueError:
    print("Вы ввели не число!")
