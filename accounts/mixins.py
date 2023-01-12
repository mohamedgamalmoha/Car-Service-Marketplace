from django.contrib.auth.mixins import AccessMixin

from .models import UserRole


class BaseAuthMixin(AccessMixin):

    def has_permission(self, request) -> bool:
        return True

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission(request):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class StaffAuthMixIn(BaseAuthMixin):
    """Allow admin user only"""

    def has_permission(self, request) -> bool:
        return request.user.is_authenticated and request.user.is_superuser


class CustomerAuthMixIn(BaseAuthMixin):
    """Allow customer user only"""

    def has_permission(self, request) -> bool:
        return request.user.is_authenticated and request.user.role == UserRole.CUSTOMER
