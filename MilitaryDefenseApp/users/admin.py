from django.contrib import admin
from users.models import User
from users.models import SoldierProfile, CommanderProfile
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from .forms import CustomUserCreationForm


class SoldierProfileInline(admin.StackedInline):
    model = SoldierProfile
    can_delete = False

class CommanderProfileInline(admin.StackedInline):
    model = CommanderProfile
    can_delete = False

class AccountsUserAdmin(AuthUserAdmin):
    # form = CustomUserCreationForm
    # add_form = CustomUserCreationForm
    # fieldsets =  AuthUserAdmin.fieldsets
    # # list_display = ["username", "name", "is_superuser"]


    inlines = [SoldierProfileInline]
    commander_inlines = [CommanderProfileInline]
    user_inlines = []
    def get_inlines(self, request, obj):
            if obj.type == "SOLDIER":
               return self.inlines
            elif obj.type == "COMMANDER":
               return self.other_set_of_inlines
            else:
               return self.user_inlines

    def add_view(self, *args, **kwargs):
        self.inlines =[]
        return super(AccountsUserAdmin, self).add_view(*args, **kwargs)

    def change_view(self,*args, **kwargs):
        return super(AccountsUserAdmin, self).change_view(*args, **kwargs)


# admin.site.register(User)
admin.site.register(User, AccountsUserAdmin)



