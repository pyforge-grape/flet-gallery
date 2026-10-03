from features.experiment.mobile.routes import ExperimentRoutes
from features.gallery.mobile.routes import GalleryRoutes
from features.home.mobile.routes import HomeRoutes
from features.index.mobile.routes import IndexRoutes
from features.master.mobile.routes import MasterRoutes
from features.notifications.mobile.routes import NotificationsRoutes
from features.profile.mobile.routes import ProfileRoutes
from features.settings.mobile.routes import SettingsRoutes


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
