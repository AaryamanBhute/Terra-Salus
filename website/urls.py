from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home, name="homepage"),
    path('about', views.about, name="aboutpage"),
    path('contact', views.contact, name="contactpage"),
    path('future', views.future, name="futurepage"),
    path('use', views.use, name="usepage"),
    path('information/<str:item_name>', views.information, name="informationpage"),
    path('None', views.none, name="nonepage")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)