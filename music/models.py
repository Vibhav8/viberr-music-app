from django.db import models
from django.core.urlresolvers import reverse #doubt


class Album(models.Model):
	artist = models.CharField(max_length = 250)
	album_title = models.CharField(max_length =500)
	genre = models.CharField(max_length = 100)
	album_logo = models.FileField(max_length = 1000)

	
	def get_absolute_url(self):
		return reverse('music:detail',kwargs={"pk":self.pk})
	def __str__(self):
		return self.album_title + '-' + self.artist


class Song(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE)
	file_type = models.CharField(max_length = 10)
	song_title = models.CharField(max_length = 250)
	audio_file = models.FileField(default = '')
	

	def __str__(self):
		return self.song_title
	 
