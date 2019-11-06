z = input('тип фигруы')
if z == "прямоугольник":
    a = int(input())
    b = int(input())
    print(a * b)
elif z == 'круг':
    r = int(input())
    print(3.14 * r * r)
elif z == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    print(s)