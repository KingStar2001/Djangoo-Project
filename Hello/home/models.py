from django.db import models

# Makemigrations = create changes and store it in a file.
# Migrate = apply the pending changes created by makemigrations 


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    subject=models.TextField(max_length=122)
    message=models.TextField()
    date=models.DateField()

# If you want to see the entries by peoples name then write this function.  

    def __str__(self):
        return self.name
    