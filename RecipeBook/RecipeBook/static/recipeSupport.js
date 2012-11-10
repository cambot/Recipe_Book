// depends on Ratio.js

// wrapper for performing string --> ratioObj math
// Returns Ratio object
function convert(input, factor){
    var ans = Ratio.parse(input).multiply(factor);
    return ans.reduce();
}

function formatOutput(input, units) {
    return input.toLocaleString() + " " + units;
}
