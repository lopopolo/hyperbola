from django.db import models
from django.urls import reverse
from localflavor.us.models import PhoneNumberField
from stdimage.models import StdImageField

from ..core import MakeUploadTo


class ContactType(models.Model):
    """A grouping of contacts (ie: Work, personal)."""

    type = models.CharField(max_length=100, unique=True)
    display_order = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return "{} - {}".format(self.display_order, self.type)

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
    date = models.DateField(auto_now_add=True, db_index=True)
    resume = models.FileField(upload_to=MakeUploadTo("resume"))

    @staticmethod
    def get_absolute_url():
        return reverse("contact:resume_pdf")

    def __str__(self):
        return "version {} as of {}".format(self.id, self.date)


class AboutMe(models.Model):
    photo = StdImageField(upload_to=MakeUploadTo("about"), variations={
        'x1': (240, 240),
        'x2': (480, 480),
        'x3': (720, 720),
    })
    blurb = models.TextField()

    def __str__(self):
        display = ""
        if self == self.__class__.objects.latest('id'):
            display = "[DISPLAY]"
        return " ".join([display, "{:.80} ...".format(self.blurb)])
