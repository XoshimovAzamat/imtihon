from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import User
from ..serializers import UserSerializer

class UserApi(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(data=serializer.data)
