import flet as ft

from features.content.home.paths import HOME
from features.content.home.tablet.layout import HomeLayout


def HomeRoutes():
    return [
        ft.Route(
            path=HOME,
            component=HomeLayout,
        ),
    ]
