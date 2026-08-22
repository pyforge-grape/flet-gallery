from collections.abc import Callable
from dataclasses import dataclass

import flet as ft

from features.gallery.router import ToGallery
from features.home.router import ToHome


@ft.component
def MobileBottomBar():
    @dataclass
    class MobileBottomBarItem:
        label: str
        icon: ft.IconData
        selected_icon: ft.IconData
        on_click: Callable[[], None]
        badge: int

    ITEMS = [
        MobileBottomBarItem(
            label="Home",
            icon=ft.Icons.HOME_OUTLINED,
            selected_icon=ft.Icons.HOME_SHARP,
            on_click=ToHome,
            badge=0,
        ),
        MobileBottomBarItem(
            label="Gallery",
            icon=ft.Icons.GRID_VIEW_OUTLINED,
            selected_icon=ft.Icons.GRID_VIEW_SHARP,
            on_click=ToGallery,
            badge=0,
        ),
        MobileBottomBarItem(
            label="Notifications",
            icon=ft.Icons.NOTIFICATIONS_OUTLINED,
            selected_icon=ft.Icons.NOTIFICATIONS_SHARP,
            on_click=(),
            badge=3,
        ),
    ]

    selected_index, set_selected_index = ft.use_state(0)

    def handle_on_click(index: int, item: MobileBottomBarItem):
        set_selected_index(index)
        item.on_click()

    return ft.BottomAppBar(
        content=ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.IconButton(
                            icon=item.icon,
                            selected_icon=item.selected_icon,
                            selected=selected_index == index,
                            on_click=lambda _, i=index, it=item: handle_on_click(i, it),
                            badge=ft.Badge(small_size=10) if item.badge > 0 else None,
                        ),
                        ft.Text(item.label),
                    ],
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                )
                for index, item in enumerate(ITEMS)
            ],
        )
    )
