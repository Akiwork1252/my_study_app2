from django.db import models
from accounts.models import CustomUser


# 学習管理モデル(興味分野、学習目標、学習Topic(Main、Sub)、＃＝関連付け)
# カテゴリ(カテゴリ名)
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# 興味カテゴリ(カテゴリ名)
class InterestCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# 中間モデル(#ユーザー名、#興味カテゴリ名)
class UserInterest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(InterestCategory, on_delete=models.CASCADE)


# 学習目標(#ユーザー名、#興味カテゴリ名、目標タイトル、設定時レベル、目標詳細、総獲得スコア、状態(完・未完)、作成日時)
class LearningObjective(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(InterestCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    level_when_set = models.CharField(max_length=100, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    total_score = models.IntegerField(blank=True, null=True, default=0)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.title}'
    

# 学習メイントピック(＃学習目標名、メイントピック名)
class LearningMainTopic(models.Model):
    learning_objective = models.ForeignKey(LearningObjective, on_delete=models.CASCADE, related_name='main_topics')
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.learning_objective.title} - {self.title}'
    

# 学習サブトピック(＃学習目標名、＃メイントピック名、サブトピック名)
class LearningSubTopic(models.Model):
    learning_objective = models.ForeignKey(LearningObjective, on_delete=models.CASCADE, related_name='sub_topics')
    main_topic = models.ForeignKey(LearningMainTopic, on_delete=models.CASCADE, related_name='sub_topics')
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.main_topic} - {self.title}'
