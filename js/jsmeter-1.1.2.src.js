/**
 * Project: JSGadget
 * Gadget:  JSMeter
 */

/**
 *
 * Copyright (c) 2014 Serge L. Ryadkow http://jsgadget.ru
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this
 * software and associated documentation files (the "Software"), to deal in the Software
 * without restriction, including without limitation the rights to use, copy, modify,
 * merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
 * permit persons to whom the Software is furnished to do so, subject to the following
 * conditions:
 *
 * The above copyright notice and this permission notice shall be included in all copies
 * or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
 * PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
 * FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
 * OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.
 *
 */

/**
 *
 * Versions history
 *
 * 1.1.2
 * Fixed bug with incorrect drawing scale with a nonzero lower end of the range
 *
 * 1.1.1
 * First release
 *
 */

var JSGadget = JSGadget || {};

/**
 * meter.js
 */

//Meter declaration
JSGadget.Meter = function(owner, options, val) {
  this.owner = typeof(owner) == "string" ? $(owner) : owner;
	this.owner.css(JSGadget.Meter.Style.OWNER);
	this.opt = {
			title: "",
			gap: 14,
			angle: 120,
			min: 0,
			max: 100,
			scale: {
				c: "black",
				w: 2,
				lm: { //large mark
					s: 20, //step
					c: "black",
					w: 2,
					l: 3,
					f: 8,
					fc: "black"
				},
				sm: { //small mark
					s: 10, //step
					c: "black",
					w: 1,
					l: 2
				}
			},
			hand: {
				c: "red",
				w: 1,
				l: 33,
				l0: 0,
				cr: 3,
				f: "l" //form: l-line(default), t-triangle
			},
			font: {
				size: 12,
				family: "sans-serif",
				color: "black"
			}
	};
	JSGadget.setopt(this.opt, options);
	val = val !== undefined ? val : 0;
	if (val < this.opt.min)
		val = this.opt.min;
	if (val > this.opt.max)
		val = this.opt.max;
	this.val = val;
	this.resize();
};
//Meter implementation
JSGadget.Meter.prototype.resize = function() {
	this.owner.empty();
	this.size = {w: this.owner.width(), h: this.owner.height()};
	if (this.size.w > 0 && this.size.h > 0) {
		this.canv = this.owner.append("<canvas width='" +	this.size.w + "' height='" + this.size.h +
				"'/>").children().last().css({position: "absolute", left: 0, top: 0});
		this.ctx = this.canv[0].getContext("2d");
		this.ctx.lineCap = "round";
		this.draw();
	} else
		this.canv = this.ctx = null;
};
JSGadget.Meter.prototype.setVal = function(val) {
	if (val < this.opt.min)
		val = this.opt.min;
	if (val > this.opt.max)
		val = this.opt.max;
	this.val = val;
	this.draw();
};
JSGadget.Meter.prototype.clear = function() {
 	if (this.ctx)
 		this.ctx.clearRect(0, 0, this.size.w, this.size.h);
};
JSGadget.Meter.prototype.draw = function() {
  if (this.ctx) {
 		this.clear();
 		this.ctx.save();
 		if (this.opt.title) {
			this.ctx.textBaseline = "middle";
			this.ctx.textAlign = "center";
			this.ctx.font = this.opt.font.size + "px " + this.opt.font.family;
			this.ctx.fillStyle = this.opt.font.color;
			this.ctx.fillText(this.opt.title, this.size.w / 2, this.size.w *
					(this.opt.angle > 180 ? 2 / 3 : 1 / 3));
 		}
 	  this.ctx.translate(this.size.w / 2, this.size.w / 2);
 	  this.ctx.scale(this.size.w / 100, this.size.w / 100);
 	  this.drawScale();
 	  this.drawHand();
 		this.ctx.restore();
  }
};


/**
 * style.js
 */

JSGadget.Meter.Style = {};

JSGadget.Meter.Style.OWNER = {
	overflow:   "hidden"
};
/**
 * scale.js
 */

JSGadget.Meter.prototype.drawScale = function() {
  var min = -this.opt.angle / 2, max = this.opt.angle / 2;
	this.ctx.save();
	this.ctx.beginPath();
	this.ctx.arc(0, 0, 50 - this.opt.gap, (min - 90) / 180 * Math.PI,
			(max - 90) / 180 * Math.PI);
	this.ctx.strokeStyle = this.opt.scale.c;
	this.ctx.lineWidth = this.opt.scale.w;
	this.ctx.stroke();
	this.ctx.restore();

	this.ctx.save();
	if (this.opt.scale.sm.s) {
		this.ctx.beginPath();
		var da = this.opt.scale.sm.s / (this.opt.max - this.opt.min) *
				this.opt.angle / 180 * Math.PI;
		this.ctx.rotate(min / 180 * Math.PI);
		for (var v = this.opt.min; v <= this.opt.max; v += this.opt.scale.sm.s) {
			this.ctx.moveTo(0, -50 + this.opt.gap);
			this.ctx.lineTo(0, -50 + this.opt.gap - this.opt.scale.sm.l);
			this.ctx.rotate(da);
		}
		this.ctx.strokeStyle = this.opt.scale.sm.c;
		this.ctx.lineWidth = this.opt.scale.sm.w;
		this.ctx.stroke();
	}
	this.ctx.restore();

	this.ctx.save();
	if (this.opt.scale.lm.s) {
		this.ctx.textBaseline = "bottom";
		this.ctx.textAlign = "center";
		this.ctx.font = "bold " + this.opt.scale.lm.f + "px " + this.opt.font.family;
		this.ctx.fillStyle = this.opt.scale.lm.fc;
		this.ctx.beginPath();
		var da = this.opt.scale.lm.s / (this.opt.max - this.opt.min) *
				this.opt.angle / 180 * Math.PI;
		this.ctx.rotate(min / 180 * Math.PI);
		for (var v = this.opt.min; v <= this.opt.max;	v += this.opt.scale.lm.s) {
			this.ctx.moveTo(0, -50 + this.opt.gap);
			this.ctx.lineTo(0, -50 + this.opt.gap - this.opt.scale.lm.l);
			this.ctx.fillText(+v.toFixed(3), 0, -50 + this.opt.gap - this.opt.scale.lm.l);
			this.ctx.rotate(da);
		}
		this.ctx.strokeStyle = this.opt.scale.lm.c;
		this.ctx.lineWidth = this.opt.scale.lm.w;
		this.ctx.stroke();
	}
	this.ctx.restore();
};
/**
 * hand.js
 */

JSGadget.Meter.prototype.drawHand = function() {
  this.ctx.save();
  var a = -this.opt.angle / 2 + (this.val - this.opt.min) /
  		(this.opt.max - this.opt.min) *	this.opt.angle;
  this.ctx.rotate((a - 90) / 180 * Math.PI);
  this.ctx.beginPath();
	switch (this.opt.hand.f) {
		case "t":
			this.ctx.moveTo(-this.opt.hand.l0, -this.opt.hand.w / 2);
			this.ctx.lineTo(-this.opt.hand.l0, this.opt.hand.w / 2);
			this.ctx.lineTo(this.opt.hand.l, 0);
			this.ctx.closePath();
		  this.ctx.fillStyle = this.opt.hand.c;
			this.ctx.lineWidth = 0;
		  this.ctx.fill();
			break;
		case "l":
		default:
			this.ctx.moveTo(-this.opt.hand.l0, 0);
			this.ctx.lineTo(this.opt.hand.l, 0);
			this.ctx.strokeStyle = this.opt.hand.c;
			this.ctx.lineWidth = this.opt.hand.w;
			this.ctx.stroke();
	}
  if (this.opt.hand.cr) {
  	this.ctx.beginPath();
  	this.ctx.arc(0, 0, this.opt.hand.cr, 0, 2 * Math.PI, false);
  	this.ctx.fillStyle = this.opt.hand.c;
		this.ctx.lineWidth = 0;
  	this.ctx.fill();
  }
  this.ctx.restore();
};
/**
 * setopt.js
 */

JSGadget.setopt = function(def, opt) {
	if (opt)
		for (var key in opt)
			if (typeof(opt[key]) == "object")
				JSGadget.setopt(def[key], opt[key]);
			else
				def[key] = opt[key];
};
