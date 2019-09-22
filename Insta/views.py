from django.views.generic import TemplateView

# Helloworld is-a TemplateView (inheritance)
class Helloworld(TemplateView):
    template_name = 'test.html'