contacts = [
    {"name": "Анна", "phone": "+79991234567"},
    {"name": "Иван", "phone": "+79123450011"}
]

new_name = input("Введите имя:")
new_phone = input("Введите номер:")

contacts.append({"name": new_name, "phone": new_phone})

print()
print("Список контактов:")

num = 1
for c in contacts:
    full_num= c["phone"]
    start = full_num[:5]
    end = full_num[-4:]
    secret_p = start + "***" + end
    print(str(num) + ".", c["name"], "-", secret_p)
    num += 1

print()
find = input("Поиск по номеру: ")

found_num = 0
for c in contacts:
    if c["phone"] == find:
        p = c["phone"]
        secret_p = p[:5] + "***" + p[-4:]
        print("Найден:", c["name"], "-", secret_p)
        found_num += 1

if found_num == 0:
    print("Ничего не найдено :(")