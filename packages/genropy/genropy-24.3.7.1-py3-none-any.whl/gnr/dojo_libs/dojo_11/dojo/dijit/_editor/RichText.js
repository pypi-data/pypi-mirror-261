/*
	Copyright (c) 2004-2008, The Dojo Foundation
	All Rights Reserved.

	Licensed under the Academic Free License version 2.1 or above OR the
	modified BSD license. For more information on Dojo licensing, see:

		http://dojotoolkit.org/book/dojo-book-0-9/introduction/licensing
*/


if(!dojo._hasResource["dijit._editor.RichText"]){
dojo._hasResource["dijit._editor.RichText"]=true;
dojo.provide("dijit._editor.RichText");
dojo.require("dijit._Widget");
dojo.require("dijit._editor.selection");
dojo.require("dijit._editor.html");
dojo.require("dojo.i18n");
dojo.requireLocalization("dijit.form","Textarea",null,"ar,cs,da,de,el,es,fi,fr,he,hu,it,ja,ko,nb,nl,pl,pt,pt-pt,ru,sv,ROOT,tr,zh,zh-tw");
if(!dojo.config["useXDomain"]||dojo.config["allowXdRichTextSave"]){
if(dojo._postLoad){
(function(){
var _1=dojo.doc.createElement("textarea");
_1.id=dijit._scopeName+"._editor.RichText.savedContent";
var s=_1.style;
s.display="none";
s.position="absolute";
s.top="-100px";
s.left="-100px";
s.height="3px";
s.width="3px";
dojo.body().appendChild(_1);
})();
}else{
try{
dojo.doc.write("<textarea id=\""+dijit._scopeName+"._editor.RichText.savedContent\" "+"style=\"display:none;position:absolute;top:-100px;left:-100px;height:3px;width:3px;overflow:hidden;\"></textarea>");
}
catch(e){
}
}
}
dojo.declare("dijit._editor.RichText",dijit._Widget,{constructor:function(){
this.contentPreFilters=[];
this.contentPostFilters=[];
this.contentDomPreFilters=[];
this.contentDomPostFilters=[];
this.editingAreaStyleSheets=[];
this._keyHandlers={};
this.contentPreFilters.push(dojo.hitch(this,"_preFixUrlAttributes"));
if(dojo.isMoz){
this.contentPreFilters.push(this._fixContentForMoz);
this.contentPostFilters.push(this._removeMozBogus);
}else{
if(dojo.isSafari){
this.contentPostFilters.push(this._removeSafariBogus);
}
}
this.onLoadDeferred=new dojo.Deferred();
},inheritWidth:false,focusOnLoad:false,name:"",styleSheets:"",_content:"",height:"300px",minHeight:"1em",isClosed:true,isLoaded:false,_SEPARATOR:"@@**%%__RICHTEXTBOUNDRY__%%**@@",onLoadDeferred:null,postCreate:function(){
dojo.publish(dijit._scopeName+"._editor.RichText::init",[this]);
this.open();
this.setupDefaultShortcuts();
},setupDefaultShortcuts:function(){
var _3=function(_4,_5){
return arguments.length==1?function(){
this.execCommand(_4);
}:function(){
this.execCommand(_4,_5);
};
};
var _6={b:_3("bold"),i:_3("italic"),u:_3("underline"),a:_3("selectall"),s:function(){
this.save(true);
},"1":_3("formatblock","h1"),"2":_3("formatblock","h2"),"3":_3("formatblock","h3"),"4":_3("formatblock","h4"),"\\":_3("insertunorderedlist")};
if(!dojo.isIE){
_6.Z=_3("redo");
}
for(var _7 in _6){
this.addKeyHandler(_7,this.KEY_CTRL,_6[_7]);
}
},events:["onKeyPress","onKeyDown","onKeyUp","onClick"],captureEvents:[],_editorCommandsLocalized:false,_localizeEditorCommands:function(){
if(this._editorCommandsLocalized){
return;
}
this._editorCommandsLocalized=true;
var _8=["p","pre","address","h1","h2","h3","h4","h5","h6","ol","div","ul"];
var _9="",_a,i=0;
while((_a=_8[i++])){
if(_a.charAt(1)!="l"){
_9+="<"+_a+"><span>content</span></"+_a+">";
}else{
_9+="<"+_a+"><li>content</li></"+_a+">";
}
}
var _c=dojo.doc.createElement("div");
_c.style.position="absolute";
_c.style.left="-2000px";
_c.style.top="-2000px";
dojo.doc.body.appendChild(_c);
_c.innerHTML=_9;
var _d=_c.firstChild;
while(_d){
dijit._editor.selection.selectElement(_d.firstChild);
dojo.withGlobal(this.window,"selectElement",dijit._editor.selection,[_d.firstChild]);
var _e=_d.tagName.toLowerCase();
this._local2NativeFormatNames[_e]=dojo.doc.queryCommandValue("formatblock");
this._native2LocalFormatNames[this._local2NativeFormatNames[_e]]=_e;
_d=_d.nextSibling;
}
dojo.doc.body.removeChild(_c);
},open:function(_f){
if((!this.onLoadDeferred)||(this.onLoadDeferred.fired>=0)){
this.onLoadDeferred=new dojo.Deferred();
}
if(!this.isClosed){
this.close();
}
dojo.publish(dijit._scopeName+"._editor.RichText::open",[this]);
this._content="";
if((arguments.length==1)&&(_f["nodeName"])){
this.domNode=_f;
}
var _10;
if((this.domNode["nodeName"])&&(this.domNode.nodeName.toLowerCase()=="textarea")){
this.textarea=this.domNode;
this.name=this.textarea.name;
_10=this._preFilterContent(this.textarea.value);
this.domNode=dojo.doc.createElement("div");
this.domNode.setAttribute("widgetId",this.id);
this.textarea.removeAttribute("widgetId");
this.domNode.cssText=this.textarea.cssText;
this.domNode.className+=" "+this.textarea.className;
dojo.place(this.domNode,this.textarea,"before");
var _11=dojo.hitch(this,function(){
dojo.attr(this.textarea,"tabIndex","-1");
with(this.textarea.style){
display="block";
position="absolute";
left=top="-1000px";
if(dojo.isIE){
this.__overflow=overflow;
overflow="hidden";
}
}
});
if(dojo.isIE){
setTimeout(_11,10);
}else{
_11();
}
}else{
_10=this._preFilterContent(dijit._editor.getChildrenHtml(this.domNode));
this.domNode.innerHTML="";
}
if(_10==""){
_10="&nbsp;";
}
var _12=dojo.contentBox(this.domNode);
this._oldHeight=_12.h;
this._oldWidth=_12.w;
if((this.domNode["nodeName"])&&(this.domNode.nodeName=="LI")){
this.domNode.innerHTML=" <br>";
}
this.editingArea=dojo.doc.createElement("div");
this.domNode.appendChild(this.editingArea);
if(this.name!=""&&(!dojo.config["useXDomain"]||dojo.config["allowXdRichTextSave"])){
var _13=dojo.byId(dijit._scopeName+"._editor.RichText.savedContent");
if(_13.value!=""){
var _14=_13.value.split(this._SEPARATOR),i=0,dat;
while((dat=_14[i++])){
var _17=dat.split(":");
if(_17[0]==this.name){
_10=_17[1];
_14.splice(i,1);
break;
}
}
}
this.connect(window,"onbeforeunload","_saveContent");
}
this.isClosed=false;
if(dojo.isIE||dojo.isSafari||dojo.isOpera){
if(dojo.config["useXDomain"]&&!dojo.config["dojoBlankHtmlUrl"]){
console.debug("dijit._editor.RichText: When using cross-domain Dojo builds,"+" please save dojo/resources/blank.html to your domain and set djConfig.dojoBlankHtmlUrl"+" to the path on your domain to blank.html");
}
var _18=dojo.config["dojoBlankHtmlUrl"]||(dojo.moduleUrl("dojo","resources/blank.html")+"");
var ifr=this.editorObject=this.iframe=dojo.doc.createElement("iframe");
ifr.id=this.id+"_iframe";
ifr.src=_18;
ifr.style.border="none";
ifr.style.width="100%";
ifr.frameBorder=0;
this.editingArea.appendChild(ifr);
var h=null;
var _1b=dojo.hitch(this,function(){
if(h){
dojo.disconnect(h);
h=null;
}
this.window=ifr.contentWindow;
var d=this.document=this.window.document;
d.open();
d.write(this._getIframeDocTxt(_10));
d.close();
if(dojo.isIE>=7){
if(this.height){
ifr.style.height=this.height;
}
if(this.minHeight){
ifr.style.minHeight=this.minHeight;
}
}else{
ifr.style.height=this.height?this.height:this.minHeight;
}
if(dojo.isIE){
this._localizeEditorCommands();
}
this.onLoad();
this.savedContent=this.getValue(true);
});
if(dojo.isIE&&dojo.isIE<7){
var t=setInterval(function(){
if(ifr.contentWindow.isLoaded){
clearInterval(t);
_1b();
}
},100);
}else{
h=dojo.connect(((dojo.isIE)?ifr.contentWindow:ifr),"onload",_1b);
}
}else{
this._drawIframe(_10);
this.savedContent=this.getValue(true);
}
if(this.domNode.nodeName=="LI"){
this.domNode.lastChild.style.marginTop="-1.2em";
}
this.domNode.className+=" RichTextEditable";
},_local2NativeFormatNames:{},_native2LocalFormatNames:{},_localizedIframeTitles:null,_getIframeDocTxt:function(_1e){
var _cs=dojo.getComputedStyle(this.domNode);
if(dojo.isIE||(!this.height&&!dojo.isMoz)){
_1e="<div>"+_1e+"</div>";
}
var _20=[_cs.fontWeight,_cs.fontSize,_cs.fontFamily].join(" ");
var _21=_cs.lineHeight;
if(_21.indexOf("px")>=0){
_21=parseFloat(_21)/parseFloat(_cs.fontSize);
}else{
if(_21.indexOf("em")>=0){
_21=parseFloat(_21);
}else{
_21="1.0";
}
}
return [this.isLeftToRight()?"<html><head>":"<html dir='rtl'><head>",(dojo.isMoz?"<title>"+this._localizedIframeTitles.iframeEditTitle+"</title>":""),"<style>","body,html {","\tbackground:transparent;","\tfont:",_20,";","\tpadding: 1em 0 0 0;","\tmargin: -1em 0 0 0;","\theight: 100%;","}","body{","\ttop:0px; left:0px; right:0px;",((this.height||dojo.isOpera)?"":"position: fixed;"),"\tmin-height:",this.minHeight,";","\tline-height:",_21,"}","p{ margin: 1em 0 !important; }",(this.height?"":"body,html{height:auto;overflow-y:hidden;/*for IE*/} body > div {overflow-x:auto;/*for FF to show vertical scrollbar*/}"),"li > ul:-moz-first-node, li > ol:-moz-first-node{ padding-top: 1.2em; } ","li{ min-height:1.2em; }","</style>",this._applyEditingAreaStyleSheets(),"</head><body>"+_1e+"</body></html>"].join("");
},_drawIframe:function(_22){
if(!this.iframe){
var ifr=this.iframe=dojo.doc.createElement("iframe");
ifr.id=this.id;
var _24=ifr.style;
_24.border="none";
_24.lineHeight="0";
_24.verticalAlign="bottom";
this.editorObject=this.iframe;
this._localizedIframeTitles=dojo.i18n.getLocalization("dijit.form","Textarea");
var _25=dojo.query("label[for=\""+this.id+"\"]");
if(_25.length){
this._localizedIframeTitles.iframeEditTitle=_25[0].innerHTML+" "+this._localizedIframeTitles.iframeEditTitle;
}
}
this.iframe.style.width=this.inheritWidth?this._oldWidth:"100%";
if(this.height){
this.iframe.style.height=this.height;
}else{
this.iframe.height=this._oldHeight;
}
var _26;
if(this.textarea){
_26=this.srcNodeRef;
}else{
_26=dojo.doc.createElement("div");
_26.style.display="none";
_26.innerHTML=_22;
this.editingArea.appendChild(_26);
}
this.editingArea.appendChild(this.iframe);
var _27=false;
var _28=this.iframe.contentDocument;
_28.open();
if(dojo.isAIR){
_28.body.innerHTML=_22;
}else{
_28.write(this._getIframeDocTxt(_22));
}
_28.close();
var _29=dojo.hitch(this,function(){
if(!_27){
_27=true;
}else{
return;
}
if(!this.editNode){
try{
if(this.iframe.contentWindow){
this.window=this.iframe.contentWindow;
this.document=this.iframe.contentWindow.document;
}else{
if(this.iframe.contentDocument){
this.window=this.iframe.contentDocument.window;
this.document=this.iframe.contentDocument;
}
}
if(!this.document.body){
throw "Error";
}
}
catch(e){
setTimeout(_29,500);
_27=false;
return;
}
dojo._destroyElement(_26);
this.onLoad();
}else{
dojo._destroyElement(_26);
this.editNode.innerHTML=_22;
this.onDisplayChanged();
}
this._preDomFilterContent(this.editNode);
});
_29();
},_applyEditingAreaStyleSheets:function(){
var _2a=[];
if(this.styleSheets){
_2a=this.styleSheets.split(";");
this.styleSheets="";
}
_2a=_2a.concat(this.editingAreaStyleSheets);
this.editingAreaStyleSheets=[];
var _2b="",i=0,url;
while((url=_2a[i++])){
var _2e=(new dojo._Url(dojo.global.location,url)).toString();
this.editingAreaStyleSheets.push(_2e);
_2b+="<link rel=\"stylesheet\" type=\"text/css\" href=\""+_2e+"\"/>";
}
return _2b;
},addStyleSheet:function(uri){
var url=uri.toString();
if(url.charAt(0)=="."||(url.charAt(0)!="/"&&!uri.host)){
url=(new dojo._Url(dojo.global.location,url)).toString();
}
if(dojo.indexOf(this.editingAreaStyleSheets,url)>-1){
return;
}
this.editingAreaStyleSheets.push(url);
if(this.document.createStyleSheet){
this.document.createStyleSheet(url);
}else{
var _31=this.document.getElementsByTagName("head")[0];
var _32=this.document.createElement("link");
with(_32){
rel="stylesheet";
type="text/css";
href=url;
}
_31.appendChild(_32);
}
},removeStyleSheet:function(uri){
var url=uri.toString();
if(url.charAt(0)=="."||(url.charAt(0)!="/"&&!uri.host)){
url=(new dojo._Url(dojo.global.location,url)).toString();
}
var _35=dojo.indexOf(this.editingAreaStyleSheets,url);
if(_35==-1){
return;
}
delete this.editingAreaStyleSheets[_35];
dojo.withGlobal(this.window,"query",dojo,["link:[href=\""+url+"\"]"]).orphan();
},disabled:true,_mozSettingProps:["styleWithCSS","insertBrOnReturn"],setDisabled:function(_36){
if(dojo.isIE||dojo.isSafari||dojo.isOpera){
if(dojo.isIE){
this.editNode.unselectable="on";
}
this.editNode.contentEditable=!_36;
if(dojo.isIE){
var _37=this;
setTimeout(function(){
_37.editNode.unselectable="off";
},0);
}
}else{
if(_36){
this._mozSettings=[false,this.blockNodeForEnter==="BR"];
}
this.document.designMode=(_36?"off":"on");
if(!_36&&this._mozSettings){
dojo.forEach(this._mozSettingProps,function(s,i){
this.document.execCommand(s,false,this._mozSettings[i]);
},this);
}
}
this.disabled=_36;
},_isResized:function(){
return false;
},onLoad:function(e){
this.isLoaded=true;
if(!this.window.__registeredWindow){
this.window.__registeredWindow=true;
dijit.registerWin(this.window);
}
if(!dojo.isIE&&(this.height||dojo.isMoz)){
this.editNode=this.document.body;
}else{
this.editNode=this.document.body.firstChild;
var _3b=this;
if(dojo.isIE){
var _3c=this.tabStop=dojo.doc.createElement("<div tabIndex=-1>");
this.editingArea.appendChild(_3c);
this.iframe.onfocus=function(){
_3b.editNode.setActive();
};
}
}
try{
this.setDisabled(false);
}
catch(e){
var _3d=dojo.connect(this,"onClick",this,function(){
this.setDisabled(false);
dojo.disconnect(_3d);
});
}
this._preDomFilterContent(this.editNode);
var _3e=this.events.concat(this.captureEvents),i=0,et;
while((et=_3e[i++])){
this.connect(this.document,et.toLowerCase(),et);
}
if(!dojo.isIE){
try{
this.document.execCommand("styleWithCSS",false,false);
}
catch(e2){
}
}else{
this.connect(this.document,"onmousedown","_onMouseDown");
this.editNode.style.zoom=1;
}
if(this.focusOnLoad){
setTimeout(dojo.hitch(this,"focus"),0);
}
this.onDisplayChanged(e);
if(this.onLoadDeferred){
this.onLoadDeferred.callback(true);
}
},onKeyDown:function(e){
if(dojo.isIE){
if(e.keyCode==dojo.keys.TAB&&e.shiftKey&&!e.ctrlKey&&!e.altKey){
this.iframe.focus();
}else{
if(e.keyCode==dojo.keys.TAB&&!e.shiftKey&&!e.ctrlKey&&!e.altKey){
this.tabStop.focus();
}else{
if(e.keyCode===dojo.keys.BACKSPACE&&this.document.selection.type==="Control"){
dojo.stopEvent(e);
this.execCommand("delete");
}else{
if((65<=e.keyCode&&e.keyCode<=90)||(e.keyCode>=37&&e.keyCode<=40)){
e.charCode=e.keyCode;
this.onKeyPress(e);
}
}
}
}
}else{
if(dojo.isMoz){
if(e.keyCode==dojo.keys.TAB&&!e.shiftKey&&!e.ctrlKey&&!e.altKey&&this.iframe){
this.iframe.contentDocument.title=this._localizedIframeTitles.iframeFocusTitle;
this.iframe.focus();
dojo.stopEvent(e);
}else{
if(e.keyCode==dojo.keys.TAB&&e.shiftKey){
if(this.toolbar){
this.toolbar.focus();
}
dojo.stopEvent(e);
}
}
}
}
},onKeyUp:function(e){
return;
},KEY_CTRL:1,KEY_SHIFT:2,onKeyPress:function(e){
var _44=(e.ctrlKey&&!e.altKey)?this.KEY_CTRL:0|e.shiftKey?this.KEY_SHIFT:0;
var key=e.keyChar||e.keyCode;
if(this._keyHandlers[key]){
var _46=this._keyHandlers[key],i=0,h;
while((h=_46[i++])){
if(_44==h.modifiers){
if(!h.handler.apply(this,arguments)){
e.preventDefault();
}
break;
}
}
}
setTimeout(dojo.hitch(this,function(){
this.onKeyPressed(e);
}),1);
},addKeyHandler:function(key,_4a,_4b){
if(!dojo.isArray(this._keyHandlers[key])){
this._keyHandlers[key]=[];
}
this._keyHandlers[key].push({modifiers:_4a||0,handler:_4b});
},onKeyPressed:function(e){
this.onDisplayChanged();
},onClick:function(e){
this.onDisplayChanged(e);
},_onMouseDown:function(e){
if(!this._focused&&!this.disabled){
this.focus();
}
},_onBlur:function(e){
this.inherited(arguments);
var _c=this.getValue(true);
if(_c!=this.savedContent){
this.onChange(_c);
this.savedContent=_c;
}
if(dojo.isMoz&&this.iframe){
this.iframe.contentDocument.title=this._localizedIframeTitles.iframeEditTitle;
}
},_initialFocus:true,_onFocus:function(e){
this.inherited(arguments);
if(dojo.isMoz&&this._initialFocus){
this._initialFocus=false;
if(this.editNode.innerHTML.replace(/^\s+|\s+$/g,"")=="&nbsp;"){
this.placeCursorAtStart();
}
}
},blur:function(){
if(!dojo.isIE&&this.window.document.documentElement&&this.window.document.documentElement.focus){
this.window.document.documentElement.focus();
}else{
if(dojo.doc.body.focus){
dojo.doc.body.focus();
}
}
},focus:function(){
if(!dojo.isIE){
dijit.focus(this.iframe);
}else{
if(this.editNode&&this.editNode.focus){
this.iframe.fireEvent("onfocus",document.createEventObject());
}
}
},updateInterval:200,_updateTimer:null,onDisplayChanged:function(e){
if(!this._updateTimer){
if(this._updateTimer){
clearTimeout(this._updateTimer);
}
this._updateTimer=setTimeout(dojo.hitch(this,this.onNormalizedDisplayChanged),this.updateInterval);
}
},onNormalizedDisplayChanged:function(){
this._updateTimer=null;
},onChange:function(_53){
},_normalizeCommand:function(cmd){
var _55=cmd.toLowerCase();
if(_55=="hilitecolor"&&!dojo.isMoz){
_55="backcolor";
}
return _55;
},queryCommandAvailable:function(_56){
var ie=1;
var _58=1<<1;
var _59=1<<2;
var _5a=1<<3;
var _5b=1<<4;
var _5c=dojo.isSafari;
function isSupportedBy(_5d){
return {ie:Boolean(_5d&ie),mozilla:Boolean(_5d&_58),safari:Boolean(_5d&_59),safari420:Boolean(_5d&_5b),opera:Boolean(_5d&_5a)};
};
var _5e=null;
switch(_56.toLowerCase()){
case "bold":
case "italic":
case "underline":
case "subscript":
case "superscript":
case "fontname":
case "fontsize":
case "forecolor":
case "hilitecolor":
case "justifycenter":
case "justifyfull":
case "justifyleft":
case "justifyright":
case "delete":
case "selectall":
case "toggledir":
_5e=isSupportedBy(_58|ie|_59|_5a);
break;
case "createlink":
case "unlink":
case "removeformat":
case "inserthorizontalrule":
case "insertimage":
case "insertorderedlist":
case "insertunorderedlist":
case "indent":
case "outdent":
case "formatblock":
case "inserthtml":
case "undo":
case "redo":
case "strikethrough":
_5e=isSupportedBy(_58|ie|_5a|_5b);
break;
case "blockdirltr":
case "blockdirrtl":
case "dirltr":
case "dirrtl":
case "inlinedirltr":
case "inlinedirrtl":
_5e=isSupportedBy(ie);
break;
case "cut":
case "copy":
case "paste":
_5e=isSupportedBy(ie|_58|_5b);
break;
case "inserttable":
_5e=isSupportedBy(_58|ie);
break;
case "insertcell":
case "insertcol":
case "insertrow":
case "deletecells":
case "deletecols":
case "deleterows":
case "mergecells":
case "splitcell":
_5e=isSupportedBy(ie|_58);
break;
default:
return false;
}
return (dojo.isIE&&_5e.ie)||(dojo.isMoz&&_5e.mozilla)||(dojo.isSafari&&_5e.safari)||(_5c&&_5e.safari420)||(dojo.isOpera&&_5e.opera);
},execCommand:function(_5f,_60){
var _61;
this.focus();
_5f=this._normalizeCommand(_5f);
if(_60!=undefined){
if(_5f=="heading"){
throw new Error("unimplemented");
}else{
if((_5f=="formatblock")&&dojo.isIE){
_60="<"+_60+">";
}
}
}
if(_5f=="inserthtml"){
_60=this._preFilterContent(_60);
if(dojo.isIE){
var _62=this.document.selection.createRange();
if(this.document.selection.type.toUpperCase()=="CONTROL"){
var n=_62.item(0);
while(_62.length){
_62.remove(_62.item(0));
}
n.outerHTML=_60;
}else{
_62.pasteHTML(_60);
}
_62.select();
_61=true;
}else{
if(dojo.isMoz&&!_60.length){
dojo.withGlobal(this.window,"remove",dijit._editor.selection);
_61=true;
}else{
_61=this.document.execCommand(_5f,false,_60);
}
}
}else{
if((_5f=="unlink")&&(this.queryCommandEnabled("unlink"))&&(dojo.isMoz||dojo.isSafari)){
var _64=this.window.getSelection();
var a=dojo.withGlobal(this.window,"getAncestorElement",dijit._editor.selection,["a"]);
dojo.withGlobal(this.window,"selectElement",dijit._editor.selection,[a]);
_61=this.document.execCommand("unlink",false,null);
}else{
if((_5f=="hilitecolor")&&(dojo.isMoz)){
this.document.execCommand("styleWithCSS",false,true);
_61=this.document.execCommand(_5f,false,_60);
this.document.execCommand("styleWithCSS",false,false);
}else{
if((dojo.isIE)&&((_5f=="backcolor")||(_5f=="forecolor"))){
_60=arguments.length>1?_60:null;
_61=this.document.execCommand(_5f,false,_60);
}else{
_60=arguments.length>1?_60:null;
if(_60||_5f!="createlink"){
_61=this.document.execCommand(_5f,false,_60);
}
}
}
}
}
this.onDisplayChanged();
return _61;
},queryCommandEnabled:function(_66){
if(this.disabled){
return false;
}
_66=this._normalizeCommand(_66);
if(dojo.isMoz||dojo.isSafari){
if(_66=="unlink"){
return dojo.withGlobal(this.window,"hasAncestorElement",dijit._editor.selection,["a"]);
}else{
if(_66=="inserttable"){
return true;
}
}
}
if(dojo.isSafari){
if(_66=="copy"){
_66="cut";
}else{
if(_66=="paste"){
return true;
}
}
}
var _67=dojo.isIE?this.document.selection.createRange():this.document;
return _67.queryCommandEnabled(_66);
},queryCommandState:function(_68){
if(this.disabled){
return false;
}
_68=this._normalizeCommand(_68);
return this.document.queryCommandState(_68);
},queryCommandValue:function(_69){
if(this.disabled){
return false;
}
_69=this._normalizeCommand(_69);
if(dojo.isIE&&_69=="formatblock"){
return this._local2NativeFormatNames[this.document.queryCommandValue(_69)];
}
return this.document.queryCommandValue(_69);
},placeCursorAtStart:function(){
this.focus();
var _6a=false;
if(dojo.isMoz){
var _6b=this.editNode.firstChild;
while(_6b){
if(_6b.nodeType==3){
if(_6b.nodeValue.replace(/^\s+|\s+$/g,"").length>0){
_6a=true;
dojo.withGlobal(this.window,"selectElement",dijit._editor.selection,[_6b]);
break;
}
}else{
if(_6b.nodeType==1){
_6a=true;
dojo.withGlobal(this.window,"selectElementChildren",dijit._editor.selection,[_6b]);
break;
}
}
_6b=_6b.nextSibling;
}
}else{
_6a=true;
dojo.withGlobal(this.window,"selectElementChildren",dijit._editor.selection,[this.editNode]);
}
if(_6a){
dojo.withGlobal(this.window,"collapse",dijit._editor.selection,[true]);
}
},placeCursorAtEnd:function(){
this.focus();
var _6c=false;
if(dojo.isMoz){
var _6d=this.editNode.lastChild;
while(_6d){
if(_6d.nodeType==3){
if(_6d.nodeValue.replace(/^\s+|\s+$/g,"").length>0){
_6c=true;
dojo.withGlobal(this.window,"selectElement",dijit._editor.selection,[_6d]);
break;
}
}else{
if(_6d.nodeType==1){
_6c=true;
if(_6d.lastChild){
dojo.withGlobal(this.window,"selectElement",dijit._editor.selection,[_6d.lastChild]);
}else{
dojo.withGlobal(this.window,"selectElement",dijit._editor.selection,[_6d]);
}
break;
}
}
_6d=_6d.previousSibling;
}
}else{
_6c=true;
dojo.withGlobal(this.window,"selectElementChildren",dijit._editor.selection,[this.editNode]);
}
if(_6c){
dojo.withGlobal(this.window,"collapse",dijit._editor.selection,[false]);
}
},getValue:function(_6e){
if(this.textarea){
if(this.isClosed||!this.isLoaded){
return this.textarea.value;
}
}
return this._postFilterContent(null,_6e);
},setValue:function(_6f){
if(!this.isLoaded){
this.onLoadDeferred.addCallback(dojo.hitch(this,function(){
this.setValue(_6f);
}));
return;
}
if(this.textarea&&(this.isClosed||!this.isLoaded)){
this.textarea.value=_6f;
}else{
_6f=this._preFilterContent(_6f);
var _70=this.isClosed?this.domNode:this.editNode;
_70.innerHTML=_6f;
this._preDomFilterContent(_70);
}
this.onDisplayChanged();
},replaceValue:function(_71){
if(this.isClosed){
this.setValue(_71);
}else{
if(this.window&&this.window.getSelection&&!dojo.isMoz){
this.setValue(_71);
}else{
if(this.window&&this.window.getSelection){
_71=this._preFilterContent(_71);
this.execCommand("selectall");
if(dojo.isMoz&&!_71){
_71="&nbsp;";
}
this.execCommand("inserthtml",_71);
this._preDomFilterContent(this.editNode);
}else{
if(this.document&&this.document.selection){
this.setValue(_71);
}
}
}
}
},_preFilterContent:function(_72){
var ec=_72;
dojo.forEach(this.contentPreFilters,function(ef){
if(ef){
ec=ef(ec);
}
});
return ec;
},_preDomFilterContent:function(dom){
dom=dom||this.editNode;
dojo.forEach(this.contentDomPreFilters,function(ef){
if(ef&&dojo.isFunction(ef)){
ef(dom);
}
},this);
},_postFilterContent:function(dom,_78){
var ec;
if(!dojo.isString(dom)){
dom=dom||this.editNode;
if(this.contentDomPostFilters.length){
if(_78&&dom["cloneNode"]){
dom=dom.cloneNode(true);
}
dojo.forEach(this.contentDomPostFilters,function(ef){
dom=ef(dom);
});
}
ec=dijit._editor.getChildrenHtml(dom);
}else{
ec=dom;
}
if(!ec.replace(/^(?:\s|\xA0)+/g,"").replace(/(?:\s|\xA0)+$/g,"").length){
ec="";
}
dojo.forEach(this.contentPostFilters,function(ef){
ec=ef(ec);
});
return ec;
},_saveContent:function(e){
var _7d=dojo.byId(dijit._scopeName+"._editor.RichText.savedContent");
_7d.value+=this._SEPARATOR+this.name+":"+this.getValue();
},escapeXml:function(str,_7f){
dojo.deprecated("dijit.Editor::escapeXml is deprecated","use dijit._editor.escapeXml instead",2);
return dijit._editor.escapeXml(str,_7f);
},getNodeHtml:function(_80){
dojo.deprecated("dijit.Editor::getNodeHtml is deprecated","use dijit._editor.getNodeHtml instead",2);
return dijit._editor.getNodeHtml(_80);
},getNodeChildrenHtml:function(dom){
dojo.deprecated("dijit.Editor::getNodeChildrenHtml is deprecated","use dijit._editor.getChildrenHtml instead",2);
return dijit._editor.getChildrenHtml(dom);
},close:function(_82,_83){
if(this.isClosed){
return false;
}
if(!arguments.length){
_82=true;
}
this._content=this.getValue();
var _84=(this.savedContent!=this._content);
if(this.interval){
clearInterval(this.interval);
}
if(this.textarea){
with(this.textarea.style){
position="";
left=top="";
if(dojo.isIE){
overflow=this.__overflow;
this.__overflow=null;
}
}
this.textarea.value=_82?this._content:this.savedContent;
dojo._destroyElement(this.domNode);
this.domNode=this.textarea;
}else{
this.domNode.innerHTML=_82?this._content:this.savedContent;
}
dojo.removeClass(this.domNode,"RichTextEditable");
this.isClosed=true;
this.isLoaded=false;
delete this.editNode;
if(this.window&&this.window._frameElement){
this.window._frameElement=null;
}
this.window=null;
this.document=null;
this.editingArea=null;
this.editorObject=null;
return _84;
},destroyRendering:function(){
},destroy:function(){
this.destroyRendering();
if(!this.isClosed){
this.close(false);
}
this.inherited("destroy",arguments);
},_removeMozBogus:function(_85){
return _85.replace(/\stype="_moz"/gi,"").replace(/\s_moz_dirty=""/gi,"");
},_removeSafariBogus:function(_86){
return _86.replace(/\sclass="webkit-block-placeholder"/gi,"");
},_fixContentForMoz:function(_87){
return _87.replace(/<(\/)?strong([ \>])/gi,"<$1b$2").replace(/<(\/)?em([ \>])/gi,"<$1i$2");
},_srcInImgRegex:/(?:(<img(?=\s).*?\ssrc=)("|')(.*?)\2)|(?:(<img\s.*?src=)([^"'][^ >]+))/gi,_hrefInARegex:/(?:(<a(?=\s).*?\shref=)("|')(.*?)\2)|(?:(<a\s.*?href=)([^"'][^ >]+))/gi,_preFixUrlAttributes:function(_88){
return _88.replace(this._hrefInARegex,"$1$4$2$3$5$2 _djrealurl=$2$3$5$2").replace(this._srcInImgRegex,"$1$4$2$3$5$2 _djrealurl=$2$3$5$2");
}});
}
