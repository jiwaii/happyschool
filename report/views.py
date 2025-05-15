from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from report.models import *
from report.serializers import *
import json
from core.utilities import get_menu


# Create your views here.
def get_menu_entry(active_app, request):
    return {
        "app": "report",
        "display": "Bulletin",
        "url": "/report/",
        "active": active_app == "report",
    }


class ReportMenuView(TemplateView):
    # context = {
    #     "test":"ceci est mon test"
    # }
    template_name = "report/menu.html"
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['menu'] = json.dumps(get_menu(self.request, "annuaire"))
        # context['test'] = "ceci est mon test"
        return context

#USING api_views and Response
# @csrf_exempt
@api_view(['GET','POST'])
def scholarYear_list(request):
    if request.method == 'GET':
        scholarYears = ScholarYear.objects.all()
        serializer = ScholaryearSerializer(scholarYears,many=True)
        # return JsonResponse(serializer.data,safe=False)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # data =JSONParser().parse(request)
        # serializer = ScholaryearSerializer(data=data)
        print(request.data)
        serializer = ScholaryearSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        #     return JsonResponse(serializer.data,status=201)
        # return JsonResponse(serializer.errors, status=400)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#using Class-based Views
class ScholarYearDetail(APIView):
    def get_object(self, pk):
        try:
            return ScholarYear.objects.get(pk=pk)
        except ScholarYear.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        scholarYear = self.get_object(pk)
        serializer = ScholaryearSerializer(scholarYear)
        return Response(serializer.data)

    def put(self, request, pk,format=None):
        scholarYear = self.get_object(pk)
        serializer = ScholaryearSerializer(scholarYear,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk,format=None):
        scholarYear = self.get_object(pk)
        scholarYear.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# class ScholarYearValidation(APIView):
#     def get(self,request):
#         scholarYear = ScholarYear.objects.filter(label = "2024-2025")
#         serializer = ScholaryearSerializer(scholarYear, many=True)
#         return Response(serializer.data)

class ScholaryearValidation(ModelViewSet):
    queryset = ScholarYear.objects.all()
    serializer_class = ScholaryearSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['label']
    
class Period(ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['periodNum']
    
    
    
    # def post(self,request,format=None):
    #     print("REQUEST DATA :")
    #     print(request.data)
    #     print(request.data.get("label"))
    #     scholarYear = ScholarYear.objects.filter(label = request.data.get("label"))
    #     exist = ScholarYear.objects.filter(label = request.data.get("label")).exists()
    #     print(exist)
        
    #     serializer = ScholaryearSerializer(scholarYear,many=True)
    #     return Response(serializer.data)

# @csrf_exempt
# def scholarYear_detail(request,pk):
#     try:
#         scholarYear = ScholarYear.objects.get(pk=pk)
#     except ScholarYear.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serializer = ScholaryearSerializer(scholarYear)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ScholaryearSerializer(scholarYear,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         scholarYear.delete()
#         return HttpResponse(status=204)