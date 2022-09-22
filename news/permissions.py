from rest_framework import permissions


class WasSynced(permissions.BasePermission):
    message = 'This Item can not be updated/deleted!'

    def has_permission(self, request, view):
        methods = ['PUT', 'PATCH', 'DELETE']
        obj = view.get_object()

        if obj.synced and request.method in methods:
            return False
        return True
