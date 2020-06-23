from django.db.models import Manager, Q
from django.utils.deprecation import MiddlewareMixin


class PermissionMiddleware(MiddlewareMixin):

    username = None
    user_is_superuser = False

    def process_request(self, request):
        PermissionMiddleware.username = request.user.username
        PermissionMiddleware.user_is_superuser = request.user.is_superuser


class ModelPermissionManager(Manager):

    def __init__(self, clause_list=None):
        super().__init__()
        if clause_list is None:
            clause_list = []
        self.clause_list = clause_list

    def get_queryset(self):
        username = PermissionMiddleware.username

        if PermissionMiddleware.user_is_superuser:
            return super().get_queryset().all()
        elif username:
            q = Q()
            for clause in self.clause_list:
                q |= Q(**{clause: username})

            return super().get_queryset().filter(q)
        else:
            return super().get_queryset().none()
