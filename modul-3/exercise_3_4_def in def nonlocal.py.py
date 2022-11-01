# Необхідно реалізувати функцію розрахунку ціни товару зі знижкою discount_price.
# Функція приймає ціну price та знижку discount — це дрібне число від 0 до 1.
# Під знижкою розумітимемо коефіцієнт, який визначає розмір від ціни. І на цей розмір ми знижуємо підсумкову вартість товару.
# Логіку функції необхідно прописати у внутрішній функції apply_discount, використовуючи оголошення зміною price як nonlocal.


def discount_price(price, discount):
    
    
    def apply_discount():
        nonlocal price

        price = price*(1-discount)
        

    apply_discount()
    
    return price

print(discount_price(int(input("Please, enter some price: ")),float(input("Plese, enter some discount '0 < discount < 1'")))) # function check
