var i = 1;

function roundMap() {
	for(var j = 1; j < 5; j++) {
		document.getElementById("span" + j).style.backgroundColor = "white";
		document.getElementById("img" + j).style.zIndex = 0;
	}

	i++;
	document.getElementById("img" + i).style.zIndex = 2;
	document.getElementById("span" + i).style.backgroundColor = "orange"

	console.log(i);

	if(i == 4) {
		i = 0;
	}

}
var Obj_set = window.setInterval("roundMap()", 2000);
var a;

function change(a) {
	window.clearInterval(Obj_set);
	for(j = 1; j < 5; j++) {
		document.getElementById("span" + j).style.backgroundColor = "white"
		document.getElementById("img" + j).style.zIndex = 0;
	}

	document.getElementById("img" + a).style.zIndex = 2;
	document.getElementById("span" + a).style.backgroundColor = "orange"

}

function leavespan(k) {

	if(k == 4) {
		k = 0;
	}
	i = k;
	Obj_set = window.setInterval("roundMap()", 2000);
}