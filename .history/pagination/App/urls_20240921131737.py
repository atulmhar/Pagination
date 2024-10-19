from django.urls import path
from import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App.urls'))
]
