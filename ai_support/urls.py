from django.urls import path
from . import views


app_name = 'ai_support'
urlpatterns = [
    path('generate_plan_preview/<int:learning_objective_id>', views.GenerateLearningPlanPreviewView.as_view(), name='genereate_plan_preview'),
]
