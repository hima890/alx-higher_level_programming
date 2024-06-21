#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    } else {
      // Creates an empty object if w or h is not a positive integer
    }
  }
}

module.exports = Rectangle;
