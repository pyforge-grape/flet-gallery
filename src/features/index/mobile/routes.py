import flet as ft

from features.index.mobile.layout import IndexLayout


def IndexRoutes():
    return [
        ft.Route(
            index=True,
            component=IndexLayout,
        ),
    ]
