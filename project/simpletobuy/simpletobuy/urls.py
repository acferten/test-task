from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-shop/', include('api.urls')),
]

# handler404 = 'utils.views.error_404'
# handler500 = 'utils.views.error_500'
