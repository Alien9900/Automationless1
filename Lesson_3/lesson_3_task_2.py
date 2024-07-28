from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Xiaomi", "14 Ultra", "+79456789012"))
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79234567890"))
catalog.append(Smartphone("Google", "Pixel 5", "+79345678901"))
catalog.append(Smartphone("Apple", "iPhone 15", "+79123456789"))
catalog.append(Smartphone("OnePlus", "8 Pro", "+79567890123"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
