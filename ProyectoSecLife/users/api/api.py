from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from users.models import User
from users.api.serializers import UserSerializer
from ProyectoSecLife import send_email

@api_view(['GET'])
def user_list(request):

    if request.method == 'GET':
        users = User.objects.filter(is_active = True)
        users_serializer = UserSerializer(users,many = True)
        return Response(users_serializer.data,status = status.HTTP_200_OK)
    
    else:
        return Response({'Solo se soporta metodo GET'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_list_admin(request):

    if request.method == 'GET':
        users = User.objects.filter(is_active = True, is_admin = True, is_superuser = False)
        users_serializer = UserSerializer(users,many = True)
        return Response(users_serializer.data,status = status.HTTP_200_OK)
    
    else:
        return Response({'Solo se soporta metodo GET'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_list_staff(request,pk=None):

    if request.method == 'GET':
        users = User.objects.filter(is_active = True, is_staff = True ,is_admin = False, is_superuser = False, site_id=pk)
        users_serializer = UserSerializer(users,many = True)
        return Response(users_serializer.data,status = status.HTTP_200_OK)
    
    else:
        return Response({'Solo se soporta metodo GET'},status = status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def user_add(request):
    
    if request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            data = {
                'email' :request.data["email"],
                'name' : request.data["name"]
            }  
            user_serializer.save()
            if(user_serializer.data["is_admin"] == True):
                send_email.send_email(data,4);
            else:
                if(user_serializer.data["is_staff"] == True):
                  send_email.send_email(data,5);  
                else:
                    send_email.send_email(data,1);            
            return Response({'message':'Usuario creado correctamente!','type_response':'1'},status = status.HTTP_201_CREATED)
        return Response(user_serializer.errors,status = status.HTTP_200_OK)
    else:
        return Response({''},status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def user_delete(request,pk=None):
    # queryset
    print(pk)
    user = User.objects.filter(id = pk).first()

    # validation
    if user:
        if request.method == 'DELETE':
            user.is_active = False;
            user.save()
            return Response({'message':'Usuario Eliminado correctamente!'},status = status.HTTP_200_OK)

    return Response({'message':'No se ha encontrado un usuario con estos datos'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_count(request):

    if request.method == 'GET':
        users_count = User.objects.filter(is_active = True).count()
        data = {
            "count": users_count
        }
        return Response(data,status = status.HTTP_200_OK)
    
    else:
        return Response({'Solo se soporta metodo GET'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_change_password(request,pk=None):
    
    if request.method == 'POST':
        user = User.objects.filter(id = pk).first()
        if user:
            User.set_password(self=user ,raw_password=request.data["password"])
            user.save()
            return Response({"Contraseña cambiada"},status = status.HTTP_200_OK)
        else:
            return Response({"Usuario no encontrado"},status =  status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'Petición invalida'},status = status.HTTP_400_BAD_REQUEST)