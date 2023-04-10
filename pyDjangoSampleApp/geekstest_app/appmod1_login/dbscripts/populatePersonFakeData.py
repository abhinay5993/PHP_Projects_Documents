from faker import Faker
import random
from appmod1_login.models import PersonModel

class populatePersonFakeData:
    def __init__(self):
        pass
    
    def run(self):
        fake = Faker()
        LIMIT = 10**3  # 1,000
        for i in range(LIMIT):
            person_obj = PersonModel.objects.create(
                fname=fake.first_name(),
                lstName=fake.last_name(),
                ageVal=random.randrange(1, 99),
                genderVal=random.choice(["M", "F", "O"]),
                emailVal=fake.email(),
            )
            print(person_obj)

obj = populatePersonFakeData()
obj.run()