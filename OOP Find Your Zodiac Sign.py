print("მოგესალმებით!\n ამ პროგრამის გამოყენებით შეგიძლიათ, გაიგოთ თქვენი ზოდიაქოს ნიშანი.\n\n")

user_name = input("შეიყვანეთ თქვენი სახელი: ")
user_birthday = input("შეიყვანეთ დაბადების თარიღი (დღე/თვე/წელი): ").split("/")[0:2]

class Zodiac:

    def __init__(self, user_name, user_birthday):
        self.user_name = user_name
        self.user_birthday = user_birthday

    def zodiac_sign(self):
        birthdate = self.user_birthday
        datee = int(birthdate[1])+int(birthdate[0])/100
        if datee <= 1.20:
            datee += 12
        signs = {
            "ვერძი" : (3.21,4.20),
            "კურო" : (4.21,5.21),
            "ტყუპები" : (5.22,6.21),
            "კირჩხიბი" : (6.22,7.23),
            "ლომი" : (7.24,8.23),
            "ქალწული" : (8.24,9.23),
            "სასწორი" : (9.24,10.23),
            "მორიელი" : (10.24,11.22),
            "მშვილდოსანი" : (11.23,12.21),
            "თხის რქა" : (12.22,13.20),
            "მერწყული" : (1.21,2.19),
            "თევზები" : (2.20,3.20),
        }

        for sign in signs:
            if signs[sign][0]<=datee and signs[sign][1]>=datee:
                print(f'{self.user_name} თქვენი ზოდიაქოს ნიშანია {sign}')


de_zodiac = Zodiac(user_name, user_birthday)
de_zodiac.zodiac_sign()
