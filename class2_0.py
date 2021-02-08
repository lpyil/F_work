
class Remote:
    def __init__(self, channel_list, current_channel, volume):
        self.channel_list = channel_list
        self.current_channel = current_channel
        self.volume = volume

    channel_list = {1: ["atv", "something about bullshit"], 2: ["Galaxy", "6.dimension"],
                    3: ["das", "sad"], 4: ["fucking", "cursed"]}

    current_channel = 1

    volume = 51

    @classmethod
    def next_channel(cls):
        if Remote.current_channel < len(Remote.channel_list):
            Remote.current_channel = Remote.current_channel + 1
        else:
            Remote.current_channel = 1

    @classmethod
    def change_channel(cls, i):
        if i <= len(Remote.channel_list):
            Remote.current_channel = i
        else:
            print("have no this channel")

    @classmethod
    def change_volume(cls, i):
        Remote.volume = i

    @classmethod
    def show_channel(cls):
        print(Remote.channel_list[Remote.current_channel])


Remote.show_channel()
Remote.change_channel(3)
Remote.show_channel()
Remote.next_channel()
Remote.show_channel()
Remote.next_channel()
Remote.show_channel()