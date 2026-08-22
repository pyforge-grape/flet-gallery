import flet as ft


@ft.component
def AppTopBar():
    ITEMS = [
        {
            "content": "Profile",
            "icon": ft.Icons.PERSON,
            "on_click": (),
        },
        {
            "content": "Settings",
            "icon": ft.Icons.SETTINGS,
            "on_click": (),
        },
        {
            "content": "Logout",
            "icon": ft.Icons.LOGOUT,
            "on_click": (),
        },
    ]

    return ft.AppBar(
        title="Flet Gallery",
        actions=[
            ft.PopupMenuButton(
                icon=ft.CircleAvatar(
                    content="USER",
                    bgcolor=ft.Colors.PRIMARY,
                    color=ft.Colors.ON_PRIMARY,
                ),
                items=[
                    ft.PopupMenuItem(
                        content=item["content"],
                        icon=item["icon"],
                        on_click=item["on_click"],
                    )
                    for item in ITEMS
                ],
            ),
        ],
    )
