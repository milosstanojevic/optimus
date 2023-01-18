from django.contrib import admin
from django.urls import path, include
import oauth2_provider.views as oauth2_views
from django.conf import settings

# OAuth2 provider endpoints
oauth2_endpoint_views = [
    path('authorize/', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    path('token/', oauth2_views.TokenView.as_view(), name="token"),
    path('revoke-token/', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]

if settings.DEBUG:
    # OAuth2 Application Management endpoints
    oauth2_endpoint_views += [
        path('applications/', oauth2_views.ApplicationList.as_view(), name="list"),
        path('applications/register/',
             oauth2_views.ApplicationRegistration.as_view(), name="register"),
        path('applications/<pk>/',
             oauth2_views.ApplicationDetail.as_view(), name="detail"),
        path('applications/<pk>/delete/',
             oauth2_views.ApplicationDelete.as_view(), name="delete"),
        path('applications/<pk>/update/',
             oauth2_views.ApplicationUpdate.as_view(), name="update"),
    ]

    # OAuth2 Token Management endpoints
    oauth2_endpoint_views += [
        path('authorized-tokens/', oauth2_views.AuthorizedTokensListView.as_view(),
             name="authorized-token-list"),
        path('authorized-tokens/<pk>/delete/', oauth2_views.AuthorizedTokenDeleteView.as_view(),
             name="authorized-token-delete"),
    ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include((oauth2_endpoint_views, 'oauth2_provider'),
         namespace="oauth2_provider")),
    path('api/warehouses/', include('warehouses.urls')),
    path('api/merchants/', include('merchants.urls')),
    path('api/articles/', include('articles.urls')),
    path('api/regals/', include('regals.urls')),
    path('api/regal-positions/', include('regal_positions.urls')),
    path('api/warehouse-articles/', include('warehouse_articles.urls')),
    path('api/merchant-articles/', include('merchant_articles.urls')),
    path('api/transports/', include('transports.urls')),
    path('api/transport-orders/', include('transport_orders.urls')),
    path('api/transport-order-articles/',
         include('transport_order_articles.urls')),
    path('api/transport-articles/', include('transport_articles.urls')),
    path('api/users/', include('users.urls')),
]
