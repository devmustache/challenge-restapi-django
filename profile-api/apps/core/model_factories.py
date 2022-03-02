from core.models import Profile, Gender
from faker.providers import person
from faker import Faker
import factory

fake = Faker(provider=person, locale='pt_BR')

class ProfileFactory(factory.Factory):

    class Meta:
        model = Profile
        
    first_name = fake.first_name_nonbinary(),
    last_name = fake.last_name_nonbinary(),
    age = fake.unique.random_int(min=0, max=120),
    sex = fake.random_choices(Gender.choices)