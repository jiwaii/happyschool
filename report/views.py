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
from report.serializers import PeriodSerializer
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
    filterset_fields = ["period_num", "scholar_year__id"]
    search_fields = ["scholarYear__label"]
