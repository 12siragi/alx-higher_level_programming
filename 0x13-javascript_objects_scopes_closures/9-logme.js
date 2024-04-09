#!/usr/bin/node
/* a function that prints the number of arguments already printed and the new argument value */

let count = 0; // Initialize a variable `count` to keep track of the number of arguments printed

exports.logMe = function(item) { // Export a function named `logMe`
  console.log(`${count++}: ${item}`); // Log the number of arguments already printed and the new argument value
};

