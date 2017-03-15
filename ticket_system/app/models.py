from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import default


SILVER = "default"
BLUE = "primary"
GREEN = "success"
LIGHT_BLUE = "info"
YELLOW = "warning"
RED = "danger"
MARKER_CHOICES = (
    (SILVER, 'silver'),
    (BLUE, 'blue'),
    (GREEN, 'green'),
    (LIGHT_BLUE, 'light blue'),
    (YELLOW, 'yellow'),
    (RED, 'red')
)

ADMIN = "administrator"
DEVELOPER = "programmer"
QA = "quality assurance"
ROLE = (
    (ADMIN, "admin"),
    (DEVELOPER, "developer"),
    (QA, "qa")
)


class Project(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(unique=True, max_length=10)
    project_owner = models.ForeignKey(to=User, null=False, related_name="owners")
    contributors = models.ManyToManyField(to=User, blank=True, related_name="contributors")
    description = models.TextField()
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('project')


class Status(models.Model):
    name = models.CharField(max_length=30)
    key = models.CharField(unique=True, max_length=10)
    marker = models.CharField(max_length=20, choices=MARKER_CHOICES, default=SILVER)

    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=30)
    key = models.CharField(unique=True, max_length=10)
    marker = models.CharField(max_length=20, choices=MARKER_CHOICES, default=SILVER)

    def __str__(self):
        return self.name


class MonthlyWeatherByCity(models.Model):
    month = models.IntegerField()
    boston_temp = models.DecimalField(max_digits=5, decimal_places=1)
    houston_temp = models.DecimalField(max_digits=5, decimal_places=1)



class Issue(models.Model):
    type = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=100)
    startDate = models.DateField()
    endDate = models.DateField()
    createdBy = models.ForeignKey(to=User, null=False, related_name="createdIssues")
    assignedTo = models.ForeignKey(to=User, null=False, related_name="assignedIssues")
    project = models.ForeignKey(to=Project, null=False)
    status = models.CharField(max_length=20, choices=MARKER_CHOICES, default=SILVER)
    priority = models.CharField(max_length=20, choices=MARKER_CHOICES, default=SILVER)
    description = models.TextField()
    spentTime = models.TimeField()
    donePercentage = models.PositiveIntegerField()


class RoleOnProject(models.Model):
    role = models.CharField(max_length=20, choices=ROLE)
    user = models.ForeignKey(to=User, null=False, related_name="roleOnProject")
    project = models.ForeignKey(to=Project, null=False, related_name="roles")

    def get_absolute_url(self):
        return reverse('roleOnProject')


class HistoryItem(models.Model):
    datetime = models.DateTimeField()
    author = models.ForeignKey(to=User, null=False, related_name="historyItem")
    issue = models.ForeignKey(to=Issue, null=False, related_name="historyItemIssue")


class Comment(HistoryItem):
    message = models.TextField()

    def __str__(self):
        return self.message


class Commit(HistoryItem):
    link = models.URLField()

class IssueChange(HistoryItem):
    propertyName = models.CharField(max_length=50)
    oldValue = models.CharField(max_length=50)
    newValue = models.CharField(max_length=50)






