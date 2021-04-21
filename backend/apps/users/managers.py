from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Email must be set')

        if not password:
            raise ValueError('Password must be set')

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user
