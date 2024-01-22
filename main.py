
#  Md AMJAD ANSARI

from tkinter import *
from tkinter import ttk
import  tkinter.messagebox


class atm:
    def __init__(self,root):
        self.root = root
        blank_space = " "
        self.root.title(110 * blank_space + "ATM System")
        self.root.geometry("790x760+280+0")
        self.root.configure(background = 'gainsboro')

#======================================================FRAMES========================================================

        MainFrame = Frame(self.root, bd=20, width=760, height=700, relief=RIDGE)
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        # lbl = Label(TopFrame1, text="Enter Your Pin")
        # lbl.grid(side=LEFT)
        # ent = Entry(TopFrame1, bd=5)
        # ent.grid(side=LEFT)
        TopFrame1.grid(row=2 ,column=0, padx=12)

        TopFrame2 = Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        TopFrame2.grid(row=1 ,column=0, padx=8)

        TopFrame2Left = Frame(TopFrame2, bd=5, width=190, height=300, relief=RIDGE)
        TopFrame2Left.grid(row=0, column=0, padx=3)

        TopFrame2Mid = Frame(TopFrame2, bd=5, width=190, height=300, relief=RIDGE)
        TopFrame2Mid.grid(row=0, column=1, padx=3)
        # lbl = Label(TopFrame2Mid, text="Enter Your Pin",height=10,width=10)
        # lbl.grid(row=1, column=2,padx=3)
        # ent = Entry(TopFrame2Mid, bd=5)
        # ent.grid(row=0, column=2)

        TopFrame2Right = Frame(TopFrame2, bd=5, width=190, height=300, relief=RIDGE)
        TopFrame2Right.grid(row=0, column=2, padx=3)

# ======================================================FUNCTIONS========================================================

        def enter_Pin():
            pinNo = self.txtReceipt.get("1.0","end-1c")
            self.txtReceipt.insert(END, 'Enter Your Pin\t\t\t' + "\n\n\n\n")


            if((pinNo == str("0443")) or (pinNo == str("1886")) or (pinNo == str("2411"))):
                self.txtReceipt.delete("1.0",END)

                self.txtReceipt.insert(END, '\t\t       ATM' + "\n\n")
                # self.txtReceipt.insert(END, 'Withdraw Cash\t\t\t Loan' + "\n\n\n\n")
                # self.txtReceipt.insert(END, 'Cash With Receipt\t\t\t Deposit' + "\n\n\n\n")
                # self.txtReceipt.insert(END, 'Balance\t\t\t Request New Pin' + "\n\n\n\n")
                # self.txtReceipt.insert(END, 'Mini Statement\t\t\t Print Statement' + "\n\n\n\n")

                self.txtReceipt.insert(END, 'Balance Inquiry\t\t\t Deposit' + "\n\n\n\n")
                self.txtReceipt.insert(END, 'Withdraw Cash\t\t\t Pin Change' + "\n\n\n\n")
                self.txtReceipt.insert(END, 'Statement\t\t\t' + "\n\n\n\n")


                self.btn_arrow_left1 = Button(TopFrame2Left, text="CLICK_HERE=>", state=NORMAL, command=balance)
                self.btn_arrow_left1.grid(row=0, column=0, padx=4, pady=20)

                self.btn_arrow_left2 = Button(TopFrame2Left, text="CLICK_HERE=>", state=NORMAL, command=withdrawcash)
                self.btn_arrow_left2.grid(row=1, column=0, padx=4, pady=20)

                self.btn_arrow_left3 = Button(TopFrame2Left, text="CLICK_HERE=>", state=NORMAL, command=statement)
                self.btn_arrow_left3.grid(row=2, column=0, padx=4, pady=20)

                self.btn_arrow_left4 = Button(TopFrame2Left, text="CLICK_HERE=>", state=NORMAL)
                self.btn_arrow_left4.grid(row=3, column=0, padx=4, pady=20)

# ====================================================================================================================#

                self.btn_arrow_right1 = Button(TopFrame2Right, text="<=CLICK_HERE", state=NORMAL, command=deposit)
                self.btn_arrow_right1.grid(row=0, column=0, padx=4, pady=20)

                self.btn_arrow_right2 = Button(TopFrame2Right, text="<=CLICK_HERE", state=NORMAL, command=Pin_Change)
                self.btn_arrow_right2.grid(row=1, column=0, padx=4, pady=20)

                self.btn_arrow_right3 = Button(TopFrame2Right, text="<=CLICK_HERE", state=NORMAL)
                self.btn_arrow_right3.grid(row=2, column=0, padx=4, pady=20)

                self.btn_arrow_right4 = Button(TopFrame2Right, text="<=CLICK_HERE", state=NORMAL)
                self.btn_arrow_right4.grid(row=3, column=0, padx=4, pady=20)

            else:
                self.txtReceipt.delete("1.0",END)
                self.txtReceipt.insert(END, 'Invalid Pin Number' + "\n\n")




        def clear():
            self.txtReceipt.delete("1.0", END)

            self.btn_arrow_left1 = Button(TopFrame2Left, text="CLICK_HERE=>", state=DISABLED)
            self.btn_arrow_left1.grid(row=0, column=0, padx=4, pady=20)

            self.btn_arrow_left2 = Button(TopFrame2Left, text="CLICK_HERE=>", state=DISABLED)
            self.btn_arrow_left2.grid(row=1, column=0, padx=4, pady=20)

            self.btn_arrow_left3 = Button(TopFrame2Left, text="CLICK_HERE=>", state=DISABLED)
            self.btn_arrow_left3.grid(row=2, column=0, padx=4, pady=20)

            self.btn_arrow_left4 = Button(TopFrame2Left, text="CLICK_HERE=>", state=DISABLED)
            self.btn_arrow_left4.grid(row=3, column=0, padx=4, pady=20)

 # ====================================================================================================================#

            self.btn_arrow_right1 = Button(TopFrame2Right, text="<=CLICK_HERE", state=DISABLED)
            self.btn_arrow_right1.grid(row=0, column=0, padx=4, pady=20)

            self.btn_arrow_right2 = Button(TopFrame2Right, text="<=CLICK_HERE", state=DISABLED)
            self.btn_arrow_right2.grid(row=1, column=0, padx=4, pady=20)

            self.btn_arrow_right3 = Button(TopFrame2Right, text="<=CLICK_HERE", state=DISABLED)
            self.btn_arrow_right3.grid(row=2, column=0, padx=4, pady=20)

            self.btn_arrow_right4 = Button(TopFrame2Right, text="<=CLICK_HERE", state=DISABLED)
            self.btn_arrow_right4.grid(row=3, column=0, padx=4, pady=20)

        def insert0():
            value0 = 0
            self.txtReceipt.insert(END,value0)

        def insert1():
            value1 = 1
            self.txtReceipt.insert(END,value1)

        def insert2():
            value2 = 2
            self.txtReceipt.insert(END,value2)

        def insert3():
            value3 = 3
            self.txtReceipt.insert(END,value3)

        def insert4():
            value4 = 4
            self.txtReceipt.insert(END,value4)

        def insert5():
            value5 = 5
            self.txtReceipt.insert(END,value5)

        def insert6():
            value6 = 6
            self.txtReceipt.insert(END,value6)

        def insert7():
            value7 = 7
            self.txtReceipt.insert(END,value7)

        def insert8():
            value8 = 8
            self.txtReceipt.insert(END,value8)

        def insert9():
            value9 = 9
            self.txtReceipt.insert(END,value9)

        def cancel():
            Cancel = tkinter.messagebox.askyesno("ATM", "Click yes if you want to cancel")
            if Cancel > 0:
                self.root.destroy()
                return

        def withdrawcash():
            enter_Pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.focus_set()


        def deposit():
            enter_Pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.focus_set()

        def Pin_Change():
            enter_Pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END, 'Enter Old Pin\t\t\t' + "\n\n\n\n")
            self.txtReceipt.insert(END, 'Enter New Pin\t\t\t' + "\n\n\n\n")
            self.txtReceipt.insert(END, 'Confirm Pin\t\t\t' + "\n\n\n\n")
            # self.txtReceipt.insert(END, 'Balance Inquiry\t\t\t Deposit' + "\n\n\n\n")

        def balance():
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END, 'Rs: 20,000' + "\n")

        def statement():
            pinNo1 = str(self.txtReceipt.get("1.0", "end - 1c"))
            pinNo2 = str(pinNo1)
            pinNo3 = float(pinNo2)
            pinNo4 = float(20000 - (pinNo3))
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.insert(END,'\n\t' + str(pinNo4) + "\t\t")
            self.txtReceipt.insert(END, '\t\t\t\n\n   Account Balance Rs' +str(pinNo4) + "\t\t\n\n")
            self.txtReceipt.insert(END, 'Rent \t\t\t\t Rs 20000' + "\n\n")
            self.txtReceipt.insert(END, 'Tax \t\t\t\t Rs 45.4' + "\n\n")




        # ======================================================WIDGET===========================================================

        self.txtReceipt = Text(TopFrame2Mid, height=17, width=42, bd=12, font=('arial',9,'bold'))
        self.txtReceipt.grid(row=0, column=0)

        self.btn_arrow_left1 = Button(TopFrame2Left,text="CLICK_HERE=>",state=DISABLED)
        self.btn_arrow_left1.grid(row=0,column=0, padx=4,pady=20)

        self.btn_arrow_left2 = Button(TopFrame2Left,text="CLICK_HERE=>",state=DISABLED)
        self.btn_arrow_left2.grid(row=1,column=0, padx=4,pady=20)

        self.btn_arrow_left3 = Button(TopFrame2Left,text="CLICK_HERE=>",state=DISABLED)
        self.btn_arrow_left3.grid(row=2,column=0, padx=4,pady=20)

        self.btn_arrow_left4 = Button(TopFrame2Left,text="CLICK_HERE=>",state=DISABLED)
        self.btn_arrow_left4.grid(row=3,column=0, padx=4,pady=20)

#====================================================================================================================#

        self.btn_arrow_right1 = Button(TopFrame2Right,text="<=CLICK_HERE",state=DISABLED)
        self.btn_arrow_right1.grid(row=0,column=0, padx=4,pady=20)

        self.btn_arrow_right2 = Button(TopFrame2Right,text="<=CLICK_HERE",state=DISABLED)
        self.btn_arrow_right2.grid(row=1,column=0, padx=4,pady=20)

        self.btn_arrow_right3 = Button(TopFrame2Right,text="<=CLICK_HERE",state=DISABLED)
        self.btn_arrow_right3.grid(row=2,column=0, padx=4,pady=20)

        self.btn_arrow_right4 = Button(TopFrame2Right,text="<=CLICK_HERE",state=DISABLED)
        self.btn_arrow_right4.grid(row=3,column=0, padx=4,pady=20)

 # ==============================================PIN NUMBER BUTTON===========================================================#

        self.btn1 = Button(TopFrame1,text="1",height=3,width=8, command=insert1)
        self.btn1.grid(row=2,column=0, padx=4,pady=8)

        self.btn2 = Button(TopFrame1,text="2",height=3,width=8, command=insert2)
        self.btn2.grid(row=2,column=1, padx=4,pady=8)

        self.btn3= Button(TopFrame1,text="3",height=3,width=8, command=insert3)
        self.btn3.grid(row=2,column=2, padx=4,pady=8)

        self.btn_can = Button(TopFrame1,text="CANCEL",height=3,width=8, command=cancel)
        self.btn_can.grid(row=2,column=3, padx=4,pady=8)
#========================================================================================================================

        self.btn4 = Button(TopFrame1,text="4",height=3,width=8, command=insert4)
        self.btn4.grid(row=3,column=0, padx=4,pady=8)

        self.btn5 = Button(TopFrame1,text="5",height=3,width=8, command=insert5)
        self.btn5.grid(row=3,column=1, padx=4,pady=8)

        self.btn6 = Button(TopFrame1,text="6",height=3,width=8, command=insert6)
        self.btn6.grid(row=3,column=2, padx=4,pady=8)

        self.btn_clr = Button(TopFrame1,text="CLEAR",height=3,width=8, command=clear)
        self.btn_clr.grid(row=3,column=3, padx=4,pady=8)
#=======================================================================================================================

        self.btn7 = Button(TopFrame1,text="7",height=3,width=8, command=insert7)
        self.btn7.grid(row=4,column=0, padx=4,pady=8)

        self.btn8 = Button(TopFrame1,text="8",height=3,width=8, command=insert8)
        self.btn8.grid(row=4,column=1, padx=4,pady=8)

        self.btn9 = Button(TopFrame1,text="9",height=3,width=8, command=insert9)
        self.btn9.grid(row=4,column=2, padx=4,pady=8)

        self.btn0 = Button(TopFrame1,text="0",height=3,width=8, command=insert0)
        self.btn0.grid(row=5,column=1, padx=4,pady=8)

        self.btn_ent = Button(TopFrame1,text="ENTER",height=3,width=8,command=enter_Pin)
        self.btn_ent.grid(row=4,column=3, padx=4,pady=8)



        # self.btnArrowL1 = Button(TopFrame2Left,width=160, height=60, state=DISABLED,image=self.btn_arrow_left.grid(row=0,column=0,padx=2,pady=4))


if __name__=='__main__':
    root = Tk()
    application = atm(root)
    root.mainloop()
