from django.db import models

PLATFORMS = (
    ('yt', 'Youtube'),
)


class Profile(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    poc = models.BooleanField(default=False)
    lgbtq = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Account(models.Model):
    identifier = models.CharField(max_length=128)
    platform = models.CharField(max_length=8, choices=PLATFORMS)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['identifier', 'platform'], name='unique__platform_account')
        ]

    def __str__(self):
        return "%s: %s" % (self.platform, self.identifier)


class Video(models.Model):
    identifier = models.CharField(max_length=128)
    platform = models.CharField(max_length=8, choices=PLATFORMS)
    title = models.CharField(max_length=128)
    description = models.TextField()
    duration = models.PositiveSmallIntegerField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s" % (self.platform, self.title)
