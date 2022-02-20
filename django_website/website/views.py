from django.views.generic import TemplateView

class IndexViews(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt['username'] =''
        return ctxt

class AboutViews(TemplateView):
    template_name = 'about.html'

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt['num_services'] = 12345678
        ctxt['skills'] = [
            'Python',
            'C++',
            'Jabascript',
            'Rust',
            'Go',
        ]
        return ctxt

