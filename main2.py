import os
# видалити контакт, знайти за імям

FILENAME = "contacts.txt"


# Завантажує контакти з файлу
def load_contacts():
    if not os.path.exists(FILENAME):
        return []
    else:
        contacts = []
        with open(FILENAME, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                if ":" not in line:
                    continue
                name, phone = line.split(":", 1)
                contact = (name.strip(), phone.strip())
                contacts.append(contact)
        return contacts


# Додає новий контакт до файлу
def save_contacts(contacts):
    with open(FILENAME, 'w', encoding="utf-8") as file:
        for name, phone in contacts:
            file.write(f"{name}: {phone}\n")


def add_contact(contacts):
    name = input("Ім'я: ").strip()
    if not name:
        print("Ім'я не може бути порожнім")
        return
    phone = input("Номер телефону: ").strip()
    if not phone:
        print("Телефон не може бути порожнім")
        return
    contacts.append((name, phone))
    save_contacts(contacts)
    print("Контакт додано")


# Показати всі контакти
def show_all(contacts):
    if not contacts:
        print("\nСписок порожній")
        return

    print("\nВсі контакти:")
    for i, (name, phone) in enumerate(contacts, 1):
        print(f"{i:2}. {name:10} - {phone}")
    print()


# Видалити контакт
def delete_contact(contacts):
    query = input("\nІм'я контакту для видалення: ").strip().lower()
    if not query:
        print('Нічого не введено')
        return
    to_delete = []
    for name, phone in contacts:
        if query in name.lower():
            to_delete.append((name, phone))

    if not to_delete:
        print("Таких контактів не знайдено")
        return

    if len(to_delete) == 1:
        name, phone = to_delete[0]
        print(f"Знайдено: {name} {phone}")
        if input('Видалити? (так/ні): ').strip().lower() == 'так':
            contacts.remove((name, phone))
            save_contacts(contacts)
            print("Видалено")
        else:
            print("Скасовано")
    else:
        print("\nЗнайдено декілька контактів:")
        for i, (name, phone) in enumerate(to_delete, 1):
            print(f"{i:2}. {name:10} - {phone}")
        try:
            num = int(input("Введіть номер для видалення:"))
            if num == 0:
                print("Скасовано")
                return
            if 1 <= num <= len(to_delete):
                name, phone = to_delete[num - 1]
                contacts.remove((name, phone))
                save_contacts(contacts)
                print("Видалено")
        except:
            print("Потрібно ввести число")


def show_menu():
    print("\n" + "-" * 35)
    print("    КОНТАКТИ")
    print("-" * 35)
    print("1 - Додати контакт")
    print("2 - Показати всі")
    print("3 - Знайти за ім'ям")
    print("4 - Видалити контакт")
    print("0 - Вихід")
    print("-" * 35)


def actions():
    contacts = load_contacts()

    while True:
        show_menu()
        choise = input().strip()

        if choise == "1":
            add_contact(contacts)
        elif choise == "2":
            show_all(contacts)
        elif choise == "3":
            pass
        elif choise == "4":
            delete_contact(contacts)
        elif choise == "0":
            pass
        else:
            print("Такого варіанта не існує")


if __name__ == "__main__":
    actions()
