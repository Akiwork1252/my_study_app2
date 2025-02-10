from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


# 学習プランを作成
class GenerateLearningPlanPreviewView(LoginRequiredMixin, View):
    pass