/*
	Copyright (c) 2004-2008, The Dojo Foundation
	All Rights Reserved.

	Licensed under the Academic Free License version 2.1 or above OR the
	modified BSD license. For more information on Dojo licensing, see:

		http://dojotoolkit.org/book/dojo-book-0-9/introduction/licensing
*/


if(!dojo._hasResource["dijit.layout.AccordionContainer"]){
dojo._hasResource["dijit.layout.AccordionContainer"]=true;
dojo.provide("dijit.layout.AccordionContainer");
dojo.require("dojo.fx");
dojo.require("dijit._Container");
dojo.require("dijit._Templated");
dojo.require("dijit.layout.StackContainer");
dojo.require("dijit.layout.ContentPane");
dojo.declare("dijit.layout.AccordionContainer",dijit.layout.StackContainer,{duration:250,_verticalSpace:0,postCreate:function(){
this.domNode.style.overflow="hidden";
this.inherited("postCreate",arguments);
dijit.setWaiRole(this.domNode,"tablist");
dojo.addClass(this.domNode,"dijitAccordionContainer");
},startup:function(){
if(this._started){
return;
}
this.inherited("startup",arguments);
if(this.selectedChildWidget){
var _1=this.selectedChildWidget.containerNode.style;
_1.display="";
_1.overflow="auto";
this.selectedChildWidget._setSelectedState(true);
}
},layout:function(){
var _2=0;
var _3=this.selectedChildWidget;
dojo.forEach(this.getChildren(),function(_4){
_2+=_4.getTitleHeight();
});
var _5=this._contentBox;
this._verticalSpace=(_5.h-_2);
if(_3){
_3.containerNode.style.height=this._verticalSpace+"px";
}
},_setupChild:function(_6){
return _6;
},_transition:function(_7,_8){
if(this._inTransition){
return;
}
this._inTransition=true;
var _9=[];
var _a=this._verticalSpace;
if(_7){
_7.setSelected(true);
var _b=_7.containerNode;
_b.style.display="";
_9.push(dojo.animateProperty({node:_b,duration:this.duration,properties:{height:{start:"1",end:_a}},onEnd:function(){
_b.style.overflow="auto";
}}));
}
if(_8){
_8.setSelected(false);
var _c=_8.containerNode;
_c.style.overflow="hidden";
_9.push(dojo.animateProperty({node:_c,duration:this.duration,properties:{height:{start:_a,end:"1"}},onEnd:function(){
_c.style.display="none";
}}));
}
this._inTransition=false;
dojo.fx.combine(_9).play();
},_onKeyPress:function(e){
if(this.disabled||e.altKey||!(e._dijitWidget||e.ctrlKey)){
return;
}
var k=dojo.keys;
var _f=e._dijitWidget;
switch(e.keyCode){
case k.LEFT_ARROW:
case k.UP_ARROW:
if(_f){
this._adjacent(false)._onTitleClick();
dojo.stopEvent(e);
}
break;
case k.PAGE_UP:
if(e.ctrlKey){
this._adjacent(false)._onTitleClick();
dojo.stopEvent(e);
}
break;
case k.RIGHT_ARROW:
case k.DOWN_ARROW:
if(_f){
this._adjacent(true)._onTitleClick();
dojo.stopEvent(e);
}
break;
case k.PAGE_DOWN:
if(e.ctrlKey){
this._adjacent(true)._onTitleClick();
dojo.stopEvent(e);
}
break;
default:
if(e.ctrlKey&&e.keyCode==k.TAB){
this._adjacent(e._dijitWidget,!e.shiftKey)._onTitleClick();
dojo.stopEvent(e);
}
}
}});
dojo.declare("dijit.layout.AccordionPane",[dijit.layout.ContentPane,dijit._Templated,dijit._Contained],{templateString:"<div class='dijitAccordionPane'\n\t><div dojoAttachPoint='titleNode,focusNode' dojoAttachEvent='ondijitclick:_onTitleClick,onkeypress:_onTitleKeyPress,onfocus:_handleFocus,onblur:_handleFocus'\n\t\tclass='dijitAccordionTitle' wairole=\"tab\"\n\t\t><div class='dijitAccordionArrow' waiRole=\"presentation\"></div\n\t\t><div class='arrowTextUp' waiRole=\"presentation\">&#9650;</div\n\t\t><div class='arrowTextDown' waiRole=\"presentation\">&#9660;</div\n\t\t><div waiRole=\"presentation\" dojoAttachPoint='titleTextNode' class='dijitAccordionText'>${title}</div></div\n\t><div><div dojoAttachPoint='containerNode' style='overflow: hidden; height: 1px; display: none'\n\t\tclass='dijitAccordionBody' wairole=\"tabpanel\"\n\t></div></div>\n</div>\n",postCreate:function(){
this.inherited("postCreate",arguments);
dojo.setSelectable(this.titleNode,false);
this.setSelected(this.selected);
},getTitleHeight:function(){
return dojo.marginBox(this.titleNode).h;
},_onTitleClick:function(){
var _10=this.getParent();
if(!_10._inTransition){
_10.selectChild(this);
dijit.focus(this.focusNode);
}
},_onTitleKeyPress:function(evt){
evt._dijitWidget=this;
return this.getParent()._onKeyPress(evt);
},_setSelectedState:function(_12){
this.selected=_12;
dojo[(_12?"addClass":"removeClass")](this.titleNode,"dijitAccordionTitle-selected");
this.focusNode.setAttribute("tabIndex",_12?"0":"-1");
},_handleFocus:function(e){
dojo[(e.type=="focus"?"addClass":"removeClass")](this.focusNode,"dijitAccordionFocused");
},setSelected:function(_14){
this._setSelectedState(_14);
if(_14){
this.onSelected();
this._loadCheck(true);
}
},onSelected:function(){
}});
}
