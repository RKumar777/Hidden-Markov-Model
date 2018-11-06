
# coding: utf-8

# In[4]:


# import sys
# import numpy as np
# pie=np.transpose(np.matrix(np.loadtxt(sys.argv[4])))
# a=np.matrix(np.loadtxt(sys.argv[6]))
# b=np.matrix(np.loadtxt(sys.argv[5]))
# # artrain=np.genfromtxt("trainwords.txt",skip_header=0,delimiter='\t',dtype=None,unpack=True)
# artest=np.genfromtxt(sys.argv[1],skip_header=0,delimiter='\t',dtype=None,unpack=True)
# atag=np.genfromtxt(sys.argv[3],skip_header=0,delimiter='\t',dtype=None,unpack=True)
# aword=np.genfromtxt(sys.argv[2],skip_header=0,delimiter='\t',dtype=None,unpack=True)
# dict1={}
# dict2={}
# dict3={}
# dict4={}
# thaap=open(sys.argv[7],"w")
# k=np.size(atag)
# m=np.size(aword)
# w=np.size(artest)


# for i in range(k):
#     dict1[i]=atag[i]
# for i in range(m):
#     dict2[aword[i]]=i
# for i in range(k):
#     dict3[atag[i]]=i
# for i in range(k):
#     dict4[i]=aword[i]
# def sentence(ax):
#     dum1=ax.split(' ')
#     lx=len(dum1)
#     sent =np.chararray((lx,1),itemsize=27)
#     dent =np.chararray((lx,1),itemsize=27)
#     for i in range(lx):
#         dum2=dum1[i].split('_')
#         sent[i,0]=dum2[0]
#         dent[i,0]=dum2[1]
#     return sent,dent

# def albeit(wds,alp,bot):
#     lg=len(wds)
#     grib=np.multiply(alp,bot)
#     for i in range(lg):
#         cr=np.where(grib==max(grib[:,i]))[0][0]
#         cr=dict1[cr[0,0]]
#         pr=wds[i][0]
#         thaap.write(str(pr)+"_"+str(cr)+" ")
#     thaap.write("\n")
#     return 1

# for i in range(w):
#     words,tags=sentence(artest[i])
#     lgbt=len(words)
#     alpha=np.matrix(np.zeros((k,lgbt)))
#     beta=np.matrix(np.ones((k,lgbt)))
#     for qw in range(k):
#         alpha[qw,0]=pie[qw]*b[qw,dict2[words[0][0]]]
#         alpha[qw,0]=pie[qw]
#         beta[qw,-1]=1
#     for txr in range(1,lgbt):
#         ole1=dict2[words[txr][0]]
#         alpha[:,txr]=np.multiply(b[:,ole1],np.transpose(a)*alpha[:,txr-1])
#     for txr in range(lgbt-2,-1,-1):
#         ole2=dict2[words[txr+1][0]]
#         beta[:,txr]=a*(np.multiply(b[:,ole2],beta[:,txr+1]))
#     albeit(words,alpha,beta)
# print("alpha:")
# print(alpha)
# print("beta:")
# print(beta)
# thaap.close()
# print(b)
# print(pie)


import sys
import numpy as np
pie=np.transpose(np.matrix(np.loadtxt(sys.argv[4])))
a=np.matrix(np.loadtxt(sys.argv[6]))
b=np.matrix(np.loadtxt(sys.argv[5]))
artest=np.genfromtxt(sys.argv[1],skip_header=0,delimiter='\t',dtype=None,unpack=True)
atag=np.genfromtxt(sys.argv[3],skip_header=0,delimiter='\t',dtype=None,unpack=True)
aword=np.genfromtxt(sys.argv[2],skip_header=0,delimiter='\t',dtype=None,unpack=True)
dict1={}
dict2={}
dict3={}
dict4={}
thaap=open(sys.argv[7],"w")

k=np.size(atag)
m=np.size(aword)
w=np.size(artest)

for i in range(k):
    dict1[i]=atag[i]
for i in range(m):
    dict2[aword[i]]=i
for i in range(k):
    dict3[atag[i]]=i
for i in range(k):
    dict4[i]=aword[i]
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

def albeit(wds,alp,bot):
    lg=len(wds)
    grib=np.multiply(alp,bot)
    for i in range(lg):
        cr=np.where(grib==max(grib[:,i]))[0][0]
        cr=dict1[cr[0,0]]
        pr=wds[i][0]
        thaap.write(str(pr)+"_"+str(cr)+" ")
    thaap.write("\n")
    return 1


for i in range(w):
    words,tags=sentence(artest[i])
    lgbt=len(words)
    alpha=np.matrix(np.zeros((k,lgbt)))
    beta=np.matrix(np.ones((k,lgbt)))
    for j in range(k):
        alpha[j,0]=pie[j]*b[j,dict2[words[0][0]]]
        beta[j,-1]=1
    for txr in range(1,lgbt):
        ole1=dict2[words[txr][0]]
        alpha[:,txr]=np.multiply(b[:,ole1],np.transpose(a)*alpha[:,txr-1])
    for txr in range(lgbt-2,-1,-1):
        ole2=dict2[words[txr+1][0]]
        beta[:,txr]=a*(np.multiply(b[:,ole2],beta[:,txr+1]))
    albeit(words,alpha,beta)
# print("alpha:")
# print(alpha)
# print("beta:")
# print(beta)
thaap.close()


