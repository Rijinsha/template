from django.db import models

# Create your models here.
# here place is a table name
class place(models.Model):
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=250)
    rating=models.TextField()
# if display ur img name using this code
    def __str__(self):
        return self.name
 #create another table "team"
class team(models.Model):
    team_img = models.ImageField(upload_to='pics')
    team_name = models.CharField(max_length=250)
    team_disc = models.TextField()
    def __str__(self):
        return self.team_name