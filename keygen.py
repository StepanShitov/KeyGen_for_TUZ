import random
import csv

def get_password_len():
    password_len = -1
    while password_len <= 0:
        password_len = int(input("""\nВведите длину необходимого пароля ( рекомендованная длина для ТУЗ - от 16 символов ): """))
    return password_len

def get_password_domen(password_len):
    print(f"Для генерации пароля длиной:{password_len}  будут использованы " \
        "ключевые слова из файла words.csv и алфавит символов из alph.scv")
    domen = 0
    while domen < 1 or domen > 2:
        domen = input("\nДля какого домена будет использоваться пароль?" \
            "\n1. Alpha (пароль будет иметь префикс A#" \
            "\n2. Sigma ( пароль будет иметь префикс S#" \
            "\nВведите ответ: ")
        if domen.isdecimal() and 1 <= int(domen) <= 2:
                return round(int(domen))
        print("Укажите правильный домен!")
        domen = 0

def upload_words():
    words = []
    with open("words.csv", 'r') as words_file:
        words_reader = csv.reader(words_file)
        for word in words_reader:
            words.append(word[0])
    return words

def upload_alphabet():
    alphabet = []
    with open("alph.csv", 'r') as alph_file:
        alph_reader = csv.reader(alph_file)
        for symbols_collection in alph_reader:
            alphabet.append(symbols_collection[0])
    return alphabet

def generate_symbols(alphabet):
    collection = random.choice(alphabet)
    return random.choice(collection)

def check_for_requirements(alphabet, password):
    for collection in alphabet:
        collection_in_password = False
        for symbol in collection:
            if symbol in password: 
                    collection_in_password = True
                    break
        if not collection_in_password:
            password_check = False
            break
        else:
            password_check = True
    return password_check

def generate_password_base(password_len, words, alphabet):
    generated_password_len = 0
    words_to_include = random.choices(words, k=2)
    for word in words_to_include:
        generated_password_len += len(word)
            
    for _ in range(password_len - generated_password_len - 2):
        symbol = generate_symbols(alphabet)
        symbol_position = random.randint(1, 3)  # 1 - before 1st, 2 - between 1 and 2, 3 - after 2nd
        if symbol_position == 1: words_to_include[0] = symbol + words_to_include[0]
        elif symbol_position == 2: words_to_include[0] += symbol
        else: words_to_include[1] += symbol

    return words_to_include

def generate_password(password_len, domen):
    words = upload_words()
    alphabet = upload_alphabet()
    generated_passwords = []
    for _ in range(5):        
        password_check = False
        while not password_check:
            password = ""
            if domen == 1: password += "A#"
            elif domen == 2: password += "S#"

            password_base = generate_password_base(password_len, words, alphabet)
            password += ''.join(password_base)

            password_check = check_for_requirements(alphabet, password[2:])
        generated_passwords.append(password)
    return generated_passwords    
        
def choose_password(passwords):
    print("\nПредлагаем вам сгенерированные пароли, выберите один из них:")
    for i, password in enumerate(passwords):
        print(f"{i + 1}. {password}")
    user_choice = -1
    while user_choice < 0:
        user_choice = input("\nВведите номер понравившегося варианта: ")
        if user_choice.isdecimal() and 1 <= int(user_choice) <= len(passwords):
            print(f"\nВы выбрали {int(user_choice)}! Ваш пароль: {passwords[int(user_choice) - 1]}")
            return passwords[int(user_choice) - 1]
        else:
            print("Введите правильный номер!")
            user_choice = -1

def load_to_file(password):
    print("Сгененрированный пароль будет загружен в файл: password.txt")
    with open("password.txt", 'w') as load_file:
        load_file.write(password)

# S# is for sigma password, A# is for alpha
def main():
    password_len = 16 #get_password_len()
    domen = get_password_domen(password_len)
    list_to_choose = generate_password(password_len, domen)
    chosen_password = choose_password(list_to_choose)
    load_to_file(chosen_password)
    
if __name__ == "__main__":
    main()