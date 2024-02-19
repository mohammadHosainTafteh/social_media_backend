from core import BaseModel


class Score(BaseModel):
    pass

    class Meta:
        verbose_name = 'Score'
        verbose_name_plural = 'Scores'
        db_table = 'scores'
