/*
	Copyright (c) 2004-2008, The Dojo Foundation
	All Rights Reserved.

	Licensed under the Academic Free License version 2.1 or above OR the
	modified BSD license. For more information on Dojo licensing, see:

		http://dojotoolkit.org/book/dojo-book-0-9/introduction/licensing
*/


if(!dojo._hasResource["dojox.image.MagnifierLite"]){dojo._hasResource["dojox.image.MagnifierLite"]=true;dojo.provide("dojox.image.MagnifierLite");dojo.experimental("dojox.image.MagnifierLite");dojo.require("dijit._Widget");dojo.declare("dojox.image.MagnifierLite",[dijit._Widget],{glassSize:125,scale:6,postCreate:function(){this.inherited(arguments);this._adjustScale();this._createGlass();this.connect(this.domNode,"onmouseenter","_showGlass");this.connect(this.glassNode,"onmousemove","_placeGlass");this.connect(this.img,"onmouseout","_hideGlass");this.connect(window,"onresize","_adjustScale");},_createGlass:function(){this.glassNode=dojo.doc.createElement("div");this.surfaceNode=this.glassNode.appendChild(dojo.doc.createElement("div"));dojo.addClass(this.glassNode,"glassNode");dojo.body().appendChild(this.glassNode);with(this.glassNode.style){height=this.glassSize+"px";width=this.glassSize+"px";}this.img=dojo.doc.createElement("img");this.glassNode.appendChild(this.img);this.img.src=this.domNode.src;with(this.img.style){position="relative";top=0;left=0;width=this._zoomSize.w+"px";height=this._zoomSize.h+"px";}},_adjustScale:function(){this.offset=dojo.coords(this.domNode,true);this._imageSize={w:this.offset.w,h:this.offset.h};this._zoomSize={w:this._imageSize.w*this.scale,h:this._imageSize.h*this.scale};},_showGlass:function(e){this._placeGlass(e);with(this.glassNode.style){visibility="visible";display="";}},_hideGlass:function(e){this.glassNode.style.visibility="hidden";this.glassNode.style.display="none";},_placeGlass:function(e){this._setImage(e);var t=Math.floor(e.pageY-(this.glassSize/2));var l=Math.floor(e.pageX-(this.glassSize/2));dojo.style(this.glassNode,"top",t);dojo.style(this.glassNode,"left",l);},_setImage:function(e){var _7=(e.pageX-this.offset.l)/this.offset.w;var _8=(e.pageY-this.offset.t)/this.offset.h;var x=(this._zoomSize.w*_7*-1)+(this.glassSize*_7);var y=(this._zoomSize.h*_8*-1)+(this.glassSize*_8);with(this.img.style){top=y+"px";left=x+"px";}}});}