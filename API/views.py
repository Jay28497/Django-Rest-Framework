from API.models import ProductTBL
from API.serializers import ProductSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def products_list(request):
    if request.method == 'GET':
        products = ProductTBL.objects.all()

        product_name = request.GET.get('product_name', None)
        if product_name is not None:
            products = products.filter(product_name__icontains=product_name)

        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)

    elif request.method == 'POST':
        products_data = JSONParser().parse(request)
        products_serializer = ProductSerializer(data=products_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse(products_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(products_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = ProductTBL.objects.all().delete()
        return JsonResponse({'message': '{} Products were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def products_detail(request, pk):
    try:
        products = ProductTBL.objects.get(pk=pk)
    except ProductTBL.DoesNotExist:
        return JsonResponse({'message': 'The products does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        products_serializer = ProductSerializer(products)
        return JsonResponse(products_serializer.data)

    elif request.method == 'PUT':
        products_data = JSONParser().parse(request)
        products_serializer = ProductSerializer(products, data=products_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse(products_serializer.data)
        return JsonResponse(products_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        products.delete()
        return JsonResponse({'message': 'Products was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def products_list_published(request):
    products = ProductTBL.objects.filter(published=True)

    if request.method == 'GET':
        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)
