print("What is your age ? ")
Age = int(input())
if Age < 18 :
    print("Sorry ! You are not allowed to drive")
elif Age > 18 and Age <= 100 :
    print("Congo, You are allowed to drive")
elif Age > 100 :
    print("Uhohh ! You are too old to drive")
elif Age == 18 :
    print("Let's meet physically and decide whether you are allowed to drive")
