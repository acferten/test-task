from rest_framework import generics
from .models import Product, Cart
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer, CartSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        products = Product.objects.all().values()

        return Response({"data:": list(products)})


class CartApiView(APIView):
    def post(self, request, pk):
        product_id = Product.objects.get(pk=pk)
        new_item = Cart.objects.create(
            product=product_id,
            user=self.request.user
        )
        return Response({"data:": ({"message:": "Product add to the cart"})})


class CartAPIList(generics.ListAPIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Cart.objects.filter(user=user)
