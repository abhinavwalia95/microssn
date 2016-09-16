import index
#SyntaxNet as a MicroService
index.syntax("i am abhinav. he is awesome")
content=None
with open('out.txt') as f:
    global content
    content = f.readlines()
content_length=len(content)
while content_length>0:
    #string= content[content_length-1]
    #string="('Input: i am abhinav. he is awesome\nParse:\nabhinav. JJ ROOT\n +-- i PRP nsubj\n +-- am VBP cop\n +-- awesome JJ ccomp\n     +-- he PRP nsubj\n     +-- is VBZ cop\n', None)"
    vari=str(content[content_length-1]).split("\\n")
    l=len(vari)
    end_list=[]
    for i in range(l):
        if i!=0 and i!=1 and i!=l-1:
            temp_list=vari[i].split("+-- ")
            temp_list_len=len(temp_list)
            end_list.append(temp_list[temp_list_len-1])
    end_list_len=len(end_list)
    print end_list
    with open("pos.txt","a") as f:
        f.write("\n")
        for i in range(end_list_len):
            if i<=end_list_len-2:
                f.write(end_list[i-1]+"/")
            else:
                f.write(end_list[i-1])
    content_length-=1