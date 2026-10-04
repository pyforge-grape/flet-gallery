from dataclasses import dataclass

import flet as ft

from apps.common.i18n.types import TranslationKey
from features import paths


@dataclass(frozen=True)
class MenuItem:
    content: TranslationKey
    icon: ft.IconData
    path: str


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
