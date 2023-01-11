from rest_framework import authentication, generics, mixins, permissions

from regals.models import Regal
from .serializers import RegalSerializer


class RegalListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = RegalSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Regal.objects.all()
        warehouse = self.request.query_params.get('warehouse')
        if warehouse is not None:
            queryset = queryset.filter(warehouse=warehouse)
        return queryset

    def perform_create(self, serializer):

        serializer.save()
        # send a Django signal


regal_list_create_view = RegalListCreateAPIView.as_view()


class RegalDetailAPIView(generics.RetrieveAPIView):
    queryset = Regal.objects.all()
    serializer_class = RegalSerializer
    lookup_field = 'pk'


regal_detail_view = RegalDetailAPIView.as_view()


class RegalUpdateAPIView(generics.UpdateAPIView):
    queryset = Regal.objects.all()
    serializer_class = RegalSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()


regal_update_view = RegalUpdateAPIView.as_view()


class RegalDestroyAPIView(generics.DestroyAPIView):
    queryset = Regal.objects.all()
    serializer_class = RegalSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


regal_destroy_view = RegalDestroyAPIView.as_view()
