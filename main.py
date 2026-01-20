from abc import ABC, abstractmethod

# print("=" * 50)
# print(" " * 15 + "1 - TOPSHIRIQ")
# print("=" * 50)

#
# class Product(ABC):
#     def __init__(self, name, price, in_stock):
#         self.__name = name
#         self.__price = price
#         self.categories = []
#         self.in_stock = in_stock
#
#     @abstractmethod
#     def get_info(self):
#         pass
#
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, value):
#         self.__name = value
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self, value):
#         self.__price = value
#
#     @price.deleter
#     def price(self):
#         del self.__price
#
# class ElectronicProduct(Product):
#     def __init__(self, name, price, in_stock, warranty_years):
#         super().__init__(name, price, in_stock)
#         self.__warranty_years = warranty_years
#
#     @property
#     def warranty_years(self):
#         return self.__warranty_years
#     @warranty_years.setter
#     def warranty_years(self, value):
#         self.__warranty_years = value
#     @warranty_years.deleter
#     def warranty_years(self):
#         del self.__warranty_years
#
#     def get_info(self):
#         return f"Name: {self.name} | price: {self.price} | warranty years: {self.__warranty_years}"
#
# p1 = ElectronicProduct("iPhone", 1000, True,2)
# p2 = ElectronicProduct("laptop", 1500, False,3)
#
# print(p1.get_info())
# p1.name = "car"
# print(p1.get_info())
# print(p2.get_info())
# p2.price = 0000
# print(p2.get_info())
# p1.categories.append("iPhone")
# p1.categories.append("laptop")
# print(p1.categories)

print("=" * 50)
print(" " * 15 + "2 - TOPSHIRIQ")
print("=" * 50)

class Team(ABC):
    def __init__(self, team_name, coach, country):
        self.__team_name = team_name
        self.__coach = coach
        self.players = []
        self.country = country

    @property
    def team_name(self):
        return self.__team_name
    @team_name.setter
    def team_name(self, value):
        self.__team_name = value
    @team_name.deleter
    def team_name(self):
        del self.__team_name

    @property
    def coach(self):
        return self.__coach

    @coach.setter
    def coach(self, value):
        self.__coach = value

    @coach.deleter
    def coach(self):
        del self.__coach

    @abstractmethod
    def get_info(self):
        pass

class FootballTeam(Team):
    def __init__(self, team_name, coach, country, stadium):
        super().__init__(team_name, coach, country)
        self.__stadium = stadium

    @property
    def stadium(self):
        return self.__stadium
    @stadium.setter
    def stadium(self, value):
        self.__stadium=value
    @stadium.deleter
    def stadium(self):
        del self.__stadium

    def get_info(self):
        return f"Name: {self.team_name} | coach: {self.coach} | country: {self.country} | stadium: {self.stadium}"

    @staticmethod
    def is_full_team(players):
        return len(players) >= 11

team1 = FootballTeam("Uzbeksitan", "Izzatillo","O'zbekiston", "Bunyodkor")
team2 = FootballTeam("RealMadrid", "H.Alonso", "Ispaniya", "santiyago_bernadeyo")

team1.players.extend([
    "Eldor Shomurodov",
    "Jaloliddin Masharipov",
    "Otabek Shukurov",
    "Odiljon Hamrobekov",
    "Rustam Ashurmatov",
    "Abbosbek Fayzullaev",
    "Dostonbek Tursunov",
    "Islom Tuxtaxujaev",
    "Akmal Mozgovoy",
    "Sherzod Nasrullaev",
    "Utkir Yusupov"
]
)

team2.players.extend([
    "Thibaut Courtois",
    "Dani Carvajal",
    "Antonio Rudiger",
    "David Alaba",
    "Ferland Mendy",
    "Luka Modric",
    "Toni Kroos",
    "Federico Valverde",
    "Jude Bellingham",
    "Vinicius Junior",


]
)

print(FootballTeam.is_full_team(team2.players))
print(FootballTeam.is_full_team(team1.players))

team2.coach="Shukurulloh"
print(team2.get_info())

del team2.stadium
print(hasattr(team2, "stadium"))
