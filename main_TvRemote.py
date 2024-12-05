from gui_TvRemote import *

def main():
    window = Tk()
    window.title('TV Remote')
    window.geometry('600x600')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()