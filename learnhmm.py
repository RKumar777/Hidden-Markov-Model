
# coding: utf-8

# In[13]:


import sys
import numpy as np
artrain=np.genfromtxt(sys.argv[1],skip_header=0,delimiter='\t',dtype=None,unpack=True)
# artest=np.genfromtxt("testwords.txt",skip_header=0,delimiter='\t',dtype=None,unpack=True)
atag=np.genfromtxt(sys.argv[3],skip_header=0,delimiter='\t',dtype=None,unpack=True)
aword=np.genfromtxt(sys.argv[2],skip_header=0,delimiter='\t',dtype=None,unpack=True)
dict1={}
dict2={}
dict3={}
# thaap=open(sys.argv[7],"w")
# hmmprior=open("hmmprior.txt","w")
# hmmemit=open("hmmemit.txt","w")
# hmmtrans=open("hmmtrans.txt","w")
n=np.size(artrain)
k=np.size(atag)
m=np.size(aword)
# w=np.size(artest)
for i in range(k):
    dict1[i]=atag[i]
for i in range(m):
    dict2[aword[i]]=i
for i in range(k):
    dict3[atag[i]]=i

# print(m)
# print(n)
#making pie array
pie=np.ones((k))
a=np.ones((k,k))
b=np.ones((k,m))
def sentence(ax):
    dum1=ax.split(' ')
    lx=len(dum1)
    sent =np.chararray((lx,1),itemsize=27)
    dent =np.chararray((lx,1),itemsize=27)
    for i in range(lx):
        dum2=dum1[i].split('_')
        sent[i,0]=dum2[0]
        dent[i,0]=dum2[1]
    return sent,dent

# def albeit(wds,alp,bot):
#     lg=len(wds)
#     grib=np.multiply(alp,bot)
#     for i in range(lg):
#         cr=np.where(grib==max(grib[:,i]))[0][0]
#         cr=dict1[cr]
#         pr=wds[i][0]
#         thaap.write(str(pr)+"_"+str(cr)+" ")
#     return 1

# for b

for i in range(n):
    words,tags=sentence(artrain[i])
    lgbt=len(words)
    for r in range(lgbt):
        if(r==0):
            pie[dict3[tags[r][0]]]+=1
        else:
            op2=dict3[tags[r][0]]
            op3=dict3[tags[r-1][0]]
            a[op3,op2]+=1
        op1=dict2[words[r][0]]
        op2=dict3[tags[r][0]]
        b[op2,op1]+=1
pie=pie/float(np.sum(pie))
for i in range(k):
    a[i,:]=a[i,:]/np.sum(a[i,:])
    b[i,:]=b[i,:]/np.sum(b[i,:])

np.savetxt(sys.argv[4],pie)
np.savetxt(sys.argv[6],a)
np.savetxt(sys.argv[5],b)
print(np.shape(pie))
print(np.shape(a))
print(np.shape(b))
# hmmprior.close()
# hmmemit.close()
# hmmtrans.close()

