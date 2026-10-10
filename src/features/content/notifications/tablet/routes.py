import flet as ft

from features.content.notifications.paths import NOTIFICATIONS
from features.content.notifications.tablet.layout import NotificationsLayout


def NotificationsRoutes():
    return [
        ft.Route(
            path=NOTIFICATIONS,
            component=NotificationsLayout,
        ),
    ]
