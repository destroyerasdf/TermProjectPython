import time
import winsound

class Library(object):

    def __init__(self, name):
        print("Welcome to music library!")
        self.notset = True
        self.tone = 3
        self.ringtone = 0

    def state(self):
        self.notset = not self.notset
        if self.notset == True:
            print("You have unset the ring tone!")
        else:
            print("You have set the ring tone!")

    def play_ringtone(self, ringTone):
        self.ringtone = ringTone
        if self.ringtone == 0:
            print("There is no ring tone set. Change ring tone to set it.")
        else:
            if self.ringtone == 1:
                print("Playing Song1")
                winsound.Beep(2500, 300)
                winsound.Beep(2000, 300)
                winsound.Beep(2500, 300)
                winsound.Beep(2000, 300)
                winsound.Beep(2500, 300)
                winsound.Beep(1500, 300)
            elif self.ringtone == 2:
                print("Playing Song2")
                winsound.Beep(2000, 300)
                winsound.Beep(2500, 300)
                winsound.Beep(3000, 300)
                winsound.Beep(2500, 300)
                winsound.Beep(3600, 300)
                winsound.Beep(2500, 300)
                winsound.Beep(2000, 400)
            elif self.ringtone == 3:
                print("Playing Song3")
                winsound.Beep(1000, 200)
                winsound.Beep(1500, 200)
                winsound.Beep(2000, 200)
                winsound.Beep(2000, 200)
                winsound.Beep(2000, 200)
                winsound.Beep(1500, 200)
                winsound.Beep(1000, 200)
            else:
                print("Broken!")


    def change_ringtone(self):
        print("Current ringtone: ", self.ringtone)

        while songChoice != 0:
            print("\t\tRingtones\n0 Back\n1 Song1\n2 Song2\n3 Song3")
            songChoice = input("Choice: ")
            if songChoice == "0":
                main()
            elif songChoice == "1":
                self.ringtone = 1
                print("Set to Song1!",self.ringtone)
                main()
            elif songChoice == "2":
                self.ringtone = 2
                print("Set to Song2!",self.ringtone)
                main()
            elif songChoice == "3":
                self.ringtone = 3
                print("Set to Song3!",self.ringtone)
                main()
        return self.ringtone


def main():
    rl = Library("Ringtones")
    choice = None
    while choice != 0:
        print("\t\tMenu\n0 Exit\n1 Play Ringtone")

        choice = input("Choice: ")
        if choice == "0":
            print("Goodbye!")
            exit()
        elif choice == "1":
            ringTone = rl.change_ringtone()
            rl.play_ringtone(ringTone)
        else:
            print("That is not a valid choice.")


main()
