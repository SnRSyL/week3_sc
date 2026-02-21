from ff import *
counter=0
for i in berkay:
    print(type(i))
    lasti=str(i)
    print(type(lasti))
    with open("efe.txt", "a", encoding='utf-8') as f:
        f.write(lasti + '\n'))
    try:
        x=i['status']
        print(type(x))
        if x.startswith('big'):
            counter+=1

        else:
            pass

    except:
         pass
    print(counter)

