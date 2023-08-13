from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import ServiceRequest, UserProfile
from .serializers import (
    ServiceRequestCreateSerializer,
    ServiceRequestSerializer,
    ServiceRequestUpdateSerializer,
    UserProfileSerializer,
    UserSerializer,
)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def submit_service_request(request):
    """
    This function subits the service request raised by the customer/user.
    """
    serializer = ServiceRequestCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(customer=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_service_requests(request):
    """
    Allow customers to track the status of their service requests. Returns all the requests raised
    by the customer.
    """
    service_requests = ServiceRequest.objects.filter(customer=request.user)
    serializer = ServiceRequestSerializer(service_requests, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def track_service_request(request, request_id):
    """
    Let's customer see the status of specific requests. Raises 404 Not found if no request with
    passed reques_id are present.

    param:
    request_id : This is the primary key identifier "id" for model "ServiceRequest".
    """
    try:
        service_request = ServiceRequest.objects.get(pk=request_id, customer=request.user)
    except ServiceRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ServiceRequestSerializer(service_request)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_service_request(request, request_id):
    """
    This function is ustilised by the company support representatives. Using this API, they can
    update the status of request raised(if any) by the customer.

    param:
    request_id : This is the primary key identifier "id" for model "ServiceRequest".
    """
    try:
        service_request = ServiceRequest.objects.get(pk=request_id, customer=request.user)
    except ServiceRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ServiceRequestUpdateSerializer(service_request, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
Below functions allow user to view and update their profile.
"""


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    serializer = UserProfileSerializer(profile)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    serializer = UserProfileSerializer(profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_details(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)
