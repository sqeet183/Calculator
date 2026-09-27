print ("--- Moй супер-калькулятор на pyton")
num1 = float(input("введи первое число:"))
operation = input ("выбери действие  (+, -,*, /,): ")
num2 =float(input("Введи второе число:"))
if operation == "+":
        result = num1 + num2
        print("РЕЗУЛЬТАТ:" +str (result))
if operation == "-":
  result = num1 - num2
  print("РЕЗУЛЬТАТ: " +str (result))
if operation == "*":
    result=num1 * num2
    print("РЕЗУЛЬТАТ:" +str(result))
if operation =="/":
    if num2 ==0:  print("ОШИБКА!на ноль делить нельзя!")
else:
    result =num1 /num2
    print("РЕЗУЛЬТАТ: "+str(result))