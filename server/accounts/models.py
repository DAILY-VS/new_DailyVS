from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('이메일 필수')
        
        email = self.normalize_email(email) # 소문자로 바꿈 + ?
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()

        return user
        
    # def create_superuser() # 형식이 똑같아야 함

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def get_full_name(self):
        return self.name
    
    def __str__(self):
        return self.email
