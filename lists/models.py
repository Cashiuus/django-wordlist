from __future__ import unicode_literals
import hashlib

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django_wordlist.base.utils.files import get_file_path


def get_attachment_file_path(instance, filename):
    return get_file_path(instance, filename, "files")


class Wordlist(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    wordlist_file = models.FileField(verbose_name='Wordlist File',
                                     blank=True, null=True,
                                     upload_to=get_attachment_file_path)
    #content_type = models.ForeignKey(ContentType, null=False, blank=False,
    #                                 verbose_name='Content Type')
    type = models.ForeignKey('WordlistType', related_name='rn_typelists')
    family = models.ForeignKey('Family', related_name='rn_familylists',
                               blank=True, null=True)
    format = models.ForeignKey('Format', related_name='rn_formatlists',
                               blank=True, null=True)

    effectiveness_rating = models.IntegerField(verbose_name='Effectiveness Rating',
                                               blank=True, null=True)
    size_rating = models.IntegerField(verbose_name='Size Rating',
                                      blank=True, null=True)

    wordcount = models.IntegerField()

    # TODO: Once it's running, add in a field for the file upload itself
    file_size = models.IntegerField(blank=True, null=True)

    date_origin = models.DateField(verbose_name='Est Date of Origin',
                                   blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    sha1 = models.CharField(max_length=40, default="", blank=True,
                            verbose_name='sha1')

    #def get_file_size(self):

    class Meta:
        verbose_name = _('Wordlist')
        verbose_name_plural = _('Wordlists')
        ordering = ('name',)

    def _generate_sha1(self, blocksize=65536):
        hasher = hashlib.sha1()
        while True:
            buff = self.attached_file.file.read(blocksize)
            if not buff:
                break
            hasher.update(buff)
        self.sha1 = hasher.hexdigest()

    def save(self, *args, **kwargs):
        if not self._importing or not self.modified_date:
            self.modified_date = timezone.now()
        if self.attached_file:
            if not self.sha1 or self.attached_file != self._orig_attached_file:
                self._generate_sha1()
        save = super().save(*args, **kwargs)
        self._orig_attached_file = self.attached_file
        if self.attached_file:
            self.attached_file.file.close()
        return save

    def __str__(self):
        return self.name


class WordlistType(models.Model):
    name = models.CharField(max_length=40, unique=True)
    color = models.CharField(max_length=20, default='#999999')

    class Meta:
        verbose_name = _('Wordlist Type')
        verbose_name_plural = _('Wordlist Types')
        ordering = ('name',)

    def __str__(self):
        return self.name


class Format(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = _('Format')
        verbose_name_plural = _('Formats')
        ordering = ('name',)

    def __str__(self):
        return self.name


class Family(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = _('Family')
        verbose_name_plural = _('Families')
        ordering = ('name',)

    def __str__(self):
        return self.name
