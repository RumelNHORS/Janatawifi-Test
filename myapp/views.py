from django.shortcuts import render, HttpResponseRedirect
from . models import Customer, JsonModel
from . forms import CustomerRegistrationForm
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
from django.http import JsonResponse

class CustomerAddView(TemplateView):
    template_name = 'myapp/add_show.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = CustomerRegistrationForm()
        cmr = Customer.objects.all()
        context = {'cmr':cmr, 'form':fm}
        return context

    def post(self, request):
        if request.method == 'POST':
            fm = CustomerRegistrationForm(request.POST)
            if fm.is_valid():
                fm.save()
            return HttpResponseRedirect('/')

class CustomerUpdate(View):
    def get(self, request, id):
        up = Customer.objects.get(pk=id)
        fm = CustomerRegistrationForm(instance=up)
        return render(request, 'myapp/update.html', {'form':fm})
    def post(self, request, id):
        up = Customer.objects.get(pk=id)
        fm = CustomerRegistrationForm(request.POST, instance=up)
        if fm.is_valid():
            fm.save()
        return render(request, 'myapp/update.html', {'form':fm})


class CustomerDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        Customer.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)

class JsonView(View):
    def get(self, request):
        data = list(JsonModel.objects.values())
        return JsonResponse(data, safe=False)
