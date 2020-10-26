from django.contrib import admin
from django.urls import path,include
#below 2 for media and any static stuff
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls'))
]

#for static and media like images videos and mp3 etc
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
