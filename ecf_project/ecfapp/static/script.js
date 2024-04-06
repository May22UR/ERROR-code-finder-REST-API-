function getErrorMeaning() {
	var errorCodeInput = document.getElementById("error-code-input").value;

// if empty validations
	if (!errorCodeInput) {
		alert("Input field should not be empty!!!");
		document.getElementById("error-code-placeholder").style.display = "none";
		document.getElementById("error-message-placeholder").style.display = "none";
		return;
	}

// integer validation
	if (!/^\d+$/.exec(errorCodeInput)) {
		alert("Error code contain only numbers (No special characters or Alphabets)!");
		resetInputAndFocus();
		return;
	}

// range validations
	if (!(errorCodeInput >= 400 && errorCodeInput <= 600)) {
		alert("Error code should be numbers between 400 and 600!!!");
		resetInputAndFocus();
		return;
	}
    
	fetch(`/error_code_meaning/${errorCodeInput}`)
		.then(response => {
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			return response.json();
		})
		.then(data => {
			document.getElementById("error-code-placeholder").innerHTML = "Error Code: " + errorCodeInput;
			document.getElementById("error-message-placeholder").innerHTML = "Error Message: " + data.meaning;

//hide the result block untill fetched
			document.getElementById("error-code-placeholder").style.display = "block";
			document.getElementById("error-message-placeholder").style.display = "block";

//clears the input field
			document.getElementById("error-code-input").value = "";
			document.getElementById("error-code-input").focus();

		})

		.catch(error => {
			console.error('There was a problem with the fetch operation:', error);
			document.getElementById("error-code-placeholder").innerHTML = "Error Code: " + errorCodeInput;
			document.getElementById("error-message-placeholder").innerHTML = "Error: Meaning not found for the entered error code.";

//hide the result block untill fetched
			document.getElementById("error-code-placeholder").style.display = "block";
			document.getElementById("error-message-placeholder").style.display = "block";

//clears the input field
			document.getElementById("error-code-input").value = "";
			document.getElementById("error-code-input").focus();

		});
}
