from django.contrib.auth.mixins import AccessMixin

from .models import UserRole


class BaseAuthMixin(AccessMixin):
    def has_permission(self, request) -> bool:
        return True

    def dispatch(self, request, *args, **kwargs):
        if self.has_permission(request):
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()


class StaffAuthMixIn(AccessMixin):
    def has_permission(self, request) -> bool:
        return request.user.is_authenticated and request.user.is_superuser


class CustomerAuthMixIn(AccessMixin):
    def has_permission(self, request) -> bool:
        return request.user.is_authenticated and request.user.role == UserRole.CUSTOMER
