from django.urls import include, path
from utilities.urls import get_model_urls

from . import views

urlpatterns = (
    # Access lists
    path(
        'access-lists/',
        include(get_model_urls('netbox_access_lists', 'accesslist', detail=False)),
    ),
    path(
        'access-lists/<int:pk>/',
        include(get_model_urls('netbox_access_lists', 'accesslist')),
    ),

    # Access list rules
    path(
        'rules/',
        include(get_model_urls('netbox_access_lists', 'accesslistrule', detail=False)),
    ),
    path(
        'rules/<int:pk>/',
        include(get_model_urls('netbox_access_lists', 'accesslistrule')),
    ),
)
