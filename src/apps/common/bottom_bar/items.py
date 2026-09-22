from dataclasses import dataclass

import flet as ft

from features.gallery.paths import GALLERY
from features.home.paths import HOME
from features.notifications.paths import NOTIFICATIONS


@dataclass(frozen=True)
class BottomBarItem:
    label: str
    icon: ft.IconData
    selected_icon: ft.IconData
    path: str


BOTTOM_BAR_ITEMS = [
    BottomBarItem(
        label="Home",
        icon=ft.Icons.HOME_OUTLINED,
        selected_icon=ft.Icons.HOME_SHARP,
        path=HOME,
    ),
    BottomBarItem(
        label="Gallery",
        icon=ft.Icons.GRID_VIEW_OUTLINED,
        selected_icon=ft.Icons.GRID_VIEW_SHARP,
        path=GALLERY,
    ),
    BottomBarItem(
        label="Notifications",
        icon=ft.Icons.NOTIFICATIONS_OUTLINED,
        selected_icon=ft.Icons.NOTIFICATIONS_SHARP,
        path=NOTIFICATIONS,
    ),
]
