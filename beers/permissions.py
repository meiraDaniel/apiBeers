from rest_framework import permissions

#Classe responsável por limitar a edição ou exclusão de determinada atividade ao usuário responsável por criar a mesma.
class IsCreatorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.userId == request.user