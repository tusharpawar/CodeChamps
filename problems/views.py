from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.files import File
import os
import signal
import filecmp
import subprocess
import time
from problems.models import problem
from .form import SubmissionForm
from .models import Submissions
from Developers.models import Developer

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Create your views here.
def AllProblems(request):
    
    if request.user.is_authenticated():
        dev=Developer.objects.get(user=request.user)
        try:
            solved_list=dev.problems_list
            solved_map={}
            solve_arr=solved_list.split()
            for i in solve_arr:
                print i
                k=i.index('.')
                A=int(i[:k])
                B=(int)(i[k+1:])
                solved_map[A]=B  

        except:
            print 'U got the wrong username'
    else:
        dev=None
        solved_list=None
        solved_map=None
    
    problems=problem.objects.all().order_by('id')
    context={'question':problems,'developer':dev,'solved':solved_list,'solved_map':solved_map}
    return render_to_response('Practice.html',context,context_instance=RequestContext(request));

def SpecificProblem(request,title):
    problem1=problem.objects.get(title=title)
    
    problem1.body="<br>".join(problem1.body.split("\n"))
    problem1.input_format="<br>".join(problem1.input_format.split("\n"))
    problem1.output_format="<br>".join(problem1.output_format.split("\n"))
    try:
        dev=Developer.objects.get(user=request.user)
        if dev:
            solved_list=dev.problems_list.split()
    except:
        dev=None
        solved_list=None
    
    print solved_list
    marks='N/A'
    if solved_list!=None:
        for sol in solved_list:
            i=sol.index('.')
            k=int (sol[:i])
            print k,k==problem1.id

            if(k==problem1.id):
                marks=int(sol[i+1:])
                break

    context={'question':problem1,'marks':marks} 
    return render_to_response('problem.html',context,context_instance=RequestContext(request));


def home(request):
    context={}
    template="index.html"
    return render(request,template,context)


#upload file for submission
def upload_submission(request,title):
    form=SubmissionForm(request.POST, request.FILES)
    submsn=None
    if(request.user.is_authenticated()):
        developer=Developer.objects.get(user=request.user)
    else:
        developer=None

    print 1
    if request.method == 'POST':
        print 2
        if form.is_valid():
            submsn=Submissions.objects.get_or_create(name=request.user.username)
            submsn[0].Code=request.FILES['codefile']
            submsn[0].save()
            print submsn[0].name
            lang=form.cleaned_data['lang_used']
            if(lang=='java'):
                flg,status=run_batch_java(request,title)
            elif(lang=='cpp'):
                flg,status=run_batch_cpp(request,title)
            elif(lang=='c'):
                flg,status=run_batch_c(request,title)
            elif(lang=='python'):
                flg,status=run_batch_python(request,title)
            if status=='timeout'and flg==False:
                compile_log=None
                run_log=None
                check_log='Time Out!!'
                marks=0
            else:
                compile_log,run_log,check_log,marks=read_file(request,title)
            return render_to_response('submission.html',{'Message':'file uploaded succesfully','compile_log':compile_log,'run_log':run_log,'check_log':check_log,'developer':developer,'Submissions':submsn[0],'marks':marks})
        else:
            Error="file invalid"
            return render_to_response('problem.html', {'form':form,'Submissions':submsn[0],'developer':developer,'error':Error},context_instance=RequestContext(request) )
    else:
            Error="Empty"
            return render_to_response('submission.html', {'form':form,'Submissions':submsn,'developer':developer,'error':Error},context_instance=RequestContext(request) )

        
#to run batch file
def run_batch_java(request,title):
    usrnm=request.user.username
    path=os.path.join(BASE_DIR,'static','media','submissions',usrnm)
    drive=path.split(':')
    drive=path[0]
    if not os.path.exists(path):
        os.mkdirs(path)
    file_path=""
    file_path_compile=os.path.join(path,'sh_java.bat')
    file_path_run=os.path.join(path,'sh_java_run.bat')
    batch_file_compile=open(file_path_compile,'wb')
    batch_file_run=open(file_path_run,'wb')
    input_file=title.replace(' ','')+'_in.txt'
    input_file=os.path.join(BASE_DIR,'static','media','input',input_file)
    file_data='cd '+path+'\n'+drive+':\n'+'javac Solution.java 2>compile.txt'
    batch_file_compile.write(file_data)
    batch_file_compile.close()
    file_data=file_data='cd '+path+'\n'+drive+':\n'+'java Solution < '+input_file+' >run.txt'
    batch_file_run.write(file_data)
    batch_file_run.close()
    flg=False
    p=subprocess.Popen(file_path_compile)
    p.wait()
    status='normal'
    file_path=os.path.join(path,'compile.txt')
    compile_txt=open(file_path)
    print compile_txt.read()==None
    if compile_txt.read()=="":
        p=subprocess.Popen(file_path_run)
        time.sleep(4)
        if p.poll()==None:
            os.kill(p.pid, signal.SIGINT)
            os.system('taskkill /f /im java.exe')
            status='timeout'
            flg=False
            print 'abnormal termination' 
        else:
            flg=True
            status='normal'
        file_path=os.path.join(path,'Solution.class')
        os.remove(file_path)
    os.remove(file_path_run)
    if os.path.exists(file_path_compile):
        os.remove(file_path_compile)
    file_path=os.path.join(path,'Solution.java')
    file_name=title.replace(' ','')+'.txt'
    file_new=os.path.join(path,file_name)
    if os.path.exists(file_new):
        os.remove(file_new)
    os.rename(file_path,file_new)
    return (flg,status)

def run_batch_cpp(request,title):
    usrnm=request.user.username
    path=os.path.join(BASE_DIR,'static','media','submissions',usrnm)
    drive=path.split(':')
    drive=path[0]
    if not os.path.exists(path):
        os.mkdirs(path)
    file_path=""
    file_path_compile=os.path.join(path,'sh_cpp.bat')
    file_path_run=os.path.join(path,'sh_cpp_run.bat')
    batch_file_compile=open(file_path_compile,'wb')
    batch_file_run=open(file_path_run,'wb')
    input_file=title.replace(' ','')+'_in.txt'
    input_file=os.path.join(BASE_DIR,'static','media','input',input_file)
    file_data='cd '+path+'\n'+drive+':\n'+'g++ -o Solution Solution.cpp 2>compile.txt'
    batch_file_compile.write(file_data)
    batch_file_compile.close()
    file_data=file_data='cd '+path+'\n'+drive+':\n'+'Solution.exe < '+input_file+' >run.txt'
    batch_file_run.write(file_data)
    batch_file_run.close()
    flg=False
    p=subprocess.Popen(file_path_compile)
    #ime.sleep(4)
    p.wait()
    status='normal'
    file_path=os.path.join(path,'compile.txt')
    compile_txt=open(file_path)
    print compile_txt.read()==None
    if compile_txt.read()=="":
        file_path=os.path.join(path,'Solution.exe')
        if os.path.exists(file_path):
            p=subprocess.Popen(file_path_run)
            time.sleep(4)
        if p.poll()==None:
            os.kill(p.pid, signal.SIGINT)
            os.system('taskkill /f /im Solution.exe')
            status='timeout'
            flg=False
            print 'abnormal termination' 
        else:
            flg=True
            status='normal'
        file_path=os.path.join(path,'Solution.exe')
        if os.path.exists(file_path):
            os.remove(file_path)
    os.remove(file_path_run)
    if os.path.exists(file_path_compile):
        os.remove(file_path_compile)
    file_path=os.path.join(path,'Solution.cpp')
    file_name=title.replace(' ','')+'.txt'
    file_new=os.path.join(path,file_name)
    if os.path.exists(file_new):
        os.remove(file_new)
    os.rename(file_path,file_new)
    return (flg,status)

    
def run_batch_c(request,title):
    usrnm=request.user.username
    path=os.path.join(BASE_DIR,'static','media','submissions',usrnm)
    drive=path.split(':')
    drive=path[0]
    if not os.path.exists(path):
        os.mkdirs(path)
    file_path=""
    file_path_compile=os.path.join(path,'sh_c.bat')
    file_path_run=os.path.join(path,'sh_c_run.bat')
    batch_file_compile=open(file_path_compile,'wb')
    batch_file_run=open(file_path_run,'wb')
    input_file=title.replace(' ','')+'_in.txt'
    input_file=os.path.join(BASE_DIR,'static','media','input',input_file)
    file_data='cd '+path+'\n'+drive+':\n'+'gcc -o Solution Solution.c 2>compile.txt'
    batch_file_compile.write(file_data)
    batch_file_compile.close()
    file_data=file_data='cd '+path+'\n'+drive+':\n'+'Solution.exe < '+input_file+' >run.txt'
    batch_file_run.write(file_data)
    batch_file_run.close()
    flg=False
    p=subprocess.Popen(file_path_compile)
    #ime.sleep(4)
    p.wait()
    status='normal'
    file_path=os.path.join(path,'compile.txt')
    compile_txt=open(file_path)
    print compile_txt.read()==None
    if compile_txt.read()=="":
        file_path=os.path.join(path,'Solution.exe')
        if os.path.exists(file_path):
            p=subprocess.Popen(file_path_run)
            time.sleep(4)
        if p.poll()==None:
            os.kill(p.pid, signal.SIGINT)
            os.system('taskkill /f /im Solution.exe')
            status='timeout'
            flg=False
            print 'abnormal termination' 
        else:
            flg=True
            status='normal'
        file_path=os.path.join(path,'Solution.exe')
        if os.path.exists(file_path):
            os.remove(file_path)
    os.remove(file_path_run)
    if os.path.exists(file_path_compile):
        os.remove(file_path_compile)
    file_path=os.path.join(path,'Solution.c')
    file_name=title.replace(' ','')+'.txt'
    file_new=os.path.join(path,file_name)
    if os.path.exists(file_new):
        os.remove(file_new)
    os.rename(file_path,file_new)
    return (flg,status)
    
def run_batch_python(request,title):
    usrnm=request.user.username
    path=os.path.join(BASE_DIR,'static','media','submissions',usrnm)
    drive=path.split(':')
    drive=path[0]
    if not os.path.exists(path):
        os.mkdirs(path)
    file_path_compile=os.path.join(path,'sh_cpp.bat')
    batch_file_compile=open(file_path_compile,'wb')
    input_file=title.replace(' ','')+'_in.txt'
    input_file=os.path.join(BASE_DIR,'static','media','input',input_file)
    file_data='cd '+path+'\n'+drive+':\n'+'pythonw Solution.py 2>compile.txt < '+input_file+' >run.txt'
    batch_file_compile.write(file_data)
    batch_file_compile.close()
    flg=False
    p=subprocess.Popen(file_path_compile)
    time.sleep(5)
    status='normal'
    if p.poll()==None:
        print os.kill(p.pid, signal.SIGINT)
        print os.system('taskkill /f /im pythonw.exe')
        status='timeout'
        flg=False
        print 'abnormal termination' 
    else:
        flg=True
        status='normal'
    os.remove(file_path_compile)
    file_path_compile=os.path.join(path,'Solution.py')
    file_name=title.replace(' ','')+'.txt'
    file_new=os.path.join(path,file_name)
    if os.path.exists(file_new):
        os.remove(file_new)
    os.rename(file_path_compile,file_new)
    return (flg,status)

def read_file(request,title):
    usrnm=request.user.username
    base_path=os.path.join(BASE_DIR,'static','media','submissions',usrnm)
    try:
        problem1=problem.objects.get(title=title)
    except:
        print 'problem not found'
    

    path=os.path.join(BASE_DIR,'static','media','submissions',usrnm,'compile.txt')
    file1=open(path)
    compile_log= file1.read()
    file1.close()
    path=os.path.join(BASE_DIR,'static','media','submissions',usrnm,'run.txt')
    file2=None
    if os.path.exists(path):
        file2=open(path)
    print compile_log
    if compile_log or file2==None:
        run_log=None
        check_log=None
        marks=0
        update_marks(problem1,request,marks)
    else:
        file2=open(path)
        run_log=file2.read()
        file2.close()
        original=title.replace(' ','')+'_out.txt'
        path=os.path.join(BASE_DIR,'static','media','output',original)
        output_file=open(path)
        out_log=output_file.read()
        output_file.close()
        check_log=""
        flg=False
        run=run_log.split('\n')
        out=out_log.split('\n')
        i=0 
        n=len(out)-1
        cnt=0
        while i<n:
            try:
                if(out[i]==run[i]):
                    cnt=cnt+1
                i=i+1
            except:
                break
        marks=cnt*10
        print marks,cnt,n
        if (marks<100 or marks>100 or marks<n*100):
            if run_log==out_log:
                marks=100
            else:
                marks=marks*100/(n*10)
        if(marks==0 or marks>100) or len(run_log)>len(out_log):
            check_log+="not accepted"
            update_marks(problem1,request,marks)
        else:
            check_log+="accepted"
            marks=marks
            run_log=problem1.output_format
            update_marks(problem1,request,marks)
    file_path_compile=os.path.join(base_path,'compile.txt')
    if os.path.exists(file_path_compile):
        os.remove(file_path_compile)
    file_path_compile=os.path.join(base_path,'run.txt')
    if os.path.exists(file_path_compile):
        os.remove(file_path_compile)
    if run_log != None:
        run_log="<br>".join(run_log.split("\n"))
    if compile_log !=None:
        compile_log="<br>".join(compile_log.split("\n"))
    return(compile_log,run_log,check_log,marks)
    
#updating marks
def update_marks(problem1,request,marks):
    try:
        #   print problem1.title
        try:
            dev=Developer.objects.get(user=request.user)
        except:
            print 'Developer not found'
        solved_list=(dev.problems_list)
        new_s=''   
        pid=str(problem1.id) 
        print solved_list,pid,marks
        if solved_list==None:
            new_s+=' '+pid+'.'+marks
        else:       
            solved_list=str(solved_list)        
            solved_list=solved_list.split()
            flg=False
            for i in solved_list:   
                ind=i.index('.')
                tmp=i[:ind]
                tmrk=int(i[ind+1:])

                if tmp==pid:
                    #print tmrk
                    #print marks
                    #print marks>tmrk
                    if marks>=tmrk:
                        marks=str(marks)
                        new_s+=' '+tmp+'.'+marks
                    else:
                        try:
                            tmrk=str(tmrk)
                            new_s+=' '+tmp+'.'+tmrk
                        except:
                            print 'error hrer'
                    flg=True
                else:
                    tmp1=i[ind+1:]
                    new_s+=' '+tmp+'.'+tmp1
            if not flg:
                new_s+=' '+pid+'.'+marks
            #print new_s
            dev.problems_list=new_s
            dev.save()
    except:
         print 'Error'
          
    
