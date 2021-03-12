import json

from flask import Blueprint, request, current_app, Response

from practice.error.invalid_input_error import InvalidInputError
from practice.mapping.score_mapper import ScoreMapper
from practice.model.score_model import ScoreModel
from practice.validation.input_validator import InputValidator

bp = Blueprint('score_controller', __name__, url_prefix='/scores/')
validator = InputValidator()
mapper = ScoreMapper()


def create_response(content, status_code):
    return Response(content, status=status_code, content_type="application/json")


@bp.before_app_first_request
def create_table():
    try:
        ScoreModel.create_table(read_capacity_units=1, write_capacity_units=1)
    except Exception as e:
        current_app.logger.error(e)


@bp.route('player', methods=['GET'])
def get_scores_by_player():
    player_name = request.args.get("playerName")
    try:
        validator.validate_player_name(player_name)
    except InvalidInputError:
        return create_response("Bad Request", 400)

    models = ScoreModel.query(player_name, ScoreModel.high_score > 0)
    json_dicts = []
    for model in models:
        json_dicts.append(mapper.model_to_json(model))

    return create_response(json.dumps(json_dicts), 200)


@bp.route('game', methods=['GET'])
def get_scores_by_game():
    game_name = request.args.get("gameName")

    try:
        validator.validate_game_name(game_name)
    except InvalidInputError:
        return create_response("Bad Request", 400)

    models = ScoreModel.scan(ScoreModel.game_name == game_name)
    json_dicts = []
    for model in models:
        json_dicts.append(mapper.model_to_json(model))

    return create_response(json.dumps(json_dicts), 200)


@bp.route('', methods=['POST'])
def register_score():
    json_data = request.get_json()

    try:
        validator.validate_json(json_data)
    except InvalidInputError:
        return create_response("Bad Request", 400)

    model = mapper.json_to_model(json_data)

    try:
        model.save()
        current_app.logger.info("Score successfully saved")
        return create_response("Success", 200)
    except Exception as e:
        current_app.logger.error(e)
        return create_response("Error", 500)
