from django.shortcuts import render
from .models import HeaderImage, Gallery

def home(request):
    # Mengambil gambar header pertama (sesuaikan logika Anda jika ada lebih dari satu gambar)
    header_image = HeaderImage.objects.first()  # Anda bisa menyesuaikan logika query ini
    
    # Ambil 5 gambar pertama dari galeri
    galleries = Gallery.objects.all()
    
    # Render ke template dengan context yang sesuai
    return render(request, 'website/home.html', {
        'header_image': header_image,
        'galleries': galleries,
    })
