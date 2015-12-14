
# coding: utf-8

# In[ ]:

from random import randint
print ('終極密碼：1~100')
bomb=randint (1,100)
b = str(1)
c = str(100)
a = 0
i = 1

while a!= bomb:
        a = int(input('請輸入數字：'))
        if a <= int(b) or a >= int(c):
            print('錯誤，請重新輸入！')
            continue
        if a>bomb:
            c = str(a)
            i += 1
            print('終極密碼:'+b+'~' +c)
        if a<bomb:
            b = str(a)
            i += 1
            print('終極密碼:'+b+'~'+c)

else:
    if i <=3:
            print('這麼快就中了！！！\n你只猜了'+str(i)+'次耶，ㄚ不就好棒棒！')
    if i>3 and i <=6:
            print('中了耶！！！\n你猜了'+str(i)+'次，還可以啦！')
    if i>6:
            print('終於中了！！！\n你總共猜了'+str(i)+'次，太爛了！')


# In[ ]:



