from rest_framework import authentication, generics, mixins, permissions, serializers

from warehouse_articles.models import WarehouseArticle
from .serializers import WarehouseArticleSerializer


class WarehouseArticleListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = WarehouseArticleSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = WarehouseArticle.objects.all()
        warehouse = self.request.query_params.get('warehouse')

        if warehouse is not None:
            queryset = queryset.filter(warehouse=warehouse)
        return queryset

    def perform_create(self, serializer):
        serializer.save()
        # send a Django signal


warehouse_article_list_create_view = WarehouseArticleListCreateAPIView.as_view()


class WarehouseArticleDetailByQueryParamsAPIView(generics.RetrieveAPIView):
    serializer_class = WarehouseArticleSerializer

    def get_object(self):
        queryset = WarehouseArticle.objects.all()
        warehouse = self.request.query_params.get('warehouse')
        article = self.request.query_params.get('article')
        regal = self.request.query_params.get('regal')
        regal_position = self.request.query_params.get('regal_position')

        if warehouse is not None and article is not None and regal is not None and regal_position is not None:
            queryset = queryset.get(
                warehouse=warehouse, article=article, regal=regal, regal_position=regal_position)
            return queryset

        raise serializers.ValidationError(
            "Expected query params not provided",
        )


warehouse_article_detail_by_query_params_view = WarehouseArticleDetailByQueryParamsAPIView.as_view()


class WarehouseArticleDetailAPIView(generics.RetrieveAPIView):
    queryset = WarehouseArticle.objects.all()
    serializer_class = WarehouseArticleSerializer
    lookup_field = 'pk'


warehouse_article_detail_view = WarehouseArticleDetailAPIView.as_view()


class WarehouseArticleUpdateAPIView(generics.UpdateAPIView):
    queryset = WarehouseArticle.objects.all()
    serializer_class = WarehouseArticleSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()


warehouse_article_update_view = WarehouseArticleUpdateAPIView.as_view()


class WarehouseArticleDestroyAPIView(generics.DestroyAPIView):
    queryset = WarehouseArticle.objects.all()
    serializer_class = WarehouseArticleSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


warehouse_article_destroy_view = WarehouseArticleDestroyAPIView.as_view()
