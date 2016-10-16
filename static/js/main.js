(function() {
  var PlayerInput, Renderable, exports,
    indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; };

  Renderable = (function() {
    function Renderable(x, y, color) {
      var canvas;
      this.x = x;
      this.y = y;
      this.color = color != null ? color : '#ff0000';
      canvas = document.getElementById('stage');
      this.ctx = canvas.getContext('2d');
    }

    Renderable.prototype.draw = function() {
      this.ctx.fillStyle = this.color;
      return this.ctx.fillRect(this.x - 3, this.y - 3, 6, 6);
    };

    return Renderable;

  })();

  PlayerInput = (function() {
    function PlayerInput() {
      this.sprite = new Renderable(10, 10);
      this.connected = false;
      this.setupSocket();
      this.setupListeners();
    }

    PlayerInput.prototype.log = function(message) {
      var control;
      control = $('#log');
      control.html(control.html() + message + '<br/>');
      return control.scrollTop(control.scrollTop() + 1000);
    };

    PlayerInput.prototype.setupSocket = function() {
      this.conn = new SockJS("http://" + window.location.host + "/sockjs/", ['websocket'], {
        debug: true
      });
      this.log('Connecting');
      this.conn.onopen = (function(_this) {
        return function() {
          _this.connected = true;
          return _this.log('Connected');
        };
      })(this);
      this.conn.onmessage = (function(_this) {
        return function(e) {
          return _this.log("Received " + e.data);
        };
      })(this);
      return this.conn.onclose = (function(_this) {
        return function() {
          _this.log("Disconnected");
          return _this.conn = null;
        };
      })(this);
    };

    PlayerInput.prototype.setupListeners = function() {
      this.keysDown = [];
      document.addEventListener('keydown', (function(_this) {
        return function(e) {
          var ref;
          if (ref = e.keyCode, indexOf.call(_this.keysDown, ref) < 0) {
            _this.keysDown.push(e.keyCode);
            _this.sendKeys();
          }
          return false;
        };
      })(this));
      return document.addEventListener('keyup', (function(_this) {
        return function(e) {
          var ind;
          ind = _this.keysDown.indexOf(e.keyCode);
          if (ind > -1) {
            _this.keysDown.splice(ind, 1);
            _this.sendKeys();
          }
          return false;
        };
      })(this));
    };

    PlayerInput.prototype.sendKeys = function() {
      var keys;
      keys = "m" + (this.keysDown.join(':'));
      return this.conn.send(keys);
    };

    PlayerInput.prototype.update = function(timestamp) {
      return this.sprite.draw();
    };

    return PlayerInput;

  })();

  exports = exports != null ? exports : this;

  exports.PlayerInput = PlayerInput;

}).call(this);
