from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),
    path("api/", include("ai_api.urls")),
    path("authentication/", include("accounts.urls"))
]
