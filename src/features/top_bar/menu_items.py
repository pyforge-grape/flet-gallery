import flet as ft

from features import paths
from features.top_bar.menu_item import MenuItem

MENU_ITEMS = [
    MenuItem(
        content="profile.link.label",
        icon=ft.Icons.PERSON,
        path=paths.PROFILE,
    ),
    MenuItem(
        content="settings.link.label",
        icon=ft.Icons.SETTINGS,
        path=paths.SETTINGS,
    ),
]
