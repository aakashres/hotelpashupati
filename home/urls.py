from django.urls import path

from . import views


urlpatterns = (
    path("admin/", views.HomeDetailView.as_view(), name="admin_home_page"),
    path("admin/create/", views.HomeCreateView.as_view(), name="admin_home_create"),
    path("admin/update/<int:pk>/", views.HomeUpdateView.as_view(), name="admin_home_update"),
    path("admin/delete/<int:pk>/", views.HomeDeleteView.as_view(), name="admin_home_delete"),
)
