from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def test_application(request):
    return Response({"message": "Hello, world!"})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def authenticated_view(request):
    return Response({"message": "This is restricted view"})


@api_view(["GET"])
@permission_classes([IsAdminUser])
def admin_view(request):
    return Response({"message": "This is admin view"})
