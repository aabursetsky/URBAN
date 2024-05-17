product = input("Наименование товара: ")
weight = float(input("Вес товара (кг): "))           # Килограммы + граммы
price = float(input("Цена (руб/кг) : "))             # Рубли + копейки
print("К оплате :", int(round(weight * price, 0)))   # Округление до рублей, копейки только на карте
payment = int(input("Оплата (руб.) : "))             # Наличка
Change = payment - weight * price
print("Сдача: ", int(round(Change, 0)))

# cheque # Чек
print("========================")
print(product)
print("Вес товара (кг)    : ", weight)
print("Цена   (руб/кг)    : ", price)
print("Итоговая стоимость : ", int(round(weight * price, 0)))
print("Внесено            : ", int(payment))
print("Сдача              : ", int(round(Change, 0)))
