from features.experiment.desktop.routes import ExperimentRoutes
from features.gallery.desktop.routes import GalleryRoutes
from features.home.desktop.routes import HomeRoutes
from features.index.desktop.routes import IndexRoutes
from features.master.desktop.routes import MasterRoutes
from features.notifications.desktop.routes import NotificationsRoutes
from features.profile.desktop.routes import ProfileRoutes
from features.settings.desktop.routes import SettingsRoutes


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
