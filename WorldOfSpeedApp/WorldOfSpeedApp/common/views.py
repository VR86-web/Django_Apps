from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = 'common/index.html'



