class Man:
    def __init__(self):
        self.name = 'Aden'
        self.surname = 'Pride'
        self.birth = '2001.12.10'
        self.phone = '+1999999999'
        self.town = 'NY'
        self.country = 'USA'
        self.address = 'NY, queens 23 A'

    def get_info(self, choice):
        self.choice = choice

        if self.choice == 1:
            print(self.name, self.surname, self.birth, self.birth, self.phone, self.town, self.country, self.address)
        elif self.choice == 2:
            print(self.name)
        elif self.choice == 3:
            print(self.surname)
        elif self.choice == 4:
            print(self.birth)
        elif self.choice == 5:
            print(self.phone)
        elif self.choice == 6:
            print(self.town)
        elif self.choice == 7:
            print(self.country)
        elif self.choice == 8:
            print(self.address)


a = Man()
print('Start')
ch = input('1) - All info\n2) - Name\n3) - Surname\n4) - Birth date\n5) - Phone number\n6) - City\n7) - County\n'
           '8) - Address\nChoice: ')

a.get_info(int(ch))
print('Over')
