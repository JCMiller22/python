import pytest
from television import Television  # Import the Television class from the television module


class TestTelevision:
    def setup_method(self):
        """Reset the Television object before each test."""
        self.tv = Television()

    def test_power_on(self):
        """Test the power method to turn the TV ON."""
        self.tv.power()  # Turn the TV on
        assert self.tv.status == True

    def test_power_off(self):
        """Test the power method to turn the TV OFF."""
        self.tv.power()  # Turn the TV on
        self.tv.power()  # Turn the TV off
        assert self.tv.status == False

    def test_mute_on(self):
        """Test the mute method to mute the TV."""
        self.tv.power()  # Ensure the TV is on
        self.tv.mute()  # Mute the TV
        assert self.tv.muted == True

    def test_mute_off(self):
        """Test the mute method to unmute the TV."""
        self.tv.power()  # Ensure the TV is on
        self.tv.mute()  # Mute the TV
        self.tv.mute()  # Unmute the TV
        assert self.tv.muted == False

    def test_channel_up(self):
        """Test the channel_up method to increase the channel."""
        self.tv.power()  # Ensure the TV is on
        initial_channel = self.tv.channel
        self.tv.channel_up()  # Channel up
        assert self.tv.channel == initial_channel + 1

    def test_channel_down(self):
        """Test the channel_down method to decrease the channel."""
        self.tv.power()  # Ensure the TV is on
        self.tv.channel_up()  # Increase channel first
        initial_channel = self.tv.channel
        self.tv.channel_down()  # Channel down
        assert self.tv.channel == initial_channel - 1

    def test_volume_up(self):
        """Test the volume_up method to increase the volume."""
        self.tv.power()  # Ensure the TV is on
        initial_volume = self.tv.volume
        self.tv.volume_up()  # Volume up
        assert self.tv.volume == initial_volume + 1

    def test_volume_down(self):
        """Test the volume_down method to decrease the volume."""
        self.tv.power()  # Ensure the TV is on
        self.tv.volume_up()  # Increase volume first
        initial_volume = self.tv.volume
        self.tv.volume_down()  # Volume down
        assert self.tv.volume == initial_volume - 1
