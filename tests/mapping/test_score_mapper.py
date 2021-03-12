import unittest

from practice.mapping.score_mapper import ScoreMapper
from practice.model.score_model import ScoreModel


class ScoreMapperTest(unittest.TestCase):

    def setUp(self):
        self.mapper = ScoreMapper()

    def test_json_to_model(self):
        json = {
            "highScore": "1000",
            "playerName": "Pat",
            "gameName": "Galaga"
        }

        model = self.mapper.json_to_model(json)

        self.assertEqual(model.high_score, 1000)
        self.assertEqual(model.player_name, "Pat")
        self.assertEqual(model.game_name, "Galaga")

    def test_model_to_json(self):
        model = ScoreModel()
        model.high_score = 1000
        model.player_name = "Pat"
        model.game_name = "Galaga"

        result = self.mapper.model_to_json(model)

        self.assertTrue(result)
        self.assertEqual(result.get("highScore"), "1000")
        self.assertEqual(result.get("playerName"), "Pat")
        self.assertEqual(result.get("gameName"), "Galaga")
