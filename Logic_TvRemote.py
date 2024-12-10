from gui_TvRemote import *

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

    def power(self):
        """
        Toggles the TV power on/off and enables/disables controls.
        """
        self.__status = not self.__status
        return self.__status

    def mute(self):
        """
        Toggles mute status.
        """
        if self.__status:
            self.__muted = not self.__muted
            return self.__muted

    def channel_up(self):
        """
        Changes the channel up, looping from max back to min if necessary.
        """
        if self.__status:
            if self.__channel < TvLogic.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = TvLogic.MIN_CHANNEL
            return self.__channel

    def channel_down(self):
        """
        Changes the channel down, looping from min back to max if necessary.
        """
        if self.__status:
            if self.__channel > TvLogic.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = TvLogic.MAX_CHANNEL
            return self.__channel

    def volume_up(self, slider_volume):
        """
        Increases the volume, respecting the max volume limit.
        """
        if self.__status:
            if self.__muted and slider_volume > 0:
                self.__muted = False
            if self.__muted == False:
                self.__volume = slider_volume
            if self.__volume < TvLogic.MAX_VOLUME:
                self.__muted = False
                self.__volume += 1
            else:
                self.__volume = TvLogic.MAX_VOLUME

            return self.__volume

    def volume_down(self, slider_volume):
        """
        Decreases the volume, respecting the min volume limit.
        """
        if self.__status:
            if self.__muted and slider_volume > 0:
                self.__muted = False
            if self.__muted == False:
                self.__volume = slider_volume
            if self.__volume > TvLogic.MIN_VOLUME:
                self.__muted = False
                self.__volume -= 1
            else:
                self.__volume = TvLogic.MIN_VOLUME

            return self.__volume

    def change_channel(self, channel):
        """
        Changes the channel directly based on the slider input.
        """
        if self.__status:
            if TvLogic.MIN_CHANNEL <= channel <= TvLogic.MAX_CHANNEL:
                self.__channel = channel
            return self.__channel

    def check_channel(self):
        """
        Returns the appropriate image filename based on the current channel.
        """
        if self.__channel == 1:
            return 'CNN.png'
        elif self.__channel == 2:
            return 'Disney.png'
        elif self.__channel == 3:
            return 'ESPN.png'

    def get_volume(self, slider_volume):
        """Returns the current volume."""
        if self.__muted == False:
            self.__volume = slider_volume
        return self.__volume
