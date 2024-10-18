from tkinter import *

# All variables

width = 600
height = 600

canvas_width = width-25
canvas_height = height-25

A_rows = 0
B_rows = 0
C_rows = 0

recognize = ""

class App():
    def __init__(self):
        self.w = Tk()
        
        self.w.title("Loto")
        self.w.configure(bg="black")
        self.w.geometry(f"{width}x{height}")
        
        self.title = Label(self.w, text="Play the loto and win absolutely nothing !!!", background="white")
        self.title.pack()
        
        self.canvas = Canvas(self.w, background="azure2", width=width-25, height=height-100)
        self.canvas.pack(expand=YES)
        
        self.canvas.create_rectangle(canvas_width-25, canvas_height/2+100, canvas_width+(25-canvas_width), canvas_height/2-100, fill="gold")
        
        self.canvas.create_rectangle(canvas_width-25, canvas_height/2+100, canvas_width+(25-canvas_width)*(2/3), canvas_height/2-100, fill="gold")
        self.canvas.create_rectangle(canvas_width-25, canvas_height/2+100, canvas_width+(25-canvas_width)*(1/3), canvas_height/2-100, fill="gold")

        # Each emplacment to draw
        def Emplacment_3():
            
            global C_rows
            
            self.canvas.create_rectangle(canvas_width-25-10, canvas_height/2+100-10, canvas_width+(25-canvas_width)*(1/3)+10, canvas_height/2-100+10, fill="orange")
            
            C_rows+=1
            
        def Emplacment_2():
            
            global B_rows
            
            self.canvas.create_rectangle(canvas_width+(25-canvas_width)*(1/3)-10, canvas_height/2+100-10, canvas_width+(25-canvas_width)*(2/3)+10, canvas_height/2-100+10, fill="blue")
            
            B_rows+=1
            
        def Emplacment_1():
            
            global A_rows
            
            self.canvas.create_rectangle(canvas_width+(25-canvas_width)*(3/3)+10, canvas_height/2+100-10, canvas_width+(25-canvas_width)*(2/3)-10, canvas_height/2-100+10, fill="red")
            
            A_rows+=1
            
        def Play():
            global A_rows, B_rows, C_rows
            
            for i in range(3):
                pass
            
        self.button = Button(self.w, text="Play")
        self.button.pack(anchor="s")
        
        self.w.mainloop()
        
if __name__ == '__main__':
    App()
