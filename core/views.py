from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Reply

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "core/index.html"
    paginate_by = 6


def conversation(request, slug):
    """ Display the conversation of the Forum post
    **Context**

    ``post``
        An instance of :model: `core.post`

    **Template:**

    :template:  `core/conversation.html`
    """

    # Get the post by slug
    post = get_object_or_404(Post, slug=slug)

    # Get all replies related to the post, ordered by creation date
    replies = Reply.objects.filter(related_post=post).order_by('created_on')

    return render(
        request,
        "core/conversation.html",
        {
            "post": post,
            "replies": replies,
        },
    )

