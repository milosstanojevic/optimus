from rest_framework import authentication, generics, mixins, permissions

from transport_orders.models import TransportOrder
from .serializers import TransportOrderSerializer, TransportOrderUpdateSerializer


class TransportOrderListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TransportOrderSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = TransportOrder.objects.all()
        parent = self.request.query_params.get('parent')
        parent_id = self.request.query_params.get('parent_id')
        transport = self.request.query_params.get('transport')
        if transport is not None and parent is not None and parent_id is not None:
            queryset = queryset.filter(
                transport=transport, parent_id=parent_id, parent=parent)
        return queryset

    def perform_create(self, serializer):

        serializer.save()
        # send a Django signal


transport_order_list_create_view = TransportOrderListCreateAPIView.as_view()


class TransportOrderDetailAPIView(generics.RetrieveAPIView):
    queryset = TransportOrder.objects.all()
    serializer_class = TransportOrderSerializer
    lookup_field = 'pk'


transport_order_detail_view = TransportOrderDetailAPIView.as_view()


class TransportOrderUpdateAPIView(generics.UpdateAPIView):
    queryset = TransportOrder.objects.all()
    serializer_class = TransportOrderUpdateSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()


transport_order_update_view = TransportOrderUpdateAPIView.as_view()


class TransportOrderDestroyAPIView(generics.DestroyAPIView):
    queryset = TransportOrder.objects.all()
    serializer_class = TransportOrderSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


transport_order_destroy_view = TransportOrderDestroyAPIView.as_view()
