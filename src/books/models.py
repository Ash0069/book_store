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

        # # qrcode_img = qrcode.make('Hello')
        # # qrcode_img.save('1.png')
        # qrcode_img = qrcode.make(self.book_id)
        # fname = f'qr_code-{self.title}.png'
        # buffer = BytesIO()
        # self.qr_code.save(fname, File(buffer), save=False)

        # canvas = Image.new('RGB', (200, 200), 'white')
        # canvas.paste(qrcode_img)
        # canvas.save(buffer, 'PNG')
        # canvas.close()

        super().save(*args, **kwargs)