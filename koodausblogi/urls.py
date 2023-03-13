from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blogi import views as blogi_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogi_views.postaukset, name="postauslista"),
    path('postaus/<int:id>', blogi_views.nayta_postaus, name="nayta_postaus"),
    path('postaus/uusi', blogi_views.uusi_postaus, name="uusi_postaus")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
