import flet as ft

from apps.desktop.layout import AppLayout
from features.gallery.desktop.routes import GalleryRoutes
from features.home.desktop.routes import HomeRoutes
from features.index.desktop.routes import IndexRoutes
from features.master.desktop.routes import MasterRoutes
from features.notifications.desktop.routes import NotificationsRoutes
from features.profile.desktop.routes import ProfileRoutes
from features.settings.desktop.routes import SettingsRoutes


def AppRouter():
    return ft.Router(
        [
            ft.Route(
                component=AppLayout,
                outlet=True,
                children=[
                    *IndexRoutes(),
                    *ProfileRoutes(),
                    *SettingsRoutes(),
                    *HomeRoutes(),
                    *GalleryRoutes(),
                    *NotificationsRoutes(),
                    *MasterRoutes(),
                ],
            ),
        ],
        manage_views=True,
    )
