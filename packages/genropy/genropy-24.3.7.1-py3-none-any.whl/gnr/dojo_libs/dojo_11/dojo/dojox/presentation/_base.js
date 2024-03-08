/*
	Copyright (c) 2004-2008, The Dojo Foundation
	All Rights Reserved.

	Licensed under the Academic Free License version 2.1 or above OR the
	modified BSD license. For more information on Dojo licensing, see:

		http://dojotoolkit.org/book/dojo-book-0-9/introduction/licensing
*/


if(!dojo._hasResource["dojox.presentation._base"]){
dojo._hasResource["dojox.presentation._base"]=true;
dojo.provide("dojox.presentation._base");
dojo.experimental("dojox.presentation");
dojo.require("dijit._Widget");
dojo.require("dijit._Container");
dojo.require("dijit._Templated");
dojo.require("dijit.layout.StackContainer");
dojo.require("dijit.layout.ContentPane");
dojo.require("dojo.fx");
dojo.declare("dojox.presentation.Deck",[dijit.layout.StackContainer,dijit._Templated],{fullScreen:true,useNav:true,navDuration:250,noClick:false,setHash:true,templateString:null,templateString:"<div class=\"dojoShow\" dojoAttachPoint=\"showHolder\">\n\t<div class=\"dojoShowNav\" dojoAttachPoint=\"showNav\" dojoAttachEvent=\"onmouseover: _showNav, onmouseout: _hideNav\">\n\t<div class=\"dojoShowNavToggler\" dojoAttachPoint=\"showToggler\">\n\t\t<img dojoAttachPoint=\"prevNode\" src=\"${prevIcon}\" dojoAttachEvent=\"onclick:previousSlide\">\n\t\t<select dojoAttachEvent=\"onchange:_onEvent\" dojoAttachPoint=\"select\">\n\t\t\t<option dojoAttachPoint=\"_option\">Title</option>\n\t\t</select>\n\t\t<img dojoAttachPoint=\"nextNode\" src=\"${nextIcon}\" dojoAttachEvent=\"onclick:nextSlide\">\n\t</div>\n\t</div>\n\t<div dojoAttachPoint=\"containerNode\"></div>\n</div>\n",nextIcon:dojo.moduleUrl("dojox.presentation","resources/icons/next.png"),prevIcon:dojo.moduleUrl("dojox.presentation","resources/icons/prev.png"),_navOpacMin:0,_navOpacMax:0.85,_slideIndex:0,_slides:[],_navShowing:true,_inNav:false,startup:function(){
this.inherited(arguments);
if(this.useNav){
this._hideNav();
}else{
this.showNav.style.display="none";
}
this.connect(document,"onclick","_onEvent");
this.connect(document,"onkeypress","_onEvent");
this.connect(window,"onresize","_resizeWindow");
this._resizeWindow();
this._updateSlides();
this._readHash();
this._setHash();
},moveTo:function(_1){
var _2=_1-1;
if(_2<0){
_2=0;
}
if(_2>this._slides.length-1){
_2=this._slides.length-1;
}
this._gotoSlide(_2);
},onMove:function(_3){
},nextSlide:function(_4){
if(!this.selectedChildWidget.isLastChild){
this._gotoSlide(this._slideIndex+1);
}
if(_4){
_4.stopPropagation();
}
},previousSlide:function(_5){
if(!this.selectedChildWidget.isFirstChild){
this._gotoSlide(this._slideIndex-1);
}else{
this.selectedChildWidget._reset();
}
if(_5){
_5.stopPropagation();
}
},getHash:function(id){
return this.id+"_SlideNo_"+id;
},_hideNav:function(_7){
if(this._navAnim){
this._navAnim.stop();
}
this._navAnim=dojo.animateProperty({node:this.showNav,duration:this.navDuration,properties:{opacity:{end:this._navOpacMin}}}).play();
},_showNav:function(_8){
if(this._navAnim){
this._navAnim.stop();
}
this._navAnim=dojo.animateProperty({node:this.showNav,duration:this.navDuration,properties:{opacity:{end:this._navOpacMax}}}).play();
},_handleNav:function(_9){
_9.stopPropagation();
},_updateSlides:function(){
this._slides=this.getChildren();
if(this.useNav){
var i=0;
dojo.forEach(this._slides,dojo.hitch(this,function(_b){
i++;
var _c=this._option.cloneNode(true);
_c.text=_b.title+" ("+i+") ";
this._option.parentNode.insertBefore(_c,this._option);
}));
if(this._option.parentNode){
this._option.parentNode.removeChild(this._option);
}
}
},_onEvent:function(_d){
var _e=_d.target;
var _f=_d.type;
if(_f=="click"||_f=="change"){
if(_e.index&&_e.parentNode==this.select){
this._gotoSlide(_e.index);
}else{
if(_e==this.select){
this._gotoSlide(_e.selectedIndex);
}else{
if(this.noClick||this.selectedChildWidget.noClick||this._isUnclickable(_d)){
return;
}
this.selectedChildWidget._nextAction(_d);
}
}
}else{
if(_f=="keydown"||_f=="keypress"){
var key=(_d.charCode==dojo.keys.SPACE?dojo.keys.SPACE:_d.keyCode);
switch(key){
case dojo.keys.DELETE:
case dojo.keys.BACKSPACE:
case dojo.keys.LEFT_ARROW:
case dojo.keys.UP_ARROW:
case dojo.keys.PAGE_UP:
case 80:
this.previousSlide(_d);
break;
case dojo.keys.ENTER:
case dojo.keys.SPACE:
case dojo.keys.RIGHT_ARROW:
case dojo.keys.DOWN_ARROW:
case dojo.keys.PAGE_DOWN:
case 78:
this.selectedChildWidget._nextAction(_d);
break;
case dojo.keys.HOME:
this._gotoSlide(0);
}
}
}
this._resizeWindow();
_d.stopPropagation();
},_gotoSlide:function(_11){
this.selectChild(this._slides[_11]);
this.selectedChildWidget._reset();
this._slideIndex=_11;
if(this.useNav){
this.select.selectedIndex=_11;
}
if(this.setHash){
this._setHash();
}
this.onMove(this._slideIndex+1);
},_isUnclickable:function(evt){
var _13=evt.target.nodeName.toLowerCase();
switch(_13){
case "a":
case "input":
case "textarea":
return true;
break;
}
return false;
},_readHash:function(){
var th=window.location.hash;
if(th.length&&this.setHash){
var _15=(""+window.location).split(this.getHash(""));
if(_15.length>1){
this._gotoSlide(parseInt(_15[1])-1);
}
}
},_setHash:function(){
if(this.setHash){
var _16=this._slideIndex+1;
window.location.href="#"+this.getHash(_16);
}
},_resizeWindow:function(evt){
dojo.body().style.height="auto";
var wh=dijit.getViewport();
var h=Math.max(document.documentElement.scrollHeight||dojo.body().scrollHeight,wh.h);
var w=wh.w;
this.selectedChildWidget.domNode.style.height=h+"px";
this.selectedChildWidget.domNode.style.width=w+"px";
},_transition:function(_1b,_1c){
var _1d=[];
if(_1c){
this._hideChild(_1c);
}
if(_1b){
this._showChild(_1b);
_1b._reset();
}
}});
dojo.declare("dojox.presentation.Slide",[dijit.layout.ContentPane,dijit._Contained,dijit._Container,dijit._Templated],{templateString:"<div dojoAttachPoint=\"showSlide\" class=\"dojoShowPrint dojoShowSlide\">\n\t<h1 class=\"showTitle\" dojoAttachPoint=\"slideTitle\"><span class=\"dojoShowSlideTitle\" dojoAttachPoint=\"slideTitleText\">${title}</span></h1>\n\t<div class=\"dojoShowBody\" dojoAttachPoint=\"containerNode\"></div>\n</div>\n",title:"",refreshOnShow:true,preLoad:false,doLayout:true,parseContent:true,noClick:false,_parts:[],_actions:[],_actionIndex:0,_runningDelay:false,startup:function(){
this.inherited(arguments);
this.slideTitleText.innerHTML=this.title;
var _1e=this.getChildren();
this._actions=[];
dojo.forEach(_1e,function(_1f){
var _20=_1f.declaredClass.toLowerCase();
switch(_20){
case "dojox.presentation.part":
this._parts.push(_1f);
break;
case "dojox.presentation.action":
this._actions.push(_1f);
break;
}
},this);
},_nextAction:function(evt){
var _22=this._actions[this._actionIndex]||0;
if(_22){
if(_22.on=="delay"){
this._runningDelay=setTimeout(dojo.hitch(_22,"_runAction"),_22.delay);
console.debug("started delay action",this._runningDelay);
}else{
_22._runAction();
}
var _23=this._getNextAction();
this._actionIndex++;
if(_23.on=="delay"){
console.debug("started delay action",this._runningDelay);
setTimeout(dojo.hitch(_23,"_runAction"),_23.delay);
}
}else{
this.getParent().nextSlide(evt);
}
},_getNextAction:function(){
return this._actions[this._actionIndex+1]||0;
},_reset:function(){
this._actionIndex=[0];
dojo.forEach(this._parts,function(_24){
_24._reset();
},this);
}});
dojo.declare("dojox.presentation.Part",[dijit._Widget,dijit._Contained],{as:"",startVisible:false,_isShowing:false,postCreate:function(){
this._reset();
},_reset:function(){
this._isShowing=!this.startVisible;
this._quickToggle();
},_quickToggle:function(){
if(this._isShowing){
dojo.style(this.domNode,"display","none");
dojo.style(this.domNode,"visibility","hidden");
dojo.style(this.domNode,"opacity",0);
}else{
dojo.style(this.domNode,"display","");
dojo.style(this.domNode,"visibility","visible");
dojo.style(this.domNode,"opacity",1);
}
this._isShowing=!this._isShowing;
}});
dojo.declare("dojox.presentation.Action",[dijit._Widget,dijit._Contained],{on:"click",forSlide:"",toggle:"fade",delay:0,duration:1000,_attached:[],_nullAnim:false,_runAction:function(){
var _25=[];
dojo.forEach(this._attached,function(_26){
var dir=(_26._isShowing)?"Out":"In";
var _28=dojo.fadeIn({node:_26.domNode,duration:this.duration,beforeBegin:dojo.hitch(_26,"_quickToggle")});
_25.push(_28);
},this);
var _29=dojo.fx.combine(_25);
if(_29){
_29.play();
}
},_getSiblingsByType:function(_2a){
var _2b=dojo.filter(this.getParent().getChildren(),function(_2c){
return _2c.declaredClass==_2a;
});
return _2b;
},postCreate:function(){
this.inherited(arguments);
dojo.style(this.domNode,"display","none");
var _2d=this._getSiblingsByType("dojox.presentation.Part");
this._attached=[];
dojo.forEach(_2d,function(_2e){
if(this.forSlide==_2e.as){
this._attached.push(_2e);
}
},this);
}});
}
