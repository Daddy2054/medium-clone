from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import UserCreationForm, UserChangeForm
from .models import User  # , Profile, UserFollows


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    list_display = [
        "pkid",
        "id",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    ]
    list_display_links = [
        "pkid",
        "id",
        "email",
    ]
    list_filter = [
        "is_active",
        "is_staff",
        "email",
    ]
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = (
        (
            _("Login Credentials"),
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Personal Info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )
    add_fieldsets = (
        None,
        {
            "classes": ("wide",),
            "fields": (
                "email",
                "first_name",
                "last_name",
                "password1",
                "password2",
            ),
        },
    )
    search_fields = [
        "email",
        "first_name",
        "last_name",
    ]


admin.site.register(User, UserAdmin)
