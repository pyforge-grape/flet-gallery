import flet as ft

from features.settings.paths import SETTINGS
from features.settings.tablet.layout import SettingsLayout


def SettingsRoutes():
    return [
        ft.Route(
            path=SETTINGS,
            component=SettingsLayout,
        ),
    ]
