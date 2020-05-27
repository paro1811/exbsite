from django.db import models
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from io import BytesIO

# Create your models here.
#class User(models.Model):
	#user_id = models.AutoField(primary_key=True)
#	user_name = models.CharField(max_length=50)
#	user_email = models.EmailField(max_length=254)
#	user_grade = models.CharField(max_length=5)
#
#	def __str__(self):
#		return self.user_name


class Post(models.Model):
    GRADES = (
    ("","Select your grade..."),
    ('Grade 5 Red','Grade 5 Red'),
    ('Grade 5 Blue','Grade 5 Blue'),
    ('Grade 5 White','Grade 5 White')
    )
    post_id = models.AutoField(primary_key=True)
    post_author = models.CharField(max_length=300)
    post_grade = models.CharField(max_length=30, choices=GRADES)
    post_email = models.EmailField(max_length=500)
  #user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    post_title = models.CharField(max_length=100)
    post_text = models.TextField(max_length=500)

    def __str__(self):
        return self.post_title


class Picture(models.Model):
    pic_id = models.AutoField(primary_key= True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg', blank = True)
    
    def __str__(self):
        return self.pic.name

    def shrink_image(self):
        print('----> in shrink_image')
        if self.pic:
            img_field = self.pic
            img_path = str(img_field.name)
            img_name = img_path[img_path.find('/')+1:]
            print(img_path)
            print(img_name)
            img = Image.open(img_field)
            print(img)
            img.thumbnail((400,400))
            buffer = BytesIO()
            img.save(fp=buffer,format='jpeg')
            cf = ContentFile(buffer.getvalue())
            self.pic.delete()
            self.pic.save(img_name,InMemoryUploadedFile(
                cf,
                None,
                '',
                'image/jpeg',
                cf.tell,
                None)
            )

