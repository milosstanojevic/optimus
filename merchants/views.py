from rest_framework import authentication, generics, mixins, permissions

from merchants.models import Merchant
from .serializers import MerchantSerializer


class MerchantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):

        serializer.save()
        # send a Django signal


merchant_list_create_view = MerchantListCreateAPIView.as_view()


class MerchantDetailAPIView(generics.RetrieveAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    lookup_field = 'pk'


merchant_detail_view = MerchantDetailAPIView.as_view()


class MerchantUpdateAPIView(generics.UpdateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()


merchant_update_view = MerchantUpdateAPIView.as_view()


class MerchantDestroyAPIView(generics.DestroyAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


merchant_destroy_view = MerchantDestroyAPIView.as_view()
