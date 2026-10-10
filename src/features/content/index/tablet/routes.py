import flet as ft

from features.content.index.tablet.layout import IndexLayout


def IndexRoutes():
    return [
        ft.Route(
            index=True,
            component=IndexLayout,
        ),
    ]
