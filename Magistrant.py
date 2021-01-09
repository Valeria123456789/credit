from Student import Student


class Magistrant(Student):

    def __init__(self, name='Noname', gradeBook='gradeBook', course='course'):
        super().__init__(name, gradeBook, course)
        self.health = 100

    def get_credit(self):
        if self.mind > 0:
            self.happiness += 20
            self.money += 1000      #стипендия
            self.health -= 30
        else:
            self.health += 30
            self.happiness -= 30
            print('И так сойдет, все равно не отчислят')
        return [self.mind, self.happiness, self.money, self.health]

    def study(self):
        self.money -= 100    #(не ходит на работу из-за пар)
        self.mind += 40
        if self.money <= 0:
            print('ПОРА ИДТИ РАБОТАТЬ')
        return [self.money, self.mind]
