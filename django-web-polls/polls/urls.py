from django.urls import path
from . import views, question_list, question_details

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('question/', polls_list, name='polls_list'),
    path('question/<int:pk>/', polls_details, name='polls_details'),

]
