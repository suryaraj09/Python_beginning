class players:
    def __init__(self, Name, Surname, Team, pay):
        self.first_name = Name
        self.last_name = Surname
        self.team = Team
        self.pay = pay

    
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def pay_raise(self):
        return f"{self.pay * 1.5}"

player1  = players("Suryaraj", "Jadeja", "India", 50000)
player2 = players('Tony', 'stark', 'USA', 100000)

print(player1.fullname() + ' : ' +player1.team)
print(player2.fullname() + ' : ' +player2.team)

print(player1.pay_raise())
print(player2.pay_raise())