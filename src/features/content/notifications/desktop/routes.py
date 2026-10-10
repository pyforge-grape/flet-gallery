import flet as ft

from features.content.notifications.desktop.layout import NotificationsLayout
from features.content.notifications.paths import NOTIFICATIONS


def NotificationsRoutes():
    return [
        ft.Route(
            path=NOTIFICATIONS,
            component=NotificationsLayout,
        ),
    ]
