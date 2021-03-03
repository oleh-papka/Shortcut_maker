async function get_data(){
	var rock_links = document.getElementById("rock_music_links").value;
	var lofi_links = document.getElementById("lo-fi_music_links").value;
	var code_links = document.getElementById("code_music_links").value;
	
	eel.get_data(rock_links, lofi_links, code_links);
}

async function get_default() {
	let data = await eel.put_default()();
	var rock = "";
	var lofi = "";
	var code = "";

	for (let index = 0; index < data.rock_music.length; index++) {
		rock = rock + data.rock_music[index] + "\n";
	}

	for (let index = 0; index < data.lofi_music.length; index++) {
		lofi = lofi + data.lofi_music[index] + "\n";
	}

	for (let index = 0; index < data.code_music.length; index++) {
		code = code + data.code_music[index] + "\n";
	}

	document.getElementById("rock_music_links").value = rock;
	document.getElementById("lo-fi_music_links").value = lofi;
	document.getElementById("code_music_links").value = code;
}



document.addEventListener("DOMContentLoaded", get_default());