from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

    def _str_(self):
        return self.title

    # Compare this snippet from backend\todo\serializers.py: