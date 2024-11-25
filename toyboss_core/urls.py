"""
URL configuration for toyboss_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from market.views import ProductView, PublicationView, AboutCompanyView, HomeView,  RecipesView, \
     PublicationInnerView, RecipesInnerView, ProductDetailView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('products/', include([
        path('', ProductView.as_view(), name='category_list'),
        path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    ])),

    path('publications/', include([
        path('', PublicationView.as_view(), name='publication_list'),
        path('<int:pk>/', PublicationInnerView.as_view(), name='publication_detail'),
    ])),

    path('about-company/', AboutCompanyView.as_view(), name='about_company'),

    path('home/', HomeView.as_view(), name='home'),

    path('recipes/', include([
        path('', RecipesView.as_view(), name='recipes_list'),
        path('<int:pk>/', RecipesInnerView.as_view(), name='recipe_detail'),
    ])),

    path('publications-inner/<int:pk>/', PublicationInnerView.as_view(), name='publication_inner')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
