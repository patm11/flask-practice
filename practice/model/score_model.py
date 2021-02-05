from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.models import Model


class ScoreModel(Model):

    class Meta:
        table_name = "scores"
        host = "http://dynamodb:8000"
    player_name = UnicodeAttribute(hash_key=True)
    high_score = NumberAttribute(range_key=True)
    game_name = UnicodeAttribute()
