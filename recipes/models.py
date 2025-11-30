from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField(help_text="List ingredients separated by newlines")
    instructions = models.TextField(help_text="List instructions separated by newlines")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
