from users.models import User
from django.db import connections
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from pets.models import Pet
from sites.models import Site
from pets.api.serializers import PetSerializer
from ProyectoSecLife import send_email


@api_view(['GET'])
def pet_list(request):

    if request.method == 'GET':
        pets = Pet.objects.filter(is_adopted = False)[:4]
        pets_serializer = PetSerializer(pets,many = True)
        return Response(pets_serializer.data,status = status.HTTP_200_OK)
    
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def pets_list_all(request,pk=None):

    if request.method == 'GET':
        pets = Pet.objects.filter(site = pk)
        pets_serializer = PetSerializer(pets,many = True)
        return Response(pets_serializer.data,status = status.HTTP_200_OK)
    
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def pets_list_site(request,pk=None):

    if request.method == 'GET':
        pets = Pet.objects.filter(site = pk, is_adopted = False)
        pets_serializer = PetSerializer(pets,many = True)
        return Response(pets_serializer.data,status = status.HTTP_200_OK)
    
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def pet_count_site(request,pk=None):

    if request.method == 'GET':
        pets = Pet.objects.filter(site = pk, is_adopted = False)
        pets_serializer = PetSerializer(pets,many = True)
        return Response(pets_serializer.data,status = status.HTTP_200_OK)
    
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def pet_list_dogs(request):

    if request.method == 'GET':
        pets = Pet.objects.filter(is_adopted = False, type_pet= 1)
        pets_serializer = PetSerializer(pets,many = True)
        return Response(pets_serializer.data,status = status.HTTP_200_OK)
    
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def pet_list_cats(request):

    if request.method == 'GET':
        pets = Pet.objects.filter(is_adopted = False, type_pet= 2)
        pets_serializer = PetSerializer(pets,many = True)
        return Response(pets_serializer.data,status = status.HTTP_200_OK)
    
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def pet_add(request):
    
    if request.method == 'POST':
        pet_serializer = PetSerializer(data = request.data)
        if pet_serializer.is_valid():
            pet_serializer.save()
            user_adm = User.objects.filter(site_id = pet_serializer.data["site"],is_admin = True ).first()
            data = {
                'email' :user_adm.email,
                'name' : pet_serializer.data["name"],
                'url' : pet_serializer.data["url_image"] 
            }
            send_email.send_email(data,6);        
            return Response({'message':'Mascota creada correctamente','type_response':'1'},status = status.HTTP_201_CREATED)
        return Response(pet_serializer.errors,status = status.HTTP_200_OK)
    else:
        return Response({''},status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def pet_edit(request,pk=None):
    if request.method == 'POST':
        pet_serializer = PetSerializer(data = request.data)
        if pet_serializer.is_valid():
            pet = Pet.objects.filter(id_pet = pk).first()
            pet2 = pet_serializer
            print(pet)
            print(pet2)
            pet.type_pet = pet2.data["type_pet"]
            pet.name = pet2.data["name"]
            pet.gender = pet2.data["gender"]
            pet.breed = pet2.data["breed"]
            pet.age = pet2.data["age"]
            pet.size = pet2.data["size"]
            pet.color = pet2.data["color"]
            pet.weight = pet2.data["weight"]
            pet.personality = pet2.data["personality"]
            pet.description = pet2.data["description"]
            pet.priority = pet2.data["priority"]
            pet.url_image = pet2.data["url_image"]
            pet.discapacity = pet2.data["discapacity"]
            pet.save()            
            return Response({'type':'1'},status = status.HTTP_201_CREATED)
        return Response(pet_serializer.errors,status = status.HTTP_200_OK)
    else:
        return Response({'type':'2'},status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def pet_adopt(request,pk=None):
    # queryset
    print(pk)
    pet = Pet.objects.filter(id_pet = pk).first()

    # validation
    if pet:
        if request.method == 'DELETE':
            pet.is_adopted  = True;
            pet.save()
            return Response({'message':'Mascota eliminada correctamente'},status = status.HTTP_200_OK)

    return Response({'message':'No se ha encontrado una mascota con estos datos'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','OPTIONS'])
def get_pet(request,pk=None):
    # queryset
    pet = Pet.objects.filter(id_pet = pk).first()
    # validation
    if pet:
        # retrieve
        if request.method == 'GET': 
            pet_serializer = PetSerializer(pet)
            return Response(pet_serializer.data,status = status.HTTP_200_OK)
        
    
    return Response({'message':'No se ha encontrado una mascota con estos datos'},status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def pets_count(request):

    if request.method == 'GET':
        pets_count = Pet.objects.filter(is_adopted = False).count()
        data = {
            "count": pets_count
        }
        return Response(data,status = status.HTTP_200_OK)
    
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)

