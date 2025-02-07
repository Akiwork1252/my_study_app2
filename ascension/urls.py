from django.urls import path
from . import views


app_name = 'ascension'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('inquiry/', views.InquiryView.as_view(), name='inquiry'),
    path('interest_category_list/', views.InterestCategoryListView.as_view(), name='interest_category_list'),
    path('add_interest_category/', views.AddInterestCategoryView.as_view(), name='add_interest_category'),
    path('delete_interest_category/<int:category_id>/', views.DeleteInterestCategoryView.as_view(), name='delete_interest_category'),
    path('learning_object/category/<int:category_id>/', views.LearningObjectiveListView.as_view(), name='learning_objective_list'),
    path('create_learning_ovjective/<int:category_id>/', views.CreateLearningObjectiveView.as_view(), name='create_learning_objective'),

]
