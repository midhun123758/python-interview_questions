print("hello")


def  odd_even(numbers):
    for i in numbers:
        if i%2==0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")

odd_even([1,2,3,4,5,6,7,8,9])


"__________________________________"


def non_repeting(letter):
    arr=[]
    for i in letter:
        if letter.count(i)==1:
            arr.append(i)
        
    print(arr)

non_repeting("midhunn")


def duplicate(char):

    arr=[]
    for i in char:
        if char.count(i)==2:
            arr.append(i)
    
    print(set(arr))

duplicate("midhunn")
         
###nums = [2,7,11,15]target = 9 Output:[0,1]##

def find_target(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return print([i])
        for j in  range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return print([i,j])

find_target([2,7,11,15],11)

#"Longest Common Prefix   Example: ["flower","flow","flight"]  Output: "fl""

def longest_word(word):
    words=''.join(word)
    coun=0
    len=[]
    for i in words:
        if words.count(i)>=coun:
            coun=words.count(i)
            len.append(i)

    print("".join(set(len)))

longest_word(["flower","flow","flight"])




# finding the max diffrent

listt2=[1,2,6,3,4,5]
dif=0

for i in range(len(listt2)):
    for j in range(len(listt2)):
        val=listt2[i] - listt2[j]
        if val > dif:
            dif = val
print(dif)

# effcent way

data = max(listt2) - min(listt2)
print(data)