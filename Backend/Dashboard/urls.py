from django.conf.urls import url
from Dashboard import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^parta/$',views.partaApi),
    url(r'^parta/([0-9]+)$',views.partaApi),

    url(r'^partb/$',views.partbApi),
    url(r'^partb/([0-9]+)$',views.partbApi),
    
]