from django.db import models

# Create your models here.


class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=50, default='')
    post_author = models.CharField(max_length=50, default='')
    post_heading0 = models.CharField(max_length=50, default='')
    post_heading0_content = models.CharField(max_length=5000, default='')
    post_heading1 = models.CharField(max_length=50, default='')
    post_heading1_content = models.CharField(max_length=5000, default='')
    post_heading2 = models.CharField(max_length=50, default='')
    post_heading2_content = models.CharField(max_length=5000, default='')
    post_thumbnail = models.ImageField(upload_to='blog/images', default='')
    post_publish_date = models.DateField()

    def __str__(self):
        return f"{self.post_title}"