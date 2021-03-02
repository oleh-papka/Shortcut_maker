import eel, json

@eel.expose
def get_data(plan_data, code_data, univ_data, rock_links, lofi_links, code_links, bass_links):
	rock_links = rock_links.split("\n")
	lofi_links = lofi_links.split("\n")
	code_links = code_links.split("\n")
	bass_links = bass_links.split("\n")

	print("plan = ", plan_data)
	print("code = ", code_data)
	print("univ = ", univ_data)
	print("rock = ", rock_links)
	print("lofi = ", lofi_links)
	print("code = ", code_links)
	print("bass = ", bass_links)

	data = {
		"plan": plan_data,
		"code": code_data,
		"univ": univ_data,
		"rock_music": rock_links,
		"lofi_music": lofi_links,
		"code_music": code_links,
		"bass_music": bass_links
	}

	output_data = json.dumps(data)

	print(output_data)

	with open("GUI\\js\\links_data.json", "w") as json_file:
		json.dump(data, json_file)
		json_file.close()



@eel.expose
def put_default():
	with open("GUI\\js\\links_data.json", "r") as json_file:
		output_data = json.load(json_file)
		json_file.close()

	return output_data



eel.init("GUI")
eel.start("html\\index.html", size=(550, 600))
