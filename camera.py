from tkinter import *
import math

class CameraUtil:

    def UpdateResult(self):
       
        tBlur =  str(self.BlurCalc(self.vel_text.get(),self.fov_text.get(),self.exp_text.get(), self.pix_text.get()))
        self.result_text.set("\nCalculated Blur: "+str(tBlur)+" [px]")
     

    def BlurCalc(self, _Velocity, _FOV, _ExpTime, _nofPixels):
        Blur = float(_Velocity) * float(_ExpTime)*0.001 * int(_nofPixels)
        Blur /= float(_FOV)
        return Blur


    def __init__(self,root):
        root.title("Basic Machine Vision Utils")
        root.geometry("500x400")
        root.maxsize(1000,800)
        label = Label(root, text="Basic blur calculator\n")
        label.pack()
        label1 = Label(root, text="Field of view in the direction of motion [mm]:")
        label1.pack()
        self.fov_text = StringVar()
        fovEntry = Entry(root, textvariable=self.fov_text)
        fovEntry.pack()
        label2 = Label(root, text="Numper of pixels in FOV [px]:")
        label2.pack()
        self.pix_text = StringVar()
        pixEntry = Entry(root, textvariable=self.pix_text)
        pixEntry.pack()
        label3 = Label(root, text="Velocity [mm/s]:")
        label3.pack()
        self.vel_text = StringVar()
        velEntry = Entry(root, textvariable=self.vel_text)
        velEntry.pack()
        label4 = Label(root, text="Exposure Time [ms]:")
        label4.pack()
        self.exp_text = StringVar()
        expEntry = Entry(root, textvariable=self.exp_text)
        expEntry.pack()
        
        button = Button(root, text="Calculate\n", command=self.UpdateResult)
        button.pack()
        self.result_text=StringVar()
        rlabel = Label(root, textvariable=self.result_text)
        rlabel.pack()
       
root = Tk()
CameraUtil(root)
root.mainloop()


