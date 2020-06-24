from authentication.models import Coders
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer
# Create your views here.

class UserApiView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    
    def get (self, request):
        model = Coders.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = UserSerializer(model, context=serializer_context, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post (self, request):
        print(request.data)
        serializer_context = {
            'request': request,
        }
        serializer = UserSerializer(data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
