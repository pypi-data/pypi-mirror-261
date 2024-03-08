/*
	Copyright (c) 2004-2008, The Dojo Foundation
	All Rights Reserved.

	Licensed under the Academic Free License version 2.1 or above OR the
	modified BSD license. For more information on Dojo licensing, see:

		http://dojotoolkit.org/book/dojo-book-0-9/introduction/licensing
*/


if(!dojo._hasResource["dijit.InlineEditBox"]){
dojo._hasResource["dijit.InlineEditBox"]=true;
dojo.provide("dijit.InlineEditBox");
dojo.require("dojo.i18n");
dojo.require("dijit._Widget");
dojo.require("dijit._Container");
dojo.require("dijit.form.Button");
dojo.require("dijit.form.TextBox");
dojo.requireLocalization("dijit","common",null,"ar,ROOT,cs,da,de,el,es,fi,fr,he,hu,it,ja,ko,nb,nl,pl,pt,pt-pt,ru,sv,tr,zh,zh-tw");
dojo.declare("dijit.InlineEditBox",dijit._Widget,{editing:false,autoSave:true,buttonSave:"",buttonCancel:"",renderAsHtml:false,editor:"dijit.form.TextBox",editorParams:{},onChange:function(_1){
},width:"100%",value:"",noValueIndicator:"<span style='font-family: wingdings; text-decoration: underline;'>&nbsp;&nbsp;&nbsp;&nbsp;&#x270d;&nbsp;&nbsp;&nbsp;&nbsp;</span>",postMixInProperties:function(){
this.inherited("postMixInProperties",arguments);
this.displayNode=this.srcNodeRef;
var _2={ondijitclick:"_onClick",onmouseover:"_onMouseOver",onmouseout:"_onMouseOut",onfocus:"_onMouseOver",onblur:"_onMouseOut"};
for(var _3 in _2){
this.connect(this.displayNode,_3,_2[_3]);
}
dijit.setWaiRole(this.displayNode,"button");
if(!this.displayNode.getAttribute("tabIndex")){
this.displayNode.setAttribute("tabIndex",0);
}
this.setValue(this.value||this.displayNode.innerHTML);
},setDisabled:function(_4){
this.disabled=_4;
dijit.setWaiState(this.focusNode||this.domNode,"disabled",_4);
},_onMouseOver:function(){
dojo.addClass(this.displayNode,this.disabled?"dijitDisabledClickableRegion":"dijitClickableRegion");
},_onMouseOut:function(){
dojo.removeClass(this.displayNode,this.disabled?"dijitDisabledClickableRegion":"dijitClickableRegion");
},_onClick:function(e){
if(this.disabled){
return;
}
if(e){
dojo.stopEvent(e);
}
this._onMouseOut();
setTimeout(dojo.hitch(this,"_edit"),0);
},_edit:function(){
this.editing=true;
var _6=(this.renderAsHtml?this.value:this.value.replace(/\s*\r?\n\s*/g,"").replace(/<br\/?>/gi,"\n").replace(/&gt;/g,">").replace(/&lt;/g,"<").replace(/&amp;/g,"&"));
var _7=dojo.doc.createElement("span");
dojo.place(_7,this.domNode,"before");
var ew=this.editWidget=new dijit._InlineEditor({value:dojo.trim(_6),autoSave:this.autoSave,buttonSave:this.buttonSave,buttonCancel:this.buttonCancel,renderAsHtml:this.renderAsHtml,editor:this.editor,editorParams:this.editorParams,style:dojo.getComputedStyle(this.displayNode),save:dojo.hitch(this,"save"),cancel:dojo.hitch(this,"cancel"),width:this.width},_7);
var _9=ew.domNode.style;
this.displayNode.style.display="none";
_9.position="static";
_9.visibility="visible";
this.domNode=ew.domNode;
setTimeout(function(){
ew.focus();
},100);
},_showText:function(_a){
this.displayNode.style.display="";
var ew=this.editWidget;
var _c=ew.domNode.style;
_c.position="absolute";
_c.visibility="hidden";
this.domNode=this.displayNode;
if(_a){
dijit.focus(this.displayNode);
}
_c.display="none";
setTimeout(function(){
ew.destroy();
delete ew;
if(dojo.isIE){
dijit.focus(dijit.getFocus());
}
},1000);
},save:function(_d){
this.editing=false;
var _e=this.editWidget.getValue()+"";
if(!this.renderAsHtml){
_e=_e.replace(/&/gm,"&amp;").replace(/</gm,"&lt;").replace(/>/gm,"&gt;").replace(/"/gm,"&quot;").replace(/\n/g,"<br>");
}
this.setValue(_e);
this.onChange(_e);
this._showText(_d);
},setValue:function(_f){
this.value=_f;
this.displayNode.innerHTML=dojo.trim(_f)||this.noValueIndicator;
},getValue:function(){
return this.value;
},cancel:function(_10){
this.editing=false;
this._showText(_10);
}});
dojo.declare("dijit._InlineEditor",[dijit._Widget,dijit._Templated],{templateString:"<fieldset dojoAttachPoint=\"editNode\" waiRole=\"presentation\" style=\"position: absolute; visibility:hidden\" class=\"dijitReset dijitInline\"\n\tdojoAttachEvent=\"onkeypress: _onKeyPress\" \n\t><input dojoAttachPoint=\"editorPlaceholder\"\n\t/><span dojoAttachPoint=\"buttonContainer\"\n\t\t><button class='saveButton' dojoAttachPoint=\"saveButton\" dojoType=\"dijit.form.Button\" dojoAttachEvent=\"onClick:save\" disabled=\"true\">${buttonSave}</button\n\t\t><button class='cancelButton' dojoAttachPoint=\"cancelButton\" dojoType=\"dijit.form.Button\" dojoAttachEvent=\"onClick:cancel\">${buttonCancel}</button\n\t></span\n></fieldset>\n",widgetsInTemplate:true,postMixInProperties:function(){
this.inherited("postMixInProperties",arguments);
this.messages=dojo.i18n.getLocalization("dijit","common",this.lang);
dojo.forEach(["buttonSave","buttonCancel"],function(_11){
if(!this[_11]){
this[_11]=this.messages[_11];
}
},this);
},postCreate:function(){
var cls=dojo.getObject(this.editor);
var ew=this.editWidget=new cls(this.editorParams,this.editorPlaceholder);
var _14=this.style;
dojo.forEach(["fontWeight","fontFamily","fontSize","fontStyle"],function(_15){
ew.focusNode.style[_15]=_14[_15];
},this);
dojo.forEach(["marginTop","marginBottom","marginLeft","marginRight"],function(_16){
this.domNode.style[_16]=_14[_16];
},this);
if(this.width=="100%"){
ew.domNode.style.width="100%";
this.domNode.style.display="block";
}else{
ew.domNode.style.width=this.width+(Number(this.width)==this.width?"px":"");
}
this.connect(ew,"onChange","_onChange");
this.connect(ew.focusNode||ew.domNode,"onkeypress","_onKeyPress");
(this.editWidget.setDisplayedValue||this.editWidget.setValue).call(this.editWidget,this.value,false);
this._initialText=this.getValue();
if(this.autoSave){
this.buttonContainer.style.display="none";
}
},destroy:function(){
this.editWidget.destroy();
this.inherited(arguments);
},getValue:function(){
var ew=this.editWidget;
return ew.getDisplayedValue?ew.getDisplayedValue():ew.getValue();
},_onKeyPress:function(e){
if(this._exitInProgress){
return;
}
if(this.autoSave){
if(e.altKey||e.ctrlKey){
return;
}
if(e.keyCode==dojo.keys.ESCAPE){
dojo.stopEvent(e);
this._exitInProgress=true;
this.cancel(true);
}else{
if(e.keyCode==dojo.keys.ENTER){
dojo.stopEvent(e);
this._exitInProgress=true;
this.save(true);
}else{
if(e.keyCode==dojo.keys.TAB){
this._exitInProgress=true;
setTimeout(dojo.hitch(this,"save",false),0);
}
}
}
}else{
var _19=this;
setTimeout(function(){
_19.saveButton.setAttribute("disabled",_19.getValue()==_19._initialText);
},100);
}
},_onBlur:function(){
this.inherited(arguments);
if(this._exitInProgress){
return;
}
if(this.autoSave){
this._exitInProgress=true;
if(this.getValue()==this._initialText){
this.cancel(false);
}else{
this.save(false);
}
}
},enableSave:function(){
return this.editWidget.isValid?this.editWidget.isValid():true;
},_onChange:function(){
if(this._exitInProgress){
return;
}
if(this.autoSave){
this._exitInProgress=true;
this.save(true);
}else{
this.saveButton.setAttribute("disabled",(this.getValue()==this._initialText)||!this.enableSave());
}
},enableSave:function(){
return this.editWidget.isValid?this.editWidget.isValid():true;
},focus:function(){
this.editWidget.focus();
dijit.selectInputText(this.editWidget.focusNode);
}});
}
