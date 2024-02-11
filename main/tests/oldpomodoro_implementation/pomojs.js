// Define a function to start the pomodoro timer
function startPomodoro() {
    // Get the study and break intervals from the input elements
    var studyInterval = document.getElementById("study_interval").value;
    var breakInterval = document.getElementById("break_interval").value;
    // Send a request to the start_pomodoro route with the intervals as query parameters
    $.get("/start_pomodoro?study_interval=" + studyInterval + "&break_interval=" + breakInterval, function(data) {
        // Get the JSON response and parse it
        var response = JSON.parse(data);
        // Update the pomodoro object and the timer display
        pomodoro = response.pomodoro;
        updateTimer();
        // Show the success message
        alert(response.message);
    });
}

// Define a function to add five minutes to the current interval
function addFiveMinutes() {
    // Send a request to the add_five_minutes route
    $.get("/add_five_minutes", function(data) {
        // Get the JSON response and parse it
        var response = JSON.parse(data);
        // Update the pomodoro object and the timer display
        pomodoro = response.pomodoro;
        updateTimer();
        // Show the success message
        alert(response.message);
    });
}

// Define a function to skip to the break interval
function skipToBreak() {
    // Send a request to the skip_to_break route
    $.get("/skip_to_break", function(data) {
        // Get the JSON response and parse it
        var response = JSON.parse(data);
        // Update the pomodoro object and the timer display
        pomodoro = response.pomodoro;
        updateTimer();
        // Show the success message
        alert(response.message);
    });
}

// Define a function to skip to the study interval
function skipToStudy() {
    // Send a request to the skip_to_study route
    $.get("/skip_to_study", function(data) {
        // Get the JSON response and parse it
        var response = JSON.parse(data);
        // Update the pomodoro object and the timer display
        pomodoro = response.pomodoro;
        updateTimer();
        // Show the success message
        alert(response.message);
    });
}
