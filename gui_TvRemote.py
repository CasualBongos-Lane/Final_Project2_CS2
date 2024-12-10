from tkinter import *
from Logic_TvRemote import *

class Gui:
    def __init__(self, window):

        self.window = window
        self.tv_logic = TvLogic()

        self.frame1 = Frame(self.window)
        self.volume_slider = Scale(self.frame1, from_=0, to=5, orient='horizontal', state='disabled', command=self.check_volume)
        self.label_volume = Label(self.frame1, text='Volume Slider', font=('Helvetica', 20))
        self.channel_slider = Scale(self.frame1, from_=1, to=3, orient='horizontal', state='disabled', command=self.change_channel)
        self.label_channel = Label(self.frame1, text='Channel Slider', font=('Helvetica', 20))
        self.label_volume.pack(side='left', padx=10)
        self.volume_slider.pack(side='left', padx=20)
        self.label_channel.pack(side='left', padx=20)
        self.channel_slider.pack(side='left', padx=10)
        self.frame1.pack()

        self.frame2 = Frame(self.window)
        self.channel_up = Button(self.frame2, text = 'Channel Up', font=('Helvetica', 20), state='disabled', command=self.channel_up)
        self.volume_up = Button(self.frame2, text='Volume Up', font=('Helvetica', 20),  state='disabled', command=self.volume_up)
        self.channel_up.pack(side='left', pady=35, padx=50)
        self.volume_up.pack(side='left', pady=35, padx=50)
        self.frame2.pack()

        self.frame3 = Frame(self.window)
        self.channel_down = Button(self.frame3, text='Channel Down', font=('Helvetica', 20), state='disabled', command=self.channel_down)
        self.volume_down = Button(self.frame3, text='Volume Down', font=('Helvetica', 20), state='disabled', command=self.volume_down)
        self.channel_down.pack(side='left',  pady=20, padx=50)
        self.volume_down.pack(side='left',  pady=20, padx=50)
        self.frame3.pack()

        self.frame4 = Frame(self.window)
        self.power = Button(self.frame4, text='Power', font=('Helvetica', 20), command=self.power)
        self.mute = Button(self.frame4, text='Mute', font=('Helvetica', 20),  state='disabled', command=self.mute)
        self.power.pack(side='left', pady=20)
        self.mute.pack(side='left', pady=20)
        self.frame4.pack()

        self.frame5 = Frame(self.window, width=480, height =300)
        self.photo = PhotoImage(file='BG.png')
        self.photo_label = Label(self.frame5, image= self.photo, width = 480, height =300, bg = 'black')
        self.photo_label.pack(side='bottom')
        self.frame5.pack()


    def power(self) -> None:
        status = self.tv_logic.power()
        if status:
            self.channel_slider.config(state='normal')
            self.volume_slider.config(state='normal')
            self.channel_up.config(state='normal')
            self.channel_down.config(state='normal')
            self.volume_up.config(state='normal')
            self.volume_down.config(state='normal')
            self.mute.config(state='normal')
            self.check_channel()
        else:
            self.channel_slider.config(state='disabled')
            self.volume_slider.config(state='disabled')
            self.channel_up.config(state='disabled')
            self.channel_down.config(state='disabled')
            self.volume_up.config(state='disabled')
            self.volume_down.config(state='disabled')
            self.mute.config(state='disabled')
            self.photo.config(file='BG.png')

    def mute(self) -> None:
        """
        Calls the Mute function in Logic
        """
        muted = self.tv_logic.mute()
        if muted:
            self.volume_slider.set(0)

    def channel_up(self) -> None:
        """
        Calls the channel_up function in Logic
        """
        new_channel = self.tv_logic.channel_up()
        self.channel_slider.set(new_channel)
        self.check_channel()

    def channel_down(self) -> None:
        """
        Calls the channel_down function in Logic
        """
        new_channel = self.tv_logic.channel_down()
        self.channel_slider.set(new_channel)
        self.check_channel()

    def volume_up(self) -> None:
        """
        Calls the volume_up function in Logic
        """
        slider_volume = self.volume_slider.get()
        new_volume = int(slider_volume) #Changes value to int
        new_volume = self.tv_logic.volume_up(new_volume)
        self.volume_slider.set(new_volume)

    def volume_down(self) -> None:
        """
        Calls the volume_down function in Logic
        """
        slider_volume = self.volume_slider.get()
        new_volume = int(slider_volume) #Changes value to int
        new_volume = self.tv_logic.volume_down(new_volume)
        self.volume_slider.set(new_volume)

    def change_channel(self, val) -> None:
        """
        Calls the Change channel function in Logic
        :param val: This parameter is needed to determine the correct value of the channel slider
        """
        new_channel = int(val) #Changes value to int
        self.tv_logic.change_channel(new_channel)
        self.check_channel()

    def check_channel(self) -> None:
        """
        This calls the check_channel function from logic which determines the correct image to display
        """
        image_file = self.tv_logic.check_channel()
        self.photo.config(file=image_file)

    def check_volume(self, val) -> None:
        """
        checks the value of slider_volume and setting the volume variable in Logic to it if the tv is unmuted
        """
        new_volume = int(val) #Changes value to int
        self.tv_logic.get_volume(new_volume)