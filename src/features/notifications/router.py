import flet as ft

from features.notifications.layout import DesktopLayout, MobileLayout

PATH = "/notifications"


def DesktopNotificationsRoutes():
    return [
        ft.Route(
            path=PATH.removeprefix("/"),
            component=DesktopLayout,
        ),
    ]


def MobileNotificationsRoutes():
    return [
        ft.Route(
            path=PATH.removeprefix("/"),
            component=MobileLayout,
        ),
    ]


def ToNotifications():
    ft.context.page.navigate(PATH)
