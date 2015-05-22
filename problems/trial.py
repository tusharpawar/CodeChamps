#import os
#os.remove('_out.txt')
s='1.100 2.80 3.90'
marks=100
s=s.split()
l={}
pid='3'
new_s=''
flg=False	
for i in s:   
	ind=i.index('.')
	tmp=i[:ind]
	tmrk=int(i[ind+1:])
	if tmp==pid:
		print tmrk
		print marks
		print marks>tmrk
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
		marks=str(marks)
		new_s+=' '+pid+'.'+marks
	print new_s