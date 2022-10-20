import ast
def restaurant():
    files = open("log_file/case1.log", 'r')
    l = files.read().splitlines()
    a=dict()
    for i in l:
        if i:
            if l.count(i)==1:
                d=ast.literal_eval(i.split(": ")[1])
                if a.get(d[1]):
                    a[d[1]]+=[d[0]]
                else:
                    a[d[1]]=[d[0]]
            else:
                return "The Repeating Data Found"
    a= {i:a[i] for i in sorted(a,key=lambda i:len(a[i]),reverse=True)}
    r=list(a.keys())
    return ", ".join(r[:3])

if __name__=="__main__":
    print(restaurant())
