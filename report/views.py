from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from report.models import CotationModel, NoteModel, PeriodModel
from report.serializers import PeriodSerializer, CotationSerializer, NoteSerializer,ResponsibleGivenCourseSerializer,StudentLevelCourseSerializer
from core.models import ResponsibleModel, StudentLevelCourseModel
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
    template_name = "report/menu.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["menu"] = json.dumps(get_menu(self.request, "annuaire"))
        return context


class PeriodViewSet(ModelViewSet):
    queryset = PeriodModel.objects.all()
    serializer_class = PeriodSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["classe_group", "scholar_year__id"]
    search_fields = ["scholarYear__label"]


class CotationViewSet(ModelViewSet):
    queryset = CotationModel.objects.all().order_by("made_date")
    serializer_class = CotationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["given_course"]

class NoteViewSet(ModelViewSet):
    queryset = NoteModel.objects.all().order_by("student_level__student__last_name")
    serializer_class = NoteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["cotation"]


class GivenCourseResponsibleViewSet(APIView):
    def get(self, request, matricule=None):
        responsible = ResponsibleModel.objects.get(matricule=matricule)
        serializer = ResponsibleGivenCourseSerializer(responsible) 
        return Response(serializer.data)
        
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["id"]
    
class StudentLevelCoursViewSet(ModelViewSet):
    queryset = StudentLevelCourseModel.objects.all()
    serializer_class = StudentLevelCourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["course"]
