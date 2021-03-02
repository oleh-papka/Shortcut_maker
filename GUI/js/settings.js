async function get_data(){
	var plan_d1_a1 = document.getElementById("plan_desktop1_app1_link").value;
	var plan_d1_a2 = document.getElementById("plan_desktop1_app2_link").value;
	var plan_d1_a3 = document.getElementById("plan_desktop1_app3_link").value;

	var plan_d2_a1 = document.getElementById("plan_desktop2_app1_link").value;
	var plan_d2_a2 = document.getElementById("plan_desktop2_app2_link").value;
	var plan_d2_a3 = document.getElementById("plan_desktop2_app3_link").value;

	var plan_d3_a1 = document.getElementById("plan_desktop3_app1_link").value;
	var plan_d3_a2 = document.getElementById("plan_desktop3_app2_link").value;
	var plan_d3_a3 = document.getElementById("plan_desktop3_app3_link").value;



	var code_d1_a1 = document.getElementById("code_desktop1_app1_link").value;
	var code_d1_a2 = document.getElementById("code_desktop1_app2_link").value;
	var code_d1_a3 = document.getElementById("code_desktop1_app3_link").value;

	var code_d2_a1 = document.getElementById("code_desktop2_app1_link").value;
	var code_d2_a2 = document.getElementById("code_desktop2_app2_link").value;
	var code_d2_a3 = document.getElementById("code_desktop2_app3_link").value;

	var code_d3_a1 = document.getElementById("code_desktop3_app1_link").value;
	var code_d3_a2 = document.getElementById("code_desktop3_app2_link").value;
	var code_d3_a3 = document.getElementById("code_desktop3_app3_link").value;


	
	var univ_d1_a1 = document.getElementById("univ_desktop1_app1_link").value;
	var univ_d1_a2 = document.getElementById("univ_desktop1_app2_link").value;
	var univ_d1_a3 = document.getElementById("univ_desktop1_app3_link").value;

	var univ_d2_a1 = document.getElementById("univ_desktop2_app1_link").value;
	var univ_d2_a2 = document.getElementById("univ_desktop2_app2_link").value;
	var univ_d2_a3 = document.getElementById("univ_desktop2_app3_link").value;

	var univ_d3_a1 = document.getElementById("univ_desktop3_app1_link").value;
	var univ_d3_a2 = document.getElementById("univ_desktop3_app2_link").value;
	var univ_d3_a3 = document.getElementById("univ_desktop3_app3_link").value;



	var rock_links = document.getElementById("rock_music_links").value;
	
	var lofi_links = document.getElementById("lo-fi_music_links").value;
	
	var code_links = document.getElementById("code_music_links").value;
	
	var bass_links = document.getElementById("bass_music_links").value;


	var plan_data = [
		plan_d1_a1, plan_d1_a2, plan_d1_a3,
		plan_d2_a1, plan_d2_a2, plan_d2_a3,
		plan_d3_a1, plan_d3_a2, plan_d3_a3
	];

	var code_data = [
		code_d1_a1, code_d1_a2, code_d1_a3,
		code_d2_a1, code_d2_a2, code_d2_a3,
		code_d3_a1, code_d3_a2, code_d3_a3
	];

	var univ_data = [
		univ_d1_a1, univ_d1_a2, univ_d1_a3,
		univ_d2_a1, univ_d2_a2, univ_d2_a3,
		univ_d3_a1, univ_d3_a2, univ_d3_a3
	];

	eel.get_data(plan_data, code_data, univ_data, rock_links, lofi_links, code_links, bass_links);
}

async function get_default() {
	let data = await eel.put_default()();
	
	document.getElementById("plan_desktop1_app2_link").value = data.plan[0];
	document.getElementById("plan_desktop1_app1_link").value = data.plan[1];
	document.getElementById("plan_desktop1_app3_link").value = data.plan[2];

	document.getElementById("plan_desktop2_app1_link").value = data.plan[3];
	document.getElementById("plan_desktop2_app2_link").value = data.plan[4];
	document.getElementById("plan_desktop2_app3_link").value = data.plan[5];

	document.getElementById("plan_desktop3_app2_link").value = data.plan[6];
	document.getElementById("plan_desktop3_app3_link").value = data.plan[7];
	document.getElementById("plan_desktop3_app1_link").value = data.plan[8];



	document.getElementById("code_desktop1_app1_link").value = data.code[0];
	document.getElementById("code_desktop1_app2_link").value = data.code[1];
	document.getElementById("code_desktop1_app3_link").value = data.code[2];

	document.getElementById("code_desktop2_app1_link").value = data.code[3];
	document.getElementById("code_desktop2_app2_link").value = data.code[4];
	document.getElementById("code_desktop2_app3_link").value = data.code[6];

	document.getElementById("code_desktop3_app1_link").value = data.code[7];
	document.getElementById("code_desktop3_app2_link").value = data.code[8];
	document.getElementById("code_desktop3_app3_link").value = data.code[9];


	
	document.getElementById("univ_desktop1_app1_link").value = data.univ[0];
	document.getElementById("univ_desktop1_app2_link").value = data.univ[1];
	document.getElementById("univ_desktop1_app3_link").value = data.univ[2];

	document.getElementById("univ_desktop2_app1_link").value = data.univ[3];
	document.getElementById("univ_desktop2_app2_link").value = data.univ[4];
	document.getElementById("univ_desktop2_app3_link").value = data.univ[5];

	document.getElementById("univ_desktop3_app1_link").value = data.univ[6];
	document.getElementById("univ_desktop3_app2_link").value = data.univ[7];
	document.getElementById("univ_desktop3_app3_link").value = data.univ[8];



	document.getElementById("rock_music_links").value = data.rock_music;
	
	document.getElementById("lo-fi_music_links").value = data.lofi_music;
	
	document.getElementById("code_music_links").value = data.code_music;
	
	document.getElementById("bass_music_links").value = data.bass_music;
}



document.addEventListener("DOMContentLoaded", get_default());