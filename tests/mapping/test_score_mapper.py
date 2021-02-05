import unittest

from practice.mapping.score_mapper import ScoreMapper


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
