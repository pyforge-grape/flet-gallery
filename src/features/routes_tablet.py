from features.experiment.tablet.routes import ExperimentRoutes
from features.gallery.tablet.routes import GalleryRoutes
from features.home.tablet.routes import HomeRoutes
from features.index.tablet.routes import IndexRoutes
from features.master.tablet.routes import MasterRoutes
from features.notifications.tablet.routes import NotificationsRoutes
from features.profile.tablet.routes import ProfileRoutes
from features.settings.tablet.routes import SettingsRoutes


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
