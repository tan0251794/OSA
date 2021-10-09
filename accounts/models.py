from django.db import models    
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserAccountManager(BaseUserManager):
    def create_user(self, name, password=None):
        # if not email:
        #     raise ValueError('User must have an email address')
        #email = self.normalize_email(email)
        user = self.model(name=name)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, name, password):
        user = self.create_user(
            #email,
            name,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserAccounts(AbstractBaseUser, PermissionsMixin):
    #email = models.EmailField(max_length=255)
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    objects = UserAccountManager()

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.name

@receiver(post_save, sender=UserAccounts)
def create_token(sender, instance, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    