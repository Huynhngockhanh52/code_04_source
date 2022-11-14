import json, subprocess

str_type = "[+]"
num=0

list_file = []
dict_mom = {}
list_mom = []
list_fields = []
dict_data = {} 


with open('test.txt') as f:
    line_count = 0
    for line in f:
        # xu ly dau vao
        line = line.lstrip("[")
        line = line.lstrip("91m")
        line = line.lstrip("92m")
        line = line.lstrip("94m")
        # print(line[0:3], end="")
        
        list_file.append(line)
        if (line[0:3] == str_type):
            str_temp = "Error " + str(num)
            num = num + 1
            dict_mom.update({str_temp: line.lstrip("[+]\x1b[0m ")})
            numline_end = line_count
        line_count += 1
    
    if len(dict_mom) == 1:
        dict_mom["Error 0"] = "Device has not a vulnerable"
        out_file = open("./output/out2.json", "w+")
        json.dump(dict_mom, out_file, indent = 4)
        out_file.close()
        exit(0)
    else:
        del dict_mom["Error 0"]
        
    for i in range(numline_end + 2, numline_end + num + 2): # start = line_end + 2,  end = start + num 
        list_mom.append(list_file[i])
    list_mom.pop(1)
f.close()
# print(line_count)

temp = list_mom[0]
list_fields = list(temp.strip("\n").split())
for i in range(1, len(list_mom)):
    description = list( list_mom[i].strip("\n").split())        
    temp = "Error " + str(i)
    sno = dict_mom.get(temp).strip("\n")
    k = 0
    dict2 = {"Error":sno.strip("is vulnerable")}
    while k < len(list_fields):
        dict2[list_fields[k]]= description[k]
        k = k + 1
    dict_data[sno]= dict2
out_file = open("./output/out2.json", "w+")
json.dump(dict_data, out_file, indent = 4)
out_file.close()