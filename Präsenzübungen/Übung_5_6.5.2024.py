zen_of_python = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren’t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you’re Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it’s a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let’s do more of those!"""

#Satzzeichen = (",",".","!","*","-")
Anzahl_Wörter = dict()
zen_processed = zen_of_python.lower().replace(".","").replace(",","").replace("!","").replace("*","").replace("-","")
list = zen_processed.split()

#while len(list) != 0:
    #count = 0
    #wort = list[0]
    #for i in range(len(list)):
#        if list[i] == wort: 
#            count += 1
#    Anzahl_Wörter[wort] = count
#    #print(count)
#    list.remove(wort)

for i in range (len(list)):
    wort = list[i]
    if wort in Anzahl_Wörter:
        Anzahl_Wörter[wort] += 1
    else: Anzahl_Wörter[wort] = 1


for string,x in Anzahl_Wörter.items():
    print(f"{string}: {x}")