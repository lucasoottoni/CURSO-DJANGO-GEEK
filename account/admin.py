# "account/admin.py"

from django.contrib import admin
#from .models import UserProfile
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#from django.contrib.auth.models import User

#admin.site.register(User) # Necessary

# class UserProfileInline(admin.TabularInline):
#     model = UserProfile

# @admin.register(User)
# class UserAdmin(BaseUserAdmin):
#     inlines = (UserProfileInline,)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass