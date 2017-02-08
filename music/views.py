from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView, UpdateView,DeleteView #for adding forum to create new object ,updateview:to update,deleteview:to delete the object

class IndexView(generic.ListView): #whenevr we listview it will refer to index.html page
	template_name = 'music/index.html'
	context_object_name = 'all_albums' #to make that default object_list to give whatever name we want here all_albums

	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView): #As in detail page there is description on one object hence we used DetailView here
	model = Album
	template_name = 'music/detail.html'

class AlbumCreate(CreateView):
	model = Album
	fields = ['artist','album_title','genre','album_logo']