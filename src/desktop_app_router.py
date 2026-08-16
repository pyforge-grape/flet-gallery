import flet as ft

from desktop_app_layout import DesktopAppLayout


def DesktopAppRouter():
    return ft.Router(
        [
            ft.Route(
                component=DesktopAppLayout,
                children=[],
            ),
        ],
    )
