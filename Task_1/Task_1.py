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


a = City()
ch = input('1) - All info\n2) - Name\n3) - Region\n4) - Country\n5) - Count people\n6) - Index\n7) - Phone code\n'
           'Choice: ')

a.get_info(int(ch))
