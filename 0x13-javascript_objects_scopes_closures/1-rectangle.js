#!/usr/bin/node
/* A class Rectangle that defines a rectangle:
 * - You must use the class notation for defining your class
 * - The constructor must take 2 arguments: w and h
 * - Initialize the instance attribute width with the value of w
 */
module.exports = class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
};
