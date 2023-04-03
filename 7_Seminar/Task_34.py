text = "пара-ра-рам рам-пам-папам па-ра-па"
vowels_alphabet = ['а','о','и','ы','у','э','е', 'я','ю']
lines = text.split()
 
lst = [sum(x in vowels_alphabet for x in lin)
 for lin in lines]
 
if len(set(lst)) == 1 :
    res = "Парам пам-пам"  
else: res = "Пам парам"
 
print(res)