from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.dispatch.dispatcher import receiver
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from car.models import Car
from accounts.models import Customer
from workshop.models import WorkShop, Service


class BookingStatus(models.TextChoices):
    PLACED: str = 0, _("PLACED")
    ESTIMATED: str = 1, _("ESTIMATED")
    PAID: str = 2, _("PAID")
    CANCELED: str = 3, _("CANCELED")
    FAILED: str = 4, _("FAILED")

    @classmethod
    def customer_choices(cls):
        return (cls.PLACED, 'PLACED'), (cls.CANCELED, 'CANCELED')


class BookingCommissionStatus(models.TextChoices):
    Collected: str = 1, _("Collected")
    NOT_Collected: str = 0, _("Not Collected")


class DiscountType(models.TextChoices):
    FIXED: str = 0, _("FIXED")
    PERCENTAGE: str = 1, _("PERCENTAGE")
    FREE: str = 2, _("FREE")

    @classmethod
    def calculate_discount(cls, typ, price, discount):
        if typ == cls.FREE:
            return 0
        if typ == cls.FIXED:
            return price - discount
        if typ == cls.PERCENTAGE:
            return price * (discount / 100)


class Coupon(models.Model):
    type = models.CharField(max_length=50, choices=DiscountType.choices, verbose_name=_('Coupon Type'))
    code = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name=_('Code'),
                            help_text=_("Leaving this field empty will generate a random code."))
    value = models.DecimalField(decimal_places=3, max_digits=8,  verbose_name=_('Value'))
    customer_limit = models.PositiveIntegerField(verbose_name=_("Customer Limit"), default=1)
    max_limit = models.PositiveIntegerField(verbose_name=_("Maximum Limit"), default=10)
    valid_from = models.DateField(verbose_name=_('Valid From'), null=True, blank=True)
    valid_until = models.DateField(verbose_name=_('Valid Till'),
                                   help_text=_("Leaving this field empty will generate a random code."))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Date'))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_('Update Date'))

    class Meta:
        ordering = ('create_at', )
        verbose_name = _("Coupon")
        verbose_name_plural = _("Coupons")

    def save(self, *args, **kwargs):
        # if the code wasn't created, generate random one
        if self.code:
            self.code = self.code.upper()
        # if the type was percentage and the value exceeds the limits (0, 100)
        if self.type == DiscountType.PERCENTAGE and (self.value not in range(0, 101)):
            raise ValidationError(
                _('In case of the type is %(type), the value should be in range 0 to 100 not %(value)'),
                params={'value': self.value, 'type': self.type}
            )
        # if the customer limit exceeds the maximum limit
        if self.customer_limit > self.max_limit:
            raise ValidationError(
                _('Limit of customers "%(customer_limit)" cant be bigger than maximum limit "%(max_limit)"'),
                params={'customer_limit': self.customer_limit, 'max_limit': self.max_limit}
            )
        return super(Coupon, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.code)

    def is_expired(self, now_time=timezone.now()):
        return self.valid_until is not None and self.valid_until < now_time

    def reached_max_limit(self):
        bookings = Booking.objects.filter(discount=self)
        return bookings.count() >= self.max_limit

    def reached_customer_limit(self, customer):
        customer_bookings = Booking.objects.filter(discount=self, customer=customer)
        return customer_bookings.count() >= self.user_limit

    def is_valid(self, customer, now_time=timezone.now()):
        return self.is_expired(now_time) and not self.reached_max_limit() and not self.reached_customer_limit(customer)

    def calculate_discount(self, value):
        return DiscountType.calculate_discount(self.type, self.value, value)

    def calculate_price(self, value):
        return value - self.calculate_discount(value)


class Discount(models.Model):
    workshop = models.ForeignKey(WorkShop,  on_delete=models.CASCADE, null=True, related_name='discounts', verbose_name=_('Workshop'))
    service = models.ForeignKey(Service,  on_delete=models.CASCADE, null=True, related_name='discounts', verbose_name=_('Service'))
    type = models.CharField(max_length=50, choices=DiscountType.choices, verbose_name=_('Coupon Type'))
    value = models.DecimalField(decimal_places=3, max_digits=8,  verbose_name=_('Value'))
    valid_from = models.DateField(verbose_name=_('Valid From'))
    valid_until = models.DateField(verbose_name=_('Valid Till'),
                                   help_text=_("Leaving this field empty will generate a random code."))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Date'))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_('Update Date'))

    class Meta:
        ordering = ('create_at', )
        verbose_name = _("Discount")
        verbose_name_plural = _("Discount")

    def save(self, *args, **kwargs):
        # if the service is in workshop services'
        if self.service not in self.workshop.services.all():
            raise ValidationError(
                _('Workshop %(workshop) doesnt offer this services  %(service)'),
                params={'workshop': self.workshop, 'service': self.service}
            )
        # if the discount is right for workshop and service
        if self.type == DiscountType.PERCENTAGE and (self.value not in range(0, 101)):
            raise ValidationError(
                _('In case of the type is %(type), the value should be in range 0 to 100 not %(value)'),
                params={'value': self.value, 'type': self.type}
            )
        # if the valid from date is none, assign it as create at date
        if self.valid_from is None:
            self.valid_from = self.create_at
        return super(Discount, self).save(*args, **kwargs)

    @property
    def is_expired(self):
        return self.valid_until is not None and self.valid_until < timezone.now()

    def calculate_discount(self, value):
        return DiscountType.calculate_discount(self.type, self.value, value)

    def calculate_price(self, value):
        return value - self.calculate_discount(value)


class Booking(models.Model):
    customer = models.ForeignKey(Customer, related_name="bookings", on_delete=models.SET_NULL, null=True,
                                 verbose_name=_('Customer'))
    workshop = models.ForeignKey(WorkShop, on_delete=models.CASCADE, null=True, related_name='bookings',
                                 verbose_name=_('Workshop'))
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, related_name='bookings',
                                verbose_name=_('Service'))
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, related_name='bookings',
                            verbose_name=_('Car'))
    discount = models.ForeignKey(Discount, related_name="bookings", on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name=_('Discount'))
    coupon = models.ForeignKey(Coupon, related_name="bookings", null=True, blank=True, on_delete=models.SET_NULL,
                               verbose_name=_('Coupon'))
    status = models.CharField(max_length=50, choices=BookingStatus.choices, default=BookingStatus.PLACED,
                              verbose_name=_('Booking Status'))
    estimated_price = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True,
                                          verbose_name=_('Estimated Price'))
    earned_amount = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True, default=0,
                                        verbose_name=_('Earned Amount'))
    commission_status = models.CharField(max_length=50, choices=BookingCommissionStatus.choices, null=True,
                                         default=BookingCommissionStatus.NOT_Collected, verbose_name=_('Commission Status'))
    expense_amount = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True, default=0,
                                         verbose_name=_('Expense Amount'))
    note = models.TextField(max_length=400, blank=True, null=True, verbose_name=_('Note'),
                            help_text=_("Tell us more about car issues and parts that need to be maintained ...etc. "))
    schedule_at = models.DateTimeField(verbose_name=_('Schedule At'), help_text=_('When would you like to book?'))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Date'))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_('Update Date'))

    def save(self, *args, **kwargs):
        # if the service is in workshop services'
        if self.service not in self.workshop.services.all():
            raise ValidationError(
                _('Workshop %(workshop) doesnt offer this services  %(service)'),
                params={'workshop': self.workshop, 'service': self.service}
            )
        # if the car owner and customer are same
        if self.car and (self.car not in self.customer.cars.all()):
            raise ValidationError(
                _('Car owner %(car_owner) and customer must be same person'),
                params={'car_owner': self.car.customer, 'customer': self.customer}
            )
        # if the discount is right for workshop and service
        if self.discount and (self.discount.workshop != self.workshop or self.discount.service != self.service):
            raise ValidationError(
                _('In case of the type is %(type), the value should be in range 0 to 100 not %(value)'),
                params={'value': self.value, 'type': self.type}
            )
        # if the coupon hits the maximum limit or user limit
        if self.coupon and not self.coupon.is_valid(self.customer, self.create_at):
            raise ValidationError(
                    _('The coupon hits the maximum limit %(max_limit) or user limit %(customer_limit)'),
                    params={'customer_limit': self.coupon.customer_limit, 'max_limit': self.coupon.max_limit}
                )
        return super(Booking, self).save(*args, **kwargs)

    def calculate_discount(self):
        discount = 0
        price = self.estimated_price
        if price is None:
            return discount
        if self.discount:
            discount += self.discount.calculate_discount(price)
        if self.coupon:
            discount += self.coupon.calculate_discount(price)
        return discount

    @property
    def customer_phone_number(self):
        return self.customer.profile.phone_number

    @property
    def customer_whatsapp_link(self):
        return f"https://wa.me/+2{self.customer_phone_number}"


class Expense(models.Model):
    cause = models.CharField(verbose_name=_('Cause'), max_length=500, help_text=_('What is this expense for?'))
    amount = models.DecimalField(verbose_name=_('Amount'), decimal_places=2, max_digits=8, null=True, blank=True, default=0)
    paid_at = models.DateTimeField(verbose_name=_('Paid At'), help_text=_('When this expense is paid?'))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Date'))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_('Update Date'))


@receiver(pre_save, sender=Booking)
def update_booking_attributes(sender, instance, **kwargs):
    """Update booking status after changing the estimated price"""
    try:
        # in case of the instance was already created before
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        # in case of exception (instance first time to be created), pass away
        if not instance.discount:
            discounts = Discount.objects.filter(
                service=instance.service,
                workshop=instance.workshop,
                valid_until__lt=timezone.now()
            ).order_by('value')
            if discounts.exists():
                instance.discount = discounts.first()
                instance.save()
    else:
        # in case of no exception (instance was already created before)
        if instance.status == BookingStatus.PLACED and (obj.estimated_price != instance.estimated_price):
            instance.status = BookingStatus.ESTIMATED
            instance.save()
