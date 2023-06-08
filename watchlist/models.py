from django.db import models

# lets create a model names movie
class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length = 200)
    # active field to tell whethere movie published or not
    active = models.BooleanField(default = True)
    # slugfield is used for url -- short label that contains numbers, letters, underscores or hyphens
    
    def __str__(self):
        return self.name
   