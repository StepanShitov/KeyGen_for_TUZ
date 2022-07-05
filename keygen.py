
def ask_for_a_password():
    pass

def get_password_len():
    password_len = 0
    while password_len >= 0:
        password_len = int(input("Введите длину необходимого пароля: "))
    return password_len


def main():
    password_len = get_password_len()
    print(password_len)
#     previous_password = input("Для генерации нового пароля будет использована \
# часть старого, введите старый пароль: ")

if __name__ == "__main__":
    main()