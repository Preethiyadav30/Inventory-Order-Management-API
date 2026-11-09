
from rest_framework import serializers
from django.db import transaction
from customers.models import Customer
from products.models import products
from .models import Order, OrderItem


class OrderItemInputSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=products.objects.all()
    )
    quantity = serializers.IntegerField(min_value=1)


class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemInputSerializer(many=True)

    class Meta:
        model = Order
        fields = ['customer', 'items']

    @transaction.atomic # if you used @transaction.atomic, Django rolls back the database changes made during that transaction.Think of it like Ctrl + Z: If something goes wrong, undo the changes made in that transaction.
    def create(self, validated_data):
        items_data = validated_data.pop('items')

        order = Order.objects.create(
            customer=validated_data['customer']
        )

        total = 0

        for item in items_data:
            product = products.objects.select_for_update().get(
                pk=item['product'].pk
            )

            quantity = item['quantity']

            if product.stock < quantity:
                raise serializers.ValidationError(
                    f"Not enough stock for {product.name}. "
                    f"Available stock: {product.stock}"
                )

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )

            product.stock -= quantity
            product.save()

            total += product.price * quantity # total = total + (product.price * quantity)

        order.total_amount = total
        order.save()

        return order


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
