

class Person:
    avg_income = 15000
    nationality = "Indian"

    def __init__(self, name, age, sex, city):
        self.name = name
        self.age = age
        self.sex = sex
        self.city = city

 
    def person_bio(self):
        bio = f'{self.name} is {self.age} years old living in {self.city} and {self.name} is a {self.sex}'
        return bio

    
    @classmethod
   
    def change_avg_income(cls, income):
        new_avg_income = sum(income)/len(income)
        cls.avg_income = new_avg_income
        return cls.avg_income

   
    @staticmethod
    def driving_eligibility(driving_license):
        if driving_license == True:
            return "You are eligible for driving"
        return "You are not eligible for driving"


person1 = Person('daniel', 19, 'male', 'Chennai')
person2 = Person('surya', 20, 'Male', 'madurai')


Person.change_avg_income([12000, 10000, 15000, 17000])


person1.driving_eligibility(False)