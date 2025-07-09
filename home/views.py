from django.shortcuts import render
from django.views.generic import TemplateView
from config.home.text_constants import COMPANY_INTRODUCTION


class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["company_introduction"] = COMPANY_INTRODUCTION
        return context
