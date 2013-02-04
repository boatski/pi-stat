function drag(id) {

    this.id = id;

}

drag.prototype = {
 
    init:function() {

        this.elem = document.getElementById(this.id);
		
        this.elem.onmousedown = this._mouseDown.bind(this);
			 
	},

    _mouseDown: function(e) {

        e = e || window.event;

        this.elem.onselectstart=function(){
return false};

        this._event_docMouseMove = this._docMouseMove.bind(this);
		
		this._event_docMouseUp = this._docMouseUp.bind(this);
	
			
        if (this.onstart) this.onstart();

        this.x = e.clientX||e.PageX;

        this.y = e.clientY||e.PageY;

		
        this.left = parseInt(this.elem.style.left);

        this.top = parseInt(this.elem.style.top);

        
        addEvent(document, 'mousemove', this._event_docMouseMove);
	
        addEvent(document, 'mouseup', this._event_docMouseUp);

        return false;
	
    },
    
    _docMouseMove: function(e) {
    
        this.setValuesClick(e);
	   
        if (this.ondrag) this.ondrag();

    },

    _docMouseUp: function(e) {

        removeEvent(document, 'mousemove', this._event_docMouseMove);

        if (this.onstop) this.onstop();

        removeEvent(document, 'mouseup', this._event_docMouseUp);

                    
    },
    
    setValuesClick: function(e){
 
        this.mouseX = e.clientX||e.PageX;

        this.mouseY = e.clientY||e.pageY;

        this.X = this.left+ this.mouseX - this.x;
	
        this.Y = this.top + this.mouseY - this.y;

        this.elem.style.left = this.X+"px";

        this.elem.style.top = this.Y +"px";
    	
    }

}