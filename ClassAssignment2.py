class Assignments():
    def subfieldsAI():
        lists=['Machine Learning','Neural Networks','Vision','Robotics','Speech processing','Natural Language Processing']
        print("Sub fields in AI are:")
        for i in lists:
                print(i)
    def oddeven():
        NUM=int(input("Enter a number:"))
        if((NUM%2)==1):
            print(NUM,"is odd number")
        else:
            print(NUM, "is even number")
            
    def eligible():
        gender=input("Your gender:")
        age=int(input("Youe Age:"))
        if(gender=='male'):
            if (age>21):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif(gender=="female"):
            if(age>18):
                print("ELIGIBLE")
            else:
                print('NOT ELIGIBLE')

    def percentage():
        sub1= int(input("Subject1="))
        sub2= int(input("Subject2="))
        sub3= int(input("Subject3="))
        sub4= int(input("Subject4="))
        sub5= int(input("Subject5="))
        total=sub1+sub2+sub3+sub4+sub5
        percentage=(total/500)*100
        print("Total=",total)
        print("Percentage=",percentage)
        
    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        print("Area formula:(Height*Breadth)/2")
        area=(height*breadth)/2
        print("Area of Triangle:",area)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth1=int(input("Breadth:"))
        print("Perimeter Formula:Height1+Height2+Breadth")
        perimeter=height1+height2+breadth1
        print("Perimeter of Triangle:",perimeter)