class Student:

    def __init__(self, name='Noname', gradeBook='gradeBook', course='course'):
        self.name = name
        self.course = course
        self.gradeBook = gradeBook
        self.mind = 100
        self.money = 100
        self.happiness = 100
        self.satiety = 100
        #print('Йа поступило!')

    def study(self):
        self.satiety -= 10
        self.money -= 10
        self.happiness -= 10
        if self.satiety <= 0:
            self.drink()
        if self.money <= 0:
            print('Бедный не тот, у кого нет денег. Бедный тот, у кого скоро сессия')
        return [self.satiety, self.money, self.happiness]

    def get_credit(self):
        if self.mind < 40:
            print('Ты лошара, иди на пересдачу')
        else:
            self.happiness -= 25
            self.money += 500        #стипендия
        return [self.mind, self.happiness, self.money]

    def read_a_book(self):
        self.happiness -= 8
        self.mind += 3
        if self.happiness <= 0:
            print('Да пошло оно все. Миру - мир, Студенту - Beer !!!')
            self.drink()
        return [self.happiness, self.mind]

    def drink(self):
        if self.money <= 0:
            print('БОМЖАРА')
        else:
            self.money -= 500
            self.happiness += 35
            self.mind -= 15
            if self.mind <= 0:
                print('ПОРА НАЧАТЬ УЧИТЬСЯ')
        return [self.money, self.happiness, self.mind]