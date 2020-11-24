from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("applications.target.urls")),
    path("info/", include("applications.inform.urls")),
    path("order/", include("applications.order.urls")),
    path("contacts/", include("applications.contacts.urls")),
    path("flowers/", include("applications.flowers.urls")),
    path("shrubs/", include("applications.shrubs.urls")),
    path("trees/", include("applications.trees.urls")),

]
