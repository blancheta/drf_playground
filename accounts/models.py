from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class CustomUser(AbstractUser):

    email = CharField(max_length=50, unique=True)
    username = CharField(max_length=50)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]