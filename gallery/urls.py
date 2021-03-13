from django.urls import path

from . import views


urlpatterns = (
    path("admin/list/", views.GalleryListView.as_view(), name="admin_gallery_list"),
    path("admin/create/", views.GalleryCreateView.as_view(), name="admin_gallery_create"),
    path("admin/detail/<int:pk>/", views.GalleryDetailView.as_view(), name="admin_gallery_detail"),
    path("admin/update/<int:pk>/", views.GalleryUpdateView.as_view(), name="admin_gallery_update"),
    path("admin/delete/<int:pk>/", views.GalleryDeleteView.as_view(), name="admin_gallery_delete"),
    path("admin/photo/update/<int:pk>/", views.PhotoUpdateView.as_view(), name="admin_photo_update"),
    path("admin/photo/delete/<int:pk>/", views.PhotoDeleteView.as_view(), name="admin_photo_delete"),
)
