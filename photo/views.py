from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic.list import ListView
from .models import Photo
from rest_framework import generics
from .serializers import PhotoListSerializer

class PhotoList(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'

from rest_framework import generics

class PhotoListAPI(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoListSerializer

from django.views.generic.edit import CreateView
class PhotoCreate(CreateView):
    model = Photo
    template_name = 'photo/photo_create.html'
    fields = ['image', 'text']

    def form_valid(self, form):
        if self.request.user.id:
            form.instance.author_id = self.request.user.id
            return super().form_valid(form)
        else:
            return False

class PhotoCreateAPI(generics.CreateAPIView):
    serializer_class = PhotoListSerializer
    def create(self, request, *args, **kwargs):
        if request.user.id:
            request.data['author'] = request.user.id
            return super().create(request, *args, **kwargs)

from django.views.generic.detail import DetailView
class PhotoDetail(DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'

class PhotoDetailAPI(generics.RetrieveAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoListSerializer

# update view, Destroy 뷰
from django.views.generic.edit import UpdateView, DeleteView
class PhotoUpdate(UpdateView):
    model = Photo
    template_name = 'photo/photo_update.html'
class PhotoDelete(DeleteView):
    model = Photo
    template_name = 'photo/photo_delete.html'
    success_url = '/'

class PhotoUpdateAPI(generics.UpdateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoListSerializer

class PhotoDeleteAPI(generics.DestroyAPIView):
    queryset = Photo.objects.all()

# 토큰 인증 기능 추가, 기본 인증, 권한 클래스님

# 1) 인증된 사용자만 API를 사용할 수 있도록 설정 : token 설정
# 2) 특정 동작에 대해 특정 권한을 득한 사용자만 사용할 수 있도록 설정 : permission 클래스 추가
