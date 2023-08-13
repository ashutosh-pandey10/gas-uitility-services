from django.urls import include, path

from . import views

urlpatterns = [
    path("submit-service-request/", views.submit_service_request),
    path("get-user-service-requests/", views.get_user_service_requests),
    path("track-service-request/<int:request_id>/", views.track_service_request),
    path("update-service-request/<int:request_id>/", views.update_service_request),
    path("get-user-profile/", views.get_user_profile),
    path("update-user-profile/", views.update_user_profile),
    path("get-user-details/", views.get_user_details),
]
