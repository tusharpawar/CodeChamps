from django.shortcuts import render_to_response
from django.template import RequestContext
from problems.models import problem
from django.core.files import File
from .form import SubmissionForm
from .models import Submissions
import subprocess
import time
from Developers.models import Developer
from .models import Solved

# Create your views here.
def AllProblems(request):
    if request.user.is_authenticated():
        dev=Developer.objects.get(user=request.user)
        try:
            solved=Solved.objects.all().filter(username=request.user.username)
        except:
            solved=None
    #print solved.username
    problems=problem.objects.all().order_by('id')
    context={'question':problems,'developer':dev,'solved':solved}
    return render_to_response('Practice.html',context,context_instance=RequestContext(request));

def SpecificProblem(request,title):
    problem1=problem.objects.get(title=title)
    context={'question':problem1}
    problem1.body="<br>".join(problem1.body.split("\n"))
    problem1.output_format="<br>".join(problem1.output_format.split("\n"))

    return render_to_response('problem.html',context,context_instance=RequestContext(request));


def home(request):
    context={}
    template="index.html"
    return render(request,template,context)

##def CreateFile(request):
##    f=open('//problems//hello.txt','w')
##    myfile=File(f)
##    myfile.write('writing in file succesfully')
##    myfile.closed()
##    f.closed()
##    context={}
##    return render(request,'submission.html',context)

#upload file for submission
def upload_submission(request,title):
    form=SubmissionForm(request.POST, request.FILES)
    submsn=None
    developer=Developer.objects.get(user=request.user)

    print 1
    if request.method == 'POST':
        print 2
        if form.is_valid():
            
            #dev=Developer.objects.get(user=form.cleaned_data['developer']) #it is a forign key to get the dynamic file path for submission
            #print form.cleaned_data['developer']
            submsn=Submissions.objects.get_or_create(name=request.user.username)
            #print submsn[0].Code
           # if not submsn.code:
            #    submsn.code.delete(True)
            #else:
            
            submsn[0].Code=request.FILES['codefile']
            #submsn[0].developer=dev
            submsn[0].save()
            print submsn[0].name
            lang=form.cleaned_data['lang_used']
            if(lang=='java'):
                run_batch_java(request)
            elif(lang=='cpp'):
                run_batch_cpp(request)
            elif(lang=='c'):
                run_batch_c(request)
            elif(lang=='python'):
                run_batch_python(request)
            time.sleep(1)
            compile_log,run_log,check_log=read_file(request,title)
            #submsn[0].Code.delete(True)
             #p=subprocess.Popen('submissions/sh.bat')
            return render_to_response('submission.html',{'Message':'file uploaded succesfully','compile_log':compile_log,'run_log':run_log,'check_log':check_log,'developer':developer,'Submissions':submsn[0]})
        else:
            Error="file invalid"
            return render_to_response('problem.html', {'form':form,'Submissions':submsn[0],'developer':developer,'error':Error},context_instance=RequestContext(request) )
    else:
            Error="Empty"
            return render_to_response('submission.html', {'form':form,'Submissions':submsn,'developer':developer,'error':Error},context_instance=RequestContext(request) )

        
#to run batch file
def run_batch_java(request):
    usrnm=request.user.username
    if(subprocess.Popen('F://tysem2project/project/tmpcodeCHamp/CodeChamps/static/media/submissions/'+usrnm+'/sh_java.bat')):
        
        return True
    else:
        return False
    
def run_batch_cpp(request):
    usrnm=request.user.username
    if(subprocess.Popen('F://tysem2project/project/tmpcodeCHamp/CodeChamps/static/media/submissions/'+usrnm+'/sh_cpp.bat')):
        
        return True
    else:
        return False
    
def run_batch_c(request):
    usrnm=request.user.username
    if(subprocess.Popen('F://tysem2project/project/tmpcodeCHamp/CodeChamps/static/media/submissions/'+usrnm+'/sh_c.bat')):
        
        return True
    else:
        return False
    
def run_batch_python(request):
    usrnm=request.user.username
    print usrnm
    #path='F://tysem2project/project/CodeChamps/static/media/submissions/'+usrnm+'/sh_python.bat'
    #print subprocess.Popen(path)
    if(subprocess.Popen('F://tysem2project/project/tmpcodeCHamp/CodeChamps/static/media/submissions/'+usrnm+'/sh_python.bat')):
        
        return True
    else:
        return False

def read_file(request,title):
    usrnm=request.user.username
    file1=open('F://tysem2project/project/tmpcodeCHamp/CodeChamps/static/media/submissions/'+usrnm+'/compile.txt')
    compile_log= file1.read()
    file2=open('F://tysem2project/project/tmpcodeCHamp/CodeChamps/static/media/submissions/'+usrnm+'/run.txt')
    run_log=file2.read()
    input_file=open('F://tysem2project/project/tmpcodeCHamp/CodeChamps/static/media/output/helloworld_out.txt')
    out_log=input_file.read()
    check_log=""
    print out_log+"\n"
    print run_log
    print out_log==run_log
    if(out_log!=run_log):
        check_log+="not accepted"
        print check_log
    else:
        check_log+="accepted"
        solved=Solved.objects.get_or_create(problemname=title)
        solved.username=usrnm
        solved.marks=100
        
    run_log="<br>".join(run_log.split("\n"))
    compile_log="<br>".join(compile_log.split("\n"))
    print run_log
    return(compile_log,run_log,check_log)
    
    
    
#def display_file(request):
    
##def update_file(request):
##    #file = UploadedFile.objects.get(pk=id)
##    if request.method == "POST":
##       from django.core.files import File
##       f = open(file.docfile.path,'w+b')
##       content = request.POST['content']
##       f.write(content)
##       file.docfile = File(f)
##       file.save()
##       return HttpResponseRedirect('/home/')
##    else:
##       docfile = file.docfile.read()
##       return render_to_response('update_file.html',{'file':file,  'docfile' :
##                   docfile}, context_instance=RequestContext(request))
##
