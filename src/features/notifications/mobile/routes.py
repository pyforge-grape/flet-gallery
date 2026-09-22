import flet as ft

from features.notifications.mobile.layout import NotificationsLayout
from features.notifications.paths import NOTIFICATIONS


def NotificationsRoutes():
    return [
        ft.Route(
            path=NOTIFICATIONS,
            component=NotificationsLayout,
        ),
    ]
