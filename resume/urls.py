from django.urls import path
from . import views


app_name = 'resume'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/detials/',views.ResumeView.as_view(),name = 'detials'),
    path('resume_form/', views.ResumeForm.as_view(), name = 'resume_form'),
]