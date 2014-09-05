from django.core.management.base import BaseCommand, CommandError
from mainapp.models import news, comment, userinfo, baseinfo, project, projectmember

class Command(BaseCommand):
    args = '<userinfo_id userinfo_id ...>'

    def handle(self, *args, **options):
        for userinfo_id in args:
            try:
                target = userinfo.objects.get(pk=int(userinfo_id))
            except target.DoesNotExist:
                raise CommandError('userinfo_ "%s" does not exist' % userinfo_id)

            target.programmer = True
            target.save()

            self.stdout.write('Successfully programmed "%s"' % userinfo_id)