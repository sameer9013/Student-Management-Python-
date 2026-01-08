Student={
    "Sameer":{"Hindi":78,"English":96,"Mathes":54,"Science":67,"Sst":73},
    "Sahil":{"Hindi":75,"English":43,"Mathes":65,"Science":97,"Sst":54},
    "Priyanka":{"Hindi":76,"English":56,"Mathes":87,"Science":57,"Sst":77},
    "Anu":{"Hindi":54,"English":43,"Mathes":86,"Science":92,"Sst":52},
    "Amir":{"Hindi":65,"English":43,"Mathes":87,"Science":90,"Sst":56},
    "Diwakar":{"Hindi":98,"English":54,"Mathes":48,"Science":85,"Sst":67},
    "Goldy":{"Hindi":57,"English":78,"Mathes":53,"Science":57,"Sst":89},
    "Shivain":{"Hindi":45,"English":78,"Mathes":98,"Science":76,"Sst":90},
    "Dhiru":{"Hindi":67,"English":89,"Mathes":56,"Science":89,"Sst":64},
    "Aniket":{"Hindi":32,"English":31,"Mathes":18,"Science":20,"Sst":36},
    "Aditiya":{"Hindi":65,"English":59,"Mathes":90,"Science":62,"Sst":78},
    "Sanchit":{"Hindi":98,"English":64,"Mathes":86,"Science":34,"Sst":95},
    "Sakshi":{"Hindi":88,"English":90,"Mathes":63,"Science":45,"Sst":97},
    "Vishwa":{"Hindi":75,"English":57,"Mathes":40,"Science":53,"Sst":74},
    "Rohit":{"Hindi":54,"English":67,"Mathes":70,"Science":86,"Sst":78},
    "Sangram":{"Hindi":90,"English":94,"Mathes":95,"Science":95,"Sst":45},
    "Saksham":{"Hindi":54,"English":86,"Mathes":95,"Science":47,"Sst":40},
    "Dhiraj":{"Hindi":65,"English":90,"Mathes":96,"Science":53,"Sst":90},
    "Vivek":{"Hindi":76,"English":78,"Mathes":84,"Science":86,"Sst":86},
    "Sidharth":{"Hindi":75,"English":53,"Mathes":90,"Science":72,"Sst":80},
    "Akki":{"Hindi":86,"English":67,"Mathes":87,"Science":48,"Sst":73},
    "Pallavi":{"Hindi":90,"English":62,"Mathes":75,"Science":49,"Sst":62},
    "Monisha":{"Hindi":30,"English":25,"Mathes":24,"Science":20,"Sst":67},
    "Esha":{"Hindi":30,"English":23,"Mathes":27,"Science":25,"Sst":80},
    "Remant":{"Hindi":73,"English":87,"Mathes":90,"Science":64,"Sst":40},
    "Kushagra":{"Hindi":19,"English":26,"Mathes":13,"Science":8,"Sst":11}
}

print("-"*50)

while True:
    user=input("Enter the Name of Student =").title()
    St=Student.get(user)

    if St==None:
        print("Record not Found!")
        print("Enter Correct Name!")
    else:
        val=St.values()
        tot_marks=sum(val)
        per=tot_marks/5

        print("-"*50)

        if per>=65:
            div="First division"
        elif per>=48:
            div="Second division"
        elif per>=35:
            div="Third division"
        else:
            div="Fail"

        print("Full Marks               :500")
        print("-"*50)
        print("Obtained Marks           :",tot_marks)
        print("-"*50)
        print("Percentage               :",per)
        print("-"*50)
        print("Division                 :",div)
        print("-"*50)

        next_student=int(input("If you want to check result of next student \n Then Key press 1 \n Exit Key press 0 \n Press key=" ))
        if next_student==1:
            continue
        else:
            break
        