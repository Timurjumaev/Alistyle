from django.shortcuts import render, redirect
from django.views import View

from .models import *


class HomeIndex2View(View):
    def get(self, request):
        data={
            'bolimlar': Bolim.objects.all()[:6]
        }
        return render(request, 'page-index-2.html', data)


class HomeIndex(View):

    def get(self, request):
        if request.user.is_authenticated:
            data={
                'bolimlar': Bolim.objects.all()[:6],
                'davomi': Bolim.objects.all()[6:]
            }
            return render(request, 'page-index.html', data)
        return redirect('/user/login/')

class BolimlarView(View):
    def get(selfself, request):
        data={
           'bolimlar': Bolim.objects.all()
        }
        return render(request, 'page-category.html', data)

class ListingGridView(View):
    def get(self,request, son):
        mahsulotlar=Mahsulot.objects.filter(ichki__id=son)
        data={
            'mahsulotlar': mahsulotlar
        }
        return render(request,'page-listing-grid.html', data)

class DetailProductView(View):
    def get(self,request, son):
        data={
            'mahsulot': Mahsulot.objects.get(id=son)
        }
        return render(request,'page-detail-product.html', data)

class IchkiView(View):
    def get(self, request, nom):
        data={
            'bolim': Bolim.objects.get(nom=nom),
            'ichkilar': Ichki.objects.filter(bolim__nom=nom)
        }
        return render(request, 'ichki.html', data)
