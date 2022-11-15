from rest_framework.permissions import BasePermission


class IsAllowed(BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action in ["list"]:
            return bool(
                request.user and 
                request.user.is_auhtenticated 
            )
