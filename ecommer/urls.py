from .views import LoginView, DashboardView
from django.urls import path
from . import views
app_name='ecommer'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login-view'),
    path('dashboard/', DashboardView.as_view(), name='dashboard-view'),
    path('user',views.user_dashboard,name='user'),
    path('view/',views.my_view,name='view')
]
