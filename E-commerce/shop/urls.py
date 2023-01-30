from django.urls import path
from .  import views ,api
app_name='shop'
app_name='checkout'
urlpatterns = [
    path('',views.shop_list,name='shop_list'),
    path('',views.shop_category),
    path('all_shop',views.all_shops,name='all_shops'),
    path('checkout',views.checkout,name='checkout'),
    path('<str:slug>',views.shop_detaile,name='shop_detail'),
    ## api ###
    path('api/list',api.shopListApi,name='shoplistapi'),
    path('api/list/<int:id>',api.shopDetailApi,name='shoplistapi'),
 ## api classe based view ###
    path('api/v2/list',api.shop_ist_api.as_view(),name='shop_ist_api'),
    path('api/v2/list/<int:id>',api.shop_detail_api.as_view(),name='shoplistapi'),
] 