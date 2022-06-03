from django.urls import path,include
from testapp import views
urlpatterns = [
    path('user/', views.user_views),
    
]
