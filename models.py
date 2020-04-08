from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.admin.edit_handlers import PageChooserPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.contrib.table_block.blocks import TableBlock
from modelcluster.fields import ParentalKey

class HomePage(Page):

    background_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)
    searchBoxTextArea = RichTextField(blank=True, verbose_name="Search Box Text Area",)

    feature_one_page = models.ForeignKey('wagtailcore.Page',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',)
    feature_one_doc = models.ForeignKey('wagtaildocs.Document',null=True,blank=True,on_delete=models.SET_NULL,related_name='+', verbose_name="Link to a document instead of a page",)
    feature_one_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)
    feature_one_text = models.CharField(blank=True, max_length=250)
    
    feature_two_page = models.ForeignKey('wagtailcore.Page',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',)
    feature_two_doc = models.ForeignKey('wagtaildocs.Document',null=True,blank=True,on_delete=models.SET_NULL,related_name='+', verbose_name="Link to a document instead of a page",)
    feature_two_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)
    feature_two_text = models.CharField(blank=True, max_length=250)

    feature_three_page = models.ForeignKey('wagtailcore.Page',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',)
    feature_three_doc = models.ForeignKey('wagtaildocs.Document',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name="Link to a document instead of a page",)
    feature_three_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)
    feature_three_text = models.CharField(blank=True, max_length=250)

    feature_four_page = models.ForeignKey('wagtailcore.Page',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',)
    feature_four_doc = models.ForeignKey('wagtaildocs.Document',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name="Link to a document instead of a page",)
    feature_four_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)
    feature_four_text = models.CharField(blank=True, max_length=250)

    newsletter_doc = models.ForeignKey('wagtaildocs.Document',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',)
    newsletter_image  = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)
    newsletter_text = models.CharField(blank=True, max_length=250)

    content_panels = [

        MultiFieldPanel(
            [

                ImageChooserPanel('background_image', classname="full"),
                FieldPanel('searchBoxTextArea', classname="full"),
            ],

            heading = "Background Image Area",
            classname = "collapsible"
            ),

        MultiFieldPanel(
            [

                ImageChooserPanel('feature_one_image', classname="full"),
                PageChooserPanel('feature_one_page'),
                DocumentChooserPanel('feature_one_doc', classname="full"),
                FieldPanel('feature_one_text', classname="full"),
            ],

            heading = "Feature One Options",
            classname = "collapsible collapsed"
            ),

        MultiFieldPanel(
            [

                ImageChooserPanel('feature_two_image', classname="full"),
                PageChooserPanel('feature_two_page'),
                DocumentChooserPanel('feature_two_doc'),
                FieldPanel('feature_two_text', classname="full"),
            ],

            heading = "Feature two Options",
            classname = "collapsible collapsed"
            ),

        MultiFieldPanel(
            [
                ImageChooserPanel('newsletter_image', classname="full"),
                DocumentChooserPanel('newsletter_doc'),
                FieldPanel('newsletter_text', classname="full"),
            ],

            heading = "Newsletter Feature",
            classname = "collapsible collapsed"
            ),

        MultiFieldPanel(
            [

                ImageChooserPanel('feature_three_image', classname="full"),
                PageChooserPanel('feature_three_page'),
                DocumentChooserPanel('feature_three_doc'),
                FieldPanel('feature_three_text', classname="full"),
            ],

            heading = "Feature three Options",
            classname = "collapsible collapsed"
            ),

         MultiFieldPanel(
            [

                ImageChooserPanel('feature_four_image', classname="full"),
                PageChooserPanel('feature_four_page'),
                DocumentChooserPanel('feature_four_doc'),
                FieldPanel('feature_four_text', classname="full"),
            ],

            heading = "Feature four Options",
            classname = "collapsible collapsed"
            ),

         MultiFieldPanel(
            [

                InlinePanel('staff_recommends', label="Staff Recommends"),
            ],

            heading = "Staff Recommends ",
            classname = "collapsible collapsed"
            ),

          MultiFieldPanel(
            [
                InlinePanel('program_slider', label="Program Slider"),

            ],

            heading = "Featured Programs ",
            classname = "collapsible collapsed"
            ),


    ]


class StaffRecommends(Orderable):
    staff_recommends = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='staff_recommends')
    book_cover = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+')
    catalogue_link = models.CharField(max_length=350)
    #rwl_choices = (
    #('R', 'read'),
    #('W', 'watch'),
    #('L', 'listen'),
    #)
    #read_watch_listen = models.CharField(max_length=1, choices=rwl_choices)
    panels = [ImageChooserPanel('book_cover'),FieldPanel('catalogue_link'),#FieldPanel('read_watch_listen'), 
    ]

class ProgramSlider(Orderable):
    program_slider = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='program_slider')
    program_slider_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',)
    program_slider_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+')
    panels = [PageChooserPanel('program_slider_link'),ImageChooserPanel('program_slider_image'),
    ]