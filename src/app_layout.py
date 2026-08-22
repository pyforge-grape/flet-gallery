import flet as ft

from sections.app_bottom_bar import MobileBottomBar
from sections.app_top_bar import AppTopBar


@ft.component
def DesktopAppLayout():
    outlet = ft.use_route_outlet()

    return ft.View(
        route=ft.use_view_path(),
        appbar=AppTopBar(),
        controls=[
            ft.SafeArea(
                expand=True,
                content=ft.Container(
                    content=outlet,
                ),
            )
        ],
    )


@ft.component
def MobileAppLayout():
    outlet = ft.use_route_outlet()

    return ft.View(
        route=ft.use_view_path(),
        appbar=AppTopBar(),
        controls=[
            ft.SafeArea(
                expand=True,
                content=ft.Container(
                    content=outlet,
                ),
            )
        ],
        bottom_appbar=MobileBottomBar(),
    )
