from django.shortcuts import render
from Test1.models import testModel

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Test1.serializer import Test1Serializer

import json

class Test1List(APIView):
    def get(self, request, format=None):
        queryset = testModel.objects.all()
        serializer = Test1Serializer(queryset, many=True)
        datas = serializer.data
        return Response(datas)
    
    def post(self, request, format=None):
        serializer = Test1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)




# Create your views here.
