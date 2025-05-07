from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from products.models import Order, Product




class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'product', 'customer', 'quantity', 'created_at', 'total_price', 'phone_number', 'is_paid']

    def get_total_price(self, obj):
        """Mahsulod narhini hisoblaydi"""
        return obj.product.price * obj.quantity

    def validate_quantity(self, value):
        """Mahsulod miqdorini tekshiradi"""
        try:
            # Buyurtma qilingan mahsulotni olish
            product_id = self.initial_data['product']
            product = Product.objects.get(id=product_id)

            # Omborda yetarli mahsulot bor yoki yo‘qligini tekshirish
            if value > product.stock:
                raise serializers.ValidationError("Not enough items in stock.")

            if value < 1:
                raise serializers.ValidationError("Quantity must be at least 1.")

            return value

        except ObjectDoesNotExist:
            raise serializers.ValidationError("Product does not exist")

    def create(self, validated_data):
        """Buyurtma yaratadi va ombordagi mahsulodni kamaytiradi"""
        order = Order.objects.create(**validated_data)
        product = order.product
        product.stock -= order.quantity
        product.save()
        self.send_confirmation_email(order)
        return order

    def send_confirmation_email(self, order):
        """bu yerda User emailga malumod jonatish mumkin"""

        print(f"Sent confirmation email for Order {order.id}")