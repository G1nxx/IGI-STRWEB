from print_color import print as pc
import pandas as pd


class Executer:
    def __init__(self):
        self.series = pd.Series()
        self.music = pd.read_csv("music_dataset.csv")

    def print_enterence(self):
        pc()
        pc(r"__  __               ______      __                     __   _____ __              __                 _____                  ", color="green")
        pc(r"\ \/ /___  __  __   / ____/___  / /____  ________  ____/ /  / ___// /_  ____ _____/ /___ _      __   /__  / ____  ____  ___  ", color="green")
        pc(r" \  / __ \/ / / /  / __/ / __ \/ __/ _ \/ ___/ _ \/ __  /   \__ \/ __ \/ __ `/ __  / __ \ | /| / /     / / / __ \/ __ \/ _ \ ", color="green")
        pc(r" / / /_/ / /_/ /  / /___/ / / / /_/  __/ /  /  __/ /_/ /   ___/ / / / / /_/ / /_/ / /_/ / |/ |/ /     / /_/ /_/ / / / /  __/ ", color="green")
        pc(r"/_/\____/\__,_/  /_____/_/ /_/\__/\___/_/   \___/\__,_/   /____/_/ /_/\__,_/\__,_/\____/|__/|__/     /____|____/_/ /_/\___/  ", color="green")
        pc()

    def print(self):
        print(self.music)

    def series_demo(self):
        data = [pd.Series([420, 380, 390])]
        data.append(pd.Series([780, 31230, 3120]))
        data.append(pd.Series([983, 50, 340]))

        df = pd.DataFrame(data, index=["data1","data2","data3"])
        print(df)


if __name__ == '__main__':
    raise Exception("You can`t use this file as executable one")