from dataclasses import dataclass

import flet as ft

from apps.common.i18n.types import TranslationKey


@dataclass(frozen=True)
class MenuItem:
    content: TranslationKey
    icon: ft.IconData
    path: str
