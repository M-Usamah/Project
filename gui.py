from tkinter import *
class gui:
    
    def __init__(self,frame):
        frame.state("zoomed")
        root.title("Updating Employees Record")
    #     pass
    # def setup_window(self, frame):
        fullwindow = Frame(frame, bg='#5f5f5f')
        fullwindow.pack(fill = BOTH, expand = 1)
        topFrame = Frame(fullwindow, bg = '#5f5f5f', height = 20)
        topFrame.pack(side = TOP, fill = X)
        setting_emp_id_name_Frame = Frame(fullwindow, bg = '#5f5f5f', height = 50)
        setting_emp_id_name_Frame.pack(side = TOP, fill = X)
        emp_id_name_Frame = Frame(setting_emp_id_name_Frame, bg='#f1f1f1',bd = 5,relief = RIDGE,height = 50, width = 1300 )
        emp_id_name_Frame.pack(side = TOP)
        emp_id_Frame = Frame(emp_id_name_Frame, bg = '#f1f1f1',width = 200, height = 50)
        emp_id_Label = Label(emp_id_Frame, text = "Employee ID", font= ("times new romen",10,"bold"))
        emp_id_Label.pack()
        emp_id_Frame.pack(side = LEFT, fill = X, padx = 105)
        emp_space_Frame = Frame(emp_id_name_Frame,width = 150, height = 50)
        emp_space_Frame.pack(side = LEFT, fill = X, padx = 140)
        emp_name_Frame = Frame(emp_id_name_Frame, bg = '#f1f1f1',width = 200, height = 50)
        emp_name_Frame.pack(side = LEFT, fill = X, padx = 105)
        emp_name_Label = Label(emp_name_Frame, text = "Employee Name", font= ("times new romen",10,"bold"))
        emp_name_Label.pack()
        centerheightFrame = Frame(fullwindow, bg = '#5f5f5f', height = 20)
        centerheightFrame.pack(side = TOP, fill = X)

        list_Frame = Frame(fullwindow, bg = '#f1f1f1',bd =5,relief = RIDGE , height = 550, width = 250)
        list_Frame.pack(side = LEFT, padx = 50)
        spaceInTopListFrame = Frame(list_Frame, bg ="#f1f1f1",width =40,height = 160)
        spaceInTopListFrame.pack(side =TOP, fill = X)
        personalButton = Button(list_Frame, text = 'Personal', font= ("times new romen",10,"bold"), width = 20,command = lambda:self.display_Frames(self.personalFrame))
        personalButton.pack(side = TOP, pady = 1,padx = 20)
        addressButton = Button(list_Frame, text = "Adddress", font= ("times new romen",10,"bold"), width = 20, command = lambda:self.display_Frames(self.addressFrame))
        addressButton.pack(side = TOP, pady = 1,padx = 20)
        contactButton = Button(list_Frame,text = "Contact",font= ("times new romen",10,"bold"),width = 20,command = lambda:self.display_Frames(self.contactFrame))
        contactButton.pack(side = TOP, pady = 1,padx = 20)
        vacationButton = Button(list_Frame,text = "Vacation",font= ("times new romen",10,"bold"),width = 20,command = lambda:self.display_Frames(self.vacationFrame))
        vacationButton.pack(side = TOP, pady = 1,padx = 20)
        sponorButton = Button(list_Frame,text = "Sponsor",font= ("times new romen",10,"bold"),width = 20,command = lambda:self.display_Frames(self.sponsorFrame))
        sponorButton.pack(side = TOP, pady = 1,padx = 20)
        projectButton = Button(list_Frame,text = "Project",font= ("times new romen",10,"bold"),width = 20,command = lambda:self.display_Frames(self.projectFrame))
        projectButton.pack(side = TOP, pady = 1,padx = 20)
        statusButton = Button(list_Frame,text = "Status",font= ("times new romen",10,"bold"),width = 20,command = lambda:self.display_Frames(self.statusFrame))
        statusButton.pack(side = TOP, pady = 1,padx = 20)
        spaceInbottomListFrame = Frame(list_Frame, bg ="#f1f1f1",width =40,height = 160)
        spaceInbottomListFrame.pack(side =TOP, fill = X)

        detailFrame = Frame(fullwindow, bg = '#f1f1f1', bd = 5, relief = RIDGE, height = 550 ,width = 920 )
        detailFrame.pack(side = LEFT, padx = 10)
        self.personalFrame = Frame(detailFrame, bg = '#f1f1f1', bd = 5, relief = RIDGE, height = 530 ,width = 900)
        self.personalFrame.pack( padx = 5,pady = 5)
        self.addressFrame = Frame(detailFrame, bg = 'blue', bd = 5, relief = RIDGE, height = 530 ,width = 900)
        self.vacationFrame = Frame(detailFrame, bg = 'green', bd = 5, relief = RIDGE, height = 530 ,width = 900)
        self.sponsorFrame = Frame(detailFrame, bg = 'yellow', bd = 5, relief = RIDGE, height = 530 ,width = 900)
        self.projectFrame = Frame(detailFrame, bg = 'orange', bd = 5, relief = RIDGE, height = 530 ,width = 900)
        self.statusFrame = Frame(detailFrame, bg = 'black', bd = 5, relief = RIDGE, height = 530 ,width = 900)
        self.contactFrame = Frame(detailFrame, bg = 'pink', bd = 5, relief = RIDGE, height = 530 ,width = 900)

        self.Setting_Personal_Frame()

    def Setting_Personal_Frame(self): 
        #================================dividing the portion ========================================================
        Top_personal_Frame = Frame(self.personalFrame,bg = '#f1f1f1', height = 240 ,width = 900)
        Top_personal_Frame.pack(side = TOP,expand = 1)
        Center_Presonal_Frame = Frame(self.personalFrame,bg = '#f1f1f1',bd = 5, relief = RIDGE, height = 240 ,width = 900)
        Center_Presonal_Frame.pack(side = TOP,expand = 1) 
        self.Bottom_personal_Frame = Frame(self.personalFrame,bg = 'purple', height = 50 ,width = 900)
        self.Bottom_personal_Frame.pack(side = TOP,expand = 1)
        
        #===================Setting Name portion=============================================
        setting_Name_Frame = Frame(Top_personal_Frame,  bg = "#f1f1f1",bd = 5, relief = RIDGE)
        setting_Name_Frame.pack(side = LEFT, fill = BOTH, expand = 1)
        

        aggTop_name_Frame=Frame(setting_Name_Frame,bg = '#f1f1f1',width = 440, height = 70)
        aggTop_name_Frame.pack(side =TOP, fill = BOTH)
        
        firstName_frame = Frame(setting_Name_Frame,bg = '#f1f1f1',width = 440)
        firstName_frame.pack(side =TOP, fill = BOTH)
        firstName_Left_frame = Frame(firstName_frame,bg = '#f1f1f1',width = 220)
        firstName_Left_frame.pack(side = LEFT,padx =40)
        firstName_Label = Label(firstName_Left_frame, text= 'First Name',font= ("times new romen",10,"bold"))
        firstName_Label.pack(side = LEFT)
        firstName_Right_frame = Frame(firstName_frame,bg = '#f1f1f1',width = 220)
        firstName_Right_frame.pack(side = LEFT)
        firstName_Entry = Entry(firstName_Right_frame,width = 35)
        firstName_Entry.pack(side = LEFT)

        secondName_frame = Frame(setting_Name_Frame,bg = '#f1f1f1',width = 440)
        secondName_frame.pack(side = TOP, fill = BOTH)
        secondName_Left_frame = Frame(secondName_frame,bg = '#f1f1f1',width = 225)
        secondName_Left_frame.pack(side = LEFT,padx =20)
        secondName_Label = Label(secondName_Left_frame, text= 'Second Name',font= ("times new romen",10,"bold"))
        secondName_Label.pack(side = LEFT)
        secondName_Right_frame = Frame(secondName_frame,bg = '#f1f1f1',width = 225)
        secondName_Right_frame.pack(side = LEFT)
        secondName_Entry = Entry(secondName_Right_frame,width = 35)
        secondName_Entry.pack(side = LEFT, padx= 19)

        middleName_frame = Frame(setting_Name_Frame,bg = '#f1f1f1',width = 440)
        middleName_frame.pack(side = TOP, fill = BOTH)
        middleName_Left_frame = Frame(middleName_frame,bg = '#f1f1f1',width = 225)
        middleName_Left_frame.pack(side = LEFT,padx =25)
        middleName_Label = Label(middleName_Left_frame, text= 'Middle Name',font= ("times new romen",10,"bold"))
        middleName_Label.pack(side = LEFT)
        middleName_Right_frame = Frame(middleName_frame,bg = '#f1f1f1',width = 225)
        middleName_Right_frame.pack(side = LEFT )
        middleName_Entry = Entry(middleName_Right_frame,width = 35)
        middleName_Entry.pack(side = LEFT,padx = 15)

        lasteName_frame = Frame(setting_Name_Frame,bg = '#f1f1f1',width = 440)
        lasteName_frame.pack(side = TOP, fill = BOTH)
        lasteName_Left_frame = Frame(lasteName_frame,bg = '#f1f1f1',width = 225)
        lasteName_Left_frame.pack(side = LEFT,padx =35)
        lasteName_Label = Label(lasteName_Left_frame, text= 'Laste Name',font= ("times new romen",10,"bold"))
        lasteName_Label.pack(side = LEFT)
        lasteName_Right_frame = Frame(lasteName_frame,bg = '#f1f1f1',width = 225)
        lasteName_Right_frame.pack(side = LEFT)
        lasteName_Entry = Entry(lasteName_Right_frame,width = 35)
        lasteName_Entry.pack(side = LEFT,padx = 3)

        aggBottom_name_Frame=Frame(setting_Name_Frame,bg = '#f1f1f1',width = 440, height = 70)
        aggBottom_name_Frame.pack(side =TOP, fill = BOTH)

        #===============================Setting Age piortion =================================
        setting_Age_Frame = Frame(Top_personal_Frame, bg = "#F1F1F1",bd = 5, relief = RIDGE,width = 450)
        setting_Age_Frame.pack(side = LEFT,fill = BOTH, expand = 1)

        aggTop_age_Frame = Frame(setting_Age_Frame, bg = "#f1f1f1",width = 440,height = 40)
        aggTop_age_Frame.pack(side = TOP)

        gender_frame = Frame(setting_Age_Frame,bg = '#f1f1f1',width = 440)
        gender_frame.pack(side = TOP, fill = BOTH)
        gender_Left_frame = Frame(gender_frame,bg = '#f1f1f1',width = 225)
        gender_Left_frame.pack(side = LEFT,padx =41)
        gender_Label = Label(gender_Left_frame, text= 'Gender',font= ("times new romen",10,"bold"))
        gender_Label.pack(side = LEFT)
        gender_Right_frame = Frame(gender_frame,bg = '#f1f1f1',width = 225)
        gender_Right_frame.pack(side = LEFT)
        gender_Entry = Entry(gender_Right_frame,width = 35)
        gender_Entry.pack(side = LEFT)

        age_frame = Frame(setting_Age_Frame,bg = '#f1f1f1',width = 440)
        age_frame.pack(side = TOP, fill = BOTH)
        age_Left_frame = Frame(age_frame,bg = '#f1f1f1',width = 225)
        age_Left_frame.pack(side = LEFT,padx =15)
        age_Label = Label(age_Left_frame, text= 'Date of Birth',font= ("times new romen",10,"bold"))
        age_Label.pack(side = LEFT)
        age_Right_frame = Frame(age_frame,bg = '#f1f1f1',width = 225)
        age_Right_frame.pack(side = LEFT)
        age_Entry = Entry(age_Right_frame,width = 35)
        age_Entry.pack(side = LEFT,padx = 20)

        religious_frame = Frame(setting_Age_Frame,bg = '#f1f1f1',width = 440)
        religious_frame.pack(side = TOP, fill = BOTH)
        religious_Left_frame = Frame(religious_frame,bg = '#f1f1f1',width = 225)
        religious_Left_frame.pack(side = LEFT,padx =35)
        religious_Label = Label(religious_Left_frame, text= 'Religious',font= ("times new romen",10,"bold"))
        religious_Label.pack(side = LEFT)
        religious_Right_frame = Frame(religious_frame,bg = '#f1f1f1',width = 225)
        religious_Right_frame.pack(side = LEFT)
        religious_Entry = Entry(religious_Right_frame,width = 35)
        religious_Entry.pack(side = LEFT)

        nationalaty_frame = Frame(setting_Age_Frame,bg = '#f1f1f1',width = 440)
        nationalaty_frame.pack(side = TOP, fill = BOTH)
        nationalaty_Left_frame = Frame(nationalaty_frame,bg = '#f1f1f1',width = 225)
        nationalaty_Left_frame.pack(side = LEFT,padx =30)
        nationalaty_Label = Label(nationalaty_Left_frame, text= 'Nationality',font= ("times new romen",10,"bold"))
        nationalaty_Label.pack(side = LEFT)
        nationalaty_Right_frame = Frame(nationalaty_frame,bg = '#f1f1f1',width = 225)
        nationalaty_Right_frame.pack(side = LEFT)
        nationalaty_Entry = Entry(nationalaty_Right_frame,width = 35)
        nationalaty_Entry.pack(side = LEFT,padx = 1)

        maritalStatus_frame = Frame(setting_Age_Frame,bg = '#f1f1f1',width = 440)
        maritalStatus_frame.pack(side = TOP, fill = BOTH)
        maritalStatus_Left_frame = Frame(maritalStatus_frame,bg = '#f1f1f1',width = 225)
        maritalStatus_Left_frame.pack(side = LEFT,padx =15)
        maritalStatus_Label = Label(maritalStatus_Left_frame, text= 'Marital Status',font= ("times new romen",10,"bold"))
        maritalStatus_Label.pack(side = LEFT)
        maritalStatus_Right_frame = Frame(maritalStatus_frame,bg = '#f1f1f1',width = 225)
        maritalStatus_Right_frame.pack(side = LEFT)
        maritalStatus_Entry = Entry(maritalStatus_Right_frame,width = 35)
        maritalStatus_Entry.pack(side = LEFT,padx = 10)
        
        bloodgroup_frame = Frame(setting_Age_Frame,bg = '#f1f1f1',width = 440)
        bloodgroup_frame.pack(side = TOP, fill = BOTH)
        bloodgroup_Left_frame = Frame(bloodgroup_frame,bg = '#f1f1f1',width = 225)
        bloodgroup_Left_frame.pack(side = LEFT,padx =22)
        bloodgroup_Label = Label(bloodgroup_Left_frame, text= 'Blood Group',font= ("times new romen",10,"bold"))
        bloodgroup_Label.pack(side = LEFT)
        bloodgroup_Right_frame = Frame(bloodgroup_frame,bg = '#f1f1f1',width = 225)
        bloodgroup_Right_frame.pack(side = LEFT)
        bloodgroup_Entry = Entry(bloodgroup_Right_frame,width = 35)
        bloodgroup_Entry.pack(side = LEFT,padx = 4)
        #==========================Setting relative frame==============
        setting_Relative_Frame = Frame(Center_Presonal_Frame, bg = "#F1F1F1",width = 890)
        setting_Relative_Frame.pack(side = LEFT,fill = BOTH, padx = 240)

        Relative_Frame = Frame(setting_Relative_Frame, bg = "#F1F1F1",bd = 5, relief = RIDGE)
        Relative_Frame.pack(side = LEFT,fill = BOTH, expand = 1)

        agg_relative_top_Frame = Frame(Relative_Frame,bg = '#f1f1f1',height = 40)
        agg_relative_top_Frame.pack(side = TOP)

        kin_frame = Frame(Relative_Frame,bg = '#f1f1f1',width = 890)
        kin_frame.pack(side = TOP, fill = BOTH)
        kin_Left_frame = Frame(kin_frame,bg = '#f1f1f1',width = 225)
        kin_Left_frame.pack(side = LEFT,padx =22)
        kin_Label = Label(kin_Left_frame, text= 'Next of Kin',font= ("times new romen",10,"bold"))
        kin_Label.pack(side = LEFT)
        kin_Right_frame = Frame(kin_frame,bg = '#f1f1f1',width = 225)
        kin_Right_frame.pack(side = LEFT)
        kin_Entry = Entry(kin_Right_frame,width = 40)
        kin_Entry.pack(side = LEFT,padx = 18)

        education_frame = Frame(Relative_Frame,bg = '#f1f1f1',width = 890)
        education_frame.pack(side = TOP, fill = BOTH)
        education_Left_frame = Frame(education_frame,bg = '#f1f1f1',width = 225)
        education_Left_frame.pack(side = LEFT,padx =29)
        education_Label = Label(education_Left_frame, text= 'Education',font= ("times new romen",10,"bold"))
        education_Label.pack(side = LEFT)
        education_Right_frame = Frame(education_frame,bg = '#f1f1f1',width = 225)
        education_Right_frame.pack(side = LEFT)
        education_Entry = Entry(education_Right_frame,width = 40)
        education_Entry.pack(side = LEFT,padx = 12)

        qualification_frame = Frame(Relative_Frame,bg = '#f1f1f1',width = 890)
        qualification_frame.pack(side = TOP, fill = BOTH)
        qualification_Left_frame = Frame(qualification_frame,bg = '#f1f1f1',width = 225)
        qualification_Left_frame.pack(side = LEFT,padx =15)
        qualification_Label = Label(qualification_Left_frame, text= 'Qualification',font= ("times new romen",10,"bold"))
        qualification_Label.pack(side = LEFT)
        qualification_Right_frame = Frame(qualification_frame,bg = '#f1f1f1',width = 225)
        qualification_Right_frame.pack(side = LEFT)
        qualification_Entry = Entry(qualification_Right_frame,width = 40)
        qualification_Entry.pack(side = LEFT,padx = 21)

        profession_frame = Frame(Relative_Frame,bg = '#f1f1f1',width = 890)
        profession_frame.pack(side = TOP, fill = BOTH)
        profession_Left_frame = Frame(profession_frame,bg = '#f1f1f1',width = 225)
        profession_Left_frame.pack(side = LEFT,padx =29)
        profession_Label = Label(profession_Left_frame, text= 'Profession',font= ("times new romen",10,"bold"))
        profession_Label.pack(side = LEFT)
        profession_Right_frame = Frame(profession_frame,bg = '#f1f1f1',width = 225)
        profession_Right_frame.pack(side = LEFT)
        profession_Entry = Entry(profession_Right_frame,width = 40)
        profession_Entry.pack(side = LEFT,padx = 8)

        hobbies_frame = Frame(Relative_Frame,bg = '#f1f1f1',width = 890)
        hobbies_frame.pack(side = TOP, fill = BOTH)
        hobbies_Left_frame = Frame(hobbies_frame,bg = '#f1f1f1',width = 225)
        hobbies_Left_frame.pack(side = LEFT,padx =40)
        hobbies_Label = Label(hobbies_Left_frame, text= 'Hobbies',font= ("times new romen",10,"bold"))
        hobbies_Label.pack(side = LEFT)
        hobbies_Right_frame = Frame(hobbies_frame,bg = '#f1f1f1',width = 225)
        hobbies_Right_frame.pack(side = LEFT)
        hobbies_Entry = Entry(hobbies_Right_frame,width = 40)
        hobbies_Entry.pack(side = LEFT,padx = 1)

        agg_relative_bottom_Frame = Frame(Relative_Frame,bg = '#f1f1f1',height = 40)
        agg_relative_bottom_Frame.pack(side = TOP)

        #=======================buttons======================================
        self.snButton(self.Bottom_personal_Frame,self.addressFrame)        

        # self.bsnButton(self.Bottom_personal_Frame)

    def snButton(self,parrent,next_frame):
        setting_Button_Frame = Frame(self.Bottom_personal_Frame, bg = "#f1f1f1",height = 50,width = 890)
        setting_Button_Frame.pack(side = TOP)

        save_button = Button(setting_Button_Frame, text = 'Save',width = 10)
        save_button.pack(side = LEFT,padx= 350)

        Next_button = Button(setting_Button_Frame, text = 'Next',width = 10,command = lambda:self.display_Frames(next_frame))
        Next_button.pack(side = RIGHT,padx= 10)
    
    def bsnButton(self,parrent,back_frame,next_frame):    
        setting_Button_Frame = Frame(parrent, bg = "#f1f1f1",height = 50,width = 890,command = lambda:self.display_Frames(back_frame))
        setting_Button_Frame.pack(side = TOP)
        
        back_button=Button(setting_Button_Frame, text = 'Back',width = 10)
        back_button.pack(side = LEFT,padx= 10)

        save_button = Button(setting_Button_Frame, text = 'Save',width = 10)
        save_button.pack(side = LEFT,padx= 300)

        Next_button = Button(setting_Button_Frame, text = 'Next',width = 10,command = lambda:self.display_Frames(next_frame))
        Next_button.pack(side = RIGHT,padx= 10)
    def display_Frames(self,frames):
        self.personalFrame.forget()
        self.addressFrame.forget()
        self.contactFrame.forget()
        self.vacationFrame.forget()
        self.sponsorFrame.forget()
        self.projectFrame.forget()
        self.statusFrame.forget()
        frames.tkraise()
        frames.pack( padx = 5,pady = 5)




root = Tk()
g1 = gui(root)
root.mainloop()