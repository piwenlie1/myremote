from django.shortcuts import render
from django.views import View
from django.http import HttpRequest,HttpResponse
# Create your views here.
class SetSession(View):
    def get(self,request):
        request.session['name'] = 'pwl'
        return  HttpResponse('ABC')

class LoginView(View):
    def get(self,request):

        return render(request,'login.html')
        return HttpResponse('get')

    def post(self, request):
        return HttpResponse('post')