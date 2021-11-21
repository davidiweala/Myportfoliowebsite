from django.urls import path
from .import views
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings

urlpatterns =[
    path('', views.home, name="home"),
    path('portfolio/', views.portfolio, name="portfolio"),
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]

