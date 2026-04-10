from django.db import models
'''
django model field:
- html widget
- validation
- db size



'''
job_type = (
    ('full time','full time'),
    ('part time','part time')
)



# Create your models here.
class Job(models.Model): #table
    title = models.CharField(max_length = 100) #column
    #location
    job_type = models.CharField(max_length=15, choices=job_type)
    describtion = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default = 0)
    experience  = models.IntegerField(default = 1)

    def __str__(self):
        return self.title