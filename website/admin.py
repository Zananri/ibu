from django.contrib import admin
from .models import HeaderImage, Gallery

@admin.register(HeaderImage)
class HeaderImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'image')  # Menampilkan ID, deskripsi, dan gambar
    list_filter = ('description',)  # Memungkinkan filter berdasarkan deskripsi
    search_fields = ('description',)  # Memungkinkan pencarian berdasarkan deskripsi


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')  # Menampilkan ID, judul, dan gambar
    list_filter = ('title',)  # Memungkinkan filter berdasarkan judul
    search_fields = ('title', 'description')  # Memungkinkan pencarian berdasarkan judul dan deskripsi
