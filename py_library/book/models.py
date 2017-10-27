from django.db import models
from django.contrib.auth.models import User
from py_library.pyuser.models import PyUser


IN_MARKET = 0
IN_WISH_LIST = 1
IN_LIBRARY = 2
HAS_BORROWED = 3

BOOK_STATUS_CHOICES = (
    (IN_MARKET, "book in the market"),
    (IN_WISH_LIST, "someone wish this book, but not bought now"),
    (IN_LIBRARY, "book in the py library"),
    (HAS_BORROWED, "book bas been borrowed by someone"),

)


def get_sentinel_user():
    return User.objects.get(username='u_lib_admin')


class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    douban_id = models.IntegerField(verbose_name="book id in douban",
                                    default=1, unique=True)
    status = models.IntegerField(default=IN_MARKET, choices=BOOK_STATUS_CHOICES)
    owner = models.ForeignKey(PyUser, blank=True, null=True,
                              on_delete=models.SET(get_sentinel_user),
                              related_name='PyBook')
    wishers = models.ManyToManyField(PyUser, related_name='bookWishers',
                                     blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return str(self.douban_id)


