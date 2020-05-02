from django.core.exceptions import PermissionDenied
from users.models import CustomUser

def user_is_entry_author(function):
    def wrap(request, *args, **kwargs):
        entry = CustomUser.objects.get(pk=kwargs['users_id'])
        if entry.created_by == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap