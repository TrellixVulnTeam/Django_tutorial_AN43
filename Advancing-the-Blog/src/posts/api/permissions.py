from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of this object'
    my_safe_method = ['GET','PUT']
    def has_permission(self, request, view):
        if request.method in self.my_safe_method:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        #my_safe_method = ['PUT']
        if request.method in self.my_safe_method:
            return True
        return obj.user == request.user
