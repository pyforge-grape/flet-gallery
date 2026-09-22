import flet as ft

from features.home.desktop.layout import HomeLayout
from features.home.paths import HOME


def HomeRoutes():
    return [
        ft.Route(
            path=HOME,
            component=HomeLayout,
        ),
    ]
