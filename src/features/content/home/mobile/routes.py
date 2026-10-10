import flet as ft

from features.content.home.mobile.layout import HomeLayout
from features.content.home.paths import HOME


def HomeRoutes():
    return [
        ft.Route(
            path=HOME,
            component=HomeLayout,
        ),
    ]
