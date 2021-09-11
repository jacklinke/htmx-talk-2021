from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    setting_one = models.BooleanField(default=False)
    setting_two = models.BooleanField(default=False)
    setting_three = models.BooleanField(default=False)
    setting_four = models.BooleanField(default=False)

    def toggle_setting_one(self):
        if self.setting_one is True:
            self.setting_one = False
        else:
            self.setting_one = True
        self.save()

    def toggle_setting_two(self):
        if self.setting_two is True:
            self.setting_two = False
        else:
            self.setting_two = True
        self.save()

    def toggle_setting_three(self):
        if self.setting_three is True:
            self.setting_three = False
        else:
            self.setting_three = True
        self.save()

    def toggle_setting_four(self):
        if self.setting_four is True:
            self.setting_four = False
        else:
            self.setting_four = True
        self.save()
