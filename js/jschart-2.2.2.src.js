/**
 * Project: JSGadget
 * Gadget:  JSChart
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
 * 2.2.2
 * To options in constructor add property background
 * 
 * 2.2.1
 * Component JSChart joined the project and namespace JSGadget
 *
 * before 2.2.1
 * Before version 2.2.1 component Chart existed as an independent project
 *
 */

var JSGadget = JSGadget || {};

/**
 * utils.js
 */

JSGadget.Utils = {};

JSGadget.Utils.extend = function(child, parent) {
	var F = function() {};
	F.prototype = parent.prototype;
	child.prototype = new F();
	child.prototype.constructor = child;
	child.superclass = parent.prototype;
};
JSGadget.Utils.int22dig = function(v) {
	return v < 10 ? "0" + v : "" + v;
};
JSGadget.Utils.date2str = function(d) {
	return JSGadget.Utils.int22dig(d.getDate()) + "." + JSGadget.Utils.int22dig(d.getMonth() + 1) + "." +
			d.getFullYear();
};
JSGadget.Utils.time2str = function(d) {
	return JSGadget.Utils.int22dig(d.getHours()) + ":" + JSGadget.Utils.int22dig(d.getMinutes()) + ":" +
			JSGadget.Utils.int22dig(d.getSeconds());
};
JSGadget.Utils.round2pix = function(v, w) {
	w = w || 1;
	if (w & 1) {
		var r = Math.round(v);
		return r < v ? r + 0.5 : r - 0.5;
	} else
		return Math.round(v);
};

/*
 * disableTextSelect
 * */
(function($) {
  if ($.browser.mozilla) {
      $.fn.disableTextSelect = function() {
          return this.each(function() {
              $(this).css({
                  'MozUserSelect' : 'none'
              });
          });
      };
      $.fn.enableTextSelect = function() {
          return this.each(function() {
              $(this).css({
                  'MozUserSelect' : ''
              });
          });
      };
  } else if ($.browser.msie) {
      $.fn.disableTextSelect = function() {
          return this.each(function() {
              $(this).bind('selectstart.disableTextSelect', function() {
                  return false;
              });
          });
      };
      $.fn.enableTextSelect = function() {
          return this.each(function() {
              $(this).unbind('selectstart.disableTextSelect');
          });
      };
  } else {
      $.fn.disableTextSelect = function() {
          return this.each(function() {
              $(this).bind('mousedown.disableTextSelect', function() {
                  return false;
              });
          });
      };
      $.fn.enableTextSelect = function() {
          return this.each(function() {
              $(this).unbind('mousedown.disableTextSelect');
          });
      };
  }
})(jQuery);
/**
 * chart.js
 */

//Chart declaration
JSGadget.Chart = function(owner, options) {
  this.owner = typeof(owner) == "string" ? $(owner) : owner;
	this.owner.css(JSGadget.Chart.Style.OWNER).attr("ondragstart", "return false;").
			attr("oncontextmenu", "return false;").disableTextSelect().
			bind("contextmenu", function(e) {return false;});
	this.opt = {
			gap: {
				t: 8,
				r: 5,
				b: 32,
				l: 40
			},
			interactive: true,
			font: {
				size: 12,
				family: "sans-serif"
			},
			mouseSens: 10,
			digital: false,
			background: JSGadget.Chart.BACKGROUND
	};
	if (options)
		for (var key in options)
			switch (key) {
				case "bAxis":
				case "lAxis":
				case "trends":
					this[key] = options[key];
					break;
				default:
					if (typeof(options[key]) == "object")
						JSGadget.setopt(this.opt[key], options[key]);
					else
						this.opt[key] = options[key];
			}
	this.owner.css("background-color", this.opt.background);
	if (this.opt.interactive)
		this.mouse = new JSGadget.Mouse(this);
	if (!this.bAxis)
		this.bAxis = new JSGadget.BAxis(this);
	else
		this.bAxis.chart = this;
	if (!this.lAxis)
		this.lAxis = this.opt.digital ? new JSGadget.DAxis(this) : new JSGadget.LAxis(this);
	else
		this.lAxis.chart = this;
	if (!this.trends)
		this.trends = [];
	else
		for (var i = 0, l = this.trends.length; i < l; ++i)
			this.trends[i].chart = this;
	this.resize();
};
//Chart implementation
JSGadget.Chart.prototype.resize = function() {
	this.owner.empty();
	this.size = {w: this.owner.width(), h: this.owner.height()};
	this.csize = {
			w: this.size.w - this.opt.gap.l - this.opt.gap.r,
			h: this.size.h - this.opt.gap.t - this.opt.gap.b
	};
	if (this.size.w > 0 && this.size.h > 0) {
		this.canv = this.owner.append("<canvas width='" +	this.size.w + "' height='" + this.size.h +
				"'/>").children().last().css({position: "absolute", left: 0, top: 0});
		this.cpos = this.canv.position();
		this.ctx = this.canv[0].getContext("2d");
		this.ctx.lineCap = "round";
		this.ctx.font = this.opt.font.size + "px " + this.opt.font.family;
		this.draw();
	} else
		this.canv = this.ctx = null;
};
JSGadget.Chart.prototype.clear = function() {
 	if (this.ctx)
 		this.ctx.clearRect(0, 0, this.size.w, this.size.h);
};
JSGadget.Chart.prototype.draw = function() {
 	if (this.ctx) {
 		this.clear();
 		if (this.bAxis.zoom || this.lAxis.zoom)
 			this.drawZoom();
 		this.bAxis.draw();
 		this.lAxis.draw();
 		this.ctx.save();
 		this.ctx.beginPath();
 		this.ctx.moveTo(this.opt.gap.l, this.opt.gap.t);
 		this.ctx.lineTo(this.opt.gap.l + this.csize.w, this.opt.gap.t);
 		this.ctx.lineTo(this.opt.gap.l + this.csize.w, this.opt.gap.t + this.csize.h);
 		this.ctx.lineTo(this.opt.gap.l, this.opt.gap.t + this.csize.h);
 		this.ctx.closePath();
 		this.ctx.clip();
 		for (var i = 0, l = this.trends.length; i < l; ++i)
 			if (this.trends[i]) {
 				if (!this.trends[i].opt.color)
 					this.trends[i].opt.color = JSGadget.Chart.COLORS[i % JSGadget.Chart.COLORS.length];
 				this.trends[i].draw(i);
 			}
 		this.ctx.restore();
 	}
};
JSGadget.Chart.prototype.drawZoom = function() {
	if (this.ctx) {
		this.ctx.save();
		var g = this.ctx.createLinearGradient(this.csize.w / 2 - this.csize.h / 6 - this.csize.h / 30,
				this.csize.h / 3 + this.csize.h / 30,
				this.csize.w / 2 - this.csize.h / 6 + this.csize.h / 30,
				this.csize.h / 3 - this.csize.h / 30);
		g.addColorStop(0, "silver");
		g.addColorStop(0.5, "white");
		g.addColorStop(1, "silver");
		this.ctx.strokeStyle = g;
		this.ctx.lineWidth = this.csize.h / 10;
		this.ctx.beginPath();
		this.ctx.moveTo(this.opt.gap.l + this.csize.w / 2 - this.csize.h / 6,
				this.opt.gap.t + this.csize.h / 3);
		this.ctx.lineTo(this.opt.gap.l + this.csize.w / 2 + this.csize.h / 3,
				this.opt.gap.t + this.csize.h * 5 / 6);
		this.ctx.stroke();
		this.ctx.strokeStyle = "#d0d0d0";
		g = this.ctx.createRadialGradient(this.csize.w / 2 - this.csize.h / 4, this.csize.h / 5,
				this.csize.h / 40, this.csize.w / 2 - this.csize.h / 6, this.csize.h / 3, this.csize.h / 4);
		g.addColorStop(0, "white");
		g.addColorStop(0.4, "#d0d0d0");
		g.addColorStop(1, "silver");
		this.ctx.fillStyle = g;
		this.ctx.lineWidth = this.csize.h / 15;
		this.ctx.beginPath();
		this.ctx.arc(this.opt.gap.l + this.csize.w / 2 - this.csize.h / 6,
				this.opt.gap.t + this.csize.h / 3, this.csize.h / 4, 0, Math.PI*2, true);
		this.ctx.fill();
		this.ctx.stroke();
		this.ctx.restore();
	}
};
JSGadget.Chart.prototype.loading = function(show) {
	if (this.ctx) {
		if (show) {
			this.loadSts = 0;
			if (!this.timer) {
				var self = this,
						x = this.csize.w / 2 - this.cpos.left,
						y = this.csize.h / 2 - this.cpos.top;
				this.timer = setInterval(function() {self.drawLoading(x, y);}, 100);
			}
		} else {
			if (this.timer)
				clearInterval(this.timer);
			this.timer = null;
			this.draw();
		}
	}
};
JSGadget.Chart.prototype.drawLoading = function(x, y) {
	if (this.ctx) {
		this.ctx.save();
		this.ctx.lineWidth = this.csize.h / 40;
		this.ctx.translate(x, y);
		this.ctx.rotate(this.loadSts * Math.PI / 6);
		for (var i = 0; i < 12; ++i) {
			var c = 220 - i * 5;
			this.ctx.strokeStyle = "rgb(" + c + "," + c + "," + c + ")";
			this.ctx.beginPath();
			this.ctx.rotate(Math.PI / 6);
			this.ctx.moveTo(this.csize.h / 10, 0);
			this.ctx.lineTo(this.csize.h / 5, 0);
			this.ctx.stroke();
		}
		this.ctx.restore();
		if (++this.loadSts >= 12)
			this.loadSts = 0;
	}
};


/**
 * const.js
 */

JSGadget.Chart.COLORS = ["#0000ff", "#00ff00", "#ff0000", "#00ffff",
                "#ffff00", "#ff00ff", "#000000", "#ffffff",
                "#ff8000", "#ff0080", "#80ff00", "#00ff80",
                "#8000ff", "#0080ff", "#ff8080", "#80ff80",
                "#8080ff", "#800000", "#008000", "#000080",
                "#808000", "#008080", "#800080", "#808080"];

JSGadget.Chart.BACKGROUND = "#e0e0e0";
/**
 * style.js
 */

JSGadget.Chart.Style = {};

JSGadget.Chart.Style.OWNER = {
		/*background: "#e0e0e0",*/
		overflow:   "hidden"
};
JSGadget.Chart.Style.CURSORS = {
		DEFAULT: "default",
		ZOOM:    "crosshair",
		DRAG:    "move"
};
JSGadget.Chart.Style.ZOOM = {
		position: "absolute",
		border: "1px dotted black"
};

/**
 * mouse.js
 */

//Mouse declaration
JSGadget.Mouse = function(chart) {
	this.chart = chart;
  var self = this;
  this.chart.owner.mousedown(function(e) {self.onDown(e);});
};
//Mouse implementation
JSGadget.Mouse.prototype.onDown = function(e) {
	if (this.chart.ctx) {
		var o = this.chart.owner.offset(), x = e.pageX - o.left, y = e.pageY - o.top;
		if (x >= this.chart.cpos.left && x <= this.chart.cpos.left + this.chart.size.w &&
				y >= this.chart.cpos.top && y <= this.chart.cpos.top + this.chart.size.h) {
			if (e.which == 1) {
				this.chart.owner.css({cursor: JSGadget.Chart.Style.CURSORS.ZOOM});
				this.zoomdiv = this.chart.owner.append("<div/>").children().last().
						css(JSGadget.Chart.Style.ZOOM);
				if (this.chart.opt.digital)
					this.zoomdiv.css({left: x + "px", top: this.chart.opt.gap.t + "px",
							height: this.chart.csize.h + "px"});
				else
					this.zoomdiv.css({left: x + "px", top: y + "px"});
				this.zoom = {x: e.pageX, y: e.pageY};
				this.bind();
			} else if (e.which == 3) {
				this.chart.owner.css({cursor: JSGadget.Chart.Style.CURSORS.DRAG});
				this.drag = {x: e.pageX, y: e.pageY};
				this.bind();
			}
		}
	}
};
JSGadget.Mouse.prototype.onUp = function(e) {
	if (this.chart.ctx) {
		this.chart.owner.css({cursor: JSGadget.Chart.Style.CURSORS.DEFAULT});
		if (this.zoom) {
			if (e.pageX - this.zoom.x > this.chart.opt.mouseSens &&
					(e.pageY - this.zoom.y > this.chart.opt.mouseSens || this.chart.opt.digital)) {
				var x1 = this.zoomdiv.position().left - this.chart.cpos.left,
				    x2 = x1 + this.zoomdiv.width();
				this.chart.bAxis.zoom = {min: this.chart.bAxis.coord2val(x1),
						max: this.chart.bAxis.coord2val(x2)};
				if (!this.chart.opt.digital) {
					var y2 = this.zoomdiv.position().top - this.chart.cpos.top,
							y1 = y2 + this.zoomdiv.height();
					this.chart.lAxis.zoom = {min: this.chart.lAxis.coord2val(y1),
							max: this.chart.lAxis.coord2val(y2)};
				}
			} else if (e.pageX - this.zoom.x < -this.chart.opt.mouseSens ||
					e.pageY - this.zoom.y < -this.chart.opt.mouseSens)
				this.chart.bAxis.zoom = this.chart.lAxis.zoom = null;
			this.zoomdiv.remove();
			this.zoom = null;
			this.unbind();
			this.chart.bAxis.calcGrid();
			this.chart.lAxis.calcGrid();
			this.chart.draw();
		} else if (this.drag) {
			this.drag = null;
			this.unbind();
		}
	}
};
JSGadget.Mouse.prototype.onLeave = function(e) {
	if (this.chart.ctx) {
		this.chart.owner.css({cursor: JSGadget.Chart.Style.CURSORS.DEFAULT});
		if (this.zoom) {
			this.zoomdiv.remove();
			this.zoom = null;
			this.unbind();
		} else if (this.drag) {
			this.drag = null;
			this.unbind();
		}
	}
};
JSGadget.Mouse.prototype.onMove = function(e) {
	if (this.chart.ctx) {
		if (this.zoom) {
			var o = this.chart.owner.offset();
			if (!this.chart.opt.digital) {
				if (e.pageX > this.zoom.x && e.pageY > this.zoom.y)
					this.zoomdiv.width(e.pageX - this.zoom.x).height(e.pageY - this.zoom.y).
							css({left: this.zoom.x - o.left + "px", top: this.zoom.y - o.top + "px"});
				else if (e.pageX > this.zoom.x && e.pageY < this.zoom.y)
					this.zoomdiv.width(e.pageX - this.zoom.x).height(this.zoom.y - e.pageY).
							css({left: this.zoom.x - o.left + "px", top: e.pageY - o.top + "px"});
				else if (e.pageX < this.zoom.x && e.pageY > this.zoom.y)
					this.zoomdiv.width(this.zoom.x - e.pageX).height(e.pageY - this.zoom.y).
							css({left: e.pageX - o.left + "px", top: this.zoom.y - o.top + "px"});
				else
					this.zoomdiv.width(this.zoom.x - e.pageX).height(this.zoom.y - e.pageY).
							css({left: e.pageX - o.left + "px", top: e.pageY - o.top + "px"});
			} else {
				if (e.pageX > this.zoom.x)
					this.zoomdiv.width(e.pageX - this.zoom.x).css({left: this.zoom.x - o.left + "px"});
				else
					this.zoomdiv.width(this.zoom.x - e.pageX).css({left: e.pageX - o.left + "px"});
			}
		} else if (this.drag) {
			var dx = this.chart.bAxis.coord2val(this.drag.x) - this.chart.bAxis.coord2val(e.pageX),
					dy = this.chart.opt.digital ? 0 :
							this.chart.lAxis.coord2val(this.drag.y) - this.chart.lAxis.coord2val(e.pageY);
			this.drag.x = e.pageX;
			this.drag.y = e.pageY;
			if (dx) {
				if (!this.chart.bAxis.zoom)
					this.chart.bAxis.zoom = {min: this.chart.bAxis.min, max: this.chart.bAxis.max};
				this.chart.bAxis.zoom.min += dx;
				this.chart.bAxis.zoom.max += dx;
				this.chart.bAxis.calcGrid();
			}
			if (dy) {
				if (!this.chart.lAxis.zoom)
					this.chart.lAxis.zoom = {min: this.chart.lAxis.min, max: this.chart.lAxis.max};
				this.chart.lAxis.zoom.min += dy;
				this.chart.lAxis.zoom.max += dy;
				this.chart.lAxis.calcGrid();
			}
			if (dx || dy)
				this.chart.draw();
		}
	}
};
JSGadget.Mouse.prototype.bind = function() {
	var self = this;
	this.chart.owner.bind("mouseup", function(e) {self.onUp(e);}).
			bind("mousemove", function(e) {self.onMove(e);}).
			bind("mouseleave", function(e) {self.onLeave(e);});
};
JSGadget.Mouse.prototype.unbind = function() {
	this.chart.owner.unbind("mousemove").unbind("mouseup").unbind("mouseleave");
};
/**
 * axis.js
 */

//Axis declaration
JSGadget.Axis = function(chart, min, max) {
	if (chart instanceof JSGadget.Chart)
		this.chart = chart;
	else {
		max = min;
		min = chart;
	}
	this.setMinMax(min !== null && min !== undefined ? min : 0,
			max !== null && max !== undefined ? max : 1);
};
//Axis implementation
JSGadget.Axis.prototype.setMinMax = function(min, max) {
  if (min !== null && min !== undefined)
		this.min = min;
  if (max !== null && max !== undefined)
		this.max = max;
  this.zoom = null;
	this.calcGrid();
};
JSGadget.Axis.prototype.val2pix = function(v) {
	var c = this.val2coord(v), r = Math.round(c);
	return r < c ? r + 0.5 : r - 0.5;
};
JSGadget.Axis.prototype.val2pix2 = function(v) {
	return Math.round(this.val2coord(v));
};
/**
 * haxis.js
 */

//HAxis declaration
JSGadget.HAxis = function(chart, min, max) {
	JSGadget.HAxis.superclass.constructor.apply(this, arguments);
};
JSGadget.Utils.extend(JSGadget.HAxis, JSGadget.Axis);
//HAxis implementation
JSGadget.HAxis.prototype.calcGrid = function() {
	var t = this.zoom ? this.zoom.max - this.zoom.min : this.max - this.min;
	if (t < 10)	this.grid = this.sGrid = 0;
	else if (t < 20) {this.grid = 4; this.sGrid = 1;}
	else if (t < 30) {this.grid = 5; this.sGrid = 1;}
	else if (t < 60) {this.grid = 10;	this.sGrid = 2;}
	else if (t < 120) {this.grid = 20;	this.sGrid = 5;}
	else if (t < 240) {this.grid = 30;	this.sGrid = 5;}
	else if (t < 480) {this.grid = 60;	this.sGrid = 15;}
	else if (t < 960) {this.grid = 120; this.sGrid = 30;}
	else if (t < 1920) {this.grid = 300; this.sGrid = 60;}
	else if (t < 3600) {this.grid = 600;	this.sGrid = 120;}
	else if (t < 7200) {this.grid = 1200; this.sGrid = 300;}
	else if (t < 14400) {this.grid = 1800;	this.sGrid = 300;}
	else if (t < 28800) {this.grid = 3600;	this.sGrid = 900;}
	else if (t < 57600) {this.grid = 7200; this.sGrid = 1800;}
	else if (t < 86400) {this.grid = 14400; this.sGrid = 3600;}
	else if (t < 172800) {this.grid = 28800; this.sGrid = 7200;}
	else if (t < 345600) {this.grid = 43200;	this.sGrid = 10800;}
	else if (t < 691200) {this.grid = 86400; this.sGrid = 21600;}
	else if (t < 1382400) {this.grid = 172800; this.sGrid = 43200;}
	else if (t < 2764800) {this.grid = 345600; this.sGrid = 86400;}
	else if (t < 5529600) {this.grid = 691200; this.sGrid = 172800;}
	else if (t < 11059200) {this.grid = 1382400; this.sGrid = 345600;}
	else if (t < 22118400) {this.grid = 2764800; this.sGrid = 691200;}
	else if (t < 44236800) {this.grid = 5529600; this.sGrid = 1382400;}
	else this.grid = this.sGrid = 0;
	this.offset = this.grid > 0 ? (this.zoom ? this.zoom.min : this.min) % this.grid : 0;
};
JSGadget.HAxis.prototype.val2coord = function(v) {
  return this.chart.opt.gap.l + (v - (this.zoom ? this.zoom.min : this.min)) /
  		(this.zoom ? this.zoom.max - this.zoom.min : this.max - this.min) *
  		(this.chart.csize.w - 2) + 1;
};
JSGadget.HAxis.prototype.coord2val = function(x) {
  return (x - this.chart.opt.gap.l - 1) / (this.chart.csize.w - 2) *
  		(this.zoom ? this.zoom.max - this.zoom.min : this.max - this.min) +
  		(this.zoom ? this.zoom.min : this.min);
};
JSGadget.HAxis.prototype.lbltxt = function(v) {
  var d1 = new Date(v * 1000);
  var d2 = new Date(d1.getUTCFullYear(), d1.getUTCMonth(), d1.getUTCDate(),
	  	d1.getUTCHours(), d1.getUTCMinutes(), d1.getUTCSeconds());
	return [JSGadget.Utils.date2str(d2),	JSGadget.Utils.time2str(d2)];
};
/**
 * vaxis.js
 */

//VAxis declaration
JSGadget.VAxis = function(chart, min, max) {
	JSGadget.VAxis.superclass.constructor.apply(this, arguments);
};
JSGadget.Utils.extend(JSGadget.VAxis, JSGadget.Axis);
//VAxis implementation
JSGadget.VAxis.prototype.calcGrid = function() {
	function order(v) {
	  var ord = 0;
	  for (; v > 1; ++ord) v /= 10;
	  for (; v < 0.1; --ord) v *= 10;
	  return ord;
	}
	function scale(v, ord) {
	  for (; ord > 0; --ord) v /= 10;
	  for (; ord < 0; ++ord) v *= 10;
	  return v;
	}
	var d = this.zoom ? this.zoom.max - this.zoom.min : this.max - this.min, o = order(d);
	d = scale(d, o);
	if (d < 0.2) {
		this.grid = 0.05;
		this.sGrid = 0.01;
	}	else if (d < 0.5) {
		this.grid = 0.1;
		this.sGrid = 0.02;
	}	else {
		this.grid = 0.2;
		this.sGrid = 0.05;
	}
	this.grid = scale(this.grid, -o);
	this.sGrid = scale(this.sGrid, -o);
	this.offset = this.grid > 0 ? (this.zoom ? this.zoom.min : this.min) % this.grid : 0;
	if (this.offset < 0)
		this.offset += this.grid;
};
JSGadget.VAxis.prototype.val2coord = function(v) {
  return this.chart.opt.gap.t + this.chart.csize.h - 1 -
  		(this.zoom ? (v - this.zoom.min) / (this.zoom.max - this.zoom.min) :
  				(v - this.min) / (this.max - this.min)) *
  		(this.chart.csize.h - 2);
};
JSGadget.VAxis.prototype.coord2val = function(y) {
  return (1 - (y - this.chart.opt.gap.t - 1) / (this.chart.csize.h - 2)) *
  		(this.zoom ? this.zoom.max - this.zoom.min : this.max - this.min) +
  		(this.zoom ? this.zoom.min : this.min);
};
JSGadget.VAxis.prototype.lbltxt = function(v) {
	return v > 100 ? v.toFixed(0) : v.toPrecision(3);
};
/**
 * baxis.js
 */

//BAxis declaration
JSGadget.BAxis = function(chart, min, max) {
	JSGadget.BAxis.superclass.constructor.apply(this, arguments);
};
JSGadget.Utils.extend(JSGadget.BAxis, JSGadget.HAxis);
//BAxis implementation
JSGadget.BAxis.prototype.draw = function() {
	this.chart.ctx.save();
	var y1 = this.chart.opt.gap.t + 1,
			y2 = this.chart.opt.gap.t + this.chart.csize.h - 1;
	if (this.grid != 0) {
		var min = this.zoom ? this.zoom.min : this.min,
				max = this.zoom ? this.zoom.max : this.max;
		this.chart.ctx.lineWidth = 1;
		//sGrid
		this.chart.ctx.strokeStyle = "#d0d0d0";
		this.chart.ctx.beginPath();
		for (var v = min - this.offset; v < max; v += this.sGrid)
		  if (v > min) {
		  	var x = this.val2pix(v);
		  	this.chart.ctx.moveTo(x, y1);
		  	this.chart.ctx.lineTo(x, y2);
			}
		this.chart.ctx.stroke();
		//grid&lbl
		this.chart.ctx.strokeStyle = "#b0b0b0";
		this.chart.ctx.fillStyle = "black";
		this.chart.ctx.textBaseline = "top";
		this.chart.ctx.textAlign = "center";
		this.chart.ctx.beginPath();
		var ly1 = this.chart.size.h - this.chart.opt.gap.b + this.chart.opt.font.size * 0.2,
				ly2 = ly1 + this.chart.opt.font.size * 1.2;
		for (var v = min - this.offset; v <= max; v += this.grid)
		  if (v >= min) {
		  	var x = this.val2pix(v);
		    if (v != min) {
		    	this.chart.ctx.moveTo(x, y1);
		    	this.chart.ctx.lineTo(x, y2);
				}
		    var la = this.lbltxt(v);
				this.chart.ctx.fillText(la[0], x, ly1);
				this.chart.ctx.fillText(la[1], x, ly2);
		    /*
				owner.append("<div class='chart_lbl chart_blbl'>" + lbltxt(v) +
						"</div>").children().last().css("left", x + "px").
						attr("unselectable", "on").
						select(function() {return false;});
						*/
			}
		this.chart.ctx.stroke();
	}
	//ray
	this.chart.ctx.lineWidth = 2;
	this.chart.ctx.strokeStyle = "black";
	this.chart.ctx.beginPath();
	this.chart.ctx.moveTo(this.chart.opt.gap.l + 1, y2);
	this.chart.ctx.lineTo(this.chart.opt.gap.l + this.chart.csize.w - 1, y2);
	this.chart.ctx.stroke();
	this.chart.ctx.restore();
};
/**
 * laxis.js
 */

//LAxis declaration
JSGadget.LAxis = function(chart, min, max) {
	JSGadget.LAxis.superclass.constructor.apply(this, arguments);
};
JSGadget.Utils.extend(JSGadget.LAxis, JSGadget.VAxis);
//LAxis implementation
JSGadget.LAxis.prototype.draw = function() {
	if (this.chart.ctx) {
		this.chart.ctx.save();
		var x1 = this.chart.opt.gap.l + 1,
				x2 = this.chart.opt.gap.l + this.chart.csize.w - 1,
				min = this.zoom ? this.zoom.min : this.min,
				max = this.zoom ? this.zoom.max : this.max;
		if (this.grid != 0) {
			this.chart.ctx.lineWidth = 1;
			//sGrid
			this.chart.ctx.strokeStyle = "#d0d0d0";
			this.chart.ctx.beginPath();
			for (var v = min - this.offset; v < max; v += this.sGrid)
			  if (v > min) {
		  		var y = this.val2pix(v);
			  	this.chart.ctx.moveTo(x1, y);
			  	this.chart.ctx.lineTo(x2, y);
				}
			this.chart.ctx.stroke();
			//grid&lbl
			this.chart.ctx.strokeStyle = "#b0b0b0";
			this.chart.ctx.fillStyle = "black";
			this.chart.ctx.textBaseline = "middle";
			this.chart.ctx.textAlign = "right";
			this.chart.ctx.beginPath();
			var lx = this.chart.opt.gap.l - this.chart.opt.font.size * 0.2;
			for (var v = min - this.offset; v <= max; v += this.grid)
			  if (v >= min) {
		  		var y = this.val2pix(v);
				  if (v != min) {
				  	this.chart.ctx.moveTo(x1, y);
				  	this.chart.ctx.lineTo(x2, y);
					}
					this.chart.ctx.fillText(this.lbltxt(v), lx, y);
				}
			this.chart.ctx.stroke();
		}
		//ray
		this.chart.ctx.lineWidth = 2;
		this.chart.ctx.strokeStyle = "black";
		this.chart.ctx.beginPath();
  	this.chart.ctx.moveTo(x1, this.chart.opt.gap.t + this.chart.csize.h - 1);
  	this.chart.ctx.lineTo(x1, this.chart.opt.gap.t + 1);
		this.chart.ctx.stroke();
		if (this.lohi) {
			this.chart.ctx.lineWidth = 2;
			this.chart.ctx.strokeStyle = "yellow";
			if (this.inRange(this.lohi.lo, min, max))
				this.drawline(this.lohi.lo, x1, x2 - 2);
			if (this.inRange(this.lohi.hi, min, max))
				this.drawline(this.lohi.hi, x1, x2 - 2);
			this.chart.ctx.strokeStyle = "red";
			if (this.inRange(this.lohi.lolo, min, max))
				this.drawline(this.lohi.lolo, x1, x2 - 2);
			if (this.inRange(this.lohi.hihi, min, max))
				this.drawline(this.lohi.hihi, x1, x2 - 2);
		}
		this.chart.ctx.restore();
	}
};
JSGadget.LAxis.prototype.drawline = function(y, x1, x2) {
	y = this.val2pix2(y);
	this.chart.ctx.beginPath();
	for (var x = x1; x < x2; x += 10) {
		this.chart.ctx.moveTo(x, y);
		this.chart.ctx.lineTo(x + 1, y);
	}
	this.chart.ctx.stroke();
};
JSGadget.LAxis.prototype.inRange = function(v, min, max) {
	return v !== null && v !== undefined && v >= min && v <= max;
};
/**
 * daxis.js
 */

//DAxis declaration
JSGadget.DAxis = function(chart, min, max) {
	JSGadget.DAxis.superclass.constructor.apply(this, arguments);
};
JSGadget.Utils.extend(JSGadget.DAxis, JSGadget.Axis);
//DAxis implementation
JSGadget.DAxis.prototype.calcGrid = function() {
	/////////////////
};
JSGadget.DAxis.prototype.val2coord = function(v, idx) {
	var n = this.chart.trends.length;
	if (!n)
		n = 1;
	if (n > 1 || this.chart.trends[0].opt.title) {
		var d = this.chart.csize.h / (n + 0.2);
		return this.chart.opt.gap.t + d * (idx + 0.3) + d * (v ? 0.2 : 0.7);
	} else
		return this.chart.opt.gap.t + this.chart.csize.h * (v ? 0.2 : 0.8);
};
JSGadget.DAxis.prototype.draw = function() {
	if (this.chart.ctx) {
		this.chart.ctx.save();
		var n = this.chart.trends.length,
				x1 = this.chart.opt.gap.l + 1,
				x2 = this.chart.opt.gap.l + this.chart.csize.w - 1;
		if (n) {
			//grid&lbl
			this.chart.ctx.lineWidth = 1;
			this.chart.ctx.strokeStyle = "#b0b0b0";
			this.chart.ctx.textBaseline = "middle";
			this.chart.ctx.beginPath();
			var lx = this.chart.opt.gap.l - this.chart.opt.font.size * 0.2,
					d = this.chart.csize.h / (n + 0.2),
					x0 = (x1 + x2) / 2;
			for (var i = 0; i < n; ++i) {
				var y;
				if (n > 1 || this.chart.trends[0].opt.title) {
					y = JSGadget.Utils.round2pix(this.chart.opt.gap.t + d * (i + 0.3));
					if (this.chart.trends[i] && this.chart.trends[i].opt.title) {
						this.chart.ctx.fillStyle = this.chart.trends[i].opt.titlecolor ||
								this.chart.trends[i].opt.color;
						this.chart.ctx.textAlign = "center";
						this.chart.ctx.fillText(this.chart.trends[i].opt.title, x0, y);
					}
					y = JSGadget.Utils.round2pix(y + d * 0.2);
				} else
					y = JSGadget.Utils.round2pix(this.chart.opt.gap.t + this.chart.csize.h * 0.2);
		  	this.chart.ctx.moveTo(x1, y);
		  	this.chart.ctx.lineTo(x2, y);
		  	if (this.chart.trends[i]) {
					this.chart.ctx.fillStyle = "black";
					this.chart.ctx.textAlign = "right";
		  		this.chart.ctx.fillText(this.chart.trends[i].opt.text1, lx, y);
		  	}
		  	y = JSGadget.Utils.round2pix(y + (n > 1 || this.chart.trends[0].opt.title ? d * 0.5 :
		  			this.chart.csize.h * 0.6));
		  	this.chart.ctx.moveTo(x1, y);
		  	this.chart.ctx.lineTo(x2, y);
		  	if (this.chart.trends[i])
		  		this.chart.ctx.fillText(this.chart.trends[i].opt.text0, lx, y);
			}
			this.chart.ctx.stroke();
		}
		//ray
		this.chart.ctx.lineWidth = 2;
		this.chart.ctx.strokeStyle = "black";
		this.chart.ctx.beginPath();
  	this.chart.ctx.moveTo(x1, this.chart.opt.gap.t + this.chart.csize.h - 1);
  	this.chart.ctx.lineTo(x1, this.chart.opt.gap.t + 1);
		this.chart.ctx.stroke();
		this.chart.ctx.restore();
	}
};
/**
 * trend.js
 */

//Trend declaration
JSGadget.Trend = function(chart, options) {
	if (chart instanceof JSGadget.Chart)
		this.chart = chart;
	else
		options = chart;
	this.opt = {
			color: null,
			xFld: "x", //0 for array
			yFld: "y", //1 for array
			width: 2
	};
	if (options)
		for (var key in options)
			switch (key) {
				case "data":
					this[key] = options[key];
					break;
				default:
					this.opt[key] = options[key];
			}
};

/**
 * atrend.js
 */

//ATrend declaration
JSGadget.ATrend = function(chart, options) {
	JSGadget.ATrend.superclass.constructor.apply(this, arguments);
};
JSGadget.Utils.extend(JSGadget.ATrend, JSGadget.Trend);
//ATrend implementation
JSGadget.ATrend.prototype.getMinMax = function(mm) {
	if (!mm)
		mm = {minX: null, maxX: null, minY: null, maxY: null};
  if (this.data) {
		for (var i = 0, l = this.data.length; i < l; ++i) {
		  if (mm.minX === null || this.data[i][this.opt.xFld] !== null &&
		  		this.data[i][this.opt.xFld] < mm.minX)
	  		mm.minX = this.data[i][this.opt.xFld];
		  if (mm.maxX === null || this.data[i][this.opt.xFld] !== null &&
		  		this.data[i][this.opt.xFld] > mm.maxX)
		  	mm.maxX = this.data[i][this.opt.xFld];
	  	if (mm.minY === null || this.data[i][this.opt.yFld] !== null &&
	  			this.data[i][this.opt.yFld] < mm.minY)
	  		mm.minY = this.data[i][this.opt.yFld];
		  if (mm.maxY === null || this.data[i][this.opt.yFld] !== null &&
		  		this.data[i][this.opt.yFld] > mm.maxY)
		  	mm.maxY = this.data[i][this.opt.yFld];
		}
	}
	return mm;
};
JSGadget.ATrend.prototype.draw = function() {
  if (this.data) {
  	var l = this.data.length;
  	if (l) {
    	this.chart.ctx.save();
    	this.chart.ctx.strokeStyle = this.opt.color;
    	this.chart.ctx.lineWidth = this.opt.width;
    	this.chart.ctx.lineJoin = "round";
    	this.chart.ctx.beginPath();
  		for (var i = 0, bf = true; i < l; ++i)
   			if (this.data[i][this.opt.yFld] !== null) {
  				if (bf) {
  					this.chart.ctx.moveTo(this.chart.bAxis.val2coord(this.data[i][this.opt.xFld]),
  							this.chart.lAxis.val2coord(this.data[i][this.opt.yFld]));
  					bf = false;
  				}
  				this.chart.ctx.lineTo(this.chart.bAxis.val2coord(this.data[i][this.opt.xFld]),
  						this.chart.lAxis.val2coord(this.data[i][this.opt.yFld]));
  			} else
  				bf = true;
  		this.chart.ctx.stroke();
  		this.chart.ctx.restore();
  	}
  }
};
/**
 * dtrend.js
 */

//DTrend declaration
JSGadget.DTrend = function(chart, options) {
	JSGadget.DTrend.superclass.constructor.apply(this, arguments);
	if (!this.opt.color)
		this.opt.color = "blue";
	if (!this.opt.text0)
		this.opt.text0 = "false";
	if (!this.opt.text1)
		this.opt.text1 = "true";
};
JSGadget.Utils.extend(JSGadget.DTrend, JSGadget.Trend);
//DTrend implementation
JSGadget.DTrend.prototype.getMinMax = function(mm) {
	if (!mm)
		mm = {minX: null, maxX: null, minY: 0, maxY: 0};
  if (this.data) {
		for (var i = 0, l = this.data.length; i < l; ++i) {
		  if (mm.minX === null || this.data[i][this.opt.xFld] !== null &&
		  		this.data[i][this.opt.xFld] < mm.minX)
	  		mm.minX = this.data[i][this.opt.xFld];
		  if (mm.maxX === null || this.data[i][this.opt.xFld] !== null &&
		  		this.data[i][this.opt.xFld] > mm.maxX)
		  	mm.maxX = this.data[i][this.opt.xFld];
		}
	}
	return mm;
};
JSGadget.DTrend.prototype.draw = function(idx) {
  if (this.data) {
  	var l = this.data.length;
  	if (l) {
    	this.chart.ctx.save();
    	this.chart.ctx.strokeStyle = this.opt.color;
    	this.chart.ctx.lineWidth = this.opt.width;
    	this.chart.ctx.lineJoin = "round";
    	this.chart.ctx.beginPath();
  		for (var i = 0, bf = true, v = null; i < l; ++i)
   			if (this.data[i][this.opt.yFld] !== null) {
  				if (bf) {
  					this.chart.ctx.moveTo(this.chart.bAxis.val2coord(this.data[i][this.opt.xFld]),
  							JSGadget.Utils.round2pix(this.chart.lAxis.val2coord(this.data[i][this.opt.yFld], idx),
  									this.opt.width));
  					bf = false;
  				} else if (this.data[i][this.opt.yFld] != v) {
    				this.chart.ctx.lineTo(this.chart.bAxis.val2coord(this.data[i][this.opt.xFld]),
    						JSGadget.Utils.round2pix(this.chart.lAxis.val2coord(v, idx), this.opt.width));
  				}
  				this.chart.ctx.lineTo(this.chart.bAxis.val2coord(this.data[i][this.opt.xFld]),
  						JSGadget.Utils.round2pix(this.chart.lAxis.val2coord(this.data[i][this.opt.yFld], idx),
									this.opt.width));
  				v = this.data[i][this.opt.yFld];
  			} else
  				bf = true;
  		this.chart.ctx.stroke();
  		this.chart.ctx.restore();
  	}
  }
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

