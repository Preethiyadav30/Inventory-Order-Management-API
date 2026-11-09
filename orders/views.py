from django.shortcuts import render

# Create your views here.

from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import Order
from .serializers import OrderCreateSerializer, OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().prefetch_related('items')
    serializer_class = OrderSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        return OrderSerializer

    @action(detail=True, methods=['post'])
    @transaction.atomic
    def cancel(self, request, pk=None):
        order = Order.objects.select_for_update().get(pk=pk)

        if order.status == 'Cancelled':
            raise ValidationError("This order is already cancelled.")

        if order.status == 'Completed':
            raise ValidationError("A completed order cannot be cancelled.")

        for item in order.items.all():
            product = item.product
            product.stock += item.quantity
            product.save()

        order.status = 'Cancelled'
        order.save()

        return Response(
            {
                'message': 'Order cancelled successfully.',
                'order_id': order.id,
                'status': order.status
            },
            status=status.HTTP_200_OK
        )
