import flet as ft

from features.content.index.mobile.layout import IndexLayout


def IndexRoutes():
    return [
        ft.Route(
            index=True,
            component=IndexLayout,
        ),
    ]
