from django.db import models

class HarAnalysis(models.Model):
    har_file = models.FileField(upload_to='har_files/')
