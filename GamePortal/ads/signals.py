from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Comment
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


@receiver(post_save, sender=Comment)
def notify_post(sender, instance, created, **kwargs):
    if created:
        subject = f'Новый отклик к Вашему посту: {instance.news.header}.'
        recipient = instance.news.author
        html_content = render_to_string('mail/new_comment.html', {'sub': recipient, 'news': instance.news, })
    else:
        subject = f'Информация о Вашем отклике.'
        recipient = instance.commentator
        html_content = render_to_string('mail/accept_comment.html', {'sub': recipient, 'news': instance.news, })
    msg = EmailMultiAlternatives(
        subject=subject,
        body=instance.text,
        from_email='elistratishka@yandex.ru',
        to=[recipient.email],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@receiver(post_delete, sender=Comment)
def notify_delete(sender, instance, **kwargs):
    subject = f'Информация о Вашем отклике.'
    recipient = instance.commentator
    html_content = render_to_string('mail/delete_comment.html', {'sub': recipient, 'news': instance.news, })

    msg = EmailMultiAlternatives(
        subject=subject,
        body=instance.text,
        from_email='elistratishka@yandex.ru',
        to=[recipient.email],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
