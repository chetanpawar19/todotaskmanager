from django.db import models

class TaskList(models.Model):
    task = models.CharField(max_length=300)   #if this fields change, then run cmd>migrations
    status = models.BooleanField(default=False)  #when add task, it will default set to not completed/done

    def __str__(self):
        return self.task + '-' + str(self.status)         #it will reflact task name on localhost:8000/admin