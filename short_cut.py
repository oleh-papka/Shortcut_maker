# Shortcut maker

#========== All imports ==========
from ctypes import WinDLL
import webbrowser
from os import path
from subprocess import call, Popen
from time import sleep
from random import randint
import eel, json

#========== Main variables ==========
script_path = path.abspath(__file__)	# full path of current script
dir_path = path.dirname(script_path)	# full path of the directory of this script
dll_path = dir_path+'\\VirtualDesktopAccessor.dll'	# full path of the .dll file for this script

desktop_accessor = WinDLL(dll_path)
desktop_count = desktop_accessor.GetDesktopCount()	- 1	# amount of all currently opened virtual desktops minus 1

lofi_music_links = [
	"https://www.youtube.com/watch?v=5qap5aO4i9A&ab_channel=ChilledCow",
	"https://www.youtube.com/watch?v=5yx6BWlEVcY&ab_channel=ChillhopMusic"
	]

coding_music_links = [
	"https://www.youtube.com/watch?v=b-EF93ebtyM&ab_channel=Mr_MoMoMusic",
	"https://www.youtube.com/watch?v=esX7SFtEjHg&ab_channel=CodePioneers",
	"https://www.youtube.com/watch?v=x1R2yQtErPc&ab_channel=Mr_MoMoMusic", 
	"https://www.youtube.com/watch?v=OntcAJYG29A&ab_channel=Mr_MoMoMusic"
	]

rock_music_links = [
	"https://www.youtube.com/watch?v=8BVPSCOz364"
	]

notion_link = "https://www.notion.so/"
anyDo_link = "https://desktop.any.do/agenda"
calendar_link = "https://calendar.google.com/calendar/u/0/r"
atutor_link = "https://dl.tntu.edu.ua/login.php"

university_dir_path = r"D:\Education\University"
anyDo_path = r"C:\Users\oleg\AppData\Local\Programs\@anydoelectron-app\Any.do.exe"
wpsOffice_path = r"C:\Users\oleg\AppData\Local\Kingsoft\WPS Office\ksolaunch.exe"

delay = 0.4

#========== Main functions ==========

# code - defines which music link list will be played (0 - lofi, 1 - coding, 2 - rock)
def open_music(code = 0):
	if code == 0:
		webbrowser.open(lofi_music_links[0 if len(lofi_music_links) == 1 else randint(0, len(lofi_music_links)-1)], new=0, autoraise=True)
		sleep(delay)
	elif code == 1:
		webbrowser.open(coding_music_links[0 if len(coding_music_links) == 1 else randint(0, len(coding_music_links)-1)], new=0, autoraise=True)
		sleep(delay)
	else:
		webbrowser.open(rock_music_links[0 if len(rock_music_links) == 1 else randint(0, len(rock_music_links)-1)], new=0, autoraise=True)
		sleep(delay)

def open_notion():
	webbrowser.open(notion_link, new=0, autoraise=True)
	sleep(delay)

def open_anyDo():
	# call([anyDo_path]) #opens desktop app 
	webbrowser.open(anyDo_link, new=0, autoraise=True)
	sleep(delay)

def open_wpsOffice():
	call([wpsOffice_path])
	sleep(delay*9)

def open_calendar():
	webbrowser.open(calendar_link, new=0, autoraise=True)
	sleep(delay)

def open_atutor():
	webbrowser.open(atutor_link, new=0, autoraise=True)
	sleep(delay)

def open_univ_dir():
	Popen(r'explorer {}'.format(university_dir_path))
	sleep(delay*5)


def get_json_data():
	with open("GUI\\js\\music_links.json", "r") as json_file:
		output_data = json.load(json_file)

	global rock_music_links, lofi_music_links, coding_music_links

	rock_music_links += output_data["rock_music"]
	lofi_music_links += output_data["lofi_music"]
	coding_music_links += output_data["code_music"]
	

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


#========== Eel part ==========

@eel.expose
def get_data(rock_links, lofi_links, code_links):
	rock_links = rock_links.split("\n")
	lofi_links = lofi_links.split("\n")
	code_links = code_links.split("\n")

	global rock_music_links, lofi_music_links, coding_music_links

	rock_music_links += rock_links
	lofi_music_links += lofi_links
	coding_music_links += code_links
	
	data = {
		"rock_music": rock_links,
		"lofi_music": lofi_links,
		"code_music": code_links
	}

	with open("GUI\\js\\music_links.json", "w") as json_file:
		json.dump(data, json_file)


@eel.expose
def put_default():
	with open("GUI\\js\\music_links.json", "r") as json_file:
		output_data = json.load(json_file)

	return output_data


@eel.expose
def preset_1():
	planning_preset()

@eel.expose
def preset_2():
	coding_preset()

@eel.expose
def preset_3():
	university_preset()

@eel.expose
def open_rock_music():
	open_music(2)

@eel.expose
def open_lofi_music():
	open_music(0)

@eel.expose
def open_code_music():
	open_music(1)



# Main function
def main():
	eel.init("GUI")
	eel.start("html\\index.html", size=(550, 600))


if __name__ == "__main__":
	get_json_data()
	main()