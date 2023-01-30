from .models import Product
from .serializers import shopSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def shopListApi(request):
    all_shops = Product.objects.all()
    data = shopSerializer(all_shops,many=True).data
    return Response(data)

@api_view(['GET'])
def shopDetailApi(request,id):
    shop_detail = Product.objects.get(id=id)
    data = shopSerializer(shop_detail).data
    return Response(data)

class shop_ist_api(generics.ListCreateAPIView):
    model = Product
    queryset = Product.objects.all()
    serializer_class = shopSerializer

class shop_detail_api(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = shopSerializer
        queryset = Product.objects.all()
        lookup_field = 'id'