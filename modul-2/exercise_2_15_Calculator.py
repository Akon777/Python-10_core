"""
Напишіть програму, яка буде виконувати найпростіші математичні операції з числами послідовно, 
приймаючи від користувача операнди (числа) та оператори (детальні умови задачі під кодом).
"""

result = None
operand = None
operator = None
wait_for_number = True
end = False

print("""Welcome to simple calculator program!
Enter + for addition
Enter - for substraction
Enter * for multiplication
Enter / for division
Enter = to Quit the program
""")
while not end:
    while wait_for_number:
        try:
            user_input = input("Enter the number: ")
            operand=float(user_input)
            wait_for_number = False
        except ValueError:
            print(f"Ви ввели не число!")
    if result == None:
        result=operand
    elif operator == "+":
        result+=operand
    elif operator == "-":
        result-=operand
    elif operator == "*":
        result*=operand
    elif operator == "/":
        try:
            result/=operand
        except ZeroDivisionError:
            print(f"Ви ділите на нуль!")
    while not wait_for_number:
        user_input = input("Enter the operator: ")
        if user_input == "+" or user_input == "-" or user_input =="*" or user_input =="/":
            operator = user_input
            wait_for_number = True
            continue
        elif user_input == "=":
                print("The result is: ", result)
                end=True
                print("Thank you for using calculator program")
                input()
                break
        else: print(f"Ви ввели не оператор!")
  
  """
Умови для цієї задачі:
    Додаток працює з цілими та дійсними числами.
    Додаток вміє виконувати такі математичні операції:
        ДОДАВАННЯ (+)
        ВІДНІМАННЯ(-)
        МНОЖЕННЯ (*)
        ДІЛЕННЯ (/)
    Програма приймає один операнд або один оператор за один цикл запит-відповідь.
    Всі операції програма виконує в порядку надходження — одну за одною.
    Програма виводить результат обчислень, коли отримує від користувача символ =.
    Додаток закінчує роботу після того, як виведе результат обчислення.
    Користувач по черзі вводить числа та оператори.
    Якщо користувач вводить оператор двічі поспіль, він отримує повідомлення про помилку і може ввести повторно.
    Якщо користувач вводить число двічі поспіль, він отримує повідомлення про помилку і може ввести повторно.
    Додаток коректно опрацьовує ситуацію некоректного введення (exception).
Початкові змінні:
result = None
operand = None
operator = None
wait_for_number = True
result — сюди поміщаємо підсумковий результат operand — завжди зберігає поточне число operator — рядковий параметр, може містити чотири значення, "+", "-", "*", "/" wait_for_number — прапорець, який вказує, що очікують на вводі оператор (operator) або операнд (operand)
"""
