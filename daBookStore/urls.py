from django.urls import path
from .views import (
    ListCreateView,
    ListUpdateView,
    ListDeleteView
)
from . import views


#This is daBookstore urls

urlpatterns = [
    path("", views.home, name = "checklistHome"),
    path('user/<str:username>', views.UserPostListView, name='userLists'),
    path('checklist/<int:pk>/', views.ChecklistDetailView, name='checklistDetail'),
    path('checklist/new/', ListCreateView.as_view(), name='createNewList'),
    path('checklist/<int:pk>/update/', ListUpdateView.as_view(), name='checklistUpdate'),
    path('checklist/<int:pk>/delete/', ListDeleteView.as_view(), name='checklistDelete'),
    path('about/', views.about, name='checklistAbout'),
]