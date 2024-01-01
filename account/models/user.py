from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManger(BaseUserManager):
    """ handel Create custom user """

    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)     # for hashing password
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_superuser', True)     # we are checking if it does not exist ,setdefault to true
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_verified', True)

        if kwargs.get('is_superuser') is not True:
            raise ValueError('super_user must be True')
        self.create_user(email, password, **kwargs)


class CustomUser (AbstractBaseUser, PermissionsMixin):
    """ Custom User for Coup """

    email = models.EmailField(max_length=256, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)      # trigger on creation
    updated = models.DateTimeField(auto_now=True)       # trigger on update

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManger()

    def __str__(self):
        return self.email
