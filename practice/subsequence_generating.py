def subseq(arr):
    n=len(arr)
    res=[]
    def generate_subseq(ind, curr):
        if ind==n:
            res.append(curr)
            return
        generate_subseq(ind+1,curr)
        generate_subseq(ind+1,curr+[arr[ind]])
    generate_subseq(0,[])
    ans=0
    for sub in res:
        if all(sub[i]>sub[i-1] for i in range(1, len(sub))):
            ans=max(ans,len(sub))
    return ans
arr=[1,2,3,51]
print(subseq(arr))
