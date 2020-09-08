class Human:

    def __init__(self, name = "No name"):
        self.name = name
        self.happiness = 0
        self.hungry = 0

    def say(self, word):
        print(self.name + " said: " + word)
    
    def eat(self, food):
        self.happiness += 5
        self.hungry += food

    def work(self, hours):
        self.happiness -= hours