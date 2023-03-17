import os


os.system("clear") #To clear the terminal

print("Welcome : ")
print("[this is most worse in sudo, so if not work, run in sudo]\n") # for problem 
print ("Enter the target you want attack, or Nmap plage ip : ") 
input1 = input() # for scan terminal
nmap_Command = ("nmap -sV -oX /Users/nils/Desktop/output.xml " +  input1) #temp var for run the command

#print('\nStarting command for this target -> ' + input1) #print a message
os.system(nmap_Command)# run the command
print("\n")
