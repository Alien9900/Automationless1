from address import Address
from mailing import Mailing

# Создание экземпляров класса Address для адресов отправителя и получателя
from_address = Address("123456", "Москва", "Тверская", "10", "50")
to_address = Address("654321", "Санкт-Петербург", "Невский", "20", "25")

# Создание экземпляра класса Mailing
mailing = Mailing(to_address, from_address, 300, "RU123456789")

# Вывод информации о почтовом отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
