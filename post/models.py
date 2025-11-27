# from django.contrib.auth.models import User
# from django.db import models
#
# """"
# Модель Author
# Модель, содержащая объекты всех авторов.
# Имеет следующие поля:
# cвязь «один к одному» с встроенной моделью пользователей User;
# рейтинг пользователя. Ниже будет дано описание того, как этот рейтинг можно посчитать.
# Модель Category
# Категории новостей/статей — темы, которые они отражают (спорт, политика, образование и т. д.). Имеет единственное поле: название категории. Поле должно быть уникальным (в определении поля необходимо написать параметр unique = True).
# Модель Post
# Эта модель должна содержать в себе статьи и новости, которые создают пользователи. Каждый объект может иметь одну или несколько категорий.
# Соответственно, модель должна включать следующие поля:
# связь «один ко многим» с моделью Author;
# поле с выбором — «статья» или «новость»;
# автоматически добавляемая дата и время создания;
# связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory);
# заголовок статьи/новости;
# текст статьи/новости;
# рейтинг статьи/новости.
# Модель PostCategory
# Промежуточная модель для связи «многие ко многим»:
# связь «один ко многим» с моделью Post;
# связь «один ко многим» с моделью Category.
# Модель Comment
# Под каждой новостью/статьёй можно оставлять комментарии, поэтому необходимо организовать их способ хранения тоже.
# Модель будет иметь следующие поля:
# связь «один ко многим» с моделью Post;
# связь «один ко многим» со встроенной моделью User (комментарии может оставить любой пользователь, необязательно автор);
# текст комментария;
# дата и время создания комментария;
# рейтинг комментария.
# """
# from email.policy import default
#
#
# class Author(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     rating = models.IntegerField(default=0)
#
# class Category(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Post(models.Model):
#     news = "NW"
#     articles = "AR"
#     TYPE_CHOICES = ((news, "Новость"),(articles, "Статья"))
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     post_type = models.CharField(max_length=100, choices=TYPE_CHOICES, default=news)
#     Category = models.ManyToManyField(Category, through= "PostCategory")
#     created_at = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100)
#     text = models.TextField()
#     rating = models.IntegerField(default=0)
#
#     def like(self):
#         self.rating +=1
#         self.save()
#
#     def dislike(self):
#         self.rating -= 1
#         self.save()
#
#     def preview(self):
#         if len(self.text)<= 124:
#             return self.text
#         else:
#             return self.text[:124] + "..."
#
#     def get_absolute_url(self):
#         return reverse_lazy('post_detail', kwargs= {'pk': self.pk})
#
#
# class PostCategory(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.category} | {self.post}'
#
#
# class Comment(models.Model):
#     commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
#     commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     dateCreation = models.DateTimeField(auto_now_add=True)
#     rating = models.SmallIntegerField(default=0)