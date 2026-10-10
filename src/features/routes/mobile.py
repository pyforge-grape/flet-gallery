from features.content.experiment.mobile.routes import ExperimentRoutes
from features.content.gallery.mobile.routes import GalleryRoutes
from features.content.home.mobile.routes import HomeRoutes
from features.content.index.mobile.routes import IndexRoutes
from features.content.master.mobile.routes import MasterRoutes
from features.content.notifications.mobile.routes import NotificationsRoutes
from features.content.profile.mobile.routes import ProfileRoutes
from features.content.settings.mobile.routes import SettingsRoutes


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
