from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('catalog.urls')), 
]

=======
    path('', include('catalog.urls')),  
]
>>>>>>> 5ca6d7ac49fd4e923175c2b31c65329d161147aa
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
