from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import ProductViewSet, ReviewViewSet, CategoryViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'Review', ReviewViewSet)
router.register(r'Category', CategoryViewSet)
router.register(r'Order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),


]