class Multifac():
    
    def Subfields():
        print("Sub-fields in AI are:")
        list=["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        for sub in list:
            print(sub)

            
    def OddEven():
        num=int(input("Enter a number:"))
        if((num%2==0)):
            print(num,"is Even number")
              
    def Elegible():
            gender=input("Your Gender:")
            age=int(input("Your age:"))
            if gender=="Male": 
                if age>=21:
                    print("Eligible")
                else:  
                    print("Not Eligible")
            elif gender=="Female":    
                if age>=18:
                    print("Eligible")
                else: 
                    print("Not Eligible")


    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        total=sub1+sub2+sub3+sub4+sub5
        print("total=", total)
        percent=(total/500)*100
        print("percentage:",percent)
        
    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        print("Area formula:,(height*breadth)/2")
        print("Area of Triangle:",(height*breadth)/2)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth1=int(input("Breadth:"))
        Perimeterformula=height1+height2+breadth1
        print("Perimeter formula:,height1+height2+breadth1")
        print("Perimeter of Triangle:",height1+height2+breadth1)

