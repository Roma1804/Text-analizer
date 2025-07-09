import string

def path_file():
    print("\n" + "*" * 62 + "\n")
    while True:
        path = r"{}".format(input("[*] Введіть шлях до файлу: "))#r відключає екранування
        if len(path) >= 1:
            return path
        else:
            print("[!] Шлях до файлу повинен мати не менше 1 символy!")

def word_count (text):
    words = text.split()
    clean_words = [word.strip(string.punctuation) for word in words]
    clean_words = [word for word in clean_words if word]
    return len(clean_words)



def text_analyzer(file, token):
    print("\n" + "*" * 62 + "\n")
    count_words = 0
    count_raws = 0
    count_symbols = 0
    if token == "file":
        text = [raw.decode("utf-8") for raw in file.readlines()]
        first_raw = text[0][:-1]
    elif token == "text":
        text = file.split("\n")
        first_raw = text[0]
    last_raw = text[-1]
    for raw in text:
        for word in raw.split():
            if word.isalnum():# перевіряє чи в строці є символи алфавіту та цифри
                count_words += 1
        count_raws += 1
        count_symbols += len(raw)
    return (count_raws, count_words, count_symbols, first_raw, last_raw)
def read_file():
    print("\n" + "*" * 62 + "\n")
    print("\t1) >>> Виберіть файл\n\t2) >>> Повернутися в головне меню\n")
    token = "file"
    return read_process(token)
def read_input():
    print("\n" + "*" * 62 + "\n")
    print("\t1) >>> Введіть текст\n\t2) >>> Повернутися в головне меню\n")
    token = "text"
    return read_process(token)

def input_text():
    print("\n" + "*" * 62 + "\n")
    print("[*] Введіть текст для аналізу(введіть ::q для виходу):\n")
    text = ""
    while True:
        text_input = input(">>> ")
        if text_input == "::q":
            break
        text += text_input + "\n"
    if text:
        return text[:-1]
    else:
        print("[!] Текст повинен мати хоча б 1 символ!")
        return read_input()

def print_result(result):
    print("\n" + "*" * 62 + "\n")
    print(f"[*] Кількість рядків: {result[0]}")
    print(f"[*] Кількість слів: {result[1]}")
    print(f"[*] Кількість символів: {result[2]}")
    print(f"[*] Перший рядок: {result[3]}")
    print(f"[*] Останній рядок: {result[4]}")

def read_process(token):
    while True:
        try:
            choice = int(input("[*] Зробіть Ваш вибір: "))
            if choice == 1:
                if token == "file":
                    path = path_file()
                    try:
                        with open(path, "rb") as file:
                            result = text_analyzer(file, token)
                    except:
                        print("[!] Файл не знайдений!")
                        return read_file()
                elif token == "text":
                    text = input_text()
                    result = text_analyzer(text, token)
                print_result(result)
                return main()
            elif choice == 2:
                return main()
            else:
                print("[!] Невірний ввід, спробуйте ввести число від 1 до 2")
        except:
            print("[!] Ви повинні вести ціле число")
def main():
    """
    Головна функція програми (головне меню)
    :return:
    """
    print("\n" + "*" * 20, "SIMPLE TEXT ANALYZER", "*" * 20 + "\n")
    print("\t1) >>> Читати текст із файлу\n\t2) >>> Ввести текст вручну\n\t3) >>> Вихід\n")
    while True:
        try:
            choice = int(input("[*} Зробіть Ваш вибір: "))
            if choice == 3:
                print("[*] Програма завершена!")
                break
            elif choice == 1:
                return read_file()
            elif choice == 2:
                return read_input()
            else:
                print("[!] Невірний ввід, спробуйте ввести число від 1 до 3")
        except (TypeError, ValueError):
            print("[!] Ви повинні вести ціле число")

main()