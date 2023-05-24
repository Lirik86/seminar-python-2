try:
    n=int(input("Введите кол-во монеток: "))
    import random
    count1 = 0
    count2 = 0
    for i in range(n):
        m = random.randint(0, 1)
        if m == 0:
            count1 += 1
        else:
            count2 += 1
    if count1 > count2:
        print(f"Кол-во монеток решкой: {count1}. Кол-во монеток орлом: {count2}. Наименьшее кол-во монеток необходимое для переворота на другую сторону {count2}")
    elif count1 == count2:
        print("Кол-во монеток одинаково!")
    else:
        print(f"Кол-во монеток решкой: {count1}. Кол-во монеток орлом: {count2}. Наименьшее кол-во монеток необходимое для переворота на другую сторону {count1}")
except ValueError:
    print("Вы ввели не целое число!")