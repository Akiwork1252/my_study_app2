from django.contrib import admin

from .models import CustomUser
from ascension.models import Category, InterestCategory, UserInterest, LearningObjective, LearningMainTopic, LearningSubTopic
from analytics.models import Progress


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(InterestCategory)
admin.site.register(UserInterest)
admin.site.register(LearningObjective)
admin.site.register(LearningMainTopic)
admin.site.register(LearningSubTopic)
admin.site.register(Progress)
