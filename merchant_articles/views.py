from rest_framework import authentication, generics, mixins, permissions

from merchant_articles.models import MerchantArticle
from .serializers import MerchantArticleSerializer


class MerchantArticleListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MerchantArticleSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = MerchantArticle.objects.all()
        merchant = self.request.query_params.get('merchant')
        if merchant is not None:
            queryset = queryset.filter(merchant=merchant)
        return queryset

    def perform_create(self, serializer):

        serializer.save()
        # send a Django signal


merchant_article_list_create_view = MerchantArticleListCreateAPIView.as_view()


class MerchantArticleDetailAPIView(generics.RetrieveAPIView):
    queryset = MerchantArticle.objects.all()
    serializer_class = MerchantArticleSerializer
    lookup_field = 'pk'


merchant_article_detail_view = MerchantArticleDetailAPIView.as_view()


class MerchantArticleUpdateAPIView(generics.UpdateAPIView):
    queryset = MerchantArticle.objects.all()
    serializer_class = MerchantArticleSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()


merchant_article_update_view = MerchantArticleUpdateAPIView.as_view()


class MerchantArticleDestroyAPIView(generics.DestroyAPIView):
    queryset = MerchantArticle.objects.all()
    serializer_class = MerchantArticleSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


merchant_article_destroy_view = MerchantArticleDestroyAPIView.as_view()
