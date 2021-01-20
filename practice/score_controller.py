from flask import Blueprint

bp = Blueprint('score_controller', __name__, url_prefix='/scores/')


# https://flask.palletsprojects.com/en/1.1.x/tutorial/views/
@bp.route('', methods=['GET'])
def get_scores():
    return str([1, 2, 3])


@bp.route('', methods=['POST'])
def register_score():
    pass
