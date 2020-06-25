from django.db.models import Manager, Q
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework.authtoken.models import Token


class PermissionMiddleware(MiddlewareMixin):

    user_token = None
    user_is_superuser = False

    def process_request(self, request):
        token = request.META.get('Token') or request.headers.get('Token')
        PermissionMiddleware.user_token = token

        try:
            if token and Token.objects.get(key=token).user.is_superuser:
                PermissionMiddleware.user_is_superuser = True
            else:
                PermissionMiddleware.user_is_superuser = False
        except Token.DoesNotExist:
            return HttpResponse(status=401, content='User not found!')


class ModelPermissionManager(Manager):

    def __init__(self, clause_list=None):
        super().__init__()
        if clause_list is None:
            clause_list = []
        self.clause_list = clause_list

    def get_queryset(self):
        user_token = PermissionMiddleware.user_token

        if PermissionMiddleware.user_is_superuser:
            return super().get_queryset().all()
        elif user_token:
            q = Q()
            for clause in self.clause_list:
                q |= Q(**{clause: user_token})

            return super().get_queryset().filter(q)
        else:
            return super().get_queryset().none()
