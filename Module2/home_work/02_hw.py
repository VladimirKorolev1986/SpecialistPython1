n = int(input("Введите число коров: "))
if n<=10 or n>=20:
    if (n - 1) % 10 == 0:
        print("корова")
    elif (n - 2) % 10 == 0 or (n - 3) % 10 == 0 or (n - 4) % 10 == 0:
        print("коровы")
    else:
        print("коров")
else:
    print("коров")
