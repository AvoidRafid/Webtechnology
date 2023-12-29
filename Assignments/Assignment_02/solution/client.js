document.addEventListener("DOMContentLoaded", function() {
    // Function to handle radio button changes
    function handleRadioChange() {
        var selectedLanguage = document.querySelector('input[name="Language"]:checked').value;
        var detailsArea = document.getElementById("details");
        detailsArea.innerHTML = ""; // Clear details area

        // Send a POST request to the server only if a language is selected
        if (selectedLanguage) {
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "http://127.0.0.1:5600/options", true);
            xhr.setRequestHeader("Content-Type", "application/json");

            xhr.onreadystatechange = function() {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    var options = JSON.parse(xhr.responseText);
                    displayOptions(options);
                }
            };

            // Simulate the server's response based on the selected language
            var simulatedServerResponse = OPTIONS[selectedLanguage];
            xhr.send(JSON.stringify(simulatedServerResponse));
        } else {
            // Disable the selection list if no language is selected
            document.getElementById("Options").disabled = true;
        }
    }

    // Function to handle selection list changes
    function handleSelectionChange() {
        var selectedOptionId = document.getElementById("Options").value;
        var detailsArea = document.getElementById("details");
        var selectedOptionData = getOptionData(selectedOptionId);

        // Display additional data in the details area
        detailsArea.innerHTML = "<p>ID: " + selectedOptionData[0] + "</p>" +
                                "<p>Name: " + selectedOptionData[1] + "</p>" +
                                "<p>Additional Data: " + selectedOptionData[2] + "</p>";
    }

    // Function to display options in the selection list
    function displayOptions(options) {
        var selectionList = document.getElementById("Options");
        selectionList.disabled = false; // Enable the selection list

        selectionList.innerHTML = ""; // Clear selection list
        options.forEach(function(option) {
            var optionElement = document.createElement("option");
            optionElement.value = option[0];
            optionElement.text = option[1];
            selectionList.appendChild(optionElement);
        });
    }

    // Function to get additional data for a selected option
    function getOptionData(optionId) {
        var selectedLanguage = document.querySelector('input[name="Language"]:checked').value;
        var options = OPTIONS[selectedLanguage];

        for (var i = 0; i < options.length; i++) {
            if (options[i][0] == optionId) {
                return options[i];
            }
        }

        return null;
    }

    // Attach event listeners
    var radioButtons = document.getElementsByName("Language");
    radioButtons.forEach(function(radioButton) {
        radioButton.addEventListener("change", handleRadioChange);
    });

    var selectionList = document.getElementById("Options");
    selectionList.addEventListener("change", handleSelectionChange);
});
