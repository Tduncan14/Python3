num = 0 
i = 0



while i < 4:
    num = int(input('Number_'))
    if num == 0:
        print("square:0")
        i += 1
        continue
    if num == 1:
        break

    sq = str(num*num)
    print('Square' + sq)
    i+=1
else:
        print('Done')
        
