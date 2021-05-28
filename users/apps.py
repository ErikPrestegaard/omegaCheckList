from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        #Reccomended by the documentation
        #
        import users.signals