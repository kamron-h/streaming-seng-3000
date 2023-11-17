from django.urls import path, include
from members import views
from streaming import views as streaming_views

urlpatterns = [
    # path('', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register_user/', views.register_user, name='register_user'),
    path('', include(('streaming.urls', 'streaming'), namespace='streaming')),
]
