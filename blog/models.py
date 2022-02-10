from django.db.models import Model, CASCADE, CharField, TextField, DateTimeField, ForeignKey
from django.utils import timezone
from django.contrib.auth.models import User


class Post(Model):
    author = ForeignKey(User, on_delete=CASCADE)
    title = CharField(max_length=128)
    content = TextField()
    created = DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
