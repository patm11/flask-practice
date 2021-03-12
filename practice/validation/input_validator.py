from string_utils import contains_html

from practice import constants
from practice.error.invalid_input_error import InvalidInputError


class InputValidator:

    def validate_game_name(self, game_name):
        if not game_name:
            raise InvalidInputError(constants.JSON_GAME_NAME_REQD_MESSAGE)
        elif contains_html(game_name):
            raise InvalidInputError(constants.JSON_INVALID_GAME_NAME_MESSAGE)

    def validate_player_name(self, player_name):
        if not player_name:
            raise InvalidInputError(constants.JSON_PLAYER_NAME_REQD_MESSAGE)
        elif not player_name.isalnum():
            raise InvalidInputError(constants.JSON_INVALID_PLAYER_NAME_MESSAGE)

    def validate_json(self, json_data):

        if not json_data:
            raise InvalidInputError(constants.JSON_REQD_IN_REQUEST)

        high_score = json_data.get(constants.JSON_HIGH_SCORE_FIELD)
        if not high_score:
            raise InvalidInputError(constants.JSON_HIGH_SCORE_REQD_MESSAGE)
        elif not high_score.isnumeric():
            raise InvalidInputError(constants.JSON_INVALID_HIGH_SCORE_MESSAGE)

        player_name = json_data.get(constants.JSON_PLAYER_NAME_FIELD)
        self.validate_player_name(player_name)

        game_name = json_data.get(constants.JSON_GAME_NAME_FIELD)
        self.validate_game_name(game_name)
