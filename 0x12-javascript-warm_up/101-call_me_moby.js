#!/usr/bin/node

// Define the callMeMoby function
function callMeMoby(x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Export the callMeMoby function to make it visible outside
module.exports.callMeMoby = callMeMoby;

