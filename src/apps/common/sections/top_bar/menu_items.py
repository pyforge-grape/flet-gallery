from dataclasses import dataclass

import flet as ft

from apps.common.i18n.types import TranslationKey
from features.profile.paths import PROFILE
from features.settings.paths import SETTINGS


@dataclass(frozen=True)
class MenuItem:
    content: TranslationKey
    icon: ft.IconData
    path: str


MENU_ITEMS = [
    MenuItem(
        content="profile.link.label",
        icon=ft.Icons.PERSON,
        path=PROFILE,
    ),
    MenuItem(
        content="settings.link.label",
        icon=ft.Icons.SETTINGS,
        path=SETTINGS,
    ),
]
