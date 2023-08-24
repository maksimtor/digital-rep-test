from django.urls import path

from testing import views

urlpatterns = [
    path('testcases/', views.TestCaseList.as_view()),
    path('testcases/<slug:testcase_slug>/', views.TestCaseDetail.as_view()),
    path('testcases/<slug:testcase_slug>/result/', views.CompletedDetail.as_view()),
    path('completed/', views.CompletedList.as_view()),
]