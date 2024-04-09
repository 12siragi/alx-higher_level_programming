#!/usr/bin/node
/* A class Rectangle that defines a rectangle */

module.exports = class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }

  print() {
    if (!this.width || !this.height) return; // Return if width or height is undefined
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width)); // Using repeat to create row of Xs
    }
  }
};

