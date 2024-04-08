from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class WeatherHistory(models.Model):
    location = models.CharField(max_length=250, null=True, blank=True)
    temperature = models.CharField(max_length=250, null=True, blank=True)
    weather_description = models.CharField(max_length=250, null=True, blank=True)
    latitude = models.CharField(max_length=250, null=True, blank=True)
    longitude = models.CharField(max_length=250, null=True, blank=True)
    date_data = models.CharField(max_length=250, null=True, blank=True)
    humidity = models.CharField(max_length=250, null=True, blank=True)
    real_feel = models.CharField(max_length=250, null=True, blank=True)
    wind_speed = models.CharField(max_length=250, null=True, blank=True)
    sun_rise = models.CharField(max_length=250, null=True, blank=True)
    sun_set = models.CharField(max_length=250, null=True, blank=True)
    max_temp = models.CharField(max_length=250, null=True, blank=True, help_text="Maximum Temerature")
    min_temp = models.CharField(max_length=250, null=True, blank=True, help_text="Minimum Temerature")
    created_at = models.DateField(auto_now_add=True)
    weather_data = models.TextField(blank=True, null=True)
    forecast_data = models.TextField(blank=True, null=True)
    # user = models.ForeignKey(User)
    def __str__(self):
        return 'Location: '+self.location+', Date: '+str(self.created_at)
    

    class Meta:
        verbose_name_plural = "Weather Histories"
        constraints = [
            models.UniqueConstraint(fields=['location', 'created_at'], name="location day constraint")
        ]