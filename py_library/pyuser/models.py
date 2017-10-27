from django.db import models
from django.contrib.auth.models import User


VISITOR = 0
EMPLOYEE = 1
ADMIN = 2

USER_TYPE_CHOICES = (
    (VISITOR, 'user just can browser the info'),
    (EMPLOYEE, 'user can borrow and return book'),
    (ADMIN, 'py library administrator'),
)


class PyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unionId = models.CharField(unique=True, max_length=100)
    nickName = models.CharField(max_length=100)
    avatarUrl = models.CharField(max_length=256)
    type = models.IntegerField(default=VISITOR, choices=USER_TYPE_CHOICES,
                               blank=True)

    def __str__(self):
        return self.user.get_full_name() + " " + self.nickName
