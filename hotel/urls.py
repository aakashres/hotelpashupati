"""XXX_PROJECT_NAME_XXX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from home.views import HomepageView, LoginView, LogoutView, AdminHomePage, bad_request_view, permission_denied_view, page_not_found_view, error_view
from room.views import RoomView
from gallery.views import GallerypageView
from services.views import ServicepageView
from contact.views import ContactpageView

handler400 = 'home.views.bad_request_view'
handler403 = 'home.views.permission_denied_view'
handler404 = 'home.views.page_not_found_view'
handler500 = 'home.views.error_view'

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('400', bad_request_view, name='400'),
    path('403', permission_denied_view, name='403'),
    path('404', page_not_found_view, name='404'),
    path('500', error_view, name='500'),
    path('hoteladmin', AdminHomePage.as_view(), name='adminpage'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('rooms', RoomView.as_view(), name='roompage'),
    path('galleries', GallerypageView.as_view(), name='gallerypage'),
    path('facilities', ServicepageView.as_view(), name='servicepage'),
    path('contact-us', ContactpageView.as_view(), name='contactpage'),
    path('services/', include(('services.urls', 'services'), 'services')),
    path('gallery/', include(('gallery.urls', 'gallery'), namespace='gallery')),
    path('room/', include(('room.urls', 'room'), 'room')),
    path('contact/', include(('contact.urls', 'contact'), 'contact')),
    path('home/', include(('home.urls', 'home'), 'home')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
