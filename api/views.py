from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from api import serializers,models
from rest_framework.parsers import JSONParser
import json

# Create your views here.
@api_view(['POST'])
def InsertCustomerDetails(request):
    body=json.loads(request.body)
    response=serializers.CustomerDetailsSerializer(data=body)

    if response.is_valid():
        result=response.save()
        response=serializers.CustomerDetailsSerializer(result)
        return Response(response.data)
 
    return Response(response.errors)

@api_view()
def FetchCustomerDetails(request, Id):
    customerDetails = models.CustomerDetails.objects.get(customerId = Id)
    response = serializers.CustomerDetailsSerializer(customerDetails)
    return Response(response.data)
