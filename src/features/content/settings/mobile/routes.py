import flet as ft

from features.content.settings.mobile.layout import SettingsLayout
from features.content.settings.paths import SETTINGS


def SettingsRoutes():
    return [
        ft.Route(
            path=SETTINGS,
            component=SettingsLayout,
        ),
    ]
