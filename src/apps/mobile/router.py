import flet as ft

from apps.mobile.layout import AppLayout
from features.gallery.mobile.routes import GalleryRoutes
from features.home.mobile.routes import HomeRoutes
from features.index.mobile.routes import IndexRoutes
from features.master.mobile.routes import MasterRoutes
from features.notifications.mobile.routes import NotificationsRoutes
from features.profile.mobile.routes import ProfileRoutes
from features.settings.mobile.routes import SettingsRoutes


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
