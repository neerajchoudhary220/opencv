class  comapres:
    def filterTxt():
                fileB = open('B.txt','r',encoding='utf8')
                compare_file = open('compare.txt','a',encoding='utf8')
                lines = fileB.readlines()
                i,x=0,1
                for line in lines:
                    linee = line.split('=>', x)[0]
                    with open('A.txt','r',encoding='utf8') as fileA:
                        fileALine = fileA.readlines()[i]
                        fileALine = fileALine.split('=>',x)[0]
                        if linee != fileALine:
                            compare_file.write(line)

                    
                    i=i+1

                fileA.close()
                # os.remove('temp.txt')
                print("done")