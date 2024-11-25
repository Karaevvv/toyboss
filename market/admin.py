from django.contrib import admin

from market.models import Product, ProductCategory, Publication, Recipes, AboutCompany, SocialMediaContact


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(SocialMediaContact)
class SocialMediaContactAdmin(admin.ModelAdmin):
    list_display = ('instagram', 'facebook', 'phone_number',)



