# -*- coding: utf-8 -*-
"""tensor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dr_PdQ-UpUD8zvluyNubkn-ekr9PNT4J
"""

class tensor:
  
  def __init__(self):
    pass
  
  #########################################################
  #                       flatten                          #
  #  Convert m dimensional list into one dimensional list #
  #########################################################
  
  def flatten(self,nums):
    cnt =0;
    def cnt_element(ans):
      nonlocal cnt
      if type(ans) is not list:
         cnt+=1   
      elif type(ans) is list:
         for i in ans:
            cnt_element(i)
    cnt_element(nums)    
    ls=self.shape_data(nums,[cnt])
    return ls
  
  
  def show_shape(self,nums):#working on it
    
    ls =list()
    cnt=0
    
    for i in nums:
      while i is list:
        i = []  
    print(cnt)
    
  
  #########################################################
  #                     Reshape list                      #
  #  Convert m dimensional list into n dimensional list   #
  #########################################################
  def shape_data(self,nums,shape):
    anss=list()
    
    def convert_to_1D(ans):
      nonlocal anss
      if type(ans) is not list:
         anss.append(ans)   
      elif type(ans) is list:
         for i in ans:
            convert_to_1D(i) 
    
    convert_to_1D(nums)
    nums = anss
    
    # padding / removing
    lst=list()
    a=len(nums)
    sum=1
    for i in shape:
      sum*=i
    if sum>a:# padding
      lst=nums
      for j in range(sum-i):
        lst+=[0]
    elif sum<a: #cut off
      for k in range(sum):
        lst+=[nums[k]]
    else: #same size
        lst=nums
        
    #creating zero list ex:[0,0,0,0,0]   
    ans =list()
    ans2 =list()
    start = 0
    for i in reversed(shape):# start from the right [1,2,3] ->3
      if start == 0:
        for j in range(i):# inner layer, just append 0
          ans += [0]
        start=1
      else:
        for k in range(i):
          ans2.append(ans)# outter layer, multipy inner list
        ans = ans2 #swap ans / ans2
        ans2=[]#reset temp buffer

    #adding elements into list/ans
    b=0
    size = len(ans)
    def helper(ans):
      nonlocal b
      if type(ans) is not list:
            if b >=len(lst):#oversize, fill in 0
              ans=0
              return ans
            else:
              ans=lst[b]#fill in from modified lst
              b+=1
              return ans
      elif type(ans) is list:
        return [helper(i) for i in ans]#recursive call to get into inner layer and set elements
    return helper(ans)

  
  #########################################################
  #                  Matrix addition                      #
  #           return the sum of 2 matrices                #
  #                                                       #
  #########################################################  
  
  def maadd(self,matrix1,matrix2):
    if type(matrix1[0]) is not list:
      x=1
      n=len(matrix1)
    else:
      x,n=len(matrix1), len(matrix1[0])
    if type(matrix2[0]) is not list:
      y=1
      m=len(matrix2)
    #print(x,n,y,m)
    
    for i in range(x):
      for k in range(n):
        if x==1: # first matrix is 1d
          matrix1[k]=matrix1[k]+matrix2[k]
        else: #both are 2d
          matrix1[i][k]+=matrix2[i][k]
    return matrix1
  
  
  
  #########################################################
  #                  Matrix multiplication                #
  #           return the product of 2 matrices            #
  #                                                       #
  #########################################################  
  
  def mamul(self,matrix1,matrix2):
    if type(matrix1[0]) is not list:
      x=1
      n=len(matrix1)
    else:
      x,n=len(matrix1), len(matrix1[0])
    if type(matrix2[0]) is not list:
      y=1
      m=len(matrix2)
    else:
      y,m=len(matrix2), len(matrix2[0])
    #print(x,n,y,m)

    product=list()
    product1=list()
    for b in range(x):
      product+=[product1]
      for a in range(m):
        product1+=[0]
      product1=[]

    if n!=y:
      return print('the product is undifined')
    else:
      for i in range(x):
        for j in range(m):
          for k in range(n):
            if x==1: # first matrix is 1d
              product[i][j]+=matrix1[k]*matrix2[k][j]
            elif y==1: #second matrix is 1d 
              product[i][j]+=matrix1[i][k]*matrix2[j]
            else: #both are 2d
              product[i][j]+=matrix1[i][k]*matrix2[k][j]
      
      
      if x==1:
        return self.shape_data(product,[m,1])
      
    return product
  
  
  #########################################################
  #                     Combine_two _mat                  #
  #     append the start of the each row in second        #
  #     matrix to the start of each row                   #
  #     in the start of the first matrix                  #
  #########################################################
  
  def combine_two2_mat(self,list1,list2):#assume two lists are in the same shape
    for i in  range(len(list1)):
      list1[i]=list1[i]+list2[i]
    return list1
  
  
  #########################################################
  #                     Tensor_Initializer                #
  #  Create a tensor with specified shape & method        #
  #         opcode:  0: Zero 1: One 2: Random             #
  #########################################################

  def Tensor_Initializer(self,opcode,shape):
    mul=1
    for i in shape:
      mul*=i
    if opcode==0:
      temp = mul*[0]
      return self.shape_data(temp,shape)
    if opcode==1:
      temp = mul*[1]
      return self.shape_data(temp,shape)
    if opcode==2:
      ranlist = list()
      for i in range(mul):
        x = random.randint(-300,300)/random.randint(1000,2000)
        ranlist.append(x)
      return self.shape_data(ranlist,shape)
 

  #########################################################
  #                     Softmax                           #
  #  Set the maximum value to 1, and set others to 0      #
  #                                                       #
  #########################################################    

  def softmax(self,data):
    max_val =-1;
    def find_max(ans):
      nonlocal max_val
      if type(ans) is not list:
        max_val = max(max_val,ans)   
      elif type(ans) is list:
         for i in ans:
            find_max(i)
    find_max(data)
    def helper(ans): #modify the original list
      if type(ans) is not list:
        if ans == max_val:
          return 1
        else:
          return 0
      elif type(ans) is list:
        return [helper(i) for i in ans]  

    return helper(data)

    
  #########################################################
  #                       Relu                            #
  #          Set  all the negative values to  0           #
  #                                                       #
  #########################################################  
    
  def relu(self,data):
    def helper(ans): #modify the original list
      if type(ans) is not list:
        if ans <0:
          return 0
        else:
          return ans
      elif type(ans) is list:
        return [helper(i) for i in ans]  
    return helper(data)