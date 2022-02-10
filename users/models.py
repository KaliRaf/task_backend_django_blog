from django.db.models import Model, CharField, OneToOneField, CASCADE
from django.contrib.auth.models import User


class Account(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    phone = CharField(max_length=16)

    def __str__(self):
        return f'Account of {self.user.username}'
