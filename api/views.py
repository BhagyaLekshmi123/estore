from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Books,Reviews
from api.serializers import BookSerializer,ReviewSerializer
class ProductsView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"inside product get"})


# localhost:8000/morning
# get
# good morning

class MorningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"Good Morning"})

class AddView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data.get("num1"))
        print(request.data.get("num2"))
        return Response({"result":"inside post"})

class NumberChkView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        if(n%2==0):
            res="num is even"
        else:
            res="num is odd"
        return Response({"result":res})

class ProductsView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()
        serializer=BookSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        # request.data
        # bname=request.data.get("name")
        # bauthor=request.data.get("author")
        # bprice=request.data.get("price")
        # bpublisher=request.data.get("publisher")
        # Books.objects.create(name=bname,author=bauthor,price=bprice,publisher=bpublisher)
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            Books.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

        # status code  :2xx success
        #              :4xx client error
        #              :5xx server error

class ProductDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=(kwargs.get("id"))
        book=Books.objects.get(id=id)
        serializer=BookSerializer(book,many=False)
        return Response(data=serializer.data)


    def delete(self,request,*args,**kwargs):
        id=(kwargs.get("id"))
        Books.objects.get(id=id).delete()
        return Response(data="deleted")

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            Books.objects.filter(id=id).update(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


# localhost:8000/reviews
# method:get
class ReviewsView(APIView):
    def get(self,request,*args,**kwargs):
        reviews=Reviews.objects.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
class ReviewDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(qs,many=False)
        return Response(data=serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        object=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(instance=object,data=request.data)
        if serializer.is_valid():
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Reviews.objects.get(id=id).delete()
        return Response(data="deleted")






