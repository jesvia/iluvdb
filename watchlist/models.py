from django.db import models

# lets create a model names movie
class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length = 200)
    website = models.URLField(max_length = 200)
    
    def __str__(self):
        return self.name

class Watchlist(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length = 200)
    # active field to tell whethere movie published or not
    active = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    # slugfield is used for url -- short label that contains numbers, letters, underscores or hyphens
    
    def __str__(self):
        return self.title
   