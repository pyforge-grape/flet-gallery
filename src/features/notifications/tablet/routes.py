import flet as ft

from features.notifications.paths import NOTIFICATIONS
from features.notifications.tablet.layout import NotificationsLayout


def NotificationsRoutes():
    return [
        ft.Route(
            path=NOTIFICATIONS,
            component=NotificationsLayout,
        ),
    ]
