from django.shortcuts import render

from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountain.jpg",
        "author": "Fidel",
        "date": date(2024, 1, 20),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like a good view from a mountain!",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Volutpat sed cras ornare arcu dui. Faucibus purus in massa tempor nec feugiat. Vitae tempus quam pellentesque nec. Libero enim sed faucibus turpis in. Id neque aliquam vestibulum morbi blandit cursus risus. Eget duis at tellus at urna. Ut diam quam nulla porttitor massa id. Quam viverra orci sagittis eu. Arcu felis bibendum ut tristique. Pellentesque adipiscing commodo elit at imperdiet dui accumsan sit amet. Morbi tincidunt ornare massa eget egestas purus viverra. Placerat duis ultricies lacus sed turpis tincidunt id."
    },
    {
        "slug": "programming-coding",
        "image": "coding.jpg",
        "author": "Fidel",
        "date": date(2023, 12, 15),
        "title": "Programming is incredible!",
        "excerpt": "If you can learn and enjoy at the same time, it will be fun!",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Volutpat sed cras ornare arcu dui. Faucibus purus in massa tempor nec feugiat. Vitae tempus quam pellentesque nec. Libero enim sed faucibus turpis in. Id neque aliquam vestibulum morbi blandit cursus risus. Eget duis at tellus at urna. Ut diam quam nulla porttitor massa id. Quam viverra orci sagittis eu. Arcu felis bibendum ut tristique. Pellentesque adipiscing commodo elit at imperdiet dui accumsan sit amet. Morbi tincidunt ornare massa eget egestas purus viverra. Placerat duis ultricies lacus sed turpis tincidunt id."
    },
    {
        "slug": "view-of-the-woods",
        "image": "woods.jpg",
        "author": "Fidel",
        "date": date(2024, 1, 17),
        "title": "Journey through the woods",
        "excerpt": "Walking through the woods can turn into an adventure!",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Volutpat sed cras ornare arcu dui. Faucibus purus in massa tempor nec feugiat. Vitae tempus quam pellentesque nec. Libero enim sed faucibus turpis in. Id neque aliquam vestibulum morbi blandit cursus risus. Eget duis at tellus at urna. Ut diam quam nulla porttitor massa id. Quam viverra orci sagittis eu. Arcu felis bibendum ut tristique. Pellentesque adipiscing commodo elit at imperdiet dui accumsan sit amet. Morbi tincidunt ornare massa eget egestas purus viverra. Placerat duis ultricies lacus sed turpis tincidunt id."
    }
]

def get_date(post):
    return post.get('date')

# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })