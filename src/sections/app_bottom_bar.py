import flet as ft


@ft.component
def MobileBottomBar():
    ITEMS = [
        {
            "label": "Home",
            "icon": ft.Icons.HOME,
            "on_click": (),
            "badge": 0,
        },
        {
            "label": "Gallery",
            "icon": ft.Icons.GRID_VIEW,
            "on_click": (),
            "badge": 0,
        },
        {
            "label": "Notifications",
            "icon": ft.Icons.NOTIFICATIONS,
            "on_click": (),
            "badge": 3,
        },
    ]

    return ft.BottomAppBar(
        content=ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.IconButton(
                            icon=item["icon"],
                            on_click=item["on_click"],
                            badge=ft.Badge(small_size=10)
                            if item["badge"] > 0
                            else None,
                        ),
                        ft.Text(item["label"]),
                    ],
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
                for item in ITEMS
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        )
    )
