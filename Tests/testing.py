# z = 10

# def afunction():
#     global z
#     z = 9

# print('Before afunction(): ', z)
# afunction()
# print('After afunction(): ', z)


# z = 10

# def func1():
#     global z
#     z = 3

# def func2(x,y):
#     global z
#     return x+y+z

# total = func2(4,5)
# print(total)

# func1()
# total = func2(4,5)
# print(total)


### ---- ####

class Actor:
    def __init__(self, name, surname, age, years_on_stage):
        self.name=name
        self.surname=surname
        self.age=age
        self.years_on_stage=years_on_stage

    def fullname(self):
        fullname = self.name + ' ' + self.surname
        return fullname.title()

    def year_of_debut(self, current_year):
        self.current_year=current_year
        year_of_debut=self.current_year-self.years_on_stage
        return year_of_debut

mario = Actor(
    'mario',
    'ballotelli',
    29,
    10
)

# print(mario.age)
# print(mario.fullname())

# print(mario.year_of_debut(2020))

class Comedian(Actor):
    def __init__(self, n_shows, field, shows_schedule, name, surname, age, years_on_stage):
        self.n_shows=n_shows
        self.field=field
        self.shows_schedule=shows_schedule
        super().__init__(name,surname,age,years_on_stage)

acomedian = Comedian(
    21, 'politics',
    'late nights', 'amelia', 'smith',
    33,
    10
)

# print(acomedian.fullname())
# print(acomedian.n_shows)

class Spotify_User:
    def __init__(self, name, email, premium):
        self.name = name
        self.email = email
        self.premium = premium

    def isPremium(self):
        if self.premium:
            print("{} is a Premium User.".format(self.name))
        else:
            print("{} is not a Premium User.".format(self.name))

user_1 = Spotify_User('Sarah Philipps', 'sphilips@gmail.com', True)
user_2 = Spotify_User('Todd', 'todd@gmail.com', False)
# print(user_1.name, user_1.premium)

user_1.isPremium()
user_2.isPremium()