from django.db import models

class User(models.Model):  # или если вы используете расширенную модель, то AbstractUser
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    # добавьте другие поля, если необходимо

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

class Faculty(models.Model): 
    college_uni = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=50)
    question_text = models.TextField()
    faculty_id = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    user_id = 1
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    

class Answer(models.Model):
    answer_text = models.TextField()
    question_id = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    user_id = 1
    likes = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Answer to {self.question_id.name}"
