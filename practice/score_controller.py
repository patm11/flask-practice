from flask import Blueprint, request, current_app

from practice.error.invalid_input_error import InvalidInputError
from practice.mapping.score_mapper import ScoreMapper
from practice.model.score_model import ScoreModel
from practice.validation.input_validator import InputValidator

bp = Blueprint('score_controller', __name__, url_prefix='/scores/')

validator = InputValidator()
mapper = ScoreMapper()


@bp.before_app_first_request
def create_table():
    try:
        ScoreModel.create_table(read_capacity_units=1, write_capacity_units=1)
    except Exception as e:
        current_app.logger.error(e)


@bp.route('', methods=['GET'])
def get_scores():
    # TODO: make this method actually query dynamodb - more a cheap health endpoint right now
    return str([1, 2, 3])


@bp.route('', methods=['POST'])
def register_score():
    json_data = request.get_json()

    try:
        validator.validate_json(json_data)
    except InvalidInputError:
        return "Bad Request", 400

    model = mapper.json_to_model(json_data)

    try:
        model.save()
        current_app.logger.info("Score successfully saved")
        return "Success", 200
    except Exception as e:
        current_app.logger.error(e)
        return "Error", 500
