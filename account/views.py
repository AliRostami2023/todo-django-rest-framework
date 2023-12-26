from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import RegisterSerializers, UserUpdateSerializers
from .models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

# Create your views here.

class RegisterApiView(APIView):
    def post(self, request):
        ser_data = RegisterSerializers(data=request.POST)
        if ser_data.is_valid():
            new_user = User()
            new_user.full_name = ser_data.validated_data.get('full_name')
            new_user.username = ser_data.validated_data.get('username')
            new_user.email = ser_data.validated_data.get('email')
            new_user.set_password(ser_data.validated_data.get('password'))
            new_user.is_active = True
            new_user.save()

            return Response(ser_data.data, status.HTTP_201_CREATED)
        return Response(ser_data.errors, status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def list(self, request):
        ser_data = UserUpdateSerializers(instance=self.queryset, many=True)
        return Response(ser_data.data)
    
    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        ser_data = UserUpdateSerializers(instance=user)
        return Response(ser_data.data)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        
        if user != request.user:
            return Response({'message': 'you are not owner !'})
        
        ser_data = UserUpdateSerializers(instance=user, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status.HTTP_200_OK)
        return Response(ser_data.errors, status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        if user != request.user:
            return Response({'message': 'you are not owner'})
        
        user.is_active = False
        user.save()
        return Response({'message': 'user deactivated'})
    
