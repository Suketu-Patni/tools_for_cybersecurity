import subprocess

# string = "~abbccdd"



# print(output)

# # command += "aabbccdd"

# def binary_search(l1):
#     length = len(l1)


# # subprocess.run(command, shell=True, executable="/bin/bash")
# # p = process('./bruteforcer')
# # p.interactive()
# # p.write(b"aabbccdd")
# print()


low = 33
high = 126

for i in range(low, high+1):
    string = "penniless" + chr(i)
    command = f"echo \"{string}\" | ./bruteforcer"
    if string not in ['penniless"', 'penniless\\', 'penniless`']:
        output = subprocess.check_output(command, shell=True, executable="/bin/bash").decode().strip()

    if output[-4:] == "high":
        print(string)
        break
    




# with open("wordlist.txt") as fs:
#     contents = fs.readlines()

# length = len(contents)

# for i in contents:
#     string = i.strip()
#     command = f"echo \"{string}\" | ./bruteforcer"
#     output = subprocess.check_output(command, shell=True, executable="/bin/bash").decode().strip()

#     if output[22] != "W":
#         print(string)



# print(contents[:10])



# # while 

# l1 = [1,2,3,4,5,6,7,7,8,9,9,10,10,14,15,20,21]

# to_find = 15

# length = len(l1)

# def binary_search(arr, low, high):
 
#     if high > low:
#         mid = (high + low) // 2

#         string = arr[mid].strip()
        

#         #Enter your password : WRONG :( Key too high


        
        
#         # order = 
        
#         elif output[-4:] == "high":
#             return binary_search(arr, low, mid - 1)
        
#         else:
#             return binary_search(arr, mid + 1, high)
 
#     elif high == low:
#         return arr[high]
#     else:
#         return -1
    
# print(binary_search(contents, 0, length))