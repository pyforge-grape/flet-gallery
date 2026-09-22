import flet as ft

from features.home.paths import HOME
from features.home.tablet.layout import HomeLayout


def HomeRoutes():
    return [
        ft.Route(
            path=HOME,
            component=HomeLayout,
        ),
    ]
