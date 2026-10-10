import flet as ft

from apps.mobile.bottom_bar import AppBottomBar
from apps.mobile.navigation import AppNavigation
from apps.mobile.top_bar import AppTopBar


@ft.component
def AppLayout():
    outlet = ft.use_route_outlet()

    return ft.View(
        route="/",
        can_pop=False,
        appbar=AppTopBar(),
        controls=[
            ft.SafeArea(
                expand=True,
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=outlet,
                        ),
                    ],
                ),
            ),
        ],
        drawer=AppNavigation(),
        bottom_appbar=AppBottomBar(),
    )
