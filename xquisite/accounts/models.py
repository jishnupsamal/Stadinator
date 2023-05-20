from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.set_password(password)
        extra_fields.setdefault('is_active', True)
        # group = Group.objects.get(name='User') 
        # user.groups.add(group)
        user.save(using=self._db)
        user.is_active = True
        group = Group.objects.get(name='User')
        user.groups.add(group) 
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, username and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    objects = CustomUserManager()
    email = models.EmailField(unique=True, blank=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

# User = get_user_model()
# class CustomGroup(Group):
#     Users = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
