from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

class User(AbstractUser):
    class Types(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        SOLDIER = "SOLDIER", "Soldier"
        COMMANDER = "COMMANDER", "Commander"

    base_type = Types.ADMIN

    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=base_type
    )

    rank = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    dateEnlisted = models.CharField(max_length=50)
    dateDischarged = models.CharField(max_length=50)
    previousTraining = models.CharField(max_length=50)
    awards = models.CharField(max_length=50)

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

class SoldierProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)

@receiver(post_save, sender=get_user_model())
def create_soldier_profile(sender, instance, created, **kwargs):
    if created and instance.type == "SOLDIER":
        SoldierProfile.objects.get_or_create(user=instance)

class CommanderManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.COMMANDER)

class Commander(User):
    base_type = User.Types.COMMANDER
    commander = CommanderManager()

    class Meta:
        proxy = True

class CommanderProfile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    responsibility = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=Commander)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.type == "COMMANDER":
        CommanderProfile.objects.get_or_create(user=instance)

from django.db import models
from django.utils.translation import gettext_lazy as _

class MilitaryCamp(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        INACTIVE = "INACTIVE", "Inactive"

    class ServiceBranch(models.TextChoices):
        ARMY = "ARMY", "Army"
        NAVY = "NAVY", "Navy"
        AIR_FORCE = "AIR_FORCE", "Air Force"
    id =models.IntegerField(_("Id"), primary_key=True)
    location = models.CharField(_("Location"), max_length=50)
    latitude = models.FloatField(_("Latitude"))
    longitude = models.FloatField(_("Longitude"))
    executes_action = models.CharField(_("Executes Action"), max_length=50)
    status = models.CharField(_("Status"), max_length=50, choices=Status.choices, default=Status.ACTIVE)
    service_branch = models.CharField(_("Service Branch"), max_length=50, choices=ServiceBranch.choices)
