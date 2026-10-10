from features.content.experiment.desktop.routes import ExperimentRoutes
from features.content.gallery.desktop.routes import GalleryRoutes
from features.content.home.desktop.routes import HomeRoutes
from features.content.index.desktop.routes import IndexRoutes
from features.content.master.desktop.routes import MasterRoutes
from features.content.notifications.desktop.routes import NotificationsRoutes
from features.content.profile.desktop.routes import ProfileRoutes
from features.content.settings.desktop.routes import SettingsRoutes


def FeatureRoutes():
    return [
        *IndexRoutes(),
        *ProfileRoutes(),
        *SettingsRoutes(),
        *HomeRoutes(),
        *GalleryRoutes(),
        *NotificationsRoutes(),
        *MasterRoutes(),
        *ExperimentRoutes(),
    ]
