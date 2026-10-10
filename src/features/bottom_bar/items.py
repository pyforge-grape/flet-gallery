import flet as ft

from features import paths
from features.bottom_bar.item import BottomBarItem

BOTTOM_BAR_ITEMS = [
    BottomBarItem(
        label="home.link.label",
        icon=ft.Icons.HOME_OUTLINED,
        selected_icon=ft.Icons.HOME_SHARP,
        path=paths.HOME,
    ),
    BottomBarItem(
        label="gallery.link.label",
        icon=ft.Icons.GRID_VIEW_OUTLINED,
        selected_icon=ft.Icons.GRID_VIEW_SHARP,
        path=paths.GALLERY,
    ),
    BottomBarItem(
        label="notifications.link.label",
        icon=ft.Icons.NOTIFICATIONS_OUTLINED,
        selected_icon=ft.Icons.NOTIFICATIONS_SHARP,
        path=paths.NOTIFICATIONS,
    ),
]
