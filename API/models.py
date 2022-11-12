from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import random

# Create your models here.



class MyUserManager(BaseUserManager):
    def create_user(self, email, phone, password=None):

        if not email:
            raise ValueError('email Required')
        if not phone:
            raise ValueError('phone Number Required')

        user = self.model(
            email = self.normalize_email(email),
            phone = phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, password=None):

        if not email:
            raise ValueError('email required')
        if not phone:
            raise ValueError('phone number Requird')

        user = self.create_user(
            email    = email,
            phone    = phone,
            password = password
        )
        user.is_admin     = True
        user.is_staff     = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email        = models.EmailField(verbose_name="email", max_length=30, unique=True)
    phone        = models.CharField(verbose_name="phone", max_length=20)
    is_admin     = models.BooleanField(default=False)
    is_staff     = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        return True 

    def has_module_perms(self, app_lable):
        return True 






class EmployeeRecord(models.Model):
    first_name           = models.CharField(max_length=30)
    last_name            = models.CharField(max_length=30)
    email                = models.EmailField()
    date_employed        = models.DateTimeField(auto_now_add=True)
    developer_role       = models.CharField(max_length=100)
    programming_language = models.CharField(max_length=100)
    userID               = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name


    # def IDGenetator(self, request):
    #     randomNum  = random.randint(10000, 99999)
    #     firstIdex = self.first_name[0]
    #     lastIdex  = self.last_name[0]

    #     user_id = firstIdex + lastIdex + str(randomNum)
        
    #     return user_id 

    
