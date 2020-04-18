from autoslug import AutoSlugField
from django.conf import settings
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from django_countries.fields import CountryField


class Cheese(TimeStampedModel):
    name = models.CharField('Name of Cheese', max_length=255)
    slug = AutoSlugField('Cheese Address',
                         unique=True,
                         always_update=False,
                         populate_from='name')
    description = models.TextField('Description', blank=True)

    class Firmness(models.TextChoices):
        UNSPECIFIED = 'unspecified', 'Unspecified'
        SOFT = 'soft', 'Soft'
        SEMI_SOFT = 'semi_soft', 'Semi_soft'
        SEMI_HARD = 'semi_hard', 'Semi_hard'
        HARD = 'hard', 'Hard'
    firmness = models.CharField("Firmness", max_length=20, choices=Firmness.choices, default=Firmness.UNSPECIFIED)
    country_of_origin = CountryField("Country of Origin", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return absolute URL to the Cheese Detail page."""
        return reverse(
            'cheeses:detail', kwargs={'slug': self.slug}
        )

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )
