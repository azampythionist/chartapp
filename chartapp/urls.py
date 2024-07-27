from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('chart/', views.chart, name='chart'),
    path('set_chart_type/', views.set_chart_type, name='set_chart_type'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
