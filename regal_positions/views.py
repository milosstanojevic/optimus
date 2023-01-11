from rest_framework import authentication, generics, mixins, permissions

from regal_positions.models import RegalPosition
from .serializers import RegalPositionSerializer


class RegalPositionListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = RegalPositionSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = RegalPosition.objects.all()
        regal = self.request.query_params.get('regal')
        if regal is not None:
            queryset = queryset.filter(regal=regal)
        return queryset

    def perform_create(self, serializer):

        serializer.save()
        # send a Django signal


regal_position_list_create_view = RegalPositionListCreateAPIView.as_view()


class RegalPositionDetailAPIView(generics.RetrieveAPIView):
    queryset = RegalPosition.objects.all()
    serializer_class = RegalPositionSerializer
    lookup_field = 'pk'


regal_position_detail_view = RegalPositionDetailAPIView.as_view()


class RegalPositionUpdateAPIView(generics.UpdateAPIView):
    queryset = RegalPosition.objects.all()
    serializer_class = RegalPositionSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()


regal_position_update_view = RegalPositionUpdateAPIView.as_view()


class RegalPositionDestroyAPIView(generics.DestroyAPIView):
    queryset = RegalPosition.objects.all()
    serializer_class = RegalPositionSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


regal_position_destroy_view = RegalPositionDestroyAPIView.as_view()
