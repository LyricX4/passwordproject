import time
from random import choice


class Card:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class App:
    def __init__(self):
        self.users = {}
        self.cards = []
        self.notes = []
        self.current_user = None

    def register(self):
        username = input("Имя пользователя: ")
        if username in self.users:
            print("Пользователь уже существует.")
            return

        password = input("Пароль (не менее 5 символов, латиница и цифры): ")
        if len(password) < 5 or not password.isalnum():
            print("Ошибка пароля.")
            return

        self.users[username] = password
        print("Регистрация успешна.")

    def login(self):
        username = input("Имя пользователя: ")
        password = input("Введите пароль: ")
        if self.users.get(username) == password:
            self.current_user = username
            print("Вход выполнен.")
            return True

        print("Ошибка входа.")
        return False

    def add_card(self):
        q = input("Вопрос: ")
        a = input("Ответ: ")
        self.cards.append(Card(q, a))

    def run_quiz(self):
        score = 0
        for card in self.cards:
            print(f"\nВопрос: {card.question}")
            start_time = time.time()
            ans = input("Ваш ответ: ")
            if time.time() - start_time > 30:
                print("Время вышло!")
            elif ans == card.answer:
                print("Верно!")
                score += 1
            else:
                print(f"Неверно. Ответ: {card.answer}")
            print(f"\nИтог: {score}/{len(self.cards)}")

    def manage_notes(self):
        while True:
            cmd = input("\n1-Добавить, 2-Показать, 3-Назад: ")
            if cmd == "1":
                self.notes.append(input("Текст заметки: "))
            elif cmd == "2":
                print(self.notes)
            else:
                break

    def main_menu(self):
        while True:
            if not self.current_user:
                print("\n=== ГЛАВНОЕ МЕНЮ ===")
                print("1. Регистрация")
                print("2. Вход")
                print("3. Выход из программы")
                choice_option = input("Выберите действие: ")
                if choice_option == "1":
                    self.register()
                elif choice_option == "2":
                    self.login()
                elif choice_option == "3":
                    break
            else:
                print(f"\n=== МЕНЮ (Пользователь: {self.current_user}) ===")
                print("1. Добавить карточку")
                print("2. Пройти викторину")
                print("3. Управление заметками")
                print("4. Выйти из аккаунта")
                choice_option = input("Выберите действие: ")
                if choice_option == "1":
                    self.add_card()
                elif choice_option == "2":
                    self.run_quiz()
                elif choice_option == "3":
                    self.manage_notes()
                elif choice_option == "4":
                    self.current_user = None


if __name__ == "__main__":
    app = App()
    app.main_menu()