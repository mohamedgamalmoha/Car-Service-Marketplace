from django.db import models
from django.utils.timezone import datetime
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, UserManager


PhoneNumberValidator = RegexValidator(r'^[0-9]{11}$', 'Invalid Phone Number')


class UserRole(models.TextChoices):
    ADMIN = "ADMIN", _("Admin")
    STAFF = "STAFF", _("Staff")
    CUSTOMER = "CUSTOMER", _("Customer")

    @classmethod
    def as_dict(cls):
        return {k: v.value for k, v in dict(cls.__members__).items()}


class UserGender(models.TextChoices):
    MALE = "M", _("Male")
    FEMALE = "F", _("Female")


class User(AbstractUser):

    base_role = UserRole.STAFF
    role = models.CharField(max_length=50, choices=UserRole.choices, verbose_name=_("Role"))

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"

    def __str__(self):
        return str(self.get_username())

    def save(self, *args, **kwargs):
        if not self.pk and not self.role:
            self.role = self.base_role
        return super().save(*args, **kwargs)


class CustomerManager(UserManager):

    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=UserRole.CUSTOMER)


class Customer(User):
    base_role = UserRole.CUSTOMER
    student = CustomerManager()

    class Meta:
        proxy = True


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name=_("User"))
    image = models.ImageField(upload_to='customers/images/', blank=True, null=True, verbose_name=_("Image"))
    phone_number = models.CharField(max_length=11, validators=[PhoneNumberValidator, ], verbose_name=_("Phone Number"))
    city = models.CharField(max_length=150, blank=True, null=True, verbose_name=_("City"))
    state = models.CharField(max_length=150, blank=True, null=True, verbose_name=_("State"))
    address = models.CharField(max_length=150, blank=True, null=True, verbose_name=_("Address"))
    gender = models.CharField(max_length=1, choices=UserGender.choices, verbose_name=_("Gender"))
    date_of_birth = models.DateField(blank=True, null=True, verbose_name=_("Date Of Birth"))
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name=_("Updated"))

    class Meta:
        verbose_name = _("Customer Profile")
        verbose_name_plural = _("Customer Profiles")

    def __str__(self):
        return str(self.name)

    @property
    def name(self):
        return self.user.get_full_name() or self.username

    @property
    def age(self):
        birthdate = self.date_of_birth
        if birthdate is None:
            return None
        today = datetime.today()
        ag = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return ag

    def show_image(self, width: int = 150, height: int = 100):
        url = self.image.url
        return mark_safe(f'<a href="{url}"> <img src="{url}" width="{width}" height={height}/></a>')
    show_image.short_description = _("Show Image")
