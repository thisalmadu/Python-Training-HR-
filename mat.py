m,n = input().split()

for i in range(int(m/2)):
  print(((2*i+1)*".|.").center(int(n),"-"))

print("Welcome".center(n,"-"))

for j in range(int(m/2),0,-1):
  print(((2*j-1)*".|.").center(int(n),"-"))
