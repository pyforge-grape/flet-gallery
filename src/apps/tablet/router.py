import flet as ft

from apps.tablet.layout import AppLayout
from features.gallery.tablet.routes import GalleryRoutes
from features.home.tablet.routes import HomeRoutes
from features.index.tablet.routes import IndexRoutes
from features.master.tablet.routes import MasterRoutes
from features.notifications.tablet.routes import NotificationsRoutes
from features.profile.tablet.routes import ProfileRoutes
from features.settings.tablet.routes import SettingsRoutes


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
