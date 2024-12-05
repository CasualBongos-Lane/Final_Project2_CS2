from tkinter import *

class Gui:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 5
    MIN_CHANNEL: int = 1
    MAX_CHANNEL: int = 3


    def __init__(self, window):
        self.__muted: bool = False
        self.__volume: int = Gui.MIN_VOLUME
        self.__channel: int = Gui.MIN_CHANNEL
        self.__status: bool = False

        self.window = window

        self.frame1 = Frame(self.window)
        self.volume_slider = Scale(self.frame1, from_=0, to=5, orient='horizontal', state='disabled')
        self.label_volume = Label(self.frame1, text='Volume Slider', font=('Helvetica', 20))
        self.channel_slider = Scale(self.frame1, from_=1, to=3, orient='horizontal', state='disabled', command=self.change_channel)
        self.label_channel = Label(self.frame1, text='Channel Slider', font=('Helvetica', 20))
        self.label_volume.pack(side='left', padx=10)
        self.volume_slider.pack(side='left', padx=20)
        self.label_channel.pack(side='left', padx=20)
        self.channel_slider.pack(side='left', padx=10)
        self.frame1.pack()

        self.frame2 = Frame(self.window)
        self.channel_up = Button(self.frame2, text = 'Channel Up', font=('Helvetica', 20), command=self.channel_up)
        self.volume_up = Button(self.frame2, text='Volume Up', font=('Helvetica', 20), command=self.volume_up)
        self.channel_up.pack(side='left', pady=35, padx=50)
        self.volume_up.pack(side='left', pady=35, padx=50)
        self.frame2.pack()

        self.frame3 = Frame(self.window)
        self.channel_down = Button(self.frame3, text='Channel Down', font=('Helvetica', 20), command=self.channel_down)
        self.volume_down = Button(self.frame3, text='Volume Down', font=('Helvetica', 20), command=self.volume_down)
        self.channel_down.pack(side='left',  pady=20, padx=50)
        self.volume_down.pack(side='left',  pady=20, padx=50)
        self.frame3.pack()

        self.frame4 = Frame(self.window)
        self.power = Button(self.frame4, text='Power', font=('Helvetica', 20), command=self.power)
        self.mute = Button(self.frame4, text='Mute', font=('Helvetica', 20), command=self.mute)
        self.power.pack(side='left', pady=20)
        self.mute.pack(side='left', pady=20)
        self.frame4.pack()

        self.frame5 = Frame(self.window, width=480, height =300)
        self.photo = PhotoImage(file='BG.png')
        self.photo_label = Label(self.frame5, image= self.photo, width = 480, height =300, bg = 'black')
        self.photo_label.pack(side='bottom')
        self.frame5.pack()


    def power(self) -> None:
        '''
        Determines if the TV is on or not,
        determines whether the functions work or not
        '''
        if self.__status == False:
            self.__status = True
            self.channel_slider.config(state='normal')
            self.volume_slider.config(state='normal')
            self.check_channel()
        elif self.__status == True:
            self.channel_slider.config(state='disabled')
            self.volume_slider.config(state='disabled')
            self.__status = False
            self.photo.config(file='BG.png')

    def mute(self) -> None:
        '''
        Determines whether the tv is muted or not
        '''
        if self.__status:
            if self.__muted == False:
                self.__muted = True
                self.volume_slider.set(0)
            else:
                self.__muted = False

    def channel_up(self) -> None:
        '''
        This function sets the channel up one and adjusts the chanel variable accordingly
        if the channel is at the maximum, it changes back to the minimum instead
        '''
        if self.__status:
            self.__channel = self.channel_slider.get()
            if self.__channel < Gui.MAX_CHANNEL:
                self.__channel += 1
                self.check_channel()
                self.channel_slider.set(self.__channel)
            else:
                self.__channel = Gui.MIN_CHANNEL
                self.check_channel()
                self.channel_slider.set(self.__channel)

    def channel_down(self) -> None:
        '''
        This function sets the channel down one and adjusts the chanel variable accordingly
        if the channel is at the minimum, it changes back to the maximum instead
        '''
        if self.__status:
            self.__channel = self.channel_slider.get()
            if self.__channel > Gui.MIN_CHANNEL:
                self.__channel -= 1
                self.check_channel()
                self.channel_slider.set(self.__channel)
            else:
                self.__channel = Gui.MAX_CHANNEL
                self.check_channel()
                self.channel_slider.set(self.__channel)

    def volume_up(self) -> None:
        '''
        Changes the volume up one and unmutes the tv.
        If the volume is at max, it stays at max
        '''
        if self.__status:
            if self.__muted == False:
                self.__volume = self.volume_slider.get()
            if self.__volume < Gui.MAX_VOLUME:
                self.__muted = False
                self.__volume += 1
                self.volume_slider.set(self.__volume)
            else:
                self.__volume = Gui.MAX_VOLUME
                self.volume_slider.set(self.__volume)

    def volume_down(self) -> None:
        '''
        Changes the volume down one and unmutes the tv.
        If the volume is at the minimum, it stays at the minimum
        '''
        if self.__status:
            if self.__muted == False:
                self.__volume = self.volume_slider.get()
            if self.__volume > Gui.MIN_VOLUME:
                self.__muted = False
                self.__volume -= 1
                self.volume_slider.set(self.__volume)
            else:
                self.__volume = Gui.MIN_VOLUME
                self.volume_slider.set(self.__volume)

    def change_channel(self, val):
        if self.__status:
            self.__channel = int(val)
            self.check_channel()

    def check_channel(self):
        if self.__channel == 1:
            self.photo.config(file='CNN.png')
        elif self.__channel == 2:
            self.photo.config(file='Disney.png')
        elif self.__channel == 3:
            self.photo.config(file='ESPN.png')
