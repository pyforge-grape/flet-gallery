import flet as ft

from apps.tablet.navigation import AppNavigation
from apps.tablet.top_bar import AppTopBar


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
                        AppNavigation(),
                        ft.VerticalDivider(),
                        ft.Container(
                            content=outlet,
                        ),
                    ],
                ),
            ),
        ],
    )
