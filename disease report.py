from tkinter import*
root = Tk()
root.title("doctor report")
root.geometry("500x500")

#Q1
question1_radioButton=stringVar(value="0")
Question1=Label(root, text="do you experience shortness of breath during routine activities or while at rest/lying down?")
Question1.pack()
question1_r1=Radiobuttton(root, text = "yes", variable=question1_radiobutton, value="yes")
question1_r1.pack()
question1_r2=Radiobuttton(root, text = "no", variable=question1_radiobutton, value="no")
question1_r2.pack()

#Q2
question2_radioButton=stringVar(value="0")
Question2=Label(root, text="Do you have swelling in feet/ankles/legs/abdomen?")
Question2.pack()
question2_r1=Radiobuttton(root, text = "yes", variable=question2_radiobutton, value="yes")
question2_r1.pack()
question2_r2=Radiobuttton(root, text = "no", variable=question2_radiobutton, value="no")
question2_r2.pack()

#Q3
question3_radioButton=stringVar(value="0")
Question3=Label(root, text="Do you feel any of these symptoms-connfusion,disorientation or loss of memory?")
Question3.pack()
question3_r1=Radiobuttton(root, text = "yes", variable=question3_radiobutton, value="yes")
question3_r1.pack()
question3_r2=Radiobuttton(root, text = "no", variable=question3_radiobutton, value="no")
question3_r2.pack()

#Q4
question4_radioButton=stringVar(value="0")
Question4=Label(root, text="Do you experience wheezing/coughing that produces white or pink blood tinged mucus?")
Question4.pack()
question4_r1=Radiobuttton(root, text = "yes", variable=question4_radiobutton, value="yes")
question4_r1.pack()
question4_r2=Radiobuttton(root, text = "no", variable=question4_radiobutton, value="no")
question4_r2.pack()

#Q5
question5_radioButton=stringVar(value="0")
Question5=Label(root, text="Do you experience fatiguness?")
Question5.pack()
question5_r1=Radiobuttton(root, text = "yes", variable=question5_radiobutton, value="yes")
question5_r1.pack()
question5_r2=Radiobuttton(root, text = "no", variable=question5_radiobutton, value="no")
question5_r2.pack()


#defination(if conditional)
def fever_score():
    score=0
    if question1_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question2_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question3_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question4_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question5_radioButton.get()=="yes":
        score = score+20
        print(score)    
        
     if score <= 20:
         messagebox.showinfo("Report","Visiting a doctor is not required.")
     elif  score > 20 and score <= 40:
         messagebox.showinfo("Report","You may have to visit a doctor.")
     else :
         messagebox.showinfo("Report","I strongly advis you to visit a doctor.")

btn = Button(root, text="click me", command= fever_score)
btn.pack()
root.mainloop()