
def isPalindrome(str):
    rev = ''.join(reversed(str))
    if (str == rev):
        return print("Полиндром.")
    return print("Не полиндром")

def creditka(card):
    return '*' * len(card[:-4]) + card[-4:]

class Tomato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленый', 3: 'Зрелый'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
            self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Томат {} сейчас {}'.format(self.index, Tomato.states[self.state]))

class TomatoBush:

    def __init__(self, count):
        self.tomates = [Tomato(index) for index in range (1, count + 1)]

    def are_all_ripe(self):
        if not all([i_tomato.is_ripe() for i_tomato in self.tomates]):
            print('Томаты еще не созрели! \n')
        else:
            print('Все томаты созрели! Можно собирать. \n')

    def grow_all(self):
        print('Томаты растут!')
        for i_tomates in self.tomates:
            i_tomates.grow()

class Gardener:
    def __init__(self, name, collected_tomates):
        self.name, self.collected_tomates = name, collected_tomates

    def gardener_info(self):
        print('Имя садовника: {}\nСколько собрал томатов: {}\n'.format(self.name, self.collected_tomates))

    def tend(worker, my_garden):
        if all([i_tomates.is_ripe() for i_tomates in my_garden.tomates]):
            question = int(input('Собрать томаты? \n1 - да, 2 - нет\n'))
            if question == 1:
                tomato_count = 0
                for i_potato in my_garden.tomates:
                    worker.collected_tomates += 1
                    tomato_count += 1
                    i_potato.state = 0

                print('{} собрал {} томатов!'.format(worker.name, tomato_count))
                worker.gardener_info()
        else:
            question = int(input('Отправить {}а ухаживать за томатами? \n 1 - да, 2 - нет\n'.format(worker.name)))
            if question == 1:
                my_garden.grow_all()
                my_garden.are_all_ripe()

    @staticmethod
    def knowledge_base():
        print('''Класс Tomato:
статическое свойство states - все стадии созревания помидора
метод __init__()определены два динамических protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
значение из словаря states
метод grow() переводит томат на следующую стадию созревания
is_ripe()проверяtn, что томат созрел (достиг последней стадии созревания)
Класс TomatoBush
метод __init__()принимать в качестве параметра количество томатов и на его основе будет создавать список объектов класса
Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
метод grow_all(), который переводит все объекты из списка томатов на следующий этап созревания
метод all_are_ripe() возвращаtn True, если все томаты из
списка стали спелыми
метод give_away_all() будет чистить список томатов после сбора урожая
Класс Gardener
метод __init__(), внутри которого определены два динамических
свойства: 1) name - передается параметром, является публичным и 2) _plant -
принимает объект класса Tomato, является protected
work(), который заставляет садовника работать, что позволяет
растению становиться более зрелым
harvest(), который проверяет, все ли плоды созрели. Если все -
садовник собирает урожай. Если нет - метод печатает предупреждение.
статический метод knowledge_base(), который выведет в консоль справку
по садоводству.''')

def main(index=None):
    while True:
        vvod = int(input("1.Задание №1. \n2.Задание №2. \n3.Задание №3.\n4.Выход.\n"))
        if vvod == 1:
            card = input("Введите номер кредитной карты: ")
            print(creditka(card))
        elif vvod == 2:
            str = input("Введите слово: ")
            isPalindrome(str)
        elif vvod == 3:
            while True:
                vvod = int(input("1.Посадить томаты и выращивать. \n2.Справка.\n3.Выход.\n"))
                if vvod == 1:
                    index = int(input("Введите количество томатов: "))
                    my_garden = TomatoBush(index)
                    worker = Gardener('Иван', 0)

                    while True:
                        Gardener.tend(worker, my_garden)

                elif vvod == 2:
                    Gardener.knowledge_base()

                elif vvod == 3:
                    break
        elif vvod == 4:
            print("Выход.")
            break
        else:
            print("Нет такого номера задания."
                  "Введите номер из списка.")

main()