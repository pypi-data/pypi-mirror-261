/*
	Copyright (c) 2004-2008, The Dojo Foundation
	All Rights Reserved.

	Licensed under the Academic Free License version 2.1 or above OR the
	modified BSD license. For more information on Dojo licensing, see:

		http://dojotoolkit.org/book/dojo-book-0-9/introduction/licensing
*/


if(!dojo._hasResource["dojox.image.SlideShow"]){
dojo._hasResource["dojox.image.SlideShow"]=true;
dojo.provide("dojox.image.SlideShow");
dojo.require("dojo.string");
dojo.require("dojo.fx");
dojo.require("dijit._Widget");
dojo.require("dijit._Templated");
dojo.declare("dojox.image.SlideShow",[dijit._Widget,dijit._Templated],{imageHeight:375,imageWidth:500,title:"",titleTemplate:"${title} <span class=\"slideShowCounterText\">(${current} of ${total})</span>",noLink:false,loop:true,hasNav:true,images:[],pageSize:20,autoLoad:true,autoStart:false,fixedHeight:false,imageStore:null,linkAttr:"link",imageLargeAttr:"imageUrl",titleAttr:"title",slideshowInterval:3,templateString:"<div dojoAttachPoint=\"outerNode\" class=\"slideShowWrapper\">\n\t<div style=\"position:relative;\" dojoAttachPoint=\"innerWrapper\">\n\t\t<div class=\"slideShowNav\" dojoAttachEvent=\"onclick: _handleClick\">\n\t\t\t<div class=\"dijitInline slideShowTitle\" dojoAttachPoint=\"titleNode\">${title}</div>\n\t\t</div>\n\t\t<div dojoAttachPoint=\"navNode\" class=\"slideShowCtrl\" dojoAttachEvent=\"onclick: _handleClick\">\n\t\t\t<span dojoAttachPoint=\"navPrev\" class=\"slideShowCtrlPrev\"></span>\n\t\t\t<span dojoAttachPoint=\"navPlay\" class=\"slideShowCtrlPlay\"></span>\n\t\t\t<span dojoAttachPoint=\"navNext\" class=\"slideShowCtrlNext\"></span>\n\t\t</div>\n\t\t<div dojoAttachPoint=\"largeNode\" class=\"slideShowImageWrapper\"></div>\t\t\n\t\t<div dojoAttachPoint=\"hiddenNode\" class=\"slideShowHidden\"></div>\n\t</div>\n</div>\n",_tempImgPath:dojo.moduleUrl("dojo","resources/blank.gif"),_imageCounter:0,_tmpImage:null,_request:null,postCreate:function(){
this.inherited(arguments);
var _1=document.createElement("img");
_1.setAttribute("width",this.imageWidth);
_1.setAttribute("height",this.imageHeight);
if(this.hasNav){
dojo.connect(this.outerNode,"onmouseover",function(_2){
try{
_3._showNav();
}
catch(e){
}
});
dojo.connect(this.outerNode,"onmouseout",function(_4){
try{
_3._hideNav(_4);
}
catch(e){
}
});
}
this.outerNode.style.width=this.imageWidth+"px";
_1.setAttribute("src",this._tempImgPath);
var _3=this;
this.largeNode.appendChild(_1);
this._tmpImage=this._currentImage=_1;
this._fitSize(true);
this._loadImage(0,function(){
_3.showImage(0);
});
this._calcNavDimensions();
},setDataStore:function(_5,_6,_7){
this.reset();
var _8=this;
this._request={query:{},start:_6.start||0,count:_6.count||this.pageSize,onBegin:function(_9,_a){
_8.maxPhotos=_9;
}};
if(_6.query){
dojo.mixin(this._request.query,_6.query);
}
if(_7){
dojo.forEach(["imageLargeAttr","linkAttr","titleAttr"],function(_b){
if(_7[_b]){
this[_b]=_7[_b];
}
},this);
}
var _c=function(_d){
_8.showImage(0);
_8._request.onComplete=null;
if(_8.autoStart){
_8.toggleSlideShow();
}
};
this.imageStore=_5;
this._request.onComplete=_c;
this._request.start=0;
this.imageStore.fetch(this._request);
},reset:function(){
while(this.largeNode.firstChild){
this.largeNode.removeChild(this.largeNode.firstChild);
}
this.largeNode.appendChild(this._tmpImage);
while(this.hiddenNode.firstChild){
this.hiddenNode.removeChild(this.hiddenNode.firstChild);
}
dojo.forEach(this.images,function(_e){
if(_e&&_e.parentNode){
_e.parentNode.removeChild(_e);
}
});
this.images=[];
this.isInitialized=false;
this._imageCounter=0;
},isImageLoaded:function(_f){
return this.images&&this.images.length>_f&&this.images[_f];
},moveImageLoadingPointer:function(_10){
this._imageCounter=_10;
},destroy:function(){
if(this._slideId){
this._stop();
}
this.inherited(arguments);
},showNextImage:function(_11,_12){
if(_11&&this._timerCancelled){
return false;
}
if(this.imageIndex+1>=this.maxPhotos){
if(_11&&(this.loop||_12)){
this.imageIndex=-1;
}else{
if(this._slideId){
this._stop();
}
return false;
}
}
var _13=this;
this.showImage(this.imageIndex+1,function(){
if(_11){
_13._startTimer();
}
});
return true;
},toggleSlideShow:function(){
if(this._slideId){
this._stop();
}else{
dojo.toggleClass(this.domNode,"slideShowPaused");
this._timerCancelled=false;
var _14=this.showNextImage(true,true);
if(!_14){
this._stop();
}
}
},getShowTopicName:function(){
return (this.widgetId||this.id)+"/imageShow";
},getLoadTopicName:function(){
return (this.widgetId?this.widgetId:this.id)+"/imageLoad";
},showImage:function(_15,_16){
if(!_16&&this._slideId){
this.toggleSlideShow();
}
var _17=this;
var _18=this.largeNode.getElementsByTagName("div");
this.imageIndex=_15;
var _19=function(){
if(_17.images[_15]){
while(_17.largeNode.firstChild){
_17.largeNode.removeChild(_17.largeNode.firstChild);
}
_17.images[_15].style.opacity=0;
_17.largeNode.appendChild(_17.images[_15]);
_17._currentImage=_17.images[_15]._img;
_17._fitSize();
var _1a=function(a,b,c){
var img=_17.images[_15].firstChild;
if(img.tagName.toLowerCase()!="img"){
img=img.firstChild;
}
title=img.getAttribute("title");
if(_17._navShowing){
_17._showNav(true);
}
dojo.publish(_17.getShowTopicName(),[{index:_15,title:title,url:img.getAttribute("src")}]);
if(_16){
_16(a,b,c);
}
_17._setTitle(title);
};
dojo.fadeIn({node:_17.images[_15],duration:300,onEnd:_1a}).play();
}else{
_17._loadImage(_15,function(){
dojo.publish(_17.getLoadTopicName(),[_15]);
_17.showImage(_15,_16);
});
}
};
if(_18&&_18.length>0){
dojo.fadeOut({node:_18[0],duration:300,onEnd:function(){
_17.hiddenNode.appendChild(_18[0]);
_19();
}}).play();
}else{
_19();
}
},_fitSize:function(_1f){
if(!this.fixedHeight||_1f){
var _20=(this._currentImage.height+(this.hasNav?20:0));
dojo.style(this.innerWrapper,"height",_20+"px");
return;
}
dojo.style(this.largeNode,"paddingTop",this._getTopPadding()+"px");
},_getTopPadding:function(){
if(!this.fixedHeight){
return 0;
}
return (this.imageHeight-this._currentImage.height)/2;
},_loadNextImage:function(){
if(!this.autoLoad){
return;
}
while(this.images.length>=this._imageCounter&&this.images[this._imageCounter]){
this._imageCounter++;
}
this._loadImage(this._imageCounter);
},_loadImage:function(_21,_22){
if(this.images[_21]||!this._request){
return;
}
var _23=_21-(_21%this.pageSize);
this._request.start=_23;
this._request.onComplete=function(_24){
var _25=_21-_23;
if(_24&&_24.length>_25){
_26(_24[_25]);
}else{
}
};
var _27=this;
var _26=function(_28){
var url=_27.imageStore.getValue(_28,_27.imageLargeAttr);
var img=document.createElement("img");
var div=document.createElement("div");
div._img=img;
var _2c=_27.imageStore.getValue(_28,_27.linkAttr);
if(!_2c||_27.noLink){
div.appendChild(img);
}else{
var a=document.createElement("a");
a.setAttribute("href",_2c);
a.setAttribute("target","_blank");
div.appendChild(a);
a.appendChild(img);
}
div.setAttribute("id",_27.id+"_imageDiv"+_21);
dojo.connect(img,"onload",function(){
_27._fitImage(img);
div.setAttribute("width",_27.imageWidth);
div.setAttribute("height",_27.imageHeight);
dojo.publish(_27.getLoadTopicName(),[_21]);
_27._loadNextImage();
if(_22){
_22();
}
});
_27.hiddenNode.appendChild(div);
var _2e=document.createElement("div");
dojo.addClass(_2e,"slideShowTitle");
div.appendChild(_2e);
_27.images[_21]=div;
img.setAttribute("src",url);
var _2f=_27.imageStore.getValue(_28,_27.titleAttr);
if(_2f){
img.setAttribute("title",_2f);
}
};
this.imageStore.fetch(this._request);
},_stop:function(){
if(this._slideId){
clearTimeout(this._slideId);
}
this._slideId=null;
this._timerCancelled=true;
dojo.removeClass(this.domNode,"slideShowPaused");
},_prev:function(){
if(this.imageIndex<1){
return;
}
this.showImage(this.imageIndex-1);
},_next:function(){
this.showNextImage();
},_startTimer:function(){
var id=this.id;
this._slideId=setTimeout(function(){
dijit.byId(id).showNextImage(true);
},this.slideshowInterval*1000);
},_calcNavDimensions:function(){
dojo.style(this.navNode,"position","absolute");
dojo.style(this.navNode,"top","-10000px");
dojo._setOpacity(this.navNode,99);
this.navPlay._size=dojo.marginBox(this.navPlay);
this.navPrev._size=dojo.marginBox(this.navPrev);
this.navNext._size=dojo.marginBox(this.navNext);
dojo._setOpacity(this.navNode,0);
dojo.style(this.navNode,"position","");
dojo.style(this.navNode,"top","");
},_setTitle:function(_31){
this.titleNode.innerHTML=dojo.string.substitute(this.titleTemplate,{title:_31,current:1+this.imageIndex,total:this.maxPhotos});
},_fitImage:function(img){
var _33=img.width;
var _34=img.height;
if(_33>this.imageWidth){
_34=Math.floor(_34*(this.imageWidth/_33));
img.setAttribute("height",_34+"px");
img.setAttribute("width",this.imageWidth+"px");
}
if(_34>this.imageHeight){
_33=Math.floor(_33*(this.imageHeight/_34));
img.setAttribute("height",this.imageHeight+"px");
img.setAttribute("width",_33+"px");
}
},_handleClick:function(e){
switch(e.target){
case this.navNext:
this._next();
break;
case this.navPrev:
this._prev();
break;
case this.navPlay:
this.toggleSlideShow();
break;
}
},_showNav:function(_36){
if(this._navShowing&&!_36){
return;
}
dojo.style(this.navNode,"marginTop","0px");
dojo.style(this.navPlay,"marginLeft","0px");
var _37=dojo.marginBox(this.outerNode);
var _38=this._currentImage.height-this.navPlay._size.h-10+this._getTopPadding();
if(_38>this._currentImage.height){
_38+=10;
}
dojo[this.imageIndex<1?"addClass":"removeClass"](this.navPrev,"slideShowCtrlHide");
dojo[this.imageIndex+1>=this.maxPhotos?"addClass":"removeClass"](this.navNext,"slideShowCtrlHide");
var _39=this;
if(this._navAnim){
this._navAnim.stop();
}
if(this._navShowing){
return;
}
this._navAnim=dojo.fadeIn({node:this.navNode,duration:300,onEnd:function(){
_39._navAnim=null;
}});
this._navAnim.play();
this._navShowing=true;
},_hideNav:function(e){
if(!e||!this._overElement(this.outerNode,e)){
var _3b=this;
if(this._navAnim){
this._navAnim.stop();
}
this._navAnim=dojo.fadeOut({node:this.navNode,duration:300,onEnd:function(){
_3b._navAnim=null;
}});
this._navAnim.play();
this._navShowing=false;
}
},_overElement:function(_3c,e){
if(typeof (dojo)=="undefined"){
return false;
}
_3c=dojo.byId(_3c);
var m={x:e.pageX,y:e.pageY};
var bb=dojo._getBorderBox(_3c);
var _40=dojo.coords(_3c,true);
var _41=_40.x;
return (m.x>=_41&&m.x<=(_41+bb.w)&&m.y>=_40.y&&m.y<=(top+bb.h));
}});
}
