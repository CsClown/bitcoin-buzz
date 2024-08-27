from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Count
from .models import Post, Reply
from .forms import ReplyForm, PostForm

Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.annotate(reply_count=Count('post_replies')).order_by('-created_on')
    template_name = "core/index.html"
    paginate_by = 6


# def index(request):
#     sort_by = request.GET.get('sort', 'latest')

#     if sort_by == 'discussed':
#         queryset = Post.objects.annotate(reply_count=Count('post_replies')).order_by('-reply_count')
#     elif sort_by == 'liked':
#         queryset = Post.objects.annotate(total_likes=Count('likes')).order_by('-total_likes')
#     else:
#         queryset = Post.objects.annotate(reply_count=Count('post_replies')).order_by('-created_on')

#     context = {
#         'post_list': queryset,
#         'sort_by': sort_by,
#     }
#     return render(request, 'core/index.html', context)

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

def post_delete(request, slug, post_id):
    """
    view to delete post
    """

    post = get_object_or_404(Post, slug=slug)

    if post.author == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Post deleted!')
    else:
        messages.add_message(request, messages.ERROR, "You can only delete your own posts")
    return redirect('home')


def reply_delete(request, slug, reply_id):
    """
    view to delete reply
    """

    post = get_object_or_404(Post, slug=slug)
    reply = get_object_or_404(Reply, pk=reply_id)

    if reply.author == request.user:
        reply.delete()
        messages.add_message(request, messages.SUCCESS, 'Reply deleted!')
    else: 
        messages.add_message(request, messages.ERROR, "You can only delete your own reply!")

    return HttpResponseRedirect(reverse('conversation', args=[slug]))

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post has been created')
            return redirect('home')
    else: 
        form = PostForm()
    
    return render(request, 'core/post_form.html', {'form': form})

@login_required
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('conversation', slug=slug)
