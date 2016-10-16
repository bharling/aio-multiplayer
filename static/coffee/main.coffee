class Renderable
	constructor: (@x, @y, @color='#ff0000') ->
		canvas = document.getElementById 'stage'
		@ctx = canvas.getContext '2d'

	draw: ->
		@ctx.fillStyle = @color
		@ctx.fillRect @x-3, @y-3, 6, 6






class PlayerInput
	constructor: () ->
		@sprite = new Renderable(10, 10)
		@connected = false
		@setupSocket()
		@setupListeners()

	log: (message) ->
		control = $('#log')
		control.html(control.html() + message + '<br/>')
		control.scrollTop(control.scrollTop() + 1000)


	setupSocket: ->
		@conn = new SockJS("http://#{window.location.host}/sockjs/", ['websocket'], {debug:true})
		@log('Connecting')

		@conn.onopen = () =>
			@connected = true
			@log('Connected')


		@conn.onmessage = (e) =>
			@log "Received #{e.data}"

		@conn.onclose = =>
			@log "Disconnected"
			@conn = null



	setupListeners: ->
		@keysDown = []
		document.addEventListener 'keydown', (e) =>
			if e.keyCode not in @keysDown
				@keysDown.push(e.keyCode)
				@sendKeys()
			false

		document.addEventListener 'keyup', (e) =>
			ind = @keysDown.indexOf e.keyCode
			if ind > -1
				@keysDown.splice ind, 1
				@sendKeys()
			false

	sendKeys: ->
		keys = "m#{@keysDown.join ':'}"
		@conn.send keys

	update: (timestamp) ->
		@sprite.draw()



exports = exports ? this

exports.PlayerInput = PlayerInput