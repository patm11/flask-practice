from .model.score import Score

scores = []


def get_scores():
    return scores


def new_score(player_name, high_score, game_name):
    score = Score()
    score.player_name = player_name
    score.high_score = high_score
    score.game_name = game_name

    scores.append(score)
