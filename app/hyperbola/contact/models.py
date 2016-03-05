from django.core.urlresolvers import reverse
from django.db import models
from localflavor.us.models import PhoneNumberField


# a grouping of contacts (ie: Work, personal)
class ContactType(models.Model):
    type = models.CharField(max_length=200, unique=True)
    display_order = models.PositiveIntegerField(unique=True)

    def __unicode__(self):
        return "{0} - {1}".format(self.display_order, self.type)

    class Meta:
        ordering = ['display_order']


class Contact(models.Model):
    type = models.ForeignKey(ContactType, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    value = "blank"

    def display_name(self):
        return self.name

    def display_value(self):
        return self.value

    def is_url(self):
        return False

    def is_email(self):
        return False

    def __unicode__(self):
        return self.value

    class Meta:
        abstract = True
        ordering = ['type', 'name', 'value']


class EmailContact(Contact):
    value = models.EmailField(max_length=75)

    def is_email(self):
        return True


class PhoneContact(Contact):
    value = PhoneNumberField()


class WebContact(Contact):
    value = models.URLField(max_length=200)

    def is_url(self):
        return True


class IMContact(Contact):
    value = models.CharField(max_length=100)


class Resume(models.Model):
    date = models.DateField(auto_now=True, db_index=True)

    resume = models.FileField(upload_to="resume/%Y/%m/%d/%H-%M/lopopolo.pdf")

    def get_absolute_url(self):
        return reverse("contact-resume-pdf")

    def display_name(self):
        return "As of {0}".format(self.date.strftime("%b %d %Y"))

    def __unicode__(self):
        return "version {0} as of {1}".format(self.id, self.date)


class AboutMe(models.Model):
    photo = models.ImageField(upload_to="about/photo/%Y/%m/%d/%H-%M/")
    blurb = models.TextField()

    def __unicode__(self):
        return "{0} ...".format(self.blurb[:50])
