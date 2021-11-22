
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('moneybook.urls')),
    path('ai-auth/', include('rest_framework.urls')),
    path('accounts/', include('accounts.urls'))
]
