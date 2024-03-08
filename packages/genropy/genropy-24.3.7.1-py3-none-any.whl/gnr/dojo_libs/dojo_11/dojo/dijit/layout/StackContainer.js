/*
	Copyright (c) 2004-2008, The Dojo Foundation
	All Rights Reserved.

	Licensed under the Academic Free License version 2.1 or above OR the
	modified BSD license. For more information on Dojo licensing, see:

		http://dojotoolkit.org/book/dojo-book-0-9/introduction/licensing
*/


if(!dojo._hasResource["dijit.layout.StackContainer"]){
dojo._hasResource["dijit.layout.StackContainer"]=true;
dojo.provide("dijit.layout.StackContainer");
dojo.require("dijit._Templated");
dojo.require("dijit.layout._LayoutWidget");
dojo.require("dijit.form.Button");
dojo.require("dijit.Menu");
dojo.requireLocalization("dijit","common",null,"ar,ROOT,cs,da,de,el,es,fi,fr,he,hu,it,ja,ko,nb,nl,pl,pt,pt-pt,ru,sv,tr,zh,zh-tw");
dojo.declare("dijit.layout.StackContainer",dijit.layout._LayoutWidget,{doLayout:true,_started:false,postCreate:function(){
dijit.setWaiRole((this.containerNode||this.domNode),"tabpanel");
this.connect(this.domNode,"onkeypress",this._onKeyPress);
},startup:function(){
if(this._started){
return;
}
var _1=this.getChildren();
dojo.forEach(_1,this._setupChild,this);
dojo.some(_1,function(_2){
if(_2.selected){
this.selectedChildWidget=_2;
}
return _2.selected;
},this);
var _3=this.selectedChildWidget;
if(!_3&&_1[0]){
_3=this.selectedChildWidget=_1[0];
_3.selected=true;
}
if(_3){
this._showChild(_3);
}
dojo.publish(this.id+"-startup",[{children:_1,selected:_3}]);
this.inherited(arguments);
},_setupChild:function(_4){
_4.domNode.style.display="none";
_4.domNode.style.position="relative";
return _4;
},addChild:function(_5,_6){
dijit._Container.prototype.addChild.apply(this,arguments);
_5=this._setupChild(_5);
if(this._started){
this.layout();
dojo.publish(this.id+"-addChild",[_5,_6]);
if(!this.selectedChildWidget){
this.selectChild(_5);
}
}
},removeChild:function(_7){
dijit._Container.prototype.removeChild.apply(this,arguments);
if(this._beingDestroyed){
return;
}
if(this._started){
dojo.publish(this.id+"-removeChild",[_7]);
this.layout();
}
if(this.selectedChildWidget===_7){
this.selectedChildWidget=undefined;
if(this._started){
var _8=this.getChildren();
if(_8.length){
this.selectChild(_8[0]);
}
}
}
},selectChild:function(_9){
_9=dijit.byId(_9);
if(this.selectedChildWidget!=_9){
this._transition(_9,this.selectedChildWidget);
this.selectedChildWidget=_9;
dojo.publish(this.id+"-selectChild",[_9]);
}
},_transition:function(_a,_b){
if(_b){
this._hideChild(_b);
}
this._showChild(_a);
if(this.doLayout&&_a.resize){
_a.resize(this._containerContentBox||this._contentBox);
}
},_adjacent:function(_c){
var _d=this.getChildren();
var _e=dojo.indexOf(_d,this.selectedChildWidget);
_e+=_c?1:_d.length-1;
return _d[_e%_d.length];
},forward:function(){
this.selectChild(this._adjacent(true));
},back:function(){
this.selectChild(this._adjacent(false));
},_onKeyPress:function(e){
dojo.publish(this.id+"-containerKeyPress",[{e:e,page:this}]);
},layout:function(){
if(this.doLayout&&this.selectedChildWidget&&this.selectedChildWidget.resize){
this.selectedChildWidget.resize(this._contentBox);
}
},_showChild:function(_10){
var _11=this.getChildren();
_10.isFirstChild=(_10==_11[0]);
_10.isLastChild=(_10==_11[_11.length-1]);
_10.selected=true;
_10.domNode.style.display="";
if(_10._loadCheck){
_10._loadCheck();
}
if(_10.onShow){
_10.onShow();
}
},_hideChild:function(_12){
_12.selected=false;
_12.domNode.style.display="none";
if(_12.onHide){
_12.onHide();
}
},closeChild:function(_13){
var _14=_13.onClose(this,_13);
if(_14){
this.removeChild(_13);
_13.destroyRecursive();
}
},destroy:function(){
this._beingDestroyed=true;
this.inherited(arguments);
}});
dojo.declare("dijit.layout.StackController",[dijit._Widget,dijit._Templated,dijit._Container],{templateString:"<span wairole='tablist' dojoAttachEvent='onkeypress' class='dijitStackController'></span>",containerId:"",buttonWidget:"dijit.layout._StackButton",postCreate:function(){
dijit.setWaiRole(this.domNode,"tablist");
this.pane2button={};
this.pane2menu={};
this._subscriptions=[dojo.subscribe(this.containerId+"-startup",this,"onStartup"),dojo.subscribe(this.containerId+"-addChild",this,"onAddChild"),dojo.subscribe(this.containerId+"-removeChild",this,"onRemoveChild"),dojo.subscribe(this.containerId+"-selectChild",this,"onSelectChild"),dojo.subscribe(this.containerId+"-containerKeyPress",this,"onContainerKeyPress")];
},onStartup:function(_15){
dojo.forEach(_15.children,this.onAddChild,this);
this.onSelectChild(_15.selected);
},destroy:function(){
for(var _16 in this.pane2button){
this.onRemoveChild(_16);
}
dojo.forEach(this._subscriptions,dojo.unsubscribe);
this.inherited(arguments);
},onAddChild:function(_17,_18){
var _19=dojo.doc.createElement("span");
this.domNode.appendChild(_19);
var cls=dojo.getObject(this.buttonWidget);
var _1b=new cls({label:_17.title,closeButton:_17.closable},_19);
this.addChild(_1b,_18);
this.pane2button[_17]=_1b;
_17.controlButton=_1b;
dojo.connect(_1b,"onClick",dojo.hitch(this,"onButtonClick",_17));
if(_17.closable){
dojo.connect(_1b,"onClickCloseButton",dojo.hitch(this,"onCloseButtonClick",_17));
var _1c=dojo.i18n.getLocalization("dijit","common");
var _1d=new dijit.Menu({targetNodeIds:[_1b.id],id:_1b.id+"_Menu"});
var _1e=new dijit.MenuItem({label:_1c.itemClose});
dojo.connect(_1e,"onClick",dojo.hitch(this,"onCloseButtonClick",_17));
_1d.addChild(_1e);
this.pane2menu[_17]=_1d;
}
if(!this._currentChild){
_1b.focusNode.setAttribute("tabIndex","0");
this._currentChild=_17;
}
if(!this.isLeftToRight()&&dojo.isIE&&this._rectifyRtlTabList){
this._rectifyRtlTabList();
}
},onRemoveChild:function(_1f){
if(this._currentChild===_1f){
this._currentChild=null;
}
var _20=this.pane2button[_1f];
var _21=this.pane2menu[_1f];
if(_21){
_21.destroy();
}
if(_20){
_20.destroy();
}
this.pane2button[_1f]=null;
},onSelectChild:function(_22){
if(!_22){
return;
}
if(this._currentChild){
var _23=this.pane2button[this._currentChild];
_23.setAttribute("checked",false);
_23.focusNode.setAttribute("tabIndex","-1");
}
var _24=this.pane2button[_22];
_24.setAttribute("checked",true);
this._currentChild=_22;
_24.focusNode.setAttribute("tabIndex","0");
var _25=dijit.byId(this.containerId);
dijit.setWaiState(_25.containerNode||_25.domNode,"labelledby",_24.id);
},onButtonClick:function(_26){
var _27=dijit.byId(this.containerId);
_27.selectChild(_26);
},onCloseButtonClick:function(_28){
var _29=dijit.byId(this.containerId);
_29.closeChild(_28);
var b=this.pane2button[this._currentChild];
if(b){
dijit.focus(b.focusNode||b.domNode);
}
},adjacent:function(_2b){
if(!this.isLeftToRight()&&(!this.tabPosition||/top|bottom/.test(this.tabPosition))){
_2b=!_2b;
}
var _2c=this.getChildren();
var _2d=dojo.indexOf(_2c,this.pane2button[this._currentChild]);
var _2e=_2b?1:_2c.length-1;
return _2c[(_2d+_2e)%_2c.length];
},onkeypress:function(e){
if(this.disabled||e.altKey){
return;
}
var _30=null;
if(e.ctrlKey||!e._djpage){
var k=dojo.keys;
switch(e.keyCode){
case k.LEFT_ARROW:
case k.UP_ARROW:
if(!e._djpage){
_30=false;
}
break;
case k.PAGE_UP:
if(e.ctrlKey){
_30=false;
}
break;
case k.RIGHT_ARROW:
case k.DOWN_ARROW:
if(!e._djpage){
_30=true;
}
break;
case k.PAGE_DOWN:
if(e.ctrlKey){
_30=true;
}
break;
case k.DELETE:
if(this._currentChild.closable){
this.onCloseButtonClick(this._currentChild);
}
dojo.stopEvent(e);
break;
default:
if(e.ctrlKey){
if(e.keyCode==k.TAB){
this.adjacent(!e.shiftKey).onClick();
dojo.stopEvent(e);
}else{
if(e.keyChar=="w"){
if(this._currentChild.closable){
this.onCloseButtonClick(this._currentChild);
}
dojo.stopEvent(e);
}
}
}
}
if(_30!==null){
this.adjacent(_30).onClick();
dojo.stopEvent(e);
}
}
},onContainerKeyPress:function(_32){
_32.e._djpage=_32.page;
this.onkeypress(_32.e);
}});
dojo.declare("dijit.layout._StackButton",dijit.form.ToggleButton,{tabIndex:"-1",postCreate:function(evt){
dijit.setWaiRole((this.focusNode||this.domNode),"tab");
this.inherited(arguments);
},onClick:function(evt){
dijit.focus(this.focusNode);
},onClickCloseButton:function(evt){
evt.stopPropagation();
}});
dojo.extend(dijit._Widget,{title:"",selected:false,closable:false,onClose:function(){
return true;
}});
}
