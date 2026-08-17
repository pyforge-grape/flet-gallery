import flet as ft


@ft.component
def DesktopAppLayout():
    outlet = ft.use_route_outlet()

    return ft.View(
        route=ft.use_view_path(),
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
        controls=[
            ft.SafeArea(
                expand=True,
                content=ft.Container(
                    content=outlet,
                ),
            )
        ],
    )
