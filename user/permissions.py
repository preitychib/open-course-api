from rest_framework import permissions


class UserIsAdmin(permissions.BasePermission):
    '''
        permission check if the user is Admin
    '''

    def has_permission(self, request, view):
        if request.user.is_admin:
            return True
        return False


class UserIsTeacher(permissions.BasePermission):
    '''
        permission check if the user is Teacher
    '''

    def has_permission(self, request, view):
        if request.user.is_teacher:
            return True
        return False


class UserIsStudent(permissions.BasePermission):
    '''
        permission check if the user is Student    
    '''

    def has_permission(self, request, view):
        if request.user.is_student:
            return True
        return False