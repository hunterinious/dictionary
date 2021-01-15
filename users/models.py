from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def __create_base_user(self, email, password):
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password, name):
        user = self.__create_base_user(email, password)

        user_profile = UserProfile.objects.create(name=name, user=user)
        user_profile.save()

        return user

    def create_superuser(self, email, password):
        user = self.__create_base_user(email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser, PermissionsMixin):
    username = None
    first_name = None
    last_name = None

    email = models.EmailField(max_length=60, unique=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ()

    objects = CustomUserManager()


class UserProfile(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
