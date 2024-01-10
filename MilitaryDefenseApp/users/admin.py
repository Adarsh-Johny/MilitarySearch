from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Soldier, Commander, SoldierProfile, CommanderProfile, MilitaryCamp

# Define the inline profiles for Soldier and Commander
class SoldierProfileInline(admin.StackedInline):
    model = SoldierProfile
    can_delete = False
    fields = ('specialization',)  # Add more fields as needed


class CommanderProfileInline(admin.StackedInline):
    model = CommanderProfile
    can_delete = False
    fields = ('responsibility',)  # Add more fields as needed


# Custom UserAdmin for Soldier
class SoldierAdmin(UserAdmin):
    inlines = [SoldierProfileInline]
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'type', 'rank', 'unit',
        'gender', 'dateEnlisted', 'dateDischarged', 'previousTraining', 'awards'
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'type', 'rank', 'unit', 'gender', 'dateEnlisted', 'dateDischarged', 'previousTraining', 'awards')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    def get_inline_instances(self, request, obj=None):
        if obj and obj.type == User.Types.SOLDIER:
            return [SoldierProfileInline(self.model, self.admin_site)]
        return super().get_inline_instances(request, obj)


# Custom UserAdmin for Commander
class CommanderAdmin(UserAdmin):
    inlines = [CommanderProfileInline]
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'type', 'rank', 'unit',
        'gender', 'dateEnlisted', 'dateDischarged', 'previousTraining', 'awards'
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'type', 'rank', 'unit', 'gender', 'dateEnlisted', 'dateDischarged', 'previousTraining', 'awards')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    def get_inline_instances(self, request, obj=None):
        if obj and obj.type == User.Types.COMMANDER:
            return [CommanderProfileInline(self.model, self.admin_site)]
        return super().get_inline_instances(request, obj)


# Register the models and admin classes
admin.site.register(User, UserAdmin)
admin.site.register(Soldier, SoldierAdmin)
admin.site.register(Commander, CommanderAdmin)
admin.site.register(MilitaryCamp)
