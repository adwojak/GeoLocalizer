class PartialPermissionsMixin:

    @property
    def partial_permission_classes(self):
        raise NotImplementedError

    def get_permissions(self):
        permissions = self.partial_permission_classes.get(self.action, self.permission_classes)
        return [permission() for permission in permissions]
