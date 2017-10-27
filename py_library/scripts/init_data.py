import traceback

from django.db import transaction
from django.contrib.auth.models import User
from django.utils.timezone import now

from pyuser.models import (PyUser, ADMIN, VISITOR, EMPLOYEE)
from book.models import (
    Book, IN_MARKET, IN_WISH_LIST, IN_LIBRARY, HAS_BORROWED
)


avatar_url_list = {
    'lib_admin': "http://wx.qlogo.cn/mmopen/PiajxSqBRaEKicoUcVQOQmGIwp8marUVgvumsBqJbCib32ibyIacib4njNZvXcnZlpqVbTibOe0u4UQqnRcicc88Ec7Jg/0",
    'ray': "http://wx.qlogo.cn/mmopen/Q3auHgzwzM6oKePxZmibYwTJZnqJB5xZ2Bxic32FNWfGmibgRb8gJnRy21PWsY3fJ4MicYuZ9AbtcIZOkdcwpQyoCA/0",
    'ldy': "http://wx.qlogo.cn/mmopen/GOVd7UZor3ps0PkhZNnl82iacoKYZQY1lh4O1gsVoCclLGt38DSERSONmRkA7DNZ9I3DSV6Jusd9jKYOJJMrj8SeEbLianS9vB/0",
   }


def run():
    try:
        with transaction.atomic():

            # 1. create django admin user
            u = User.objects.create_user(
                username='root',
                password='password111'
            )
            u.is_staff = True
            u.is_superuser = True
            u.save()

            # 2. create library admin
            u = User.objects.create_user(
                username='u_lib_admin',
                password='password111'
            )
            pu = PyUser.objects.create(
                user=u,
                nickName='lib_admin',
                avatarUrl=avatar_url_list['lib_admin'],
                unionId='1',
                type=ADMIN
            )

            # 3. create employee ray
            u = User.objects.create_user(
                username='u_ray',
                password='password111'
            )
            pu_ray = PyUser.objects.create(
                user=u,
                nickName='ray',
                avatarUrl=avatar_url_list['ray'],
                unionId='2',
                type=EMPLOYEE
            )

            # 3. create employee lu
            u = User.objects.create_user(
                username='u_lu',
                password='password111'
            )
            pu_lu = PyUser.objects.create(
                user=u,
                nickName='lu',
                avatarUrl=avatar_url_list['ldy'],
                unionId='3',
                type=EMPLOYEE
            )

            book = Book.objects.create(
                created=now(),
                douban_id=111,
                status=HAS_BORROWED,
                owner=pu_ray,
            )
            book = Book.objects.create(
                created=now(),
                douban_id=222,
                status=IN_WISH_LIST,
                owner=None,
            )
            book.wishers.add(pu_lu, pu_ray)
            book.save()
    except:
        traceback.print_exc()

