from django.urls import path
from .views import TaskList,TaskDetailView,TaskCreate,TaskUpdate,DeleteView,CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns =[
      path('login/',CustomLoginView.as_view(),name='login'),
      path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
      path('register/',RegisterPage.as_view(),name='register'),
      
      path('',TaskList.as_view(),name='tasks'),
      path('task/<int:pk>/',TaskDetailView.as_view(),name='task'),
      path('create-task/',TaskCreate.as_view(),name='create-task'),
      path('update-task/<int:pk>/',TaskUpdate.as_view(),name='update-task'),
      path('delete-task/<int:pk>/', DeleteView.as_view(),name='delete-task')
]