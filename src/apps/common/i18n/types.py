from typing import Literal

Locale = Literal[
    "en-US",
    "ja-JP",
]


TranslationKey = Literal[
    "title",
    "message",
]

Translation = dict[TranslationKey, str]
