from django.urls import path

from phonebook.views import ListViewPhoneBook, \
    DetailViewPhoneBook, HomePageView, PhbooCreate, PhbooDelete,\
    PhbooUpdate, SearchResultsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('phonebooks/', ListViewPhoneBook.as_view(), name='phonebooks'),
    path('phonebooks/<slug:slug>/', DetailViewPhoneBook.as_view(), name='phonebook_detail'),
    path('posts/new/', PhbooCreate.as_view(), name='phonebook_new'),
    path('posts/<slug:slug>/delete/', PhbooDelete.as_view(), name='phonebook_delete'),
    path('posts/<slug:slug>/update/', PhbooUpdate.as_view(), name='phonebook_update'),
    path('search/', SearchResultsView.as_view(), name='search_results'),


]