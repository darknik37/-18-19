import random
from .models import Post

post_types = ['NW', 'AR']

authors_ids = [5, 6, 7, 8, 9]

def gen_post():
    for i in range(4, 50):
        kwargs = {
            'author_id': random.choice(authors_ids),
            'post_type': random.choice(post_types),
            'title': f'Заголовок поста {i}',
            'text': f'Содержание поста {i}'
        }

        Post.objects.create(**kwargs)
    print('Все посты успешно созданы!')

