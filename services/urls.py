from django.urls import path

from . import views


urlpatterns = (
    path("admin/service/list", views.ServiceListView.as_view(), name="admin_service_list"),
    path("admin/service/create/", views.ServiceCreateView.as_view(), name="admin_service_create"),
    path("admin/service/detail/<int:pk>/", views.ServiceDetailView.as_view(), name="admin_service_detail"),
    path("admin/service/update/<int:pk>/", views.ServiceUpdateView.as_view(), name="admin_service_update"),
    path("admin/service/delete/<int:pk>/", views.ServiceDeleteView.as_view(), name="admin_service_delete"),
)
