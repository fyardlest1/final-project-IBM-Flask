let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.send();
}


// function RunSentimentAnalysis() {
//     // Get the text to analyze from the input field
//     var textToAnalyze = document.getElementById("textToAnalyze").value;
    
//     // Send an AJAX POST request to the Flask server
//     $.ajax({
//         type: "POST",
//         url: "/emotionDetector",
//         data: {textToAnalyze: textToAnalyze},
//         success: function(response) {
//             if (response.error) {
//                 document.getElementById("system_response").innerHTML = response.error;
//             } else {
//                 document.getElementById("system_response").innerHTML = 
//                     "<p>Anger: " + response.anger + "</p>" +
//                     "<p>Disgust: " + response.disgust + "</p>" +
//                     "<p>Fear: " + response.fear + "</p>" +
//                     "<p>Joy: " + response.joy + "</p>" +
//                     "<p>Sadness: " + response.sadness + "</p>" +
//                     "<p><strong>Dominant Emotion: " + response.dominant_emotion + "</strong></p>";
//             }
//         },
//         error: function() {
//             document.getElementById("system_response").innerHTML = "An error occurred. Please try again.";
//         }
//     });
// }

