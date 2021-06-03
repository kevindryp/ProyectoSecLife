from sites.models import Site
from django.db import connections
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from requests.models import Request
from pets.models import Pet
from users.models import User
from requests.api.serializers import RequestSerializer
from ProyectoSecLife import send_email


@api_view(['POST'])
def request_add(request):
    
    if request.method == 'POST':
        reques_serializer = RequestSerializer(data = request.data)
        if reques_serializer.is_valid():
            user = User.objects.filter(id = request.data["applicant"]).first()
            pet = Pet.objects.filter(id_pet = request.data["pet"]).first()
            request = Request.objects.filter(applicant = user.id, pet = pet.id_pet, is_active = True).first()
            if(request):
                return Response({'message':'Ya tiene una solicitud para esta mascota','type_response':'4'},status = status.HTTP_400_BAD_REQUEST)
            else: 
                if(pet.is_adopted == False):
                    data = {
                        'email' :user.email,
                        'name' : pet.name,
                        'url' : pet.url_image 
                    }
                    send_email.send_email(data,2);
                    reques_serializer.save()            
                    return Response({'message':'Solicitud enviadad correctamente','type_response':'1'},status = status.HTTP_201_CREATED)
                return Response({'message':'Mascota no disponible','type_response':'2'},status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message':'Error al enviar la solicitud','type_response':'3'},status = status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message':'Error al enviar la solicitud','type_response':'3'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','OPTIONS'])
def get_requests_user(request,pk=None):
    # queryset
    list_request = Request.objects.filter(applicant = pk, is_active = True)
    if list_request:

        if request.method == 'GET': 
            request_serializer = RequestSerializer(list_request,many = True)
            return Response(request_serializer.data,status = status.HTTP_200_OK)
    
    return Response({'type_response' : '2'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST','OPTIONS'])
def cancelar_request_user(request,pk=None):
    request_user = Request.objects.filter(id_request = pk, is_active = True).first()
    if request_user:
        if request.method == 'POST':
            user = User.objects.filter(id = request_user.applicant.id).first()
            pet = Pet.objects.filter(id_pet = request_user.pet.id_pet).first()
            request_user.is_active = False
            request_user.state = "Cancelada"
            request_user.comments = "El usuario canceló la solicitud"
            request_user.save()
            data = {
                        'email' :user.email,
                        'name' : pet.name,
                        'url' : pet.url_image 
                    }
            send_email.send_email(data,3);
            return Response({'type_response':'1'},status = status.HTTP_200_OK)
        else:
            return Response({'type_response':'2'},status = status.HTTP_400_BAD_REQUEST)


@api_view(['POST','OPTIONS'])
def rechazar_request_user(request,pk=None):
    request_user = Request.objects.filter(id_request = pk, is_active = True).first()
    if request_user:
        if request.method == 'POST':
            user = User.objects.filter(id = request_user.applicant.id).first()
            pet = Pet.objects.filter(id_pet = request_user.pet.id_pet).first()
            request_user.is_active = False
            request_user.state = "Rechazada"
            request_user.comments = request.data["razon"]
            request_user.save()
            data = {
                        'email' :user.email,
                        'name' : pet.name,
                        'url' : pet.url_image 
                    }
            send_email.send_email(data,8);
            return Response({'type_response':'1'},status = status.HTTP_200_OK)
        else:
            return Response({'type_response':'2'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST','OPTIONS'])
def aceptar_request_user(request,pk=None):
    request_user = Request.objects.filter(id_request = pk, is_active = True).first()
    if request_user:
        if request.method == 'POST':
            pet = Pet.objects.filter(id_pet = request_user.pet.id_pet).first()
            pet.is_adopted =  True
            request_user.is_active = False
            request_user.state = "Aceptada"
            request_user.comments = "La solicitud fue aceptada"
            request_user.save()
            for request_other in Request.objects.filter(pet = request_user.pet.id_pet, is_active=True):
                request_other.is_active = False
                request_other.state = "Rechazada"
                request_other.comments = "La mascota fue adoptada por otra persona"
                user_other = User.objects.filter(id = request_other.applicant.id).first()
                data = {
                        'email' :user_other.email,
                        'name' : pet.name,
                        'url' : pet.url_image 
                    }
                send_email.send_email(data,9);
                request_other.save()

            user = User.objects.filter(id = request_user.applicant.id).first()
            site = Site.objects.filter(id_site = pet.site.id_site).first()
            data2 = {
                    'email' :user.email,
                    'name' : pet.name,
                    'url' : pet.url_image,
                    'lugar': site.name,
                    'direccion': site.address,
                    }
            send_email.send_email(data2,10);
            pet.save()
            return Response({'type_response':'1'},status = status.HTTP_200_OK)
        else:
            return Response({'type_response':'2'},status = status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','OPTIONS'])
def get_requests_site_all(request,pk=None):
    # queryset
    list_request = Request.objects.filter(site = pk)
    if list_request:
        if request.method == 'GET': 
            request_serializer = RequestSerializer(list_request,many = True)
            return Response(request_serializer.data,status = status.HTTP_200_OK)
    
    return Response({'type_response' : '2'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','OPTIONS'])
def get_requests_site(request,pk=None):
    # queryset
    list_request = Request.objects.filter(site = pk, is_active=True)
    if list_request:
        if request.method == 'GET': 
            request_serializer = RequestSerializer(list_request,many = True)
            return Response(request_serializer.data,status = status.HTTP_200_OK)
    
    return Response({'type_response' : '2'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST','OPTIONS'])
def programar_request_user(request,pk=None):
    request_user = Request.objects.filter(id_request = pk, is_active = True).first()
    if request_user:
        if request.method == 'POST':
            user = User.objects.filter(id = request_user.applicant.id).first()
            user2 = User.objects.filter(id= request.data["id"]).first()
            pet = Pet.objects.filter(id_pet = request_user.pet.id_pet).first()
            request_user.state = "Cita programada"
            request_user.comments = "Fecha: " + request.data["date"] + " " + "Hora: " + request.data["hour"]
            request_user.save()
            data1 = {
                    'email' :user.email,
                    'url' : pet.url_image,
                    'url_meet' : request.data["meet"],
                    'date' : request.data["date"],
                    'hour' : request.data["hour"],
                    }
            data2 = {
                    'email' :user2.email,
                    'url' : pet.url_image,
                    'url_meet' : request.data["meet"],
                    'date' : request.data["date"],
                    'hour' : request.data["hour"],
                    }
            send_email.send_email(data1,7);
            send_email.send_email(data2,7);
            return Response({'type_response':'1'},status = status.HTTP_200_OK)
        else:
            return Response({'type_response':'2'},status = status.HTTP_400_BAD_REQUEST)