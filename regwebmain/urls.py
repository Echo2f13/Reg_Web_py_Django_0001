from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',include('rpage.urls')),
    path('admin/',admin.site.urls),
    path('user/',include('users.urls'))
]

