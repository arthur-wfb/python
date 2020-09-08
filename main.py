from model.Human import Human
from model.Woman import Woman

human = Human("Vasya")
human.say("Hello")

woman = Woman("Katya")

child = Woman.sex(human, woman, "Petya")
child.say("My name is Petya")