from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIview
from rest_framework.response import Response
class ProductsView(APIview):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"inside products get"})