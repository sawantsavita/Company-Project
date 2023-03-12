"""company_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name = 'home'),
    path('show/', views.show_company, name = "show_company"),
    path('single-record/<int:id>/', views.single_company, name = "single_company"),
    path('show-second-db/', views.show_company_second_db, name = "show_company_second_db"),
    path('single-record-second-db/<int:id>/', views.single_company_second_db, name = "single_company_second_db"),
    path('update/<int:id>/', views.update, name = "update"),
    path('harddelete/<int:id>/', views.hard_delete, name = "hard_delete"),
    path('softdelete/<int:id>/', views.soft_delete, name = "soft_delete"),
    path('restore/<int:id>/', views.restore, name="restore"),
    path('inactivecompany/', views.show_inactive_company, name="show_inactive_company"),
    # path('register/', views.register, name = "register"),
    path('register/', user_views.register_request, name = "register"),
    path("login/", user_views.login_request, name="login_user"),   
    path("logout/", user_views.logout_request, name="logout_user"), 
    path("get-all-student/", views.get_all_students),   
     
]
