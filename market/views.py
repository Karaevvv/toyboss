from django.shortcuts import render
from market.models import Product, Publication, AboutCompany, \
    SocialMediaContact, Recipes

from django.core.paginator import Paginator


from django.views.generic import TemplateView, ListView


class ProductView(TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['products_1'] = Product.objects.filter(category='1')
        context['products_2'] = Product.objects.filter(category='2')
        context['products_3'] = Product.objects.filter(category='3')

        return context


class ProductDetailView(TemplateView):
    template_name = 'product-inner.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.first()
        context['recipes'] = Recipes.objects.first()

        return context


class PublicationView(TemplateView):
    template_name = 'publications.html'

    def get_context_data(self, **kwargs):
        context = {
            'publications': Publication.objects.all(),
            'social_media': SocialMediaContact.objects.first()
        }
        return context


class PublicationInnerView(TemplateView):
    template_name = 'publications-inner.html'

    def get_context_data(self, **kwargs):
        publication_pk = kwargs['pk']
        context = {
            'publication': Publication.objects.get(id=publication_pk),
            'social_media': SocialMediaContact.objects.first()
        }
        return context


class RecipesView(TemplateView):
    template_name = 'recipes.html'

    def get_context_data(self, **kwargs):
        recipes = Recipes.objects.all()

        def post(request):

            object_list = Recipes.objects.all()
            paginator = Paginator(object_list, 2)

            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            return render(request, 'your_template.html', {'page_obj': page_obj})

        '''paginator = Paginator(recipes,2)
        try:
            page_number = self.request.GET['page']
        except KeyError:
            page_number = 1

        page_obj = paginator.get_page(page_number)'''

        context = {
            'recipes': recipes,
            'social_media': SocialMediaContact.objects.first()
        }
        return context


class RecipesInnerView(TemplateView):
    template_name = 'recipes-inner.html'

    def get_context_data(self, **kwargs):
        recipes_pk = kwargs['pk']

        context = {
            'recipe': Recipes.objects.get(id=recipes_pk),
            'social_media': SocialMediaContact.objects.first()
        }
        return context


class AboutCompanyView(TemplateView):
    template_name = 'about-company.html'

    def get_context_data(self, **kwargs):
        context = {
            'about_company': AboutCompany.objects.all(),
            'social_media': SocialMediaContact.objects.first()
        }
        return context


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):

        context = {
            'about_company': AboutCompany.objects.first(),
            'publication': Publication.objects.first(),
            'social_media': SocialMediaContact.objects.first()
        }
        return context









