from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from .models import mainUserCentral
from .serializers import MainUserCentralSerializer
from .utils import create_supabase_folder
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#The api for creation of the user with the trigger to create and initialize Supabase folders in bucket.
@api_view(['GET', 'POST'])
def data_list(request):
    if request.method=='GET':
        data=mainUserCentral.objects.all()
        serializer = MainUserCentralSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method =='POST':
        serializer=MainUserCentralSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            if not instance.UniqueID:
                instance.UniqueID = f'SIH1016FS{instance.id:03}'
                instance.bucket_url=f'https://zwxpudmuwltonzohjbse.supabase.co/storage/v1/object/public/sihbucketbackend/{instance.UniqueID}/'
                instance.save() 
            create_supabase_folder(instance.UniqueID)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#The api for single user request. Valid for get request only.
@api_view(['GET'])
def fetch_single_data(request, UniqueID, password):
    #obj=mainUserCentral.objects.filter(name=name,  email=email)
    obj = get_object_or_404(mainUserCentral, UniqueID=UniqueID, password=password)
    serializer=MainUserCentralSerializer(obj)
    return Response(serializer.data, status=status.HTTP_200_OK)


"""class MainUserCentralViewSet(viewsets.ModelViewSet):
    queryset = mainUserCentral.objects.all()
    serializer_class = MainUserCentralSerializer
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.UniqueID = f'SIH1016FS{instance.id:03}'  
        instance.save()
        create_supabase_folder(instance.UniqueID)"""
