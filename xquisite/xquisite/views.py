from django.shortcuts import render
from django.views import View

class home(View):
    def get(self, request):
        context = {
            'title': 'Xquisite',
        }
        return render(request, 'home.html', context=context)