import flet as ft

from features.settings.desktop.layout import SettingsLayout
from features.settings.paths import SETTINGS


def SettingsRoutes():
    return [
        ft.Route(
            path=SETTINGS,
            component=SettingsLayout,
        ),
    ]
