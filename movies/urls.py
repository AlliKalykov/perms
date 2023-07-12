from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'saloon', views.SaloonViewSet)
router.register(r'ticket', views.TicketViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    path('movie/', views.ListCreateMovieAPIView.as_view(), name='get_post_movies'),
    path('movie/<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
]