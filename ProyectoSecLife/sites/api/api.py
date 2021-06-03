from django.db import connections
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from sites.models import Site
from users.models import User
from sites.api.serializers import SiteSerializer
from users.api.serializers import UserSerializer


@api_view(['GET'])
def sites_list(request):

    if request.method == 'GET':
        sites = Site.objects.filter()
        sites_serializer = SiteSerializer(sites,many = True)
        return Response(sites_serializer.data,status = status.HTTP_200_OK)
    
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def site_add(request):
    if request.method == 'POST':
        site_validate = Site.objects.filter(administrator = request.data["administrator"])
        if(site_validate):
            return Response({'type':'1'},status = status.HTTP_400_BAD_REQUEST)
        else:
            site_serializer = SiteSerializer(data = request.data)
            if site_serializer.is_valid():
                site_serializer.save()
                user_admin = User.objects.filter(id = site_serializer.data["administrator"]).first()
                site_created = Site.objects.filter(administrator = request.data["administrator"]).first()
                user_admin.site_id = site_created.id_site
                user_admin.save()                   
                return Response({'type':'2'},status = status.HTTP_201_CREATED)

        return Response(site_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'Solo permite método POST'},status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','OPTIONS'])
def get_site_ad(request,pk=None):
    # queryset
    site = Site.objects.filter(administrator = pk).first()
    # validation
    if site:
        # retrieve
        if request.method == 'GET': 
            site_serializer = SiteSerializer(site)
            return Response(site_serializer.data,status = status.HTTP_200_OK)
    
    return Response({'message':'No se ha encontrado un sitio'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','OPTIONS'])
def get_site(request,pk=None):
    # queryset
    site = Site.objects.filter(id_site = pk).first()
    # validation
    if site:
        # retrieve
        if request.method == 'GET': 
            site_serializer = SiteSerializer(site)
            return Response(site_serializer.data,status = status.HTTP_200_OK)
    
    return Response({'message':'No se ha encontrado un sitio'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','OPTIONS'])
def get_site_administrator(request,pk=None):
    # queryset
    site = Site.objects.filter(id_site = pk).first()
    # validation
    if site:
        # retrieve
        if request.method == 'GET': 
            administrator = site.administrator
            users_serializer = UserSerializer(administrator)
            return Response(users_serializer.data,status = status.HTTP_200_OK)
        
    
    return Response({'message':'No se ha encontrado un sitio'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','OPTIONS'])
def site_admin_delete(request,pk=None):
    # queryset
    site = Site.objects.filter(administrator = pk).first()
    # validation
    if site:
        # retrieve
        if request.method == 'GET': 
            return Response({'type':'1'}, status = status.HTTP_200_OK)
    else:
        return Response({'type':'2'}, status = status.HTTP_200_OK)
        
    
    return Response({'message':'No se ha encontrado un sitio'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def change_admin(request):
    print(request)
    pk1 = request.data["id_site"]
    pk2 = request.data["id_user"]
    
    if request.method == 'POST':
        site = Site.objects.filter(administrator = pk2).first()
        if(site):
            return Response({'type':'1'},status = status.HTTP_200_OK)
        else:
            user = User.objects.filter(id = pk2).first()
            site2 = Site.objects.filter(id_site = pk1).first()
            
            user2 = site2.administrator
            user2.site_id = 0
            user.site_id = site2.id_site 
            site2.administrator = user
            user.save()
            user2.save()
            site2.save()
            return Response({'type':'2'},status = status.HTTP_200_OK)
        
            
    
    else:
        return Response({'Solo se soporta método POST'},status = status.HTTP_400_BAD_REQUEST)