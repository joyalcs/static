from django.shortcuts import render
from django.views import View

from .models import Product,Category

# Create your views here.
class HomeView(View):
    def get(self, request):
        products = Product.objects.all()
        categories = Category.objects.all()
        context ={
            'products':products,
            'categories':categories,
        }
        return render(request, 'app/home.html', context)


