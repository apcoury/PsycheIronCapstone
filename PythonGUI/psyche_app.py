import tkinter as tk
HEIGHT = 800
WIDTH = 800
FONT = ('Times New Roman', 12)
FRAMECOLOR = '#303030'
BUTTONCOLOR = '#181818'
FONTCOLOR = '#F0F0F0'

class psyche_app:
    
    def __init__(self,master):
        window = master
        canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
        canvas.pack()

        self.root = tk.Frame(master=window, bg = FRAMECOLOR)
        self.root.place( relx= .05, rely=.05,relheight = .90, relwidth = .90)

        self.left_side = tk.Frame(master = self.root, bg = FRAMECOLOR)
        self.left_side.place(relx = 0, rely = 0, relheight = 1, relwidth = .5)
        self.left_title = tk.Label(master= self.left_side, text ="Current Kernels", font = FONT, bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.left_title.place(relx=0,rely =0,relwidth = 1, relheight = .05)
        self.kernel_list = tk.Listbox(master=self.left_side)
        self.kernel_list.place(relx=.05,rely=.05,relwidth = 1, relheight =.65)
        self.kernel_menu = tk.Frame(master= self.left_side,bg = FRAMECOLOR)
        self.add_kernal = tk.Button(master=self.kernel_menu, text = "Import Kernel", font = FONT, bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.add_kernal.grid(row= 0, column =0, padx = 15, pady = 5)
        self.remove_kernal = tk.Button(master=self.kernel_menu, text = "Remove Kernel", font = FONT,bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.remove_kernal.grid(row= 0, column =1, padx = 15, pady = 5)
        self.refresh_kernal = tk.Button(master=self.kernel_menu, text = "Refresh", font = FONT,bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.refresh_kernal.grid(row= 0, column =3, padx = 15, pady = 5)
        self.kernel_menu.place(relx=0,rely=.7,relwidth = 1, relheight =.3)


        self.right_side = tk.Frame(master = self.root, bg = FRAMECOLOR)
        self.right_side.place(relx = .5, rely = 0, relheight = 1, relwidth = .5)
        self.right_title = tk.Label(master= self.right_side, text ="Meta Information", font = FONT, bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.right_title.place(relx=0,rely =0,relwidth = 1, relheight = .05)

        self.right_information = tk.Frame(master = self.right_side, bg = FRAMECOLOR)
        self.right_information.place(relx=0,rely=.05,relwidth = 1, relheight =.65)
        
        self.time_one_label = tk.Label(master= self.right_information, text = "Time One: ", bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.time_one_entry = tk.Entry(master= self.right_information)
        self.time_one_label.grid(row = 0 , column = 0, padx = 45, pady = 15)
        self.time_one_entry.grid(row = 0 , column = 1, padx = 45, pady = 15)

        self.time_two_label = tk.Label(master= self.right_information, text = "Time Two: ", bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.time_two_entry = tk.Entry(master= self.right_information)
        self.time_two_label.grid(row = 1 , column = 0, padx = 45, pady = 15)
        self.time_two_entry.grid(row = 1 , column = 1, padx = 45, pady = 15)

        self.time_step_label = tk.Label(master= self.right_information, text = "Time Step: ", bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.time_step_entry = tk.Entry(master= self.right_information)
        self.time_step_label.grid(row = 3 , column = 0, padx = 45, pady = 15)
        self.time_step_entry.grid(row = 3 , column = 1, padx = 45, pady = 15)
        
        self.reference_label = tk.Label(master= self.right_information, text = "Reference: ", bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.reference_entry = tk.Entry(master= self.right_information)
        self.reference_label.grid(row = 4 , column = 0, padx = 45, pady = 15)
        self.reference_entry.grid(row = 4 , column = 1, padx = 45, pady = 15)

        self.abberration_corr_label = tk.Label(master= self.right_information, text = "Abcorr: ", bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.abberration_corr_entry = tk.Entry(master= self.right_information)
        self.abberration_corr_label.grid(row = 5 , column = 0, padx = 45, pady = 15)
        self.abberration_corr_entry.grid(row = 5 , column = 1, padx = 45, pady = 15)

        self.target_label = tk.Label(master= self.right_information, text = "Target: ", bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.target_entry = tk.Entry(master= self.right_information)
        self.target_label.grid(row = 6 , column = 0, padx = 45, pady = 15)
        self.target_entry.grid(row = 6 , column = 1, padx = 45, pady = 15)

        self.observer_label = tk.Label(master= self.right_information, text = "Observer: ", bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.observer_entry = tk.Entry(master= self.right_information)
        self.observer_label.grid(row = 6 , column = 0, padx = 45, pady = 15)
        self.observer_entry.grid(row = 6 , column = 1, padx = 45, pady = 15)


        self.export_menu = tk.Frame(master= self.right_side, bg = FRAMECOLOR)
        self.export_kernal = tk.Button(master=self.export_menu, text = "Export Kernel", font = FONT,bg = BUTTONCOLOR, fg = FONTCOLOR)
        self.export_kernal.grid(row= 0, columnspan = 3, padx = 125, pady = 5)
        self.export_menu.place(relx=0,rely=.7,relwidth = 1, relheight =.3)

        window.mainloop()



if __name__ == "__main__":
    
    app = psyche_app(tk.Tk())
