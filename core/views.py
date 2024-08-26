from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post, Reply
from .forms import ReplyForm

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
    reply_count = replies.count()

    # post a reply to the related post 
    if request.method == "POST":
        reply_form = ReplyForm(data=request.POST)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.author = request.user
            reply.related_post = post
            reply.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Reply submitted'
            )


    reply_form = ReplyForm()

    return render(
        request,
        "core/conversation.html",
        {
            "post": post,
            "replies": replies,
            "reply_count": reply_count,
            "reply_form": reply_form,
        },
    )

