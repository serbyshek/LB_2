a = int(input("Введите единицу первого числа"))
d = int(input("Введите десяток первого числа"))
b = int(input("Введите второе число"))
e = (a +b)%10
c = (d+(a+b))//10
print("Результат {0}{1}". format(c, e))