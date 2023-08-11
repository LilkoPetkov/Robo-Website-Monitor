from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth import models as auth_models, get_user_model as gum


# Create your models here.

class AppUserManager(auth_models.BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, password2, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.password2 = make_password(password2)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, password2=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, password2, **extra_fields)

    def create_superuser(self, email=None, password=None, password2=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, password2, **extra_fields)


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    objects = AppUserManager()
    USERNAME_FIELD = "email"
    email = models.EmailField(
        null=False,
        blank=False,
        unique=True
    )

    is_staff = models.BooleanField(
        default=False,
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email


class Profile(models.Model):
    user_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    user = models.OneToOneField(gum(), on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.pk} {self.first_name} {self.last_name}"


# --------------------- Websites ------------------------ #

class Websites(models.Model):
    class REFRESH_RATE(models.TextChoices):
        FIVE_MINUTES = 5, ("Every 5 Minutes")
        FIFTEEN_MINUTES = 15, ("Every 15 Minutes")
        THIRTY_MINUTES = 30, ("Every 30 Minutes")
        EVERY_HOUR = 60, ("Every 60 Minutes")
        ONCE_A_DAY = 24, ("Once a day")

    domain = models.CharField(max_length=50, validators=[
        RegexValidator(
            regex='^[a-z0-9]+\.[a-z0-9]{1,4}$',
            message='Domain must be Alphanumeric without http / https protocols',
            code='invalid_username'
        ),
    ])
    verification_status = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )
    verification_record = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    checker_rate = models.CharField(
        max_length=15,
        choices=REFRESH_RATE.choices,
        default=REFRESH_RATE.ONCE_A_DAY,
    )

    user = models.ForeignKey(gum(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'

    def __str__(self):
        return self.domain


# --------------------- Logs ------------------------ #

class Logs(models.Model):
    status_code = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    response_headers = models.CharField(
        max_length=5000,
        null=True,
        blank=True,
    )
    date_time = models.DateTimeField(auto_now=True)
    website_speed = models.CharField(
        max_length=100,
    )

    website = models.ForeignKey(Websites, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'

    def __str__(self):
        return self.website.domain
