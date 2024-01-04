# your_app/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Soldier, Commander, SoldierProfile, CommanderProfile

class UserProfileInline(admin.StackedInline):
    model = SoldierProfile
    can_delete = False
    verbose_name_plural = 'Soldier Profile'

class CommanderProfileInline(admin.StackedInline):
    model = CommanderProfile
    can_delete = False
    verbose_name_plural = 'Commander Profile'

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Additional Information',
            {
                'fields': (
                    'rank',
                    'unit',
                    'gender',
                    'dateEnlisted',
                    'dateDischarged',
                    'previousTraining',
                    'awards',
                ),
            },
        ),
    )

    def get_inlines(self, request, obj):
        if obj.type == User.Types.SOLDIER:
            return [UserProfileInline]
        elif obj.type == User.Types.COMMANDER:
            return [CommanderProfileInline]
        return super().get_inlines(request, obj)

# Register your models with the custom admin class
admin.site.register(User, CustomUserAdmin)
admin.site.register(Soldier)
admin.site.register(Commander)
