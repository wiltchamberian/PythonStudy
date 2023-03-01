


def insert_sort(array):
    size = len(array);
    for j in range(1,size):
        key = array[j]
        i = j-1
        while (i>0 and array[i]>key):
            array[i+1]=array[i]
            i-=1
        array[i+1]=key

def merge(ar1,ar2):
     ar=[None] * (len(ar1)+len(ar2))
     i,j,k =0,0,0
     while(len(ar1)>i and len(ar2)>j):
         if ar1[i]<=ar2[j]:
             ar[k]=ar1[i]
             i+=1
         else:
             ar[k]=ar2[j]
             j+=1
         k+=1
     if i<len(ar1):
         ar[k:len(ar)]=ar1[i:len(ar1)]
     if j<len(ar2):
         ar[k:len(ar)]=ar2[j:len(ar2)]
     return ar


def merge_sort(array):
     if(len(array)==1):
         return array
     if(len(array)==2):
         if(array[0]>array[1]):
             array[0],array[1]=array[1],array[0]
         return array
     siz = len(array);
     array[0:siz//2] = merge_sort(array[0:siz//2])
     array[siz//2 : siz] = merge_sort(array[siz//2:siz]);
     array = merge(array[0:siz//2],array[siz//2: siz])
     return array
    
def main():
    lis = [1,6,2,5,3,8,4]
    print(type(lis))
    lis = merge_sort(lis)
    print(lis)

main()