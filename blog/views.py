from django.db.models import Q
from hitcount.models import HitCount
from hitcount.views import HitCountMixin, get_hitcount_model
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from blog.models import Sungla, About, Haqida, Carusel, Foydalanuvchi
from .forms import ContactForm, CommentForm
# Create your views here.


def about(request):
    about = About.objects.all()
    context = {
        'about': about
    }
    return render(request, 'about.html', context=context)


class AboutUpdateView(UpdateView):
    model = About
    fields = ('name', 'img', 'bio', 'status', 'slug',)
    template_name = 'AboutUpdateView.html'


class AboutDeleteView(DeleteView):
    model = About
    template_name = 'AboutDeleteView.html'
    success_url = reverse_lazy('index')


def glasses(request):
    sun = Sungla.objects.all()

    context = {
        'sun': sun,
    }
    return render(request, 'glasses.html', context=context)


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h1>Sorovingiz qabul qilindi </h1>")
    context = {
        'form': form
    }
    return render(request, 'contact.html', context=context)


def index(request):
    sun = Sungla.objects.all()
    about = About.objects.all()
    haqida = Haqida.objects.all()
    carus = Carusel.objects.all()
    context = {
        'sun': sun,
        'about':about,
        'haqida': haqida,
        'carus': carus
    }
    return render(request, 'index.html', context=context)


def product(request):
    return render(request, 'product.html', context={})


def remot(request):
    return render(request, 'remot.html', context={})


def shop(request):
    haqida = Haqida.objects.all()
    context = {
        'haqida': haqida
    }
    return render(request, 'shop.html', context=context)


class HaqidaUpdateView(UpdateView):
    model = Haqida
    fields = ('name', 'img', 'status', 'bio','slug',)
    template_name = 'HaqidaUpdateView.html'


class HaqidaDeleteView(DeleteView):
    model = Haqida
    template_name = 'HaqidaDeleteView.html'
    success_url = reverse_lazy('index')


def video(request):
    return render(request, 'video.html', context={})


def sunDetailView(requests, sun):
    sun = get_object_or_404(Sungla, slug=sun)
    context = {
        'sun': sun
    }
    return render(requests, 'sunDetail.html', context=context)


def aboutVVV(request, id):
    about = get_object_or_404(About, id=id)
    context = {}
    # hitcount logic
    hit_count = get_hitcount_model().objects.get_for_object(about)
    hits = hit_count.hits
    hitcontext = context['hitcout'] = {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits

    comments = about.comments.filter(active=True)
    comment_count = comments.count()
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.products = about
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    context = {
        'about': about,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'comment_count': comment_count
    }
    return render(request, 'aboutDetail.html', context=context)


def haqidaDetailView(requests, haqida):
    haqida = get_object_or_404(Haqida, slug=haqida)
    context = {
        'haqida': haqida
    }
    return render(requests, 'haqidaDetail.html', context=context)


def caruselDetailView(requests, carus):
    carus = get_object_or_404(Carusel, slug=carus)
    context = {
        'carus': carus
    }
    return render(requests, 'carusDetail.html', context=context)


class SunlaCreateView(CreateView):
    model = Sungla
    fields = ('slug', 'img', 'name', 'price')
    template_name = 'suns_create.html'


class SunglaUpdateView(UpdateView):
    model = Sungla
    fields = ('slug', 'img', 'name', 'price')
    template_name = 'SunglaUpdateView.html'


class SunglaDeleteView(DeleteView):
    model = Sungla
    template_name = 'SunglaDeleteView.html'
    success_url = reverse_lazy('index')


class SearchResultslist(ListView):
    model = Haqida
    template_name = 'search_result.html'
    context_object_name = 'barcha_kozoynaklar'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Haqida.objects.filter(
            Q(name__icontains=query) | Q(bio__icontains=query)
        )

