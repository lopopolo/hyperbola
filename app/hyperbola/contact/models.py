from django.core.urlresolvers import reverse
from django.db import models
from localflavor.us.models import PhoneNumberField


# a grouping of contacts (ie: Work, personal)
class ContactType(models.Model):
    type = models.CharField(max_length=255, unique=True)
    display_order = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return "{0} - {1}".format(self.display_order, self.type)

    class Meta:
        ordering = ['display_order']


class Contact(models.Model):
    type = models.ForeignKey(ContactType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = None

    def display_name(self):
        return self.name

    def display_value(self):
        return self.value

    @staticmethod
    def is_url():
        return False

    @staticmethod
    def is_email():
        return False

    def __str__(self):
        return str(self.value)

    class Meta:
        abstract = True
        ordering = ['type', 'name', 'value']


class EmailContact(Contact):
    value = models.EmailField()

    @staticmethod
    def is_email():
        return True


class PhoneContact(Contact):
    value = PhoneNumberField()


class WebContact(Contact):
    value = models.URLField()

    @staticmethod
    def is_url():
        return True


class IMContact(Contact):
    value = models.CharField(max_length=255)


class Resume(models.Model):
    date = models.DateField(auto_now=True, db_index=True)

    resume = models.FileField(upload_to="resume/%Y/%m/%d/%H-%M/lopopolo.pdf")

    @staticmethod
    def get_absolute_url():
        return reverse("contact-resume-pdf")

    def display_name(self):
        return "As of {0}".format(self.date.strftime("%b %d %Y"))

    def __str__(self):
        return "version {0} as of {1}".format(self.id, self.date)


class AboutMe(models.Model):
    photo = models.ImageField(upload_to="about/photo/%Y/%m/%d/%H-%M/")
    blurb = models.TextField()

    def __str__(self):
        return "{0} ...".format(self.blurb[:50])
