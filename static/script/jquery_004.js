(function($){

	$.fn.milk_simpleSlide = function(user_params) {
		var _this = this;
		_this.item_selected = 0;
		_this.total_elements = 0;
		_this.timer = false;

		_this.params = $.extend ({
			"bt_prev":"",
			"bt_next":"",
			"step":50,
			"duration":400,
			"timer":0
		},user_params);



		_this.init = function () {
			_this.each(function () {
				_this.element = $(this);
			});
			_this.total_elements = _this.element.find("div").length;
			_this.setStyles();
			_this.setEvents();

			if ( _this.params.timer !=  0 ) {
				_this.playTimer();
			}
		};

		_this.setStyles = function (){
			_this.css({"white-space":"nowrap","overflow":"hidden","font-size":0});
		};

		_this.setEvents = function () {
			//alert("previous bouton =" + _this.params.bt_prev);
			_this.params.bt_prev.click(function(){
				if (_this.item_selected > 0 ) {
					_this.item_selected --;
					_this.moveScroll();
				}
			});

			_this.params.bt_prev.hover(
				function(){
					_this.stopTimer();
				},
				function() {
					_this.playTimer();
				}
			);

			_this.params.bt_next.hover(
				function(){
					_this.stopTimer();
				},
				function() {
					_this.playTimer();
				}
			);

			_this.params.bt_next.click(function(){
				//alert(_this.element.width());
				_this.nextSlide();
			});
		}

		_this.nextSlide = function () {
			var max_incremente = _this.total_elements - Math.round(_this.element.width()/_this.params.step);

				if (_this.item_selected < max_incremente ) {
					_this.item_selected ++;
				}else _this.item_selected  = 0;
				_this.moveScroll();
		};



		_this.moveScroll = function () {
			var pos_x = _this.item_selected *_this.params.step;
			_this.element.stop().animate({
	            scrollLeft:pos_x
        	},{duration:_this.params.duration,easing:"easeInOutSine"});
		}

		_this.playTimer = function () {
			_this.timer = setInterval(_this.nextSlide,_this.params.timer);
		}

		_this.stopTimer = function () {
			clearInterval(_this.timer);
		}

		_this.init();
    };

})(jQuery)