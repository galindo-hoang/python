from django.urls import path
from .views import ProductViewSet, UserAPIView

urlpatterns = [
    path('product', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('product/<int:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('user', UserAPIView.as_view())
]
