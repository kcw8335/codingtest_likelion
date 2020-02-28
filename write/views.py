from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.views.generic.base import View
from django.http import HttpResponseForbidden
from urllib.parse import urlparse

from django.views.generic.list import ListView


from django.contrib.auth.models import User

from django.core.paginator import Paginator

from .models import Account
from .models import Subject_range
from .models import Subject_code    
from .models import Subject    
from .models import Evaluation
from .models import Write_index
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from hitcount.views import HitCountDetailView


#class형 뷰의 generic view를 이용하여 구현

class BoardIndex(ListView):
    model = Subject
    template_name = 'write/index.html'

class BoardSearchlist(ListView):
    model = Subject
    template_name = 'write/searchlist.html'
    subject=Subject.objects.all()

def searchlist(request):
    searchtext=request.GET.get('searchtext','')
    subject=Subject.objects.all()

    if not searchtext == '':
        subject=subject.filter(subject_name__icontains=searchtext)
        return render(request, 'write/searchlist.html', {'subject':subject, 'searchtext':searchtext})
    else:
        return redirect('write/index')

class BoardDetail(ListView):
    model = Subject
    template_name = 'write/detail.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        global page
        context = super(BoardDetail, self).get_context_data(**kwargs)
        paginator = context['paginator']

        #5개씩 잘라서 보여줌
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context


# class BoardCreate(CreateView) : 
#     model = Subject, Evaluation
#     fields = ['writer_id', 'evaluation_text' , 'homework_large','homework_medium','homework_small',' homework_best','team_yes','team_no','team_best','grade_good','grade_bad','grade_f',' grade_best','attendance_speak','attendance_elec','attendance_none','attendance_best','test_3','test_2','test_1','test_0','test_best',]
#     template_name_suffix = '_create'
#     success_url ='/write/detail/'

    
#     로그인한 사람 글쓰기 가능
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         form.instance.autor_id = self.request.user.id
#         if form.is_valid() :
#             form.instance.save()
#             return redirect('/write')
#         else : 
#             return self.render_to_response({'form' : form})
        
        
def create(request):
    return render(request, 'write/create.html')
