from tkinter import *
import math

class LensUtil:

    def UpdateResult(self):
        tangle=self.angle_text.get()
        twd = self.wd_text.get()
        tFOV =  str(self.FOVfromAngleD(tangle,twd))
        self.result_text.set("\nCalculated Field of View: "+str(tFOV)+" [mm]")
     

    def FOVfromAngleD(self, _angFOV, _WD):
        hang = float(_angFOV)/2
        fWD = float(_WD)
        hFOV = abs(math.tan(math.radians(hang))*fWD)
        FOV = 2*hFOV
        return FOV

    def __init__(self,root):
        root.title("Basic Machine Vision Utils")
        root.geometry("500x400")
        root.maxsize(1000,800)
        label = Label(root, text="Basic lens calculator\n")
        label.pack()
        label2 = Label(root, text="Angular field of view [degrees]:")
        label2.pack()
        self.angle_text = StringVar()
        angleEntry = Entry(root, textvariable=self.angle_text)
        angleEntry.pack()
        label3 = Label(root, text="Working Distance [mm]:")
        label3.pack()
        self.wd_text = StringVar()
        wdEntry = Entry(root, textvariable=self.wd_text)
        wdEntry.pack()
        button = Button(root, text="Calculate\n", command=self.UpdateResult)
        button.pack()
        self.result_text=StringVar()
        rlabel = Label(root, textvariable=self.result_text)
        rlabel.pack()
       
root = Tk()
LensUtil(root)
root.mainloop()


