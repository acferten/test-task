from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import Product, Cart, AdvUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import ProductSerializer, CartSerializer, UserSerializer

"""
Представления продуктов
"""


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        products = Product.objects.all().values()
        return Response({"data:": list(products)})


class CreateProductView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_new = Product.objects.create(
            name=request.data['name'],
            description=request.data['description'],
            price=request.data['price']
        )
        headers = self.get_success_headers(serializer.data)
        return Response({"data:": ({"id": post_new.id, "message:": "Product added"})})


class DeleteUpdateProductView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(({"data:": ({"message:": "Product removed"})}), status=status.HTTP_200_OK)


"""
Представления корзины
"""


class CartCreateDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def post(self, request, pk):
        # if Cart.objects.filter(product=pk).exists():
        #     return Response({"data:": ({"message:": "Product add to the cart"})})
        # else:
        user = request.user
        # pk = Cart.objects.get_or_create(user=user)
        product = Product.objects.get(pk=pk)
        name = product.name
        description = product.description
        price = product.price
        cart_instance = Cart(user=user, product=product, name=name, description=description, price=price)
        cart_instance.save()
        return Response({"data:": ({"message:": "Product add to the cart"})})

    def delete(self, request, pk):
        Cart.objects.filter(user=request.user, id=pk).delete()
        return Response({"data:": ({"message:": "Item removed from cart"})})


class CartListView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)


"""
Аутентификация
"""


class SignUpView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = AdvUser.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        user = AdvUser.objects.get(email=request.data['email'])
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "data": ({"user_token": str(refresh.access_token)})
            }, status=status.HTTP_201_CREATED, headers=headers)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = Response()
        response.delete_cookie('jwt')
        return Response({"data:": ({"message:": "logout"})}, status=status.HTTP_200_OK)
