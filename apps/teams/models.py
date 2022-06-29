from django.db import models
class Team(models.Model):
    id_team = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, unique=True, null=False)
    img_flag = models.ImageField(upload_to='img/flags', blank=True, null=True)
    img_shield = models.ImageField(upload_to='img/shields', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'team'
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        ordering = ('name',)

    def __str__(self):
        return self.name

