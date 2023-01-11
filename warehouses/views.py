from rest_framework import authentication, generics, mixins, permissions

from warehouses.models import Warehouse
from .serializers import WarehouseSerializer


class WarehouseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):

        serializer.save()
        # send a Django signal


warehouse_list_create_view = WarehouseListCreateAPIView.as_view()


class WarehouseDetailAPIView(generics.RetrieveAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    lookup_field = 'pk'


warehouse_detail_view = WarehouseDetailAPIView.as_view()


class WarehouseUpdateAPIView(generics.UpdateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()


warehouse_update_view = WarehouseUpdateAPIView.as_view()


class WarehouseDestroyAPIView(generics.DestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


warehouse_destroy_view = WarehouseDestroyAPIView.as_view()
