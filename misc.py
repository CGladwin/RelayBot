import random
import math
import itertools
#roles=["watchman","doc","cop","vig"]
def perms(pcount):
    roles=["watchman","doc","cop","vig"]
    if pcount>5:
      roles+=["mayor","hillbilly",]
    mafcount=0
    totalperms=[]
    baselist=roles[:]
    neutroles=["fool","executioner","urchin"]
    if pcount>5:
          roles+=neutroles
          print(roles)
    pcount-=1
    while mafcount<=pcount:
      vilcount=pcount-mafcount
      truelist=list(itertools.combinations(roles,r=vilcount))
      for y in range(len(truelist)):
        truelist[y]=list(truelist[y])
        for x in range(mafcount):
            truelist[y].append("lackey")
        if "godfather" not in truelist[y] and "lackey" in truelist[y]:
          truelist[y].remove("lackey")
          truelist[y].append("godfather")
        if "godfather" not in truelist[y] and "urchin" in truelist[y]:
          truelist[y].remove("urchin")
          truelist[y].append("godfather")
        if "lackey" not in truelist[y] and "urchin" not in truelist[y] and "godfather" in truelist[y]:
          truelist[y].remove("godfather")
          truelist[y].append("Solo godfather")
      for z in range(len(truelist)):
        truelist[z]=list(truelist[z])
        truelist[z].append("detective")
      if pcount==5:
        neutremove=[]
        for w in range(len(truelist)):
          if len(set(truelist[w]) & set(neutroles))>1:
            neutremove.append(truelist[w])
        truelist=[tuple(l) for l in truelist]
        neutremove=[tuple(l) for l in neutremove]
        truelist=list(set(truelist)-set(neutremove))
      if pcount in [6,7]:
        neutremove=[]
        for w in range(len(truelist)):
          if len(set(truelist[w]) & set(set(neutroles) - {"urchin"}))>1:
            neutremove.append(truelist[w])
        truelist=[tuple(l) for l in truelist]
        neutremove=[tuple(l) for l in neutremove]
        truelist=list(set(truelist)-set(neutremove))
        for w in range(len(truelist)):
          if len(set(truelist[w]) & set(neutroles))>1:
            print("youre looking for:\n",truelist[w])
      if pcount>5:
        for x in range(len(truelist)):
          if len(set(baselist) & set(truelist[x]))==0:
            truelist[x]=list(truelist[x])
            truelist[x].remove("detective")
            truelist[x].append("vengeful detective")
      mafcount+=1
      totalperms+=truelist
    print("number of combinations is: ",len(totalperms))
    print(totalperms)
    return(totalperms)
perms(7)

'''
l=['a','b','c']
a=[]
b=list(itertools.combinations(l,r=2))
for x in range(len(b)):
  b[x]=list(b[x])
  b[x].append('d')
print(b)

l=['a','b','c']
a=[]
b=list(itertools.combinations(l,r=2))
for x in b:
  x=list(x)
  a.append(x)
  x.append('d')
print(a)
'''
'''
"""import random
import math
import itertools
#roles=["watchman","doc","cop","vig"]
def perms(pcount):
    roles=["watchman","doc","cop","vig"]
    if pcount>5:
      roles+=["mayor","hillbilly",]
    mafcount=0
    totalperms=[]
    baselist=roles[:]
    neutroles=["fool","executioner","urchin"]
    if pcount>5:
          roles+=neutroles
          print(roles)
    pcount-=1
    while mafcount<=pcount:
      vilcount=pcount-mafcount
      truelist=list(itertools.combinations(roles,r=vilcount))
      for y in range(len(truelist)):
        truelist[y]=list(truelist[y])
        for x in range(mafcount):
            truelist[y].append("lackey")
        if "godfather" not in truelist[y] and "lackey" in truelist[y]:
          truelist[y].remove("lackey")
          truelist[y].append("godfather")
        if "godfather" not in truelist[y] and "urchin" in truelist[y]:
          truelist[y].remove("urchin")
          truelist[y].append("godfather")
        if "lackey" not in truelist[y] and "urchin" not in truelist[y] and "godfather" in truelist[y]:
          truelist[y].remove("godfather")
          truelist[y].append("Solo godfather")
      for z in range(len(truelist)):
        truelist[z]=list(truelist[z])
        truelist[z].append("detective")
      if pcount==5:
        neutremove=[]
        for w in range(len(truelist)):
          if len(set(truelist[w]) & set(neutroles))>1:
            neutremove.append(truelist[w])
        truelist=[tuple(l) for l in truelist]
        neutremove=[tuple(l) for l in neutremove]
        truelist=list(set(truelist)-set(neutremove))
      if pcount in [6,7]:
        neutremove=[]
        for w in range(len(truelist)):
          if len(set(truelist[w]) & set(set(neutroles) - {"urchin"}))>1:
            neutremove.append(truelist[w])
        truelist=[tuple(l) for l in truelist]
        neutremove=[tuple(l) for l in neutremove]
        truelist=list(set(truelist)-set(neutremove))
        urchminority=[]
        for w in range(len(truelist)):
          if (truelist[w]).count("lackey")+(truelist[w]).count("godfather")<pcount//2 and "urchin" in truelist[w]:
            urchminority.append(truelist[w])
            #print("stinky list:\n",truelist[w])
        truelist=[tuple(l) for l in truelist]
        urchminority=[tuple(l) for l in urchminority]
        truelist=list(set(truelist)-set(urchminority))
        print("urchminority is:\n",urchminority)
        for w in range(len(truelist)):
          if len(set(truelist[w]) & set(neutroles))>1:
            print("youre looking for:\n",truelist[w])
          if (truelist[w]).count("lackey")+(truelist[w]).count("godfather")<pcount//2 and "urchin" in truelist[w]:
            print("stinky list:\n",truelist[w])
      if pcount>5:
        for x in range(len(truelist)):
          if len(set(baselist) & set(truelist[x]))==0:
            truelist[x]=list(truelist[x])
            truelist[x].remove("detective")
            truelist[x].append("vengeful detective")
      mafcount+=1
      totalperms+=truelist
    print("number of combinations is: ",len(totalperms))
    print(totalperms)
    return(totalperms)
perms(7)
'''
