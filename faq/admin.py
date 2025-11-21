from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, FAQTopic, FAQArticle

# Personaliza o Admin do CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'full_name', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('full_name', 'profile_image')}),
    )

# Configurações do Artigo FAQ
class FAQArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'is_frequent', 'created_at')
    list_filter = ('topic', 'is_frequent')
    search_fields = ('title', 'content')
    filter_horizontal = ('similar_articles',) # Para um melhor widget de Many-to-Many

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(FAQTopic)
admin.site.register(FAQArticle, FAQArticleAdmin)