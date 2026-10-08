import flet as ft

from apps.common.sections.top_bar_menu_item import MenuItem
from features import paths

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
