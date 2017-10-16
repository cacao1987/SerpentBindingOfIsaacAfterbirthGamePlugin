from serpent.game import Game

from .api.api import BindingOfIsaacAfterbirthAPI

from serpent.utilities import Singleton


class SerpentBindingOfIsaacAfterbirthGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "steam"

        kwargs["window_name"] = "Binding of Isaac: Afterbirth+"

        kwargs["app_id"] = "250900"
        kwargs["app_args"] = None

        super().__init__(**kwargs)

        self.api_class = BindingOfIsaacAfterbirthAPI
        self.api_instance = None

        self.frame_transformation_pipeline_string = "RESIZE:100x100|GRAYSCALE|FLOAT"

        self.frame_width = 100
        self.frame_height = 100
        self.frame_channels = 0

    @property
    def screen_regions(self):
        regions = dict(
            HUD_HEALTH=(33, 121, 102, 333),
            HUD_COINS=(95, 67, 117, 117),
            HUD_BOMBS=(118, 67, 141, 117),
            HUD_KEYS=(142, 67, 167, 117),
            HUD_ITEM_ACQUIRED=(81, 167, 113, 787),
            HUD_MAP=(32, 800, 125, 910),
            HUD_MAP_CENTER=(71, 845, 85, 861),
            HUD_HEART_1=(12, 84, 32, 106),
            HUD_HEART_2=(12, 108, 32, 130),
            HUD_HEART_3=(12, 132, 32, 154),
            HUD_HEART_4=(12, 156, 32, 178),
            HUD_HEART_5=(12, 180, 32, 202),
            HUD_HEART_6=(12, 204, 32, 226),
            HUD_HEART_7=(32, 84, 52, 106),
            HUD_HEART_8=(32, 108, 52, 130),
            HUD_HEART_9=(32, 132, 52, 154),
            HUD_HEART_10=(32, 156, 52, 178),
            HUD_HEART_11=(32, 180, 52, 202),
            HUD_HEART_12=(32, 204, 52, 226),
            HUD_BOSS_HP=(519, 371, 522, 592),
            HUD_BOSS_SKULL=(496, 340, 529, 373)
        )

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
