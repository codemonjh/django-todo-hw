
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='Todolist'

urlpatterns = [
    path('',views.lists,name='lists'),
    path('<int:todo_id>/',views.detail,name='detail'),
    path('writing/',views.writing,name='writing'),
    path('login/',auth_views.LoginView.as_view(), name='log_in'),
    path('logout/', auth_views.LogoutView.as_view(), name='log_out'),
    path('signup/', views.signup, name='signup'),
]

