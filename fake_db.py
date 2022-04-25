from models import Person, PersonType

t1 = Person(name="Nikita", age=21, type=PersonType.STUDENT)
t2 = Person(name="Katya", age=20, type=PersonType.TEACHER)
data = {
    0: t1,
    1: t2
}