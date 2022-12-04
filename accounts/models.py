from django.utils.timezone import datetime
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, UserManager

PhoneNumberValidator = RegexValidator(r'^[0-9]{11}$', 'Invalid Phone Number')


class UserRole(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    STAFF = "STAFF", "Staff"
    CUSTOMER = "CUSTOMER", "Customer"


class UserGender(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"


class User(AbstractUser):

    base_role = UserRole.STAFF
    role = models.CharField(max_length=50, choices=UserRole.choices)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"

    def save(self, *args, **kwargs):
        if not self.pk:
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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='customers/images/', blank=True, null=True)
    phone_number = models.CharField("Phone Number", max_length=11, validators=[PhoneNumberValidator, ])
    city = models.CharField("City", max_length=150, blank=True, null=True)
    state = models.CharField("State", max_length=150, blank=True, null=True)
    address = models.CharField("Address", max_length=150, blank=True, null=True)
    gender = models.CharField("Gender", max_length=1, choices=UserGender.choices)
    date_of_birth = models.DateField("Date Of Birth", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self.user.get_full_name()

    @property
    def age(self):
        birthdate = self.date_of_birth
        if birthdate is None:
            return None
        today = datetime.today()
        ag = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return ag


@receiver(post_save, sender=Customer)
def create_customer_profile(sender, instance, created, **kwargs):
    if created and instance.role == UserRole.CUSTOMER:
        CustomerProfile.objects.create(user=instance)
