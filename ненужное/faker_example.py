from faker import Faker


fake1 = Faker('ru_Ru')

data = {
    'first_name': fake1.first_name(),
    'last_name': fake1.last_name(),
    'email': fake1.email(),
    'address': fake1.address(),
    'age': fake1.random_int(min=18, max=90)
}
print(data)