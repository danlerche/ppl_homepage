from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import PageChooserPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.contrib.table_block.blocks import TableBlock
from modelcluster.fields import ParentalKey

class HomePage(Page):
    searchBoxTextArea = RichTextField(blank=True)

    feature_one_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    feature_one_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)
    feature_one_text = models.CharField(blank=True, max_length=250)
    feature_two_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    feature_two_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)
    feature_two_text = models.CharField(blank=True, max_length=250)

    content_panels = Page.content_panels + [
        FieldPanel('searchBoxTextArea', classname="Search Box Text Area"),
        PageChooserPanel('feature_one_page'),
        ImageChooserPanel('feature_one_image', classname="full"),
        FieldPanel('feature_one_text', classname="full"),
        PageChooserPanel('feature_two_page'),
        ImageChooserPanel('feature_two_image', classname="full"),
        FieldPanel('feature_two_text', classname="full"),
        InlinePanel('staff_recommends', label="Staff Recommends"),
        ]

class StaffRecommends(Orderable):
    staff_recommends = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='staff_recommends')
    book_cover = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+')
    catalogue_link = models.CharField(max_length=350)
    panels = [ImageChooserPanel('book_cover'),FieldPanel('catalogue_link'),
    ]
