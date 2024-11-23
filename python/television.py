class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, volume=MIN_VOLUME, channel=MIN_CHANNEL, status=False, muted=False):
        self.status = status
        self.muted = muted
        self.volume = volume
        self.channel = channel

    def power(self):
        self.status = not self.status


    def mute(self):
        self.muted = not self.muted


    def channel_up(self):
        if self.status:
            if self.channel == self.MAX_CHANNEL:
                self.channel = self.MIN_CHANNEL
            else:
                self.channel += 1


    def channel_down(self):
        if self.status:
            if self.channel == self.MIN_CHANNEL:
                self.channel = self.MAX_CHANNEL
            else:
                self.channel -= 1

    def volume_up(self):
        if self.status:
            if self.muted:
                self.muted = False

                if self.volume < self.MAX_VOLUME:
                    self.volume += 1

            elif self.volume < self.MAX_VOLUME:
                self.volume += 1


    def volume_down(self):
        if self.status:
            if self.muted:
                self.muted = False

                if self.volume == self.MIN_VOLUME:
                    self.volume == self.MIN_VOLUME
                else:
                    self.volume -= 1

            elif self.volume > self.MIN_VOLUME:
                self.volume -= 1


    def __str__(self):
        power_status = "True" if self.status else "False"
        return f"Power = {power_status}, Channel = {self.channel}, Volume = {self.volume}"

