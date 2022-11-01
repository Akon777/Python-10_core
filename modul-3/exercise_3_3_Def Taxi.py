# Необхідно написати функцію, яка буде обчислювати суму за користування послугами таксі.
# Сума складається з базового тарифу 40 грн, та 10 грн за кожен кілометр поїздки.
# Напишіть функцію, яка приймає один параметр — відстань поїздки в кілометрах.
# Функція має повертати підсумкову суму оплати за послуги таксі дійсним числом.
# Також функція повинна змінювати глобальну змінну — лічильник total_trip після кожного виклику та збільшувати її на одиницю.

base_rate = 40
price_per_km = 10
total_trip = 0


def trip_price(path):
    
    global total_trip
    
    total_trip += 1
    trip_price = base_rate + price_per_km * path
    print (f"{trip_price} грн - суму оплати за послуги таксі")
    
    return


trip_price(float(input("Please, enter some distance in km "))) # для перевірки коду
trip_price(float(input("Please, enter some distance in km "))) # для перевірки коду

print(f"{total_trip} - кількість викликів таксі")
