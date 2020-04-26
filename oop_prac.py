class PlayerChar:
    def__init__(self, name, income):
       self.name = name
       self.income = income
    
    def wage(self):
        return self.income

    def speak(self, lang):
        print(f"{self.name} speaks {lang}")


class Members(PlayerChar):
    def __init__(self,name, arrow):
        self.arrow = arrow


    def attack(self):
        print(f"attacking with {self.arrow}")

    def study(self, hours):
        print(self)


player1 = PlayerChar('Tommas', 75)

print(player1)