from django.contrib import admin
from django.contrib.auth.models import Group
from import_export.admin import ImportExportMixin

from .models import (Favorite, Ingredient, IngredientAmount, Recipe,
                     ShoppingList, Tag)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'slug')
    search_fields = ('name',)
    list_filter = ('name', 'slug')
    empty_value_display = '-пусто-'


class IngredientAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'measurement_unit'
    )
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class IngredientAmountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ingredient',
        'recipe',
        'amount'
    )
    empty_value_display = '-пусто-'


class IngredientsInline(admin.TabularInline):
    model = Ingredient


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'name',
        'image',
        'text',
        'is_favorited',
        'ingredients',
    )
    search_fields = ('author', 'name')
    list_filter = ('author', 'name', 'tags')
    empty_value_display = '-пусто-'

    def is_favorited(self, obj):
        return obj.favorites.count()

    def ingredients(self, obj):
        return list(obj.ingredients.all())
    ingredients.short_description = 'Ингредиенты'


class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe',
    )
    empty_value_display = '-пусто-'


class ShoppingListAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe',
    )
    empty_value_display = '-пусто-'


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(ShoppingList, ShoppingListAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(IngredientAmount, IngredientAmountAdmin)
admin.site.unregister(Group)
