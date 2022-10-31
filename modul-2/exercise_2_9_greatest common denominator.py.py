# Є кілька алгоритмів знаходження НСД, але ми розберемо циклічний алгоритм.

# 1, Хай є два початкових числа first та second.
# 2. Виберемо менше з них та привласнимо значення змінній gcd.
# 3. Поки first i second не діляться на gcd без залишку, треба виконувати цикл, в якому зменшуємо змінну gcd на одиницю.
# 4. Коли цикл закінчиться в змінній gcd буде НСД для чисел first та second.

# Напишіть програму, яка для двох додатних цілих чисел знаходить НСД.

first = int(input("Enter the first integer: "))

second = int(input("Enter the second integer: "))

gcd = first if first<second else second

while not (first%gcd == 0 and second%gcd == 0):

    gcd=gcd - 1

print(gcd)
