from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    class Types(models.TextChoices):
        
        ADMIN = "ADMIN", "Admin"
        SOLDIER = "SOLDIER", "Soldier"
        COMMANDER = "COMMANDER", "Commander"

    base_type = Types.ADMIN

    # What type of user are we?
    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=base_type
    )

    # First Name and Last Name Do Not Cover Name Patterns
    # Around the Globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)


class SoldierManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.SOLDIER)


class Soldier(User):
    base_type = User.Types.SOLDIER
    soldier = SoldierManager()

    class Meta:
        proxy = True


#Extend Soldier's model with additional information
class SoldierProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)


@receiver(post_save, sender=Soldier)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "SOLDIER":
        SoldierProfile.objects.create(user=instance)


class CommanderManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.COMMANDER)
#Extend Commander's model with additional information
    

class Commander(User):
    base_type = User.Types.COMMANDER
    commander = CommanderManager()

    class Meta:
        proxy = True
    

class CommanderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)
    responsibility = models.CharField(max_length=100)


@receiver(post_save, sender=Commander)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "COMMANDER":
        CommanderProfile.objects.create(user=instance)

