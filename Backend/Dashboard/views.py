from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Dashboard.models import Parta,Partb
from Dashboard.serializers import PartaSerializer,PartbSerializer

from django.core.files.storage import default_storage

# Create your views here.

# Create your views here.
@csrf_exempt
def partaApi(request,id=0):
    if request.method=='GET':
        parta = Parta.objects.all()
        parta_serializer = PartaSerializer(parta, many=True)
        return JsonResponse(parta_serializer.data, safe=False)

    elif request.method=='POST':
        parta_data=JSONParser().parse(request)
        parta_serializer = PartaSerializer(data=parta_data)
        if parta_serializer.is_valid():
            parta_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        parta_data = JSONParser().parse(request)
        parta=Parta.objects.get(PartaId=parta_data['PartaId'])
        parta_serializer=PartaSerializer(parta,data=parta_data)
        if parta_serializer.is_valid():
            parta_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        parta=Parta.objects.get(PartaId=id)
        parta.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
    
@csrf_exempt
def partbApi(request,id=0):
    if request.method=='GET':
        partb = Partb.objects.all()
        partb_serializer = PartbSerializer(partb, many=True)
        return JsonResponse(partb_serializer.data, safe=False)

    elif request.method=='POST':
        partb_data=JSONParser().parse(request)
        partb_serializer = PartbSerializer(data=partb_data)
        if partb_serializer.is_valid():
            partb_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        partb_data = JSONParser().parse(request)
        partb=Partb.objects.get(PartbId=partb_data['PartbId'])
        partb_serializer=PartbSerializer(partb,data=partb_data)
        if partb_serializer.is_valid():
            partb_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        partb=Partb.objects.get(PartbId=id)
        partb.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)