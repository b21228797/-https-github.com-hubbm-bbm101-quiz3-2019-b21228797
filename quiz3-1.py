a = int(input("Enter a value"))
b = int(input("Enter second value"))

number = pow(a, b)
sum= 0
while float(number) / 10 >= .1:

    m = number % 10
    sum += m
    number = number // 10

    if float(number) / 10 > .1:
       print(m, end=" + ")
    else:
       print(m, "=", sum)