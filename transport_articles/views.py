from rest_framework import authentication, generics, mixins, permissions

from transport_articles.models import TransportArticle
from .serializers import TransportArticleSerializer, TransportArticleListSerializer


class TransportArticleListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TransportArticleSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TransportArticleListSerializer
        return TransportArticleSerializer

    def get_queryset(self):
        queryset = TransportArticle.objects.all()
        transport_order_article = self.request.query_params.get(
            'transport_order_article')
        if transport_order_article is not None:
            queryset = queryset.filter(
                transport_order_article=transport_order_article)
        return queryset

    def perform_create(self, serializer):
        # warehouse = serializer.validated_data.get('warehouse')
        # regal = serializer.validated_data.get('regal')
        # regal_position = serializer.validated_data.get('regal_position')

        # print(serializer)
        # return
        serializer.save()
        # send a Django signal


transport_article_list_create_view = TransportArticleListCreateAPIView.as_view()


class TransportArticleDetailAPIView(generics.RetrieveAPIView):
    queryset = TransportArticle.objects.all()
    serializer_class = TransportArticleSerializer
    lookup_field = 'pk'


transport_article_detail_view = TransportArticleDetailAPIView.as_view()


class TransportArticleUpdateAPIView(generics.UpdateAPIView):
    queryset = TransportArticle.objects.all()
    serializer_class = TransportArticleSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()


transport_article_update_view = TransportArticleUpdateAPIView.as_view()


class TransportArticleDestroyAPIView(generics.DestroyAPIView):
    queryset = TransportArticle.objects.all()
    serializer_class = TransportArticleSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


transport_article_destroy_view = TransportArticleDestroyAPIView.as_view()
