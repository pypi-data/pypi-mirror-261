from django.http import HttpResponse
from django.views.generic import DetailView

from djangoaddicts.htmxify.mixins import HtmxViewMixin


class HtmxOptionalDetailView(HtmxViewMixin, DetailView):
    template_name = None 
    htmx_template_name = None 
    
    def get(self, request, *args, **kwargs):
        """ if request is htmx, use htmx_template_name if available, otherwise use the template_name"""
        if self.is_htmx():
            if self.htmx_template_name:
                self.template_name = self.htmx_template_name
        return super().get(request, *args, **kwargs)


class HtmxDetailView(HtmxViewMixin, DetailView):
    def get(self, request, *args, **kwargs):
        if not self.is_htmx():
            return HttpResponse("Invalid request", status=400)
        return super().get(request, *args, **kwargs)
