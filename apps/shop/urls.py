from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^vacation$', views.vacation_index, name='vacation'),
    url(r'^main$', views.main_index, name='main'),
    url(r'^show/product/(?P<id>\d+)$', views.products.product, name='show_product'),
    url(r'^add/cart/(?P<product_id>\d+)$', views.add_cart, name='add_to_cart'),
    url(r'^show/cart$', views.show_cart, name='show_cart'),
    url(r'^remove/cart/(?P<product_id>\d+)$', views.remove_cart, name='remove_from_cart'),
    url(r'^checkout$', views.checkout, name='checkout'),
    url(r'^checkout/complete$', views.complete, name='complete'),
    url(r'^news$', views.news, name='news'),
    url(r'^filter$', views.search, name='filter'),
    url(r'^shipping_cost$', views.shipping_cost, name="shipping_cost"),
    url(r'^cart_total$', views.get_cart_total, name="cart_total"),
    url(r'^create/order$', views.order_handler, name="order_handler"),
    url(r'^show_email$', views.show_email, name='show_email')
]