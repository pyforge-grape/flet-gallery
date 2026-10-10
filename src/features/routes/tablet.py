from features.content.experiment.tablet.routes import ExperimentRoutes
from features.content.gallery.tablet.routes import GalleryRoutes
from features.content.home.tablet.routes import HomeRoutes
from features.content.index.tablet.routes import IndexRoutes
from features.content.master.tablet.routes import MasterRoutes
from features.content.notifications.tablet.routes import NotificationsRoutes
from features.content.profile.tablet.routes import ProfileRoutes
from features.content.settings.tablet.routes import SettingsRoutes


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
