import unittest

from practice import constants
from practice.error.invalid_input_error import InvalidInputError
from practice.validation.input_validator import InputValidator


class InputValidatorTest(unittest.TestCase):

    def setUp(self):
        self.validator = InputValidator()

    def test_valid_input(self):
        valid_json = {
            "highScore": "1000",
            "playerName": "Pat",
            "gameName": "Galaga"
        }

        self.validator.validate_json(valid_json)

    def test_no_json(self):
        json_input = None

        with self.assertRaises(InvalidInputError) as cm:
            self.validator.validate_json(json_input)

        self.assertEqual(cm.exception.message, constants.JSON_REQD_IN_REQUEST)

    def test_no_high_score(self):
        no_high_score = {
            "playerName": "Pat",
            "gameName": "Galaga"
        }

        with self.assertRaises(InvalidInputError) as cm:
            self.validator.validate_json(no_high_score)

        self.assertEqual(cm.exception.message, constants.JSON_HIGH_SCORE_REQD_MESSAGE)

    def test_invalid_high_score(self):
        invalid_score = {
            "highScore": "blah",
            "playerName": "Pat",
            "gameName": "Galaga"
        }

        with self.assertRaises(InvalidInputError) as cm:
            self.validator.validate_json(invalid_score)

        self.assertEqual(cm.exception.message, constants.JSON_INVALID_HIGH_SCORE_MESSAGE)

    def test_no_player_name(self):
        no_player_name = {
            "highScore": "1000",
            "gameName": "Galaga"
        }

        with self.assertRaises(InvalidInputError) as cm:
            self.validator.validate_json(no_player_name)

        self.assertEqual(cm.exception.message, constants.JSON_PLAYER_NAME_REQD_MESSAGE)

    def test_invalid_player_name(self):
        invalid_player_name = {
            "highScore": "1000",
            "playerName": "<script>window.alert(\\\"got ya\\\")</script>",
            "gameName": "Galaga"
        }

        with self.assertRaises(InvalidInputError) as cm:
            self.validator.validate_json(invalid_player_name)

        self.assertEqual(cm.exception.message, constants.JSON_INVALID_PLAYER_NAME_MESSAGE)

    def test_no_game_name(self):
        no_game_name = {
            "highScore": "1000",
            "playerName": "Pat"
        }

        with self.assertRaises(InvalidInputError) as cm:
            self.validator.validate_json(no_game_name)

        self.assertEqual(cm.exception.message, constants.JSON_GAME_NAME_REQD_MESSAGE)

    def test_invalid_game_name(self):
        invalid_game_name = {
            "highScore": "1000",
            "playerName": "Pat",
            "gameName": "<script>window.alert(\\\"got ya\\\")</script>"
        }

        with self.assertRaises(InvalidInputError) as cm:
            self.validator.validate_json(invalid_game_name)

        self.assertEqual(cm.exception.message, constants.JSON_INVALID_GAME_NAME_MESSAGE)

    def test_game_name_with_space_is_valid(self):
        json_data = {
            "highScore": "1000",
            "playerName": "Pat",
            "gameName": "Halo 2"
        }

        self.validator.validate_json(json_data)
