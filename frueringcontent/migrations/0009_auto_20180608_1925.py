# Generated by Django 2.0.3 on 2018-06-08 19:25

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('frueringcontent', '0008_auto_20180608_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpage',
            name='body',
            field=wagtail.core.fields.StreamField([('article', wagtail.core.blocks.StructBlock([('banner_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('article_title', wagtail.core.blocks.CharBlock(required=True)), ('article_body', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='title', template='frueringcontent/article/blocks/article_header_block.html')), ('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link'], template='frueringcontent/article/blocks/article_text_block.html')), ('image', wagtail.images.blocks.ImageChooserBlock(template='frueringcontent/article/blocks/article_image_block.html'))]))]))]),
        ),
    ]
