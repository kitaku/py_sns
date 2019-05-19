from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Message, Friend, Good
from .forms import  MessageForm, SearchForm, FriendForm, PostForm

from django.db.models import Q
from django.contrib.auth.decorators import login_required

#index
@login_required(login_url='/sns/login/')
def index(request):
    # POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            raise ValueError('invalid form')
        content = request.POST['content']
        msg = Message()
        msg.owner = request.user
        msg.content = content
        msg.image = form.cleaned_data['image']
        msg.save()
        # form.save()
        return redirect(to='/sns')
    elif request.method == 'GET':
        messages = Message.objects.all()
        form = PostForm(request.POST,request.FILES)
    #共通処理
    params = {
        'login_user' : request.user,
        'form' : form,
        'contents' : messages,
    }
    return render(request, 'sns/index.html' , params)

#メッセージPOST処理
@login_required(login_url='/sns/login/')
def post(request):
    # POST送信時の処理
    if request.method == 'POST':
        content = request.POST['content']

        msg = Message()
        msg.owner = request.user
        msg.content = content
        msg.save()

        messages.success(request, '新しいメッセージを投稿しました!')
        return redirect(to='/sns')

    # else:
    #     form = PostForm(request.user)

    if request.method == 'GET':
        form = PostForm(request.POST)

    params = {
        'login_user' : request.user,
        'form' : form,
    }
    return render(request, 'sns/post.html', params)

#投稿をシェアする
@login_required(login_url='/sns/login')
def share(request, share_id):
    share = Message.objects.get(id=share_id)

    if request.method == 'POST':

        content = request.POST['content']

        msg = Message()
        msg.owner = request.user
        msg.content = content
        msg.share_id = share.id
        msg.save()
        share_msg = msg.get_share()
        share_msg.share_count +=1
        share_msg.save()

        messages.success(request, 'メッセージをシェアしました!')
        return redirect(to='/sns')

    if request.method == 'GET':
        form = PostForm(request.POST)

    # form = PostForm(request.user)
    params = {
        'login_user' : request.user,
        'form' : form,
        'share' : share,
    }
    return render(request, 'sns/share.html', params)

#goodボタン
@login_required(login_url='/sns/login')
def good(request, good_id):
    good_msg = Message.objects.get(id = good_id)
    #good数を調べる
    is_good = Good.objects.filter(owner = request.user).filter(message=good_msg).count()
    #0より大きければ既にgood済み
    print(is_good)
    if is_good % 2 != 0:
        # messages.success(request, '既にメッセージにはGoodしています。')
        good_msg.good_count -=1
        good_msg.save()
        good = Good()
        good.owner = request.user
        good.message = good_msg
        good.save()
        return redirect(to='/sns')
    else:
        #Messageのgood_countを増やす
        good_msg.good_count +=1
        good_msg.save()
        good = Good()
        good.owner = request.user
        good.message = good_msg
        good.save()

        messages.success(request, 'メッセージにグッドしました!')
        return redirect(to='/sns')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'sns/signup.html', {'form' : form})
