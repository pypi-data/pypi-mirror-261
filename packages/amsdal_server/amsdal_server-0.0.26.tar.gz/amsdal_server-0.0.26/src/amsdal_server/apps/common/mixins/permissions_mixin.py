from amsdal_models.classes.helpers.reference_loader import ReferenceLoader
from amsdal_models.classes.model import Model
from amsdal_utils.lifecycle.enum import LifecycleEvent
from amsdal_utils.lifecycle.producer import LifecycleProducer
from amsdal_utils.models.data_models.reference import Reference
from starlette.authentication import BaseUser

from amsdal_server.apps.common.permissions.enums import AccessTypes
from amsdal_server.apps.common.permissions.models import PermissionsInfo


class PermissionsMixin:
    @classmethod
    def get_permissions_info(
        cls,
        class_item: type[Model],
        user: BaseUser,
        access_types: list[AccessTypes] | None = None,
    ) -> PermissionsInfo:
        permissions_info = PermissionsInfo()
        _access_types = access_types or [AccessTypes.READ]

        if getattr(user, 'permissions', None):
            user.permissions = [  # type: ignore[attr-defined]
                ReferenceLoader(p).load_reference() if isinstance(p, Reference) else p for p in user.permissions  # type: ignore[attr-defined]
            ]

        LifecycleProducer.publish(
            LifecycleEvent.ON_PERMISSION_CHECK,
            object_class=class_item,
            user=user,
            access_types=_access_types,
            permissions_info=permissions_info,
        )

        return permissions_info
