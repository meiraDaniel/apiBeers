from django.urls import include, path
from rest_framework import routers
from beers import views as beers_views

router = routers.DefaultRouter()
router.register(r'beers', beers_views.BeerList)


urlpatterns = [
    path('', include(router.urls)),
]