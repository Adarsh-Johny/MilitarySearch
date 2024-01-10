# your_app/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Soldier, Commander, SoldierProfile, CommanderProfile, MilitaryCamp

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

    def get_inline_instances(self, request, obj):
        if obj and obj.type == User.Types.SOLDIER:
            return [UserProfileInline]
        elif obj and obj.type == User.Types.COMMANDER:
            return [CommanderProfileInline]
        return super().get_inline_instances(request, obj)

class MilitaryCampAdmin(admin.ModelAdmin):
    list_display = ('location', 'latitude', 'longitude', 'executes_action', 'status', 'service_branch')
    search_fields = ('location', 'service_branch')

# Register your models with the custom admin class
admin.site.register(User, CustomUserAdmin)
admin.site.register(Soldier)
admin.site.register(Commander)
admin.site.register(MilitaryCamp)

