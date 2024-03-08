/*
	Copyright (c) 2004-2008, The Dojo Foundation
	All Rights Reserved.

	Licensed under the Academic Free License version 2.1 or above OR the
	modified BSD license. For more information on Dojo licensing, see:

		http://dojotoolkit.org/book/dojo-book-0-9/introduction/licensing
*/


if(!dojo._hasResource["dijit.layout.TabContainer"]){
dojo._hasResource["dijit.layout.TabContainer"]=true;
dojo.provide("dijit.layout.TabContainer");
dojo.require("dijit.layout.StackContainer");
dojo.require("dijit._Templated");
dojo.declare("dijit.layout.TabContainer",[dijit.layout.StackContainer,dijit._Templated],{tabPosition:"top",templateString:null,templateString:"<div class=\"dijitTabContainer\">\n\t<div dojoAttachPoint=\"tablistNode\"></div>\n\t<div class=\"dijitTabPaneWrapper\" dojoAttachPoint=\"containerNode\"></div>\n</div>\n",_controllerWidget:"dijit.layout.TabController",postCreate:function(){
this.inherited(arguments);
var _1=dojo.getObject(this._controllerWidget);
this.tablist=new _1({id:this.id+"_tablist",tabPosition:this.tabPosition,doLayout:this.doLayout,containerId:this.id},this.tablistNode);
},_setupChild:function(_2){
dojo.addClass(_2.domNode,"dijitTabPane");
this.inherited(arguments);
return _2;
},startup:function(){
if(this._started){
return;
}
this.tablist.startup();
this.inherited(arguments);
if(dojo.isSafari){
setTimeout(dojo.hitch(this,"layout"),0);
}
if(dojo.isIE&&!this.isLeftToRight()&&this.tabPosition=="right-h"&&this.tablist&&this.tablist.pane2button){
for(var _3 in this.tablist.pane2button){
var _4=this.tablist.pane2button[_3];
if(!_4.closeButton){
continue;
}
tabButtonStyle=_4.closeButtonNode.style;
tabButtonStyle.position="absolute";
if(dojo.isIE<7){
tabButtonStyle.left=_4.domNode.offsetWidth+"px";
}else{
tabButtonStyle.padding="0px";
}
}
}
},layout:function(){
if(!this.doLayout){
return;
}
var _5=this.tabPosition.replace(/-h/,"");
var _6=[{domNode:this.tablist.domNode,layoutAlign:_5},{domNode:this.containerNode,layoutAlign:"client"}];
dijit.layout.layoutChildren(this.domNode,this._contentBox,_6);
this._containerContentBox=dijit.layout.marginBox2contentBox(this.containerNode,_6[1]);
if(this.selectedChildWidget){
this._showChild(this.selectedChildWidget);
if(this.doLayout&&this.selectedChildWidget.resize){
this.selectedChildWidget.resize(this._containerContentBox);
}
}
},destroy:function(){
if(this.tablist){
this.tablist.destroy();
}
this.inherited(arguments);
}});
dojo.declare("dijit.layout.TabController",dijit.layout.StackController,{templateString:"<div wairole='tablist' dojoAttachEvent='onkeypress:onkeypress'></div>",tabPosition:"top",doLayout:true,buttonWidget:"dijit.layout._TabButton",postMixInProperties:function(){
this["class"]="dijitTabLabels-"+this.tabPosition+(this.doLayout?"":" dijitTabNoLayout");
this.inherited(arguments);
},_rectifyRtlTabList:function(){
if(0>=this.tabPosition.indexOf("-h")){
return;
}
if(!this.pane2button){
return;
}
var _7=0;
for(var _8 in this.pane2button){
_7=Math.max(_7,dojo.marginBox(this.pane2button[_8].innerDiv).w);
}
for(_8 in this.pane2button){
this.pane2button[_8].innerDiv.style.width=_7+"px";
}
}});
dojo.declare("dijit.layout._TabButton",dijit.layout._StackButton,{baseClass:"dijitTab",templateString:"<div waiRole=\"presentation\" dojoAttachEvent='onclick:onClick,onmouseenter:_onMouse,onmouseleave:_onMouse'>\n    <div waiRole=\"presentation\" class='dijitTabInnerDiv' dojoAttachPoint='innerDiv'>\n        <div waiRole=\"presentation\" class='dijitTabContent' dojoAttachPoint='tabContent'>\n\t        <span dojoAttachPoint='containerNode,focusNode' class='tabLabel'>${!label}</span>\n\t        <span dojoAttachPoint='closeButtonNode' class='closeImage' dojoAttachEvent='onmouseenter:_onMouse, onmouseleave:_onMouse, onclick:onClickCloseButton' stateModifier='CloseButton'>\n\t            <span dojoAttachPoint='closeText' class='closeText'>x</span>\n\t        </span>\n        </div>\n    </div>\n</div>\n",postCreate:function(){
if(this.closeButton){
dojo.addClass(this.innerDiv,"dijitClosable");
}else{
this.closeButtonNode.style.display="none";
}
this.inherited(arguments);
dojo.setSelectable(this.containerNode,false);
}});
}
