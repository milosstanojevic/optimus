from rest_framework import authentication, generics, mixins, permissions

from transports.models import Transport
from .serializers import TransportSerializer


class TransportListCreateAPIView(generics.ListCreateAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):

        serializer.save()
        # send a Django signal


transport_list_create_view = TransportListCreateAPIView.as_view()


class TransportDetailAPIView(generics.RetrieveAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    lookup_field = 'pk'


transport_detail_view = TransportDetailAPIView.as_view()


class TransportUpdateAPIView(generics.UpdateAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()


transport_update_view = TransportUpdateAPIView.as_view()


class TransportDestroyAPIView(generics.DestroyAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


transport_destroy_view = TransportDestroyAPIView.as_view()
