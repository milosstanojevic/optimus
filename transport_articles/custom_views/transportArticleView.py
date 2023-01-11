from rest_framework import authentication, generics, mixins, permissions, serializers
from warehouses.models import Warehouse
from warehouse_articles.models import WarehouseArticle
from regals.models import Regal
from regal_positions.models import RegalPosition


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'name']


class TransportArticleOptionsListAPIView(generics.ListAPIView):
    serializer_class = WarehouseSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Warehouse.objects.all()

        article_type = self.request.query_params.get(
            'type')
        article_id = self.request.query_params.get(
            'article_id')

        if article_type is None or article_id is None:
            raise serializers.ValidationError(
                "Expected query params not provided",
            )

        if article_type == 'warehouse':
            warehouse_ids = WarehouseArticle.objects.filter(
                article=article_id).order_by().values('warehouse_id').distinct()
            queryset = Warehouse.objects.filter(
                id__in=warehouse_ids).values('id', 'name')

        if article_type == 'regal':
            warehouse_id = self.request.query_params.get('warehouse_id')
            regal_ids = WarehouseArticle.objects.filter(
                article=article_id, warehouse=warehouse_id).order_by().values('regal_id').distinct()

            queryset = Regal.objects.filter(
                id__in=regal_ids).values('id', 'name')

        if article_type == 'regal_position':
            warehouse_id = self.request.query_params.get('warehouse_id')
            regal_id = self.request.query_params.get('regal_id')
            regal_p_ids = WarehouseArticle.objects.filter(
                article=article_id, warehouse=warehouse_id, regal=regal_id).order_by().values('regal_position_id').distinct()

            queryset = RegalPosition.objects.filter(
                id__in=regal_p_ids).values('id', 'name')

        return queryset


transport_article_options_list_view = TransportArticleOptionsListAPIView.as_view()
