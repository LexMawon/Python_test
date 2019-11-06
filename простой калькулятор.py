a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = input('Введите операцию: +, -, /, *, mod, pow, div')
if c == "+":
    print(float(a) + float(b))
elif c == "-":
    print(float(a) - float(b))
elif c == "/":
    if float(b) != 0.0:
        print(float(a) / float(b))
    else:
        print("Деление на 0!")
elif c == "*":
    print(float(a) * float(b))
elif c == "mod":
    if float(b) != 0.0:
        print(float(a) % float(b))
    else:
        print("Деление на 0!")
elif c == "pow":
    print(float(a) ** float(b))
elif c == "div":
    if float(b) != 0:
        print(int(a) // int(b))
    else:
        print("Деление на 0")
    
    