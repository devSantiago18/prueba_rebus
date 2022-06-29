from django.db import models

class Team(models.Model):
    id_team = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250,unique=True)
    url_flag = models.ImageField()
    url_shield = models.ImageField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'team'
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.name

