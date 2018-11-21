from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Profile.models import profileModel

from Profile.serializer import ProfileSerializer
import json


class ProfileList(APIView):
    def get(self, request, format=None):
        queryset = profileModel.objects.filter(delete = False)
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responde = repuestaJson("success", datas, "Mensaje de respuesta")
            return Response(responde, status=status.HTTP_201_CREATED)
        responde = repuestaJson(serializer.errors, " ", "Mensaje de respuesta")
        return Response(responde, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetail(APIView):
    def get_object(self, pk):
        try:
            return profileModel.objects.get(pk=pk)
        except profileModel.DoesNotExist:
            return "No"

    def get(self, request, pk, format=None):
        Id = self.get_object(pk)
        if Id != "No":
            Id = ProfileSerializer(Id)
            return Response(Id.data)
        responde = repuestaJson("Error", " ", "No hay coincodencias")
        return Response(responde)

    def put(self, request, pk, format=None):
        Id = self.get_object(pk)
        serializer = ProfileSerializer(Id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responde = repuestaJson("success", datas, "Actualización Exitosa")
            return Response(responde)
        responde = repuestaJson(serializer.errors, "", "Error Actualización")
        return Response(responde, status=status.HTTP_400_BAD_REQUEST)


def repuestaJson(success, datas, message):
    respuesta = '{'
    respuesta += '"status"'
    respuesta += ":"
    respuesta += '"'+str(success)+'"'
    respuesta += ","

    respuesta += '"data"'
    respuesta += ":"
    respuesta += '"'+str(datas)+'"'
    respuesta += ","

    respuesta += '"message"'
    respuesta += ":"
    respuesta += '"'+str(message)+'"'

    respuesta += '}'
    respuesta = json.loads(respuesta)

    return(respuesta)