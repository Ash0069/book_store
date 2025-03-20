from django.db import models
from publishers.models import Publisher
from authors.models import Author
from django.utils.text import slugify
import uuid
#imports for qrcode
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
# Create your models here.

class BookTitle(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Book : {self.title}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Book(models.Model):
    title = models.ForeignKey(BookTitle, on_delete=models.CASCADE)
    book_id = models.CharField(max_length=24, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
    
    def save(self, *args, **kwargs):
        if not self.book_id:
            self.book_id = str(uuid.uuid4()).replace("-", "")[:24].lower()

            #qrcode
            qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
            qr.add_data(self.book_id)
            qr.make(fit = True)
            img = qr.make_image(fill_color = 'black', back_color = 'white')
            buffer = BytesIO()
            img.save(buffer, format='PNG')
            buffer.seek(0)
            file_name = f'qr_code-{self.book_id}.png'
            self.qr_code.save(file_name, File(buffer), save=False)

        super().save(*args, **kwargs)