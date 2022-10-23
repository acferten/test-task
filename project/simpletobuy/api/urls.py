from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, )

urlpatterns = [
    path('signup', SignUpView.as_view(), name="signup"),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout', LogoutView.as_view(), name='auth_logout'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    path('products', ProductListView.as_view(), name="products"),
    path('product', CreateProductView.as_view(), name="product"),
    path('product/<int:pk>', DeleteUpdateProductView.as_view()),

    path('cart/', CartListView.as_view(), name="cart"),
    path('cart/<int:pk>', CartCreateDeleteView.as_view(), name="add_cart"),
]
