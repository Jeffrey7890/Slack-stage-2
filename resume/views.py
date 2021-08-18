from django.shortcuts import render
from django.views import generic

from . models import Resume
from . forms import ResumeForm

# def index(request):
#     return render(request, 'resume/index.html')

# def resume(request):
#     return render(request, 'resume/resume.html')


class IndexView(generic.ListView):
    model = Resume
    template_name = 'resume/index.html' 
    context_object_name = 'resume_list'
    def get_queryset(self):
        return Resume.objects.all()

class ResumeView(generic.DetailView):
    model = Resume
    template_name = 'resume/resume.html'
    context_object_name = 'resume_detial'

class ResumeForm(generic.CreateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'resume/resumeform.html'
    # fields = '__all__'

# def resume_form(request):

#     if request.method == 'POST':

#         form = ResumeForm(request.POST)

#         if form.is_valid():

#             return HttpResponseRedirect('/resume/')

#     else:
#         form = ResumeForm()
#     return render(request,'resume/resumeform.html',{'form':form})