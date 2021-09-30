// function check_one_lang() {
// 	var language = document.getElementsByName("language");
// 	if (language.checked == false) {
// 		alert("You need to choose at least one language!");
// 	}
// 	else {
// 		var form = document.getElementById("form");
// 		form.submit();
// 	}
// }

function insert_result(response) {
	var maintext = document.getElementById("maintext");
	maintext.innerHTML = response;
}


function insert_result2(response) {
	var maintext = document.getElementById("container");
	maintext.innerHTML = response;
}


function update_page() {
	var form = document.getElementById("form");
	var formData = new FormData(form);
	var searchParams = new URLSearchParams(formData);
	var queryString = searchParams.toString();
	xmlHttpRqst = new XMLHttpRequest();
	xmlHttpRqst.onload = function (e) { insert_result(xmlHttpRqst.response); }
	// alert(queryString);
	xmlHttpRqst.open("GET", "/corpus/?" + queryString);
	xmlHttpRqst.send();

}

function update_page2() {
	var form = document.getElementById("about-form");
	var formData = new FormData(form);
	var searchParams = new URLSearchParams(formData);
	var queryString = searchParams.toString();
	xmlHttpRqst = new XMLHttpRequest();
	xmlHttpRqst.onload = function (e) { insert_result2(xmlHttpRqst.response); }
	xmlHttpRqst.open("GET", "/about/?" + queryString);
	xmlHttpRqst.send();

}

function update_page3() {
	var form = document.getElementById("how-to-use-form");
	var formData = new FormData(form);
	var searchParams = new URLSearchParams(formData);
	var queryString = searchParams.toString();
	xmlHttpRqst = new XMLHttpRequest();
	xmlHttpRqst.onload = function (e) { insert_result2(xmlHttpRqst.response); }
	xmlHttpRqst.open("GET", "/how-to-use/?" + queryString);
	xmlHttpRqst.send();

}

function update_page4() {
	var form = document.getElementById("dataviz-form");
	var formData = new FormData(form);
	var searchParams = new URLSearchParams(formData);
	var queryString = searchParams.toString();
	xmlHttpRqst = new XMLHttpRequest();
	xmlHttpRqst.onload = function (e) { insert_result2(xmlHttpRqst.response); }
	xmlHttpRqst.open("GET", "/dataviz/?" + queryString);
	xmlHttpRqst.send();

}

function update_page5() {
	var form = document.getElementById("demo-form");
	var formData = new FormData(form);
	var searchParams = new URLSearchParams(formData);
	var queryString = searchParams.toString();
	xmlHttpRqst = new XMLHttpRequest();
	xmlHttpRqst.onload = function (e) { insert_result2(xmlHttpRqst.response); }
	xmlHttpRqst.open("GET", "/demo/?" + queryString);
	xmlHttpRqst.send();

}
