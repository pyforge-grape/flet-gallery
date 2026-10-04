from dataclasses import dataclass

import flet as ft

from apps.common.i18n.types import TranslationKey
from features.experiment.paths import EXPERIMENT
from features.gallery.paths import GALLERY
from features.home.paths import HOME
from features.master.paths import MASTER
from features.notifications.paths import NOTIFICATIONS


@dataclass(frozen=True)
class NavigationItem:
    label: TranslationKey
    icon: ft.IconData
    selected_icon: ft.IconData
    path: str


NAVIGATION_ITEMS = [
    NavigationItem(
        label="home.link.label",
        icon=ft.Icons.HOME_OUTLINED,
        selected_icon=ft.Icons.HOME_SHARP,
        path=HOME,
    ),
    NavigationItem(
        label="gallery.link.label",
        icon=ft.Icons.GRID_VIEW_OUTLINED,
        selected_icon=ft.Icons.GRID_VIEW_SHARP,
        path=GALLERY,
    ),
    NavigationItem(
        label="notifications.link.label",
        icon=ft.Icons.NOTIFICATIONS_OUTLINED,
        selected_icon=ft.Icons.NOTIFICATIONS_SHARP,
        path=NOTIFICATIONS,
    ),
    NavigationItem(
        label="master.link.label",
        icon=ft.Icons.TABLE_ROWS_OUTLINED,
        selected_icon=ft.Icons.TABLE_ROWS_SHARP,
        path=MASTER,
    ),
    NavigationItem(
        label="experiment.link.label",
        icon=ft.Icons.SCIENCE_OUTLINED,
        selected_icon=ft.Icons.SCIENCE_SHARP,
        path=EXPERIMENT,
    ),
]

NAVIGATION_ITEMS_MOBILE = [
    item
    for item in NAVIGATION_ITEMS
    if item.path
    not in (
        HOME,
        GALLERY,
        NOTIFICATIONS,
    )
]
