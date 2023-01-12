
from .models import UserRole


def user_roles(request):
    return {"user_role": UserRole.as_dict()}
