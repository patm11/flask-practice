from practice.model.score_model import ScoreModel


class ScoreMapper:

    def json_to_model(self, json_data):
        model = ScoreModel()
        model.high_score = int(json_data["highScore"])
        model.player_name = json_data["playerName"]
        model.game_name = json_data["gameName"]

        return model

    def model_to_json(self, model):
        json_dict = {
            "highScore": str(model.high_score),
            "playerName": model.player_name,
            "gameName": model.game_name
        }

        return json_dict
