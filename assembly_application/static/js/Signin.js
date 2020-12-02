function pass6() {
	var password1 = pass.value;
	if ( password1 > 6 ) {
		document.getElementById("pText2").innerHTML = " ";
	}
}
function passValue() {	
	var password = pass.value;
	var password1 = pass2.value;
		if (password == password1) {
			document.getElementById("pText3").innerHTML = "The passwords are 			matching";
		}
		else {
			if (password != password1) {
				document.getElementById("pText3").innerHTML = "The passwords 					don't match! Kindly check";
			}
		}
}
