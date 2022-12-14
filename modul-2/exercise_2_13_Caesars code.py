# Напишіть програму, що реалізує код Цезаря. Він названий на честь великого римського імператора Юлія Цезаря.
# Ідея шифрування полягає у циклічному зміщенні букв на задану кількість. Наприклад, якщо зміщення на три позиції, 
# то літера A стає літерою D, B – E тощо. Останні три літери алфавіту зациклюються та переносяться на початок. 
# Літера X стає A, Y – B, а Z – C. Цифри, пробіли та інші символи не шифруються.
# У програмі користувач вводить фразу та число для зсуву, після чого треба вирахувати нове закодоване повідомлення.

# Програма шифруватиме як малі (a-z), так і великі літери (A-Z).
# Для розв'язку цього завдання знадобиться знання двох нових функцій. 
# Перша функція ord. Вона перетворює символ на число, яке є позицією в таблиці ASCII.

# ord("a")  # 97
# Можна вважати, що отриманий результат '97' — це числове представлення символу "a" для комп'ютера.
# Зворотна функція chr повертає рядковий символ у таблиці ASCII за позицією, переданою як аргумент.
# chr(118)  # 'v'


message = input("Enter your message: ")
offset = int(input("Enter encryption step: "))
encoded_message = ""

for ch in message:
    if ch in "abcdefghijklmnopqrstuvwxyz":
        pos = ord(ch) - ord("a")
        pos = (pos + offset) % 26
        new_char = chr(pos + ord("a"))
        encoded_message+= new_char
    elif ch in "ABCDEFGHIJKLMNOPQRSTUWXYZ":
        pos = ord(ch) - ord("A")
        pos = (pos + offset) % 26
        new_char = chr(pos + ord("A"))
        encoded_message+= new_char
    else:
        encoded_message+=ch
print(encoded_message)
