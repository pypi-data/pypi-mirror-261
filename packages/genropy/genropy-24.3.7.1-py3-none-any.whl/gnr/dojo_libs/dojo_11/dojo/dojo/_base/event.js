/*
	Copyright (c) 2004-2008, The Dojo Foundation
	All Rights Reserved.

	Licensed under the Academic Free License version 2.1 or above OR the
	modified BSD license. For more information on Dojo licensing, see:

		http://dojotoolkit.org/book/dojo-book-0-9/introduction/licensing
*/


if(!dojo._hasResource["dojo._base.event"]){
dojo._hasResource["dojo._base.event"]=true;
dojo.provide("dojo._base.event");
dojo.require("dojo._base.connect");
(function(){
var _1=(dojo._event_listener={add:function(_2,_3,fp){
if(!_2){
return;
}
_3=_1._normalizeEventName(_3);
fp=_1._fixCallback(_3,fp);
var _5=_3;
if(!dojo.isIE&&(_3=="mouseenter"||_3=="mouseleave")){
var _6=fp;
_3=(_3=="mouseenter")?"mouseover":"mouseout";
fp=function(e){
if(!dojo.isDescendant(e.relatedTarget,_2)){
return _6.call(this,e);
}
};
}
_2.addEventListener(_3,fp,false);
return fp;
},remove:function(_8,_9,_a){
if(_8){
_8.removeEventListener(_1._normalizeEventName(_9),_a,false);
}
},_normalizeEventName:function(_b){
return _b.slice(0,2)=="on"?_b.slice(2):_b;
},_fixCallback:function(_c,fp){
return _c!="keypress"?fp:function(e){
return fp.call(this,_1._fixEvent(e,this));
};
},_fixEvent:function(_f,_10){
switch(_f.type){
case "keypress":
_1._setKeyChar(_f);
break;
}
return _f;
},_setKeyChar:function(evt){
evt.keyChar=evt.charCode?String.fromCharCode(evt.charCode):"";
}});
dojo.fixEvent=function(evt,_13){
return _1._fixEvent(evt,_13);
};
dojo.stopEvent=function(evt){
evt.preventDefault();
evt.stopPropagation();
};
var _15=dojo._listener;
dojo._connect=function(obj,_17,_18,_19,_1a){
var _1b=obj&&(obj.nodeType||obj.attachEvent||obj.addEventListener);
var lid=!_1b?0:(!_1a?1:2),l=[dojo._listener,_1,_15][lid];
var h=l.add(obj,_17,dojo.hitch(_18,_19));
return [obj,_17,h,lid];
};
dojo._disconnect=function(obj,_20,_21,_22){
([dojo._listener,_1,_15][_22]).remove(obj,_20,_21);
};
dojo.keys={BACKSPACE:8,TAB:9,CLEAR:12,ENTER:13,SHIFT:16,CTRL:17,ALT:18,PAUSE:19,CAPS_LOCK:20,ESCAPE:27,SPACE:32,PAGE_UP:33,PAGE_DOWN:34,END:35,HOME:36,LEFT_ARROW:37,UP_ARROW:38,RIGHT_ARROW:39,DOWN_ARROW:40,INSERT:45,DELETE:46,HELP:47,LEFT_WINDOW:91,RIGHT_WINDOW:92,SELECT:93,NUMPAD_0:96,NUMPAD_1:97,NUMPAD_2:98,NUMPAD_3:99,NUMPAD_4:100,NUMPAD_5:101,NUMPAD_6:102,NUMPAD_7:103,NUMPAD_8:104,NUMPAD_9:105,NUMPAD_MULTIPLY:106,NUMPAD_PLUS:107,NUMPAD_ENTER:108,NUMPAD_MINUS:109,NUMPAD_PERIOD:110,NUMPAD_DIVIDE:111,F1:112,F2:113,F3:114,F4:115,F5:116,F6:117,F7:118,F8:119,F9:120,F10:121,F11:122,F12:123,F13:124,F14:125,F15:126,NUM_LOCK:144,SCROLL_LOCK:145};
if(dojo.isIE){
var _23=function(e,_25){
try{
return (e.keyCode=_25);
}
catch(e){
return 0;
}
};
var iel=dojo._listener;
if(!dojo.config._allow_leaks){
_15=iel=dojo._ie_listener={handlers:[],add:function(_27,_28,_29){
_27=_27||dojo.global;
var f=_27[_28];
if(!f||!f._listeners){
var d=dojo._getIeDispatcher();
d.target=f&&(ieh.push(f)-1);
d._listeners=[];
f=_27[_28]=d;
}
return f._listeners.push(ieh.push(_29)-1);
},remove:function(_2d,_2e,_2f){
var f=(_2d||dojo.global)[_2e],l=f&&f._listeners;
if(f&&l&&_2f--){
delete ieh[l[_2f]];
delete l[_2f];
}
}};
var ieh=iel.handlers;
}
dojo.mixin(_1,{add:function(_32,_33,fp){
if(!_32){
return;
}
_33=_1._normalizeEventName(_33);
if(_33=="onkeypress"){
var kd=_32.onkeydown;
if(!kd||!kd._listeners||!kd._stealthKeydownHandle){
var h=_1.add(_32,"onkeydown",_1._stealthKeyDown);
kd=_32.onkeydown;
kd._stealthKeydownHandle=h;
kd._stealthKeydownRefs=1;
}else{
kd._stealthKeydownRefs++;
}
}
return iel.add(_32,_33,_1._fixCallback(fp));
},remove:function(_37,_38,_39){
_38=_1._normalizeEventName(_38);
iel.remove(_37,_38,_39);
if(_38=="onkeypress"){
var kd=_37.onkeydown;
if(--kd._stealthKeydownRefs<=0){
iel.remove(_37,"onkeydown",kd._stealthKeydownHandle);
delete kd._stealthKeydownHandle;
}
}
},_normalizeEventName:function(_3b){
return _3b.slice(0,2)!="on"?"on"+_3b:_3b;
},_nop:function(){
},_fixEvent:function(evt,_3d){
if(!evt){
var w=_3d&&(_3d.ownerDocument||_3d.document||_3d).parentWindow||window;
evt=w.event;
}
if(!evt){
return (evt);
}
evt.target=evt.srcElement;
evt.currentTarget=(_3d||evt.srcElement);
evt.layerX=evt.offsetX;
evt.layerY=evt.offsetY;
var se=evt.srcElement,doc=(se&&se.ownerDocument)||document;
var _41=((dojo.isIE<6)||(doc["compatMode"]=="BackCompat"))?doc.body:doc.documentElement;
var _42=dojo._getIeDocumentElementOffset();
evt.pageX=evt.clientX+dojo._fixIeBiDiScrollLeft(_41.scrollLeft||0)-_42.x;
evt.pageY=evt.clientY+(_41.scrollTop||0)-_42.y;
if(evt.type=="mouseover"){
evt.relatedTarget=evt.fromElement;
}
if(evt.type=="mouseout"){
evt.relatedTarget=evt.toElement;
}
evt.stopPropagation=_1._stopPropagation;
evt.preventDefault=_1._preventDefault;
return _1._fixKeys(evt);
},_fixKeys:function(evt){
switch(evt.type){
case "keypress":
var c=("charCode" in evt?evt.charCode:evt.keyCode);
if(c==10){
c=0;
evt.keyCode=13;
}else{
if(c==13||c==27){
c=0;
}else{
if(c==3){
c=99;
}
}
}
evt.charCode=c;
_1._setKeyChar(evt);
break;
}
return evt;
},_punctMap:{106:42,111:47,186:59,187:43,188:44,189:45,190:46,191:47,192:96,219:91,220:92,221:93,222:39},_stealthKeyDown:function(evt){
var kp=evt.currentTarget.onkeypress;
if(!kp||!kp._listeners){
return;
}
var k=evt.keyCode;
var _48=(k!=13)&&(k!=32)&&(k!=27)&&(k<48||k>90)&&(k<96||k>111)&&(k<186||k>192)&&(k<219||k>222);
if(_48||evt.ctrlKey){
var c=_48?0:k;
if(evt.ctrlKey){
if(k==3||k==13){
return;
}else{
if(c>95&&c<106){
c-=48;
}else{
if((!evt.shiftKey)&&(c>=65&&c<=90)){
c+=32;
}else{
c=_1._punctMap[c]||c;
}
}
}
}
var _4a=_1._synthesizeEvent(evt,{type:"keypress",faux:true,charCode:c});
kp.call(evt.currentTarget,_4a);
evt.cancelBubble=_4a.cancelBubble;
evt.returnValue=_4a.returnValue;
_23(evt,_4a.keyCode);
}
},_stopPropagation:function(){
this.cancelBubble=true;
},_preventDefault:function(){
this.bubbledKeyCode=this.keyCode;
if(this.ctrlKey){
_23(this,0);
}
this.returnValue=false;
}});
dojo.stopEvent=function(evt){
evt=evt||window.event;
_1._stopPropagation.call(evt);
_1._preventDefault.call(evt);
};
}
_1._synthesizeEvent=function(evt,_4d){
var _4e=dojo.mixin({},evt,_4d);
_1._setKeyChar(_4e);
_4e.preventDefault=function(){
evt.preventDefault();
};
_4e.stopPropagation=function(){
evt.stopPropagation();
};
return _4e;
};
if(dojo.isOpera){
dojo.mixin(_1,{_fixEvent:function(evt,_50){
switch(evt.type){
case "keypress":
var c=evt.which;
if(c==3){
c=99;
}
c=((c<41)&&(!evt.shiftKey)?0:c);
if((evt.ctrlKey)&&(!evt.shiftKey)&&(c>=65)&&(c<=90)){
c+=32;
}
return _1._synthesizeEvent(evt,{charCode:c});
}
return evt;
}});
}
if(dojo.isSafari){
dojo.mixin(_1,{_fixEvent:function(evt,_53){
switch(evt.type){
case "keypress":
var c=evt.charCode,s=evt.shiftKey,k=evt.keyCode;
k=k||_57[evt.keyIdentifier]||0;
if(evt.keyIdentifier=="Enter"){
c=0;
}else{
if((evt.ctrlKey)&&(c>0)&&(c<27)){
c+=96;
}else{
if(c==dojo.keys.SHIFT_TAB){
c=dojo.keys.TAB;
s=true;
}else{
c=(c>=32&&c<63232?c:0);
}
}
}
return _1._synthesizeEvent(evt,{charCode:c,shiftKey:s,keyCode:k});
}
return evt;
}});
dojo.mixin(dojo.keys,{SHIFT_TAB:25,UP_ARROW:63232,DOWN_ARROW:63233,LEFT_ARROW:63234,RIGHT_ARROW:63235,F1:63236,F2:63237,F3:63238,F4:63239,F5:63240,F6:63241,F7:63242,F8:63243,F9:63244,F10:63245,F11:63246,F12:63247,PAUSE:63250,DELETE:63272,HOME:63273,END:63275,PAGE_UP:63276,PAGE_DOWN:63277,INSERT:63302,PRINT_SCREEN:63248,SCROLL_LOCK:63249,NUM_LOCK:63289});
var dk=dojo.keys,_57={"Up":dk.UP_ARROW,"Down":dk.DOWN_ARROW,"Left":dk.LEFT_ARROW,"Right":dk.RIGHT_ARROW,"PageUp":dk.PAGE_UP,"PageDown":dk.PAGE_DOWN};
}
})();
if(dojo.isIE){
dojo._ieDispatcher=function(_59,_5a){
var ap=Array.prototype,h=dojo._ie_listener.handlers,c=_59.callee,ls=c._listeners,t=h[c.target];
var r=t&&t.apply(_5a,_59);
for(var i in ls){
if(!(i in ap)){
h[ls[i]].apply(_5a,_59);
}
}
return r;
};
dojo._getIeDispatcher=function(){
return new Function(dojo._scopeName+"._ieDispatcher(arguments, this)");
};
dojo._event_listener._fixCallback=function(fp){
var f=dojo._event_listener._fixEvent;
return function(e){
return fp.call(this,f(e,this));
};
};
}
}
