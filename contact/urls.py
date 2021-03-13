from django.urls import path

from . import views


urlpatterns = (
    path("admin/contact/list/", views.ContactListView.as_view(), name="admin_contact_list"),
    path("admin/contact/create/", views.ContactCreateView.as_view(), name="admin_contact_create"),
    path("admin/contact/detail/<int:pk>/", views.ContactDetailView.as_view(), name="admin_contact_detail"),
    path("admin/contact/update/<int:pk>/", views.ContactUpdateView.as_view(), name="admin_contact_update"),
    path("admin/contact/delete/<int:pk>/", views.ContactDeleteView.as_view(), name="admin_contact_delete"),

    path("admin/social/list/", views.SocialMediaListView.as_view(), name="admin_social_list"),
    path("admin/social/create/", views.SocialMediaCreateView.as_view(), name="admin_social_create"),
    path("admin/social/update/<int:pk>/", views.SocialMediaUpdateView.as_view(), name="admin_social_update"),
    path("admin/social/delete/<int:pk>/", views.SocialMediaDeleteView.as_view(), name="admin_social_delete"),
)
