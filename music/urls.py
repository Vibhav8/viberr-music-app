from django.conf.urls import url
from . import views # . means look into current directory

app_name = "music"
urlpatterns= [
		# /music/
       url(r'^$' , views.IndexView.as_view() , name = 'index'), #as_view() this means as here we used class IndexView not function hence take it as view
       
       url(r'^register/$' , views.UserFormView.as_view() , name = 'register' ), 
       # /music/id/
       url(r'^(?P<pk>[0-9]+)/$' , views.DetailView.as_view(), name= 'detail'),

       # /music/album/add/
      url(r'^album/add/$',views.AlbumCreate.as_view(),name ='album-add'),

      # /music/album/2/
      url(r'^album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name ='album-update'),
    
     # /music/album/2/delete/
      url(r'^album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name ='album-delete'),

       url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),

        url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),

         url(r'^register/$', views.register, name='register'),

        url(r'^logout_user/$', views.logout_user, name='logout_user'),

         url(r'^login_user/$', views.login_user, name='login_user'),



]



