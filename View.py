from tkinter import *
import tkinter.font as tkfont
from PIL import Image, ImageTk

class View(Tk):

    def __init__(self, controller, model):
        super().__init__()
        self.controller = controller
        self.model = model
        self.userinput = StringVar()

        self.big_font_style = tkfont.Font(family='Courier', size=18, weight='bold')
        self.default_font_style_bold = tkfont.Font(family='Verdana', size=10, weight='bold')
        self.default_font_style = tkfont.Font(family='Verdana', size=10)

        # Window properties
        self.geometry('515x200')
        self.title('Hangman Sikka')
        self.center(self)

        # Create frames
        self.frames_top, self.frames_bottom, self.frames_img = self.create_three_frames()

        self.image = ImageTk.PhotoImage(Image.open(self.model.image_files[len(self.model.image_files)-1]))
        self.label_image = None

        # Create all Buttons, Labels and Entry
        self.btn_new_game, self.btn_cancel, self.btn_send = self.create_all_buttons()
        self.lbl_error, self.lbl_time, self.lbl_result = self.create_all_labels()
        self.ltr_input = self.create_input_entry()


    def main(self):
        self.mainloop()

    @staticmethod
    def center(win):
        """
        https://stackoverflow.com/questions/3352918
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    def create_three_frames(self): #  create frames 4 hangman
        frames_top = Frame(self, bg='#7078f8', height=50) # blue
        frames_bottom = Frame(self, bg='#5729c8', height=50) #

        frames_top.pack(fill=BOTH)
        frames_bottom.pack(expand=True, fill=BOTH)

        #  Hangman image frame
        frames_img = Frame(frames_top, bg='white', width=130, height=130) #  image frame itself
        frames_img.grid(row=0, column=3, rowspan=4, padx=5, pady=5)

        return frames_top, frames_bottom, frames_img #  method returns 3 objects

    def create_all_buttons(self):
        #  New game button
        btn_new_game = Button(self.frames_top, text='New game', relief=FLAT, font=self.default_font_style)
        # Leaderboard butoon, create & place
        Button(self.frames_top, text='Leaderboard', relief=FLAT, font=self.default_font_style).grid(
            row=0, column=1, padx=5, pady=2, sticky=EW)
        #  Cancel & send buttons
        btn_cancel = Button(self.frames_top, text='Cancel', relief=FLAT, font=self.default_font_style, state='disabled')
        btn_send = Button(self.frames_top, text='Send', relief=FLAT, font=self.default_font_style, state='disabled')
        #  Place three buttons on frame_top
        btn_new_game.grid(row=0, column=0, padx=5, pady=2, sticky=EW)
        btn_cancel.grid(row=0, column=2, padx=5, pady=2, sticky=EW)
        btn_send.grid(row=1, column=2, padx=5, pady=2, sticky=EW)

        return btn_new_game, btn_cancel, btn_send

    def create_all_labels(self):
        #  Create Input letter label
        Label(self.frames_top, text='Input letter', font=self.default_font_style_bold).grid(row=1, column=0, padx=5,
                                                                                               pady=2)
        lbl_error = Label(self.frames_top, text='Wrong 0 letter(s)', anchor='w', font=self.default_font_style_bold)
        lbl_time = Label(self.frames_top, text='0:00:00', font=self.default_font_style)
        lbl_result = Label(self.frames_bottom, text='Let\'s play'.upper(), font=self.big_font_style, bg='#5729c8')

        self.label_image = Label(self.frames_img, image=self.image)
        self.label_image.pack()

        #  Labels positioning
        lbl_error.grid(row=2, column=0, columnspan=3, sticky=EW, padx=5, pady=2)
        lbl_time.grid(row=3, column=0, columnspan=3, sticky=EW, padx=5, pady=2)
        lbl_result.pack(padx=5, pady=2)

        return lbl_error, lbl_time, lbl_result

    def create_input_entry(self):
        ltr_input = Entry(self.frames_top, textvariable=self.userinput, justify='center', font=self.default_font_style)
        ltr_input['state'] = 'disabled'
        ltr_input.grid(row=1, column=1, padx=5, pady=2)

        return ltr_input
