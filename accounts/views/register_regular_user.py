from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import RegisterRegularUserSerializer


class RegisterRegularUserView(APIView):
    @staticmethod
    def post(request):
        serializer = RegisterRegularUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
