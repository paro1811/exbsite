from django.db import models

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

