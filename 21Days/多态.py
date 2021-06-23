class Person(object):
    def work_with_dog(self, dog):
        dog.work()


class Dog(object):
    def work(self):
        pass

class Army_dog(Dog):
    def work(self):
        print('军犬正在杀敌')

class Drug_dog(Dog):
    def work(self):
        print('警犬正在破案')

dog = Dog()
ad = Army_dog()
dd = Drug_dog()

p = Person()
p.work_with_dog(dog)
p.work_with_dog(ad)
p.work_with_dog(dd)
