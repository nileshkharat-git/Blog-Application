from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self,email,username,first_name,last_name,password=None):
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name=first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,first_name,last_name,password):
        user = self.create_user(
            email=email,
            username=username,
            first_name = first_name,
            last_name = last_name,
            password=password
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class Accounts(AbstractBaseUser):
    email=models.EmailField(primary_key=True, max_length=255, verbose_name="Email")
    username= models.CharField(max_length=255,unique=True,verbose_name="Username")
    first_name=models.CharField(max_length=255,verbose_name="First name")
    last_name=models.CharField(max_length=255,verbose_name="Last name")

    date_joined=models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name',]

    object = AccountManager()

    def has_perm(self,perm,obj=None):
        return  self.is_admin

    def has_module_perms(self,app_label):
        return True

