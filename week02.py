def calculate(min, max, step):
    if max<min:
        print("最大值必須大於最小值,且setp須為正整數")
    elif max%1!=0:
        print("最大值必須大於最小值,且setp須為正整數")
    elif step<=0:
        print("最大值必須大於最小值,且setp須為正整數")
    else:
        answer1=0
        while min<=max:
            answer1=answer1+min
            min=min+step
            
        print(answer1)


calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0



# /*第二題--------------------------*/
def avg(data):
    #  console.log(data);  // data是一個JSON
    #  console.log(data.employees[0].name);
    #  console.log(data.employees.length)
    a=0
    b=0
    salary=data["employees"][b]["salary"]
    manager=data["employees"][b]["manager"]
    while(b<len(data["employees"])):
        if manager==False:
            a=a+salary
        else:
            a=a+0
        b=b+1
    #a=非員工薪水總和

    c=0
    d=0
    while(d < len(data["employees"])):
        if data["employees"][d]["manager"] == False:
            c=c+1
            d=d+1
        else:
            c=c+0
            d=d+1
        
    #c=非員工人數
    answer2=a/c
    print(int(answer2))


avg({
    "employees":[
    {
    "name":"John",
    "salary":30000,
    "manager":False
    },
    {
    "name":"Bob",
    "salary":60000,
    "manager":True
    },
    {
    "name":"Jenny",
    "salary":50000,
    "manager":False
    },
    {
    "name":"Tony",
    "salary":40000,
    "manager":False
    }
]}); 


# /*第三題--------------------------*/
def func(a):
    def f(b,c):
        return print( a+(b*c))
    return f        


func(2)(3, 4); #你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5); # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9); # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

# /*第四題--------------------------*/
def maxProduct(nums):
    n=1
    newnums=[]        
    while(n<len(nums)):
        i=0
        while i<len(nums)-n:
            newnums.append(nums[i]*nums[i+n])
            i=i+1
        if n+1<=len(nums):
            n=n+1
        else:
            break

    max=newnums[0]
    x=0
    while x<len(newnums):
        if newnums[x]>=max:
            max=newnums[x]
        x=x+1
    print(max)

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) #得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0 或 -0
maxProduct([5, -1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10


# /*第五題--------------------------*/
def twoSum(nums, target):
    a=1
    b=0
    n=3
    x=None
    while(b<len(nums)-1):
        if x!=None:
            break
        while a<len(nums):
            if nums[b]==target-nums[a] and nums[b]!=nums[a]:
                x=(nums[b],nums[a])
                print(b,a)
                break            
            else:
                a=a+1                    

    # a=4=len(nums), b=0
        b=b+1
        a=a-n
        n=n-1
    
    
twoSum([2, 11, 7, 15], 9)
# let result=twoSum([2, 11, 7, 15], 9);
# console.log(result); // show [0, 2] because nums[0]+nums[2] is 9




# /*第六題( Optional )--------------------------*/
# function maxZeros(nums){
# // 請用你的程式補完這個函式的區塊
# }
# maxZeros([0, 1, 0, 0]); // 得到 2
# maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
# maxZeros([1, 1, 1, 1, 1]); // 得到 0
# maxZeros([0, 0, 0, 1, 1]) // 得到 3
