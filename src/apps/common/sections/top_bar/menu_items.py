from dataclasses import dataclass

import flet as ft

from features.profile.paths import PROFILE
from features.settings.paths import SETTINGS


@dataclass(frozen=True)
class MenuItem:
    content: str
    icon: ft.IconData
    path: str


MENU_ITEMS = [
    MenuItem(
        content="Profile",
        icon=ft.Icons.PERSON,
        path=PROFILE,
    ),
    MenuItem(
        content="Settings",
        icon=ft.Icons.SETTINGS,
        path=SETTINGS,
    ),
]
