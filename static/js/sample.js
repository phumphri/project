console.log("sample.js was constructed.")

try {
    Plotly.purge('sample_chart');

    console.log("\n\n Purged sample_chart.")
} catch (err) {
    console.log("\n\nPurge", err.message)
}


var window_location_host = window.location.host

if (window_location_host.indexOf("heroku") == -1) {
    url = "http://"
}
else {
    url = "https://"
}


url = url + window_location_host + "/api/sample"
console.log("\n\nurl:", url)

try {
    d3.json(url, function (error, response) {

        if (error) {
            console.log("\n\n")
            console.log("****************")
            console.log("d3.json failed.")
            return console.warn(error);
        }

        console.log("\n\nresponse:")
        console.log(response)

        var trace1 = {
            x: response['diabetes_X_test'],
            y: response['diabetes_y_test'],
            mode: 'markers',
            name: 'test'
        };

        var trace2 = {
            x: response['diabetes_X_test'],
            y: response['diabetes_y_pred'],
            mode: 'lines',
            name: 'prediction'
        };

        var data = [trace1, trace2];

        X_min = Math.min(response['diabetes_X_test'])
        X_max = Math.max(response['diabetes_X_test'])
        

        var layout = {
            showlegend: false,
            xaxis: { title: 'Data', range: [X_min, X_max] },
            yaxis: { title: 'Observation' },
            autosize: false,
            height: 500,
            width: 900
        };

        Plotly.newPlot('sample_chart', data, layout)
    }
)
} catch (err) {
    console.log(err.message)
}
