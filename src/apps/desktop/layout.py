import flet as ft

from apps.desktop.sections.navigation import AppNavigation
from apps.desktop.sections.top_bar import AppTopBar


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
