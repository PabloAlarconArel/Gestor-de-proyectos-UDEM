from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


# Create your models here.
class Rol(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50,unique= True)
    its_active = models.BooleanField(default = True)

    class Meta():
        verbose_name= 'Role'
        verbose_name='Roles'

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return f'Model Rol: {self.name}'

class managerUser(BaseUserManager):
    def create_user(self,email,names,lastnames,phone,password=None):
        if not email:
            raise ValueError('The user must have an email!')

        user = self.model(
            email = self.normalize_email(email),
            names = names,
            lastnames = lastnames,
            phone = phone,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,names,lastnames,phone,password):
        user = self.create_user(
            email,
            names = names,
            lastnames = lastnames,
            phone = phone,
            password = password,


        )
        user.its_staff = True
        user.role_id = 1
        user.save()
        return user

#Model User
class user(AbstractBaseUser):
    id = models.AutoField(primary_key = True)
    email = models.EmailField('Email', max_length=254,unique = True)
    names = models.CharField('Names', max_length=200, blank = True, null = True)
    lastnames = models.CharField('Lastnames', max_length=200,blank = True, null = True)
    phone = models.CharField('Phone', max_length=9,blank = True, null = True)
    its_active = models.BooleanField(default = True)
    its_staff = models.BooleanField(default = False)
    role = models.ForeignKey(Rol, null=True, blank=True, on_delete=models.CASCADE)
    #department = models.ForeignKey()
    objects = managerUser()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['names','lastnames','phone']

    def __str__(self):
        return f'{self.names} {self.lastnames}'
    
    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.its_staff



# Create your models here.
