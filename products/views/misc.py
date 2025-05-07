from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from products.models import Order
from products.models import Review, Category
from products.serializers import OrderSerializer
from products.serializers import ReviewSerializer, CategorySerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
