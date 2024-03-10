import arrow
import factory
import uuid

from db import Session
from models.user import UserDB


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = UserDB
        sqlalchemy_session = Session

    id = factory.LazyFunction(lambda: uuid.uuid4())
    username = factory.Faker("username")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    created_at = arrow.utcnow()
    updated_at = arrow.utcnow()

    @factory.LazyAttribute
    def email(self):
        return f"{self.first_name}-{self.last_name}@lolz.net"