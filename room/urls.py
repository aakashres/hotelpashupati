from django.urls import path

from . import views


urlpatterns = (
    path("admin/list/", views.RoomListView.as_view(), name="admin_room_list"),
    path("admin/create/", views.RoomCreateView.as_view(), name="admin_room_create"),
    path("admin/detail/<int:pk>/", views.RoomDetailView.as_view(), name="admin_room_detail"),
    path("admin/update/<int:pk>/", views.RoomUpdateView.as_view(), name="admin_room_update"),
    path("admin/delete/<int:pk>/", views.RoomDeleteView.as_view(), name="admin_room_delete"),
)
