from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Count
from .models import Post, Reply, Topic
from .forms import ReplyForm, PostForm

#Create your views here.
class PostList(generic.ListView):
    model = Post
    template_name = "core/index.html"
    context_object_name = "post_list"
    paginate_by = 6

    def get_queryset(self):
        sort_by = self.request.GET.get('sort', 'latest')

        if sort_by == 'discussed':
            queryset = Post.objects.annotate(reply_count=Count('post_replies')).order_by('-reply_count')
        elif sort_by == 'liked':
            queryset = Post.objects.annotate(total_likes=Count('likes')).order_by('-total_likes')
        else:
            queryset = Post.objects.annotate(reply_count=Count('post_replies')).order_by('-created_on')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort_by'] = self.request.GET.get('sort', 'latest')
        return context

# View to display all topics
class TopicList(generic.ListView):
    model = Topic
    template_name = "core/topic_list.html"
    context_object_name = "topics"

# View to display posts related to a specific topic
class TopicPostList(generic.ListView):
    model = Post
    template_name = "core/topic_posts.html"
    context_object_name = "post_list"

    def get_queryset(self):
        # Filter posts by topic based on the topic ID in the URL
        topic = get_object_or_404(Topic, pk=self.kwargs['pk'])
        return Post.objects.filter(topic=topic)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic'] = get_object_or_404(Topic, pk=self.kwargs['pk'])
        return context


def conversation(request, slug):
    post = get_object_or_404(Post, slug=slug)
    replies = Reply.objects.filter(related_post=post).order_by('-created_on')
    reply_count = replies.count()

    reply_form = ReplyForm()

    if request.method == "POST":
        reply_id = request.POST.get('reply_id')
        
        if reply_id:  # This handles the edit reply form
            try:
                reply = Reply.objects.get(pk=reply_id)
                if reply.author == request.user:  # Ensure that only the author can edit the reply
                    reply_form = ReplyForm(data=request.POST, instance=reply)
                    if reply_form.is_valid():
                        reply_form.save()
                        messages.success(request, 'Reply updated successfully.')
                    else:
                        messages.error(request, 'Failed to update reply.')
                else:
                    messages.error(request, 'You are not allowed to edit this reply.')
            except Reply.DoesNotExist:
                messages.error(request, 'Reply does not exist.')
            return redirect('conversation', slug=slug)
        else:  # This handles creating a new reply
            reply_form = ReplyForm(data=request.POST)
            if reply_form.is_valid():
                reply = reply_form.save(commit=False)
                reply.author = request.user
                reply.related_post = post
                reply.save()
                messages.success(request, 'Reply submitted successfully.')
            else:
                messages.error(request, 'Failed to submit reply.')
            return redirect('conversation', slug=slug)

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

def reply_edit(request, slug, reply_id):
    """
    view to edit a reply
    """
    if request.method == "POST":
        post = get_object_or_404(Post, slug=slug)
        reply = get_object_or_404(Reply, pk=reply_id)

        reply_form = ReplyForm(data=request.POST, instance=reply)

        if reply_form.is_valid() and reply.author == request.user:
            reply = reply_form.save(commit=False)
            reply.post = post
            reply.save()
            messages.add_message(request, messages.SUCCESS, 'Reply Updated!')
        else: messages.add_message(request, messages.ERROR, 'Error updating Reply!')

    return redirect('conversation', slug=slug)