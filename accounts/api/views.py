from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import api_view, permission_classes



@api_view(["POST"])
def api_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception as e:
            return Response(data={
                "success": False,
                "errors": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response(data={
            "success": True,
            "message": "User has been created successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)