from typing import Literal

Locale = Literal[
    "en-US",
    "ja-JP",
]


TranslationKey = Literal[
    "app.title",
    "profile.link.label",
    "settings.link.label",
    "home.link.label",
    "gallery.link.label",
    "notifications.link.label",
    "master.link.label",
    "experiment.link.label",
]

Translation = dict[TranslationKey, str]
