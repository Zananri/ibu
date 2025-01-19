from django.db import models
import os

class HeaderImage(models.Model):
    image = models.ImageField(upload_to='header_images/')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

    def edit_header_image(self, new_image=None, new_description=None):
        if new_image:
            self.image = new_image
        if new_description:
            self.description = new_description
        self.save()

    def delete(self, *args, **kwargs):
        # Menghapus file gambar saat objek dihapus
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)


class Gallery(models.Model):
    title = models.CharField(max_length=255, default='Default Title')  # Menambahkan default
    image = models.ImageField(upload_to='gallery_images/')
    description = models.TextField()

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Menghapus file gambar saat objek dihapus
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)
