class TvLogic:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 5
    MIN_CHANNEL: int = 1
    MAX_CHANNEL: int = 3

    def __init__(self):
        self.__muted: bool = False
        self.__volume: int = TvLogic.MIN_VOLUME
        self.__channel: int = TvLogic.MIN_CHANNEL
        self.__status: bool = False

    def power(self) -> bool:
        """
        This Function determines whether the TV Power is on or not
        :return: Returns a bool True/False depending if the TV is On or Not
        """
        self.__status = not self.__status
        return self.__status

    def mute(self) -> bool:
        """
        This Function Determines whether the TV is muted and affects the Volume
        :return: Returns the Bool True/False if Muted or UnMuted
        """
        if self.__status:
            self.__muted = not self.__muted
            return self.__muted

    def channel_up(self) -> int:
        """
        This function Determines the correct channel to display
        :return: The Channel Value is returned thus allowing the check_channel function to be run determining the correct channel to display
        """
        #If the channel is on max and the button is clicked this respects the boundary and the channel is moved back down to the min
        if self.__status:
            if self.__channel < TvLogic.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = TvLogic.MIN_CHANNEL
            return self.__channel

    def channel_down(self) -> int:
        """
        This function Determines the correct channel to display when channel down is pressed
        :return: The Channel Value is returned thus allowing the check_channel function to be run determining the correct channel
        """
        #If the channel is on minimum and the button is clicked this respects the boundary and changes it to the max
        if self.__status:
            if self.__channel > TvLogic.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = TvLogic.MAX_CHANNEL
            return self.__channel

    def volume_up(self, slider_volume) -> int:
        """
        This function determines the correct volume. If the TV is muted it unmutes the TV and resets the volume back to where it was then increases it by one.
        This funciton also determines whether the slider has been moved after the TV has been muted.
        If the slider has moved, it unmutes the tv and sets the volume depending on the slider
        :param slider_volume: This value is needed in order to determine whether the volume slider has been moved or not.
        :return: This returns the value of volume
        """
        #Changes the volume based on if the tv is muted or not. Also depends on the sliders value, If the vol is at the max, it does not reset to 0 and stays at the max.
        if self.__status:
            if self.__muted and slider_volume > 0:
                self.__muted = False
            if not self.__muted:
                self.__volume = slider_volume
            if self.__volume < TvLogic.MAX_VOLUME:
                self.__muted = False
                self.__volume += 1
            else:
                self.__volume = TvLogic.MAX_VOLUME

            return self.__volume

    def volume_down(self, slider_volume) -> int:
        """
        This function determines the correct volume. If the TV is muted it unmutes the TV and resets the volume back to where it was then decreases it by one.
        This funciton also determines whether the slider has been moved after the TV has been muted.
        If the slider has moved, it unmutes the tv and sets the volume depending on the slider
        :param slider_volume: This value is needed in order to determine whether the volume slider has been moved or not.
        :return: Returns the value of Volume
        """
        #Changes the volume based on if the tv is muted or not. Also depends on the sliders value, If the vol is at the min, it does not reset to 5 and stays at the min
        if self.__status:
            if self.__muted and slider_volume > 0:
                self.__muted = False
            if not self.__muted:
                self.__volume = slider_volume
            if self.__volume > TvLogic.MIN_VOLUME:
                self.__muted = False
                self.__volume -= 1
            else:
                self.__volume = TvLogic.MIN_VOLUME

            return self.__volume

    def change_channel(self, channel) -> int:
        """
        This function is specifically used for the Channel Slider and determines the channel image depending on the value of the channel slider
        :param channel: This parameter contains the value of the channel slider
        :return: This returns channel value which has been set to the value of the channel slider. Thus allowing the channel to change using the slider
        """
        #Used to determine the correct channel based off the slider value
        if self.__status:
            if TvLogic.MIN_CHANNEL <= channel <= TvLogic.MAX_CHANNEL:
                self.__channel = channel
            return self.__channel

    def check_channel(self) -> str:
        """
        This Function Sets the correct image for each channel
        :return: Returns the image file name for each channel
        """
        #Sets the correct image for each channel for either the buttons or slider
        if self.__channel == 1:
            return 'CNN.png'
        elif self.__channel == 2:
            return 'Disney.png'
        elif self.__channel == 3:
            return 'ESPN.png'

    def get_volume(self, slider_volume) -> int:
        """
        This Helps to correct the self.__volume based off the value of slider_volume
        :param slider_volume: Used to set the volume value to the volume slider value
        :return: This returns the correct volume based off the slider
        """
        #Helps determine volume value based off of the sliders value
        if not self.__muted:
            self.__volume = slider_volume
        return self.__volume
