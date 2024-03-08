/*
	Copyright (c) 2004-2008, The Dojo Foundation
	All Rights Reserved.

	Licensed under the Academic Free License version 2.1 or above OR the
	modified BSD license. For more information on Dojo licensing, see:

		http://dojotoolkit.org/book/dojo-book-0-9/introduction/licensing
*/


if(!dojo._hasResource["dijit._Container"]){
dojo._hasResource["dijit._Container"]=true;
dojo.provide("dijit._Container");
dojo.declare("dijit._Contained",null,{getParent:function(){
for(var p=this.domNode.parentNode;p;p=p.parentNode){
var id=p.getAttribute&&p.getAttribute("widgetId");
if(id){
var _3=dijit.byId(id);
return _3.isContainer?_3:null;
}
}
return null;
},_getSibling:function(_4){
var _5=this.domNode;
do{
_5=_5[_4+"Sibling"];
}while(_5&&_5.nodeType!=1);
if(!_5){
return null;
}
var id=_5.getAttribute("widgetId");
return dijit.byId(id);
},getPreviousSibling:function(){
return this._getSibling("previous");
},getNextSibling:function(){
return this._getSibling("next");
}});
dojo.declare("dijit._Container",null,{isContainer:true,addChild:function(_7,_8){
if(_8===undefined){
_8="last";
}
var _9=this.containerNode||this.domNode;
if(_8&&typeof _8=="number"){
var _a=dojo.query("> [widgetid]",_9);
if(_a&&_a.length>=_8){
_9=_a[_8-1];
_8="after";
}
}
dojo.place(_7.domNode,_9,_8);
if(this._started&&!_7._started){
_7.startup();
}
},removeChild:function(_b){
var _c=_b.domNode;
_c.parentNode.removeChild(_c);
},_nextElement:function(_d){
do{
_d=_d.nextSibling;
}while(_d&&_d.nodeType!=1);
return _d;
},_firstElement:function(_e){
_e=_e.firstChild;
if(_e&&_e.nodeType!=1){
_e=this._nextElement(_e);
}
return _e;
},getChildren:function(){
return dojo.query("> [widgetId]",this.containerNode||this.domNode).map(dijit.byNode);
},hasChildren:function(){
var cn=this.containerNode||this.domNode;
return !!this._firstElement(cn);
},_getSiblingOfChild:function(_10,dir){
var _12=_10.domNode;
var _13=(dir>0?"nextSibling":"previousSibling");
do{
_12=_12[_13];
}while(_12&&(_12.nodeType!=1||!dijit.byNode(_12)));
return _12?dijit.byNode(_12):null;
}});
dojo.declare("dijit._KeyNavContainer",[dijit._Container],{_keyNavCodes:{},connectKeyNavHandlers:function(_14,_15){
var _16=this._keyNavCodes={};
var _17=dojo.hitch(this,this.focusPrev);
var _18=dojo.hitch(this,this.focusNext);
dojo.forEach(_14,function(_19){
_16[_19]=_17;
});
dojo.forEach(_15,function(_1a){
_16[_1a]=_18;
});
this.connect(this.domNode,"onkeypress","_onContainerKeypress");
this.connect(this.domNode,"onfocus","_onContainerFocus");
},startupKeyNavChildren:function(){
dojo.forEach(this.getChildren(),dojo.hitch(this,"_startupChild"));
},addChild:function(_1b,_1c){
dijit._KeyNavContainer.superclass.addChild.apply(this,arguments);
this._startupChild(_1b);
},focus:function(){
this.focusFirstChild();
},focusFirstChild:function(){
this.focusChild(this._getFirstFocusableChild());
},focusNext:function(){
if(this.focusedChild&&this.focusedChild.hasNextFocalNode&&this.focusedChild.hasNextFocalNode()){
this.focusedChild.focusNext();
return;
}
var _1d=this._getNextFocusableChild(this.focusedChild,1);
if(_1d.getFocalNodes){
this.focusChild(_1d,_1d.getFocalNodes()[0]);
}else{
this.focusChild(_1d);
}
},focusPrev:function(){
if(this.focusedChild&&this.focusedChild.hasPrevFocalNode&&this.focusedChild.hasPrevFocalNode()){
this.focusedChild.focusPrev();
return;
}
var _1e=this._getNextFocusableChild(this.focusedChild,-1);
if(_1e.getFocalNodes){
var _1f=_1e.getFocalNodes();
this.focusChild(_1e,_1f[_1f.length-1]);
}else{
this.focusChild(_1e);
}
},focusChild:function(_20,_21){
if(_20){
if(this.focusedChild&&_20!==this.focusedChild){
this._onChildBlur(this.focusedChild);
}
this.focusedChild=_20;
if(_21&&_20.focusFocalNode){
_20.focusFocalNode(_21);
}else{
_20.focus();
}
}
},_startupChild:function(_22){
if(_22.getFocalNodes){
dojo.forEach(_22.getFocalNodes(),function(_23){
dojo.attr(_23,"tabindex",-1);
this._connectNode(_23);
},this);
}else{
var _24=_22.focusNode||_22.domNode;
if(_22.isFocusable()){
dojo.attr(_24,"tabindex",-1);
}
this._connectNode(_24);
}
},_connectNode:function(_25){
this.connect(_25,"onfocus","_onNodeFocus");
this.connect(_25,"onblur","_onNodeBlur");
},_onContainerFocus:function(evt){
if(evt.target===this.domNode){
this.focusFirstChild();
}
},_onContainerKeypress:function(evt){
if(evt.ctrlKey||evt.altKey){
return;
}
var _28=this._keyNavCodes[evt.keyCode];
if(_28){
_28();
dojo.stopEvent(evt);
}
},_onNodeFocus:function(evt){
dojo.attr(this.domNode,"tabindex",-1);
var _2a=dijit.getEnclosingWidget(evt.target);
if(_2a&&_2a.isFocusable()){
this.focusedChild=_2a;
}
dojo.stopEvent(evt);
},_onNodeBlur:function(evt){
if(this.tabIndex){
dojo.attr(this.domNode,"tabindex",this.tabIndex);
}
dojo.stopEvent(evt);
},_onChildBlur:function(_2c){
},_getFirstFocusableChild:function(){
return this._getNextFocusableChild(null,1);
},_getNextFocusableChild:function(_2d,dir){
if(_2d){
_2d=this._getSiblingOfChild(_2d,dir);
}
var _2f=this.getChildren();
for(var i=0;i<_2f.length;i++){
if(!_2d){
_2d=_2f[(dir>0)?0:(_2f.length-1)];
}
if(_2d.isFocusable()){
return _2d;
}
_2d=this._getSiblingOfChild(_2d,dir);
}
return null;
}});
}
