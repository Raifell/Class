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
ch = input('1) - All info\n2) - Name\n3) - Surname\n4) - Birth date\n5) - Phone number\n6) - City\n7) - County\n'
           '8) - Address\nChoice: ')

a.get_info(int(ch))

class City:
    def __init__(self):
        self.name = 'Argon'
        self.region = 'Valarant'
        self.country = 'Silvermilen'
        self.count_people = 5000
        self.index = 159753
        self.phone_code = 321


    def get_info(self, choice):
        self.choice = choice

        if self.choice == 1:
            print(self.name, self.region, self.country, self.count_people, self.index, self.phone_code)
        elif self.choice == 2:
            print(self.name)
        elif self.choice == 3:
            print(self.region)
        elif self.choice == 4:
            print(self.country)
        elif self.choice == 5:
            print(self.count_people)
        elif self.choice == 6:
            print(self.index)
        elif self.choice == 7:
            print(self.phone_code)


b = City()
ch = input('1) - All info\n2) - Name\n3) - Region\n4) - Country\n5) - Count people\n6) - Index\n7) - Phone code\n'
           'Choice: ')

b.get_info(int(ch))


class City:
    def __init__(self):
        self.name = 'Dion'
        self.region = 'Morgal'
        self.country = 'Silvermilen'
        self.count_people = 7000
        self.index = 159753
        self.phone_code = 322


    def get_info(self, choice):
        self.choice = choice

        if self.choice == 1:
            print(self.name, self.region, self.country, self.count_people, self.index, self.phone_code)
        elif self.choice == 2:
            print(self.name)
        elif self.choice == 3:
            print(self.region)
        elif self.choice == 4:
            print(self.country)
        elif self.choice == 5:
            print(self.count_people)
        elif self.choice == 6:
            print(self.index)
        elif self.choice == 7:
            print(self.phone_code)


c = City()
ch = input('1) - All info\n2) - Name\n3) - Region\n4) - Country\n5) - Count people\n6) - Index\n7) - Phone code\n'
           'Choice: ')

c.get_info(int(ch))
