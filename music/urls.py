from django.conf.urls import url
from . import views # . means look into current directory

app_name = "music"
urlpatterns= [
		# /music/
       url(r'^$' , views.IndexView.as_view() , name = "index" ), #as_view() this means as here we used class IndexView not function hence take it as view

       # /music/id/
       url(r'^(?P<pk>[0-9]+)/$' , views.DetailView.as_view(), name= 'detail'),

       # /music/album/add/
      url(r'^album/add/$',views.AlbumCreate.as_view(),name ='album-add'),
]


