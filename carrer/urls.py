from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('alljobs/', views.main, name='jobs'),
    path('job/', views.getJob.as_view(), name='get-job'),
    path('jobs/', views.jobsPgae, name='job-page'),
    path('getAllJobs/', views.getAllJobs.as_view(), name='getAllJobs'),
    # path('filter/', views.filteForm.as_view(), name='filter'),
    path('application/', views.ApplicationView.as_view(), name='ApplicationView'),
    
]