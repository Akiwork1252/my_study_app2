from django.db import models

from accounts.models import CustomUser
from ascension.models import InterestCategory, LearningObjective, LearningMainTopic, LearningSubTopic


#　学習進捗管理モデル(＃ユーザー名、＃学習目標名、＃学習サブTopic、スコア、日付)
class Progress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    learning_objective = models.ForeignKey(LearningObjective, on_delete=models.CASCADE)
    sub_topic = models.ForeignKey(LearningSubTopic, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.sub_topic.title} - {self.score}'
