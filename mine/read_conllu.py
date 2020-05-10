file1 = open("/Users/rohitpentapati/PycharmProjects/ccbd/hi_hdtb-ud-dev.conllu","r")
contents = file1.read()
l = len(contents)

while("# text" in contents):
    ind = contents.find("# text")
    # print(ind)
    start = ind
    result = ""
    while(contents[start] != "\n"):
        result += contents[start]
        start += 1
    result = result.strip("# text = ")
    # print(result)
    contents = contents.replace('# text', '', 1) 

    file2 = open("/Users/rohitpentapati/PycharmProjects/ccbd/conllu_hindi.txt", "a")
    file2.write("\n")
    file2.write(result) 
    file2.close() 
file1.close()