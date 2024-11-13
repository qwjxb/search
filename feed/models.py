from django.db import models

# Create your models here.

class Post(models.Model):
    user_id = 1
    title = models.CharField(max_length=150)
    text = models.TextField()
    image = models.ImageField(upload_to='feed-posts',null=True,default=True)
    likes = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    

class Comment(models.Model):
    user_id = 1
    text = models.TextField()
    likes = models.IntegerField()
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self) -> str:
        return self.post.title