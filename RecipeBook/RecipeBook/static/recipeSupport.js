// depends on Ratio.js

// wrapper for performing string --> ratioObj math
// Returns Ratio object
function convert(input, factor){
    var ans = Ratio.parse(input).multiply(factor);
    return ans.reduce();
}

function formatOutput(input, units) {
    //var output = "";
    //if (input.denominator == 1) { output = input.numerator; }
    //else { output = input.toString();}
    //return output + " " + units;
    return input.toLocaleString() + " " + units;
}
