
#File 1 -write method/create file and write file
file=open('demofile.txt','w')
for i in range(1,20):

    file.write('Line'+str(i)+'\n')
file.write('line21')
file.close()
#Read only
file=open('demofile.txt','r')
content2=file.read()
print(content2)
file.seek(0) #It sends pointer to 0 position.If not content2 will not be displayed

content=file.readlines()
# to remove \n from the list.
content=[i.rstrip('\n') for i in content]
print(content)

file.close()

#Read+ writing r+

file=open('demofile.txt','r+')

content3=file.read()

print('this is content3\n'+content3)
file.close()