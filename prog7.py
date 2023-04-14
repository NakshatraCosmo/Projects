rhymes={"1":"fun","2":"blue","3":"happiness","4":"intelligence","5":"Idiot"}
n=input("Type a number:")
if n in rhymes:
    rhyme=rhymes[n]
    print(rhyme)
else:
    print("Not found.")