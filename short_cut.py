# Shortcut maker

#========== All imports ==========
from ctypes import WinDLL
from webbrowser import open
from os import path
from subprocess import call, Popen
from time import sleep
from random import randint
from sys import exit

#========== Main variables ==========
script_path = path.abspath(__file__)	# full path of current script
dir_path = path.dirname(script_path)	# full path of the directory of this script
dll_path = dir_path+'\\VirtualDesktopAccessor.dll'	# full path of the .dll file for this script

desktop_accessor = WinDLL(dll_path)
desktop_count = desktop_accessor.GetDesktopCount()	- 1	# amount of all currently opened virtual desktops minus 1

planning_music_links = [
	"https://www.youtube.com/watch?v=5qap5aO4i9A&ab_channel=ChilledCow",
	"https://www.youtube.com/watch?v=5yx6BWlEVcY&ab_channel=ChillhopMusic"
]

coding_music_links = [
	"https://www.youtube.com/watch?v=b-EF93ebtyM&ab_channel=Mr_MoMoMusic",
	"https://www.youtube.com/watch?v=esX7SFtEjHg&ab_channel=CodePioneers",
	# playlists
	"https://www.youtube.com/watch?v=x1R2yQtErPc&ab_channel=Mr_MoMoMusic", 
	"https://www.youtube.com/watch?v=OntcAJYG29A&ab_channel=Mr_MoMoMusic"
]

cyberpunk_music_link = "https://www.youtube.com/watch?v=zLAfTaCFXk4"

notion_link = "https://www.notion.so/"
anyDo_link = "https://desktop.any.do/agenda"
calendar_link = "https://calendar.google.com/calendar/u/0/r"
atutor_link = "https://dl.tntu.edu.ua/login.php"
youtube_watchlist_link = "https://www.youtube.com/playlist?list=WL"

university_dir_path = r"D:\Education\University"
anyDo_path = r"C:\Users\oleg\AppData\Local\Programs\@anydoelectron-app\Any.do.exe"
wpsOffice_path = r"C:\Users\oleg\AppData\Local\Kingsoft\WPS Office\ksolaunch.exe"

delay = 0.4

#========== Main functions ==========

# code - defines which music link list will be played (0 - planning, 1 - coding, 2 - cyberpunk)
def open_music(code = 0):
	if code == 0:
		open(planning_music_links[randint(0, len(planning_music_links))-1], new=0, autoraise=True)
		sleep(delay)
	elif code == 1:
		open(coding_music_links[randint(0, len(planning_music_links))-1], new=0, autoraise=True)
		sleep(delay)
	else:
		open(cyberpunk_music_link, new=0, autoraise=True)
		sleep(delay)

def open_notion():
	open(notion_link, new=0, autoraise=True)
	sleep(delay)

def open_anyDo():
	# call([anyDo_path]) #opens desktop app 
	open(anyDo_link, new=0, autoraise=True)
	sleep(delay)

def open_wpsOffice():
	call([wpsOffice_path])
	sleep(delay*8)

def open_calendar():
	open(calendar_link, new=0, autoraise=True)
	sleep(delay)

def open_youtube_watchlist():
	open(youtube_watchlist_link, new=0, autoraise=True)
	sleep(delay)

def open_atutor():
	open(atutor_link, new=0, autoraise=True)
	sleep(delay)

def open_univ_dir():
	Popen(r'explorer {}'.format(university_dir_path))
	sleep(delay*5)


#========== Main presets ==========

# Planning preset
def planning_preset():
	desktop_accessor.GoToDesktopNumber(0)
	if desktop_count == 0:
		open_music(0)
		open_anyDo()
		open_notion()
	elif desktop_count == 1:
		open_music(0)
		desktop_accessor.GoToDesktopNumber(1)
		open_anyDo()
		open_notion()
	else:
		open_music(0)
		desktop_accessor.GoToDesktopNumber(1)
		open_anyDo()
		desktop_accessor.GoToDesktopNumber(2)
		open_notion()

	desktop_accessor.GoToDesktopNumber(0)


# Coding preset
def coding_preset():
	desktop_accessor.GoToDesktopNumber(0)
	if desktop_count == 0:
		open_music(1)
		open_anyDo()
	else:
		open_music(1)
		desktop_accessor.GoToDesktopNumber(1)
		open_anyDo()

	desktop_accessor.GoToDesktopNumber(0)


# University preset
def university_preset():
	desktop_accessor.GoToDesktopNumber(0)
	if desktop_count == 0:
		open_music(0)
		open_anyDo()
		open_univ_dir()
		open_wpsOffice()
	elif desktop_count == 1:
		open_music(0)
		open_calendar()
		open_notion()
		open_anyDo()
		open_atutor()
		desktop_accessor.GoToDesktopNumber(1)
		open_univ_dir()
		open_wpsOffice()
	else:
		open_music(0)
		open_anyDo()
		open_notion()
		desktop_accessor.GoToDesktopNumber(1)
		open_atutor()
		open_calendar()
		desktop_accessor.GoToDesktopNumber(2)
		open_univ_dir()
		open_wpsOffice()
		
	desktop_accessor.GoToDesktopNumber(0)


# Free time preset
def freeTime_preset():
	desktop_accessor.GoToDesktopNumber(0)
	open_youtube_watchlist()


# Main function

def main():
	pass


if __name__ == "__main__":
	main()
	exit()