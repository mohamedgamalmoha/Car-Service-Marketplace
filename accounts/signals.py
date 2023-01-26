from django.dispatch import receiver
from django.db.models.signals import post_save

from allauth.account.signals import user_signed_up

from accounts.models import Customer, UserRole, CustomerProfile


@receiver(user_signed_up)
def social_signed_up(sender, request, user, **kwargs):
    # set role as customer
    user.role = UserRole.CUSTOMER
    user.save()
    # create customer profile
    CustomerProfile.objects.create(user=user)


@receiver(post_save, sender=Customer)
def create_customer_profile(sender, instance, created, **kwargs):
    # create profile in case of being customer
    if created and instance.role == UserRole.CUSTOMER:
        CustomerProfile.objects.create(user=instance)
