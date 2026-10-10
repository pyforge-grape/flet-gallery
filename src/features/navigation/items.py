import flet as ft

from features import paths
from features.navigation.item import NavigationItem

NAVIGATION_ITEMS = [
    NavigationItem(
        label="home.link.label",
        icon=ft.Icons.HOME_OUTLINED,
        selected_icon=ft.Icons.HOME_SHARP,
        path=paths.HOME,
    ),
    NavigationItem(
        label="gallery.link.label",
        icon=ft.Icons.GRID_VIEW_OUTLINED,
        selected_icon=ft.Icons.GRID_VIEW_SHARP,
        path=paths.GALLERY,
    ),
    NavigationItem(
        label="notifications.link.label",
        icon=ft.Icons.NOTIFICATIONS_OUTLINED,
        selected_icon=ft.Icons.NOTIFICATIONS_SHARP,
        path=paths.NOTIFICATIONS,
    ),
    NavigationItem(
        label="master.link.label",
        icon=ft.Icons.TABLE_ROWS_OUTLINED,
        selected_icon=ft.Icons.TABLE_ROWS_SHARP,
        path=paths.MASTER,
    ),
    NavigationItem(
        label="experiment.link.label",
        icon=ft.Icons.SCIENCE_OUTLINED,
        selected_icon=ft.Icons.SCIENCE_SHARP,
        path=paths.EXPERIMENT,
    ),
]

NAVIGATION_ITEMS_MOBILE = [
    item
    for item in NAVIGATION_ITEMS
    if item.path
    not in (
        paths.HOME,
        paths.GALLERY,
        paths.NOTIFICATIONS,
    )
]
