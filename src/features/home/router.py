import flet as ft

from features.home.layout import DesktopLayout, MobileLayout

PATH = "/home"


def DesktopHomeRoutes():
    return [
        ft.Route(
            path=PATH.removeprefix("/"),
            component=DesktopLayout,
        ),
    ]


def MobileHomeRoutes():
    return [
        ft.Route(
            path=PATH.removeprefix("/"),
            component=MobileLayout,
        ),
    ]


def ToHome():
    ft.context.page.navigate(PATH)
