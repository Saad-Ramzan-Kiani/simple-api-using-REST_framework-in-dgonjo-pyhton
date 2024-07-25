from django.contrib import admin
from django.urls import path, include  # Correct import
from saad import views  # Adjust according to your actual views import

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('home/', include('saad.urls')),
    path('api/', include('saad.urls')),
]