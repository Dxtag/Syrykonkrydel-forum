from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    





class Board(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=200)
    parent = models.ForeignKey("self", verbose_name=_("parent"), on_delete=models.CASCADE, null=True, blank=True, related_name="sub_boards")
    is_archived = models.BooleanField(_("archived"), default=False)
    is_auth_only = models.BooleanField(_("authorized only"), default=False)

    @property
    def is_sub(self)->bool:
        return bool(self.parent)
    
    class Meta:
        verbose_name = _("board")
        verbose_name_plurl = _("boards")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("board_detail", kwargs={"pk": self.pk})
    


class Thread(models.Model):
    name = models.CharField(_("name"), max_length=200)    
    board = models.ForeignKey(Board, verbose_name=_("board"), on_delete=models.CASCADE, related_name="threads") 
    content = models.TextField(_("content"))
    author = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("thread")
        verbose_name_plurl = _("threads")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


