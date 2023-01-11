from rest_framework import authentication, generics, mixins, permissions

from transport_order_articles.models import TransportOrderArticle
from .serializers import TransportOrderArticleSerializer, TransportOrderArticleStockSerializer


class TransportOrderArticleListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TransportOrderArticleSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = TransportOrderArticle.objects.all()
        transport_order = self.request.query_params.get('transport_order')
        if transport_order is not None:
            queryset = queryset.filter(transport_order=transport_order)
        return queryset

    def perform_create(self, serializer):

        serializer.save()
        # send a Django signal


transport_order_article_list_create_view = TransportOrderArticleListCreateAPIView.as_view()


class TransportOrderArticleDetailAPIView(generics.RetrieveAPIView):
    queryset = TransportOrderArticle.objects.all()
    serializer_class = TransportOrderArticleSerializer
    lookup_field = 'pk'


transport_order_article_detail_view = TransportOrderArticleDetailAPIView.as_view()


class TransportOrderArticleUpdateAPIView(generics.UpdateAPIView):
    queryset = TransportOrderArticle.objects.all()
    serializer_class = TransportOrderArticleSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()


transport_order_article_update_view = TransportOrderArticleUpdateAPIView.as_view()

class TransportOrderArticleAddToStockAPIView(generics.UpdateAPIView):
    queryset = TransportOrderArticle.objects.all()
    serializer_class = TransportOrderArticleStockSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()


transport_order_article_add_to_stock_view = TransportOrderArticleAddToStockAPIView.as_view()


class TransportOrderArticleDestroyAPIView(generics.DestroyAPIView):
    queryset = TransportOrderArticle.objects.all()
    serializer_class = TransportOrderArticleSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


transport_order_article_destroy_view = TransportOrderArticleDestroyAPIView.as_view()
