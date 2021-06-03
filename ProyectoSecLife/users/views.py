
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from users.api.serializers import UserTokenSerializer

# Create your views here.
class Login(ObtainAuthToken):
    
    def post(self,request,*args,**kwargs):
        # send to serializer username and password
        print(request.data)
        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        if login_serializer.is_valid():
            # login serializer return user in validated_data
            user = login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de Sesión Exitoso.'
                    }, status = status.HTTP_201_CREATED)
                else:
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de Sesión Exitoso.'
                    }, status = status.HTTP_201_CREATED)
                  
            else:
                return Response({'error':'Este usuario no puede iniciar sesión.'}, 
                                    status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Nombre de usuario o contraseña incorrectos.'},
                                    status = status.HTTP_400_BAD_REQUEST)
            
class Logout(APIView):
    
    def get(self,request,*args,**kwargs):
        try:
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()

            if token:
                user = token.user
                token.delete() 
                token_message = 'Token eliminado.'
                return Response({'token_message': token_message,}, status = status.HTTP_200_OK)
            
            return Response({'error':'No se ha encontrado un usuario con estas credenciales.'},
                    status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'No se ha encontrado token en la petición.'}, 
                                    status = status.HTTP_409_CONFLICT)
        
        
class UserToken(APIView):

    def post(self,request,*args,**kwargs):    
        try:      
            print(request.data)
            token = request.data['token']
            token = Token.objects.filter(key = token).first()

            if token:
                return Response({'is_validate': 'true',}, status = status.HTTP_200_OK)
            
            else:
                return Response({'is_validate': 'false',}, status = status.HTTP_200_OK)
        except:
            return Response({'peticion invalida',}, status = status.HTTP_400_BAD_REQUEST)