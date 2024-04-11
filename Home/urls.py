from django.urls import path
from Home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('search/',views.search,name="search"),
    path('signup/',views.userSignup,name="userSignup"),
    path('login/',views.userLogin,name="userLogin"),
    path('logout/',views.logoutUser,name="logoutUser"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)