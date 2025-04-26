from django.urls import path
from .views.main_view import home,create_blog,single_blog,edit_blog,delete_blog;
from .views.auth_view import register,login

urlpatterns=[
    path("",home,name="home"),
    path("register/",register),
    path("login/",login,name="login"),
    path("create/",create_blog,name="create"),
    path("<int:crud_id>/",single_blog, name='crud_detail'),
    path("<int:crud_id>/edit/",edit_blog, name="crud_edit"),
    path('<int:crud_id>/delete/', delete_blog, name='crud_delete'),



]