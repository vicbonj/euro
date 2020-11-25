var trace1 = {
    var x = document.getElementById('x_wcs').value;
    var y = document.getElementById('y_wcs').value;
    var z = document.getElementById('zs').value;
    var c = document.getElementById('d2ms').value;
    x: x, y: y, z: z,
    mode: 'markers',
    marker: {
	size: 12,
	line: {
	    color: 'rgba(217, 217, 217, 0.14)',
	    width: 0.5},
	opacity: 0.8},
    type: 'scatter3d'
};

var data = [trace1];
var layout = {margin: {
	l: 0,
	r: 0,
	b: 0,
	t: 0
    }};
Plotly.newPlot('myDiv', data, layout);
