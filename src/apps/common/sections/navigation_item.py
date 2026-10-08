from dataclasses import dataclass

import flet as ft

from apps.common.i18n.types import TranslationKey


@dataclass(frozen=True)
class NavigationItem:
    label: TranslationKey
    icon: ft.IconData
    selected_icon: ft.IconData
    path: str
