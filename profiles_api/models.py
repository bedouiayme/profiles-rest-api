from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfilManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('USer must have an email address')

        email = email.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(self._db)
        return user

    def create_superuser(self, email, name, password):
        """Create and save a new super user with givin details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(self._db)
        return user


# Create your models here.
class UserProfil(AbstractBaseUser, PermissionsMixin):
    """Database model for users system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfilManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return a string representation of our user"""
        # return self.email," ",self.name
        return self.email
