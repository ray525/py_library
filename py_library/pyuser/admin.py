from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import PyUser


# Define an inline admin descriptor for PyUser model
# which acts a bit like a singleton
class PyUserInline(admin.StackedInline):
    model = PyUser
    can_delete = False
    verbose_name_plural = 'pyuser_wx_infp'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (PyUserInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
