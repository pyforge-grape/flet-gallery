import flet as ft

from mobile_app_layout import MobileAppLayout


def MobileAppRouter():
    return ft.Router(
        [
            ft.Route(
                component=MobileAppLayout,
                children=[],
            ),
        ],
    )
