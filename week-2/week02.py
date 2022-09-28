def calculate(min, max, step):
    if max<min:
        print("最大值必須大於最小值,且setp須為正整數")
    elif max%1!=0:
        print("最大值必須大於最小值,且setp須為正整數")
    elif step<=0:
        print("最大值必須大於最小值,且setp須為正整數")
    else:
        result=0
        while min<=max:
            result=result+min
            min=min+step
            
        print(result)


calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0



# /*第二題--------------------------*/
def avg(data):
    #  console.log(data);  // data是一個JSON
    #  console.log(data.employees[0].name);
    #  console.log(data.employees.length)
    sum=0
    number_1=0
    salary=data["employees"][number_1]["salary"]
    manager=data["employees"][number_1]["manager"]
    while(number_1<len(data["employees"])):
        if manager==False:
            sum=sum+salary
        else:
            sum=sum+0
        number_1=number_1+1
    #a=非員工薪水總和

    nonemployee=0
    number_2=0
    while(number_2 < len(data["employees"])):
        if data["employees"][number_2]["manager"] == False:
            nonemployee=nonemployee+1
            number_2=number_2+1
        else:
            nonemployee=nonemployee+0
            number_2=number_2+1
        
    #c=非員工人數
    average=sum/nonemployee
    print(int(average))


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
        ]
}) # 呼叫 avg 函式 


# /*第三題--------------------------*/
def func(a):
    def func2(b,c):
        return print( a+(b*c))
    return func2      


func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

# /*第四題--------------------------*/
def maxProduct(nums):
    a=1
    newnums=[]        
    while(a<len(nums)):
        number=0
        while number<len(nums)-a:
            newnums.append(nums[number]*nums[number+a])
            number=number+1
        if a+1<=len(nums):
            a=a+1
        else:
            break

    max=newnums[0]
    number=0
    while number<len(newnums):
        if newnums[number]>=max:
            max=newnums[number]
        number=number+1
    print(max)

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10



# /*第五題--------------------------*/
def twoSum(nums, target):
    index1=0
    index2=1
    n=len(nums)-1
    index=None
    while(index1<len(nums)-1):
        if index !=None:
            break
        while index2<len(nums):
            if nums[index1]==target-nums[index2] and nums[index1]!=nums[index2]:
                x=(nums[index1],nums[index2])
                return[index1,index2]
                break            
            else:
                index2=index2+1                    

        #index1=0
        index1=index1+1
        index2=index2-n
        n=n-1
    
    
twoSum([2, 11, 7, 15], 9)
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9




# /*第六題( Optional )--------------------------*/
# def maxZeros(nums):
# # 請用你的程式補完這個函式的區塊
# maxZeros([0, 1, 0, 0]) # 得到 2
# maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
# maxZeros([1, 1, 1, 1, 1]) # 得到 0
# maxZeros([0, 0, 0, 1, 1]) # 得到 3
