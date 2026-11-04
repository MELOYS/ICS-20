
class CAR:
    def __init__(self, Number, Model, Producer, Year, Owner):
        self.Number = Number
        self.Model = Model
        self.Producer = Producer
        self.Year = Year
        self.Owner = Owner

    def ChangeNumber(self, number):
        self.Number = number

    def ChangeOwner(self, owner):
        self.Owner = owner

    def DisplayProp(self):
        print(self.Number, self.Model, self.Producer,
              self.Year, self.Owner)

    def GetYear(self):
        return self.Year

    def GetOwner(self):
        return self.Owner
