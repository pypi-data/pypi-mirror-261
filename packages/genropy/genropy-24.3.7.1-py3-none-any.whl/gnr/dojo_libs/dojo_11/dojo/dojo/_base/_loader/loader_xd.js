/*
	Copyright (c) 2004-2008, The Dojo Foundation
	All Rights Reserved.

	Licensed under the Academic Free License version 2.1 or above OR the
	modified BSD license. For more information on Dojo licensing, see:

		http://dojotoolkit.org/book/dojo-book-0-9/introduction/licensing
*/


if(!dojo._hasResource["dojo._base._loader.loader_xd"]){
dojo._hasResource["dojo._base._loader.loader_xd"]=true;
dojo.provide("dojo._base._loader.loader_xd");
dojo._xdReset=function(){
this._isXDomain=dojo.config.useXDomain||false;
this._xdTimer=0;
this._xdInFlight={};
this._xdOrderedReqs=[];
this._xdDepMap={};
this._xdContents=[];
this._xdDefList=[];
};
dojo._xdReset();
dojo._xdCreateResource=function(_1,_2,_3){
var _4=_1.replace(/(\/\*([\s\S]*?)\*\/|\/\/(.*)$)/mg,"");
var _5=[];
var _6=/dojo.(require|requireIf|provide|requireAfterIf|platformRequire|requireLocalization)\(([\w\W]*?)\)/mg;
var _7;
while((_7=_6.exec(_4))!=null){
if(_7[1]=="requireLocalization"){
eval(_7[0]);
}else{
_5.push("\""+_7[1]+"\", "+_7[2]);
}
}
var _8=[];
_8.push(dojo._scopeName+"._xdResourceLoaded({\n");
if(_5.length>0){
_8.push("depends: [");
for(var i=0;i<_5.length;i++){
if(i>0){
_8.push(",\n");
}
_8.push("["+_5[i]+"]");
}
_8.push("],");
}
_8.push("\ndefineResource: function("+dojo._scopePrefixArgs+"){");
if(!dojo.config["debugAtAllCosts"]||_2=="dojo._base._loader.loader_debug"){
_8.push(_1);
}
_8.push("\n}, resourceName: '"+_2+"', resourcePath: '"+_3+"'});");
return _8.join("");
};
dojo._xdIsXDomainPath=function(_a){
var _b=_a.indexOf(":");
var _c=_a.indexOf("/");
if(_b>0&&_b<_c){
return true;
}else{
var _d=this.baseUrl;
_b=_d.indexOf(":");
_c=_d.indexOf("/");
if(_b>0&&_b<_c&&(!location.host||_d.indexOf("http://"+location.host)!=0)){
return true;
}
}
return false;
};
dojo._loadPath=function(_e,_f,cb){
var _11=this._xdIsXDomainPath(_e);
this._isXDomain|=_11;
var uri=((_e.charAt(0)=="/"||_e.match(/^\w+:/))?"":this.baseUrl)+_e;
try{
return ((!_f||this._isXDomain)?this._loadUri(uri,cb,_11,_f):this._loadUriAndCheck(uri,_f,cb));
}
catch(e){
console.debug(e);
return false;
}
};
dojo._loadUri=function(uri,cb,_15,_16){
if(this._loadedUrls[uri]){
return 1;
}
if(this._isXDomain&&_16&&_16!="dojo.i18n"){
this._xdOrderedReqs.push(_16);
if(_15||uri.indexOf("/nls/")==-1){
this._xdInFlight[_16]=true;
this._inFlightCount++;
}
if(!this._xdTimer){
if(dojo.isAIR){
this._xdTimer=setInterval(function(){
dojo._xdWatchInFlight();
},100);
}else{
this._xdTimer=setInterval(dojo._scopeName+"._xdWatchInFlight();",100);
}
}
this._xdStartTime=(new Date()).getTime();
}
if(_15){
var _17=uri.lastIndexOf(".");
if(_17<=0){
_17=uri.length-1;
}
var _18=uri.substring(0,_17)+".xd";
if(_17!=uri.length-1){
_18+=uri.substring(_17,uri.length);
}
if(dojo.isAIR){
_18=_18.replace("app:/","/");
}
var _19=document.createElement("script");
_19.type="text/javascript";
_19.src=_18;
if(!this.headElement){
this._headElement=document.getElementsByTagName("head")[0];
if(!this._headElement){
this._headElement=document.getElementsByTagName("html")[0];
}
}
this._headElement.appendChild(_19);
}else{
var _1a=this._getText(uri,null,true);
if(_1a==null){
return 0;
}
if(this._isXDomain&&uri.indexOf("/nls/")==-1&&_16!="dojo.i18n"){
var res=this._xdCreateResource(_1a,_16,uri);
dojo.eval(res);
}else{
if(cb){
_1a="("+_1a+")";
}else{
_1a=this._scopePrefix+_1a+this._scopeSuffix;
}
var _1c=dojo["eval"](_1a+"\r\n//@ sourceURL="+uri);
if(cb){
cb(_1c);
}
}
}
this._loadedUrls[uri]=true;
this._loadedUrls.push(uri);
return true;
};
dojo._xdResourceLoaded=function(res){
var _1e=res.depends;
var _1f=null;
var _20=null;
var _21=[];
if(_1e&&_1e.length>0){
var dep=null;
var _23=0;
var _24=false;
for(var i=0;i<_1e.length;i++){
dep=_1e[i];
if(dep[0]=="provide"){
_21.push(dep[1]);
}else{
if(!_1f){
_1f=[];
}
if(!_20){
_20=[];
}
var _26=this._xdUnpackDependency(dep);
if(_26.requires){
_1f=_1f.concat(_26.requires);
}
if(_26.requiresAfter){
_20=_20.concat(_26.requiresAfter);
}
}
var _27=dep[0];
var _28=_27.split(".");
if(_28.length==2){
dojo[_28[0]][_28[1]].apply(dojo[_28[0]],dep.slice(1));
}else{
dojo[_27].apply(dojo,dep.slice(1));
}
}
if(_21.length==1&&_21[0]=="dojo._base._loader.loader_debug"){
res.defineResource(dojo);
}else{
var _29=this._xdContents.push({content:res.defineResource,resourceName:res["resourceName"],resourcePath:res["resourcePath"],isDefined:false})-1;
for(var i=0;i<_21.length;i++){
this._xdDepMap[_21[i]]={requires:_1f,requiresAfter:_20,contentIndex:_29};
}
}
for(var i=0;i<_21.length;i++){
this._xdInFlight[_21[i]]=false;
}
}
};
dojo._xdLoadFlattenedBundle=function(_2a,_2b,_2c,_2d){
_2c=_2c||"root";
var _2e=dojo.i18n.normalizeLocale(_2c).replace("-","_");
var _2f=[_2a,"nls",_2b].join(".");
var _30=dojo["provide"](_2f);
_30[_2e]=_2d;
var _31=[_2a,_2e,_2b].join(".");
var _32=dojo._xdBundleMap[_31];
if(_32){
for(var _33 in _32){
_30[_33]=_2d;
}
}
};
dojo._xdInitExtraLocales=function(){
var _34=dojo.config.extraLocale;
if(_34){
if(!_34 instanceof Array){
_34=[_34];
}
dojo._xdReqLoc=dojo.xdRequireLocalization;
dojo.xdRequireLocalization=function(m,b,_37,_38){
dojo._xdReqLoc(m,b,_37,_38);
if(_37){
return;
}
for(var i=0;i<_34.length;i++){
dojo._xdReqLoc(m,b,_34[i],_38);
}
};
}
};
dojo._xdBundleMap={};
dojo.xdRequireLocalization=function(_3a,_3b,_3c,_3d){
if(dojo._xdInitExtraLocales){
dojo._xdInitExtraLocales();
dojo._xdInitExtraLocales=null;
dojo.xdRequireLocalization.apply(dojo,arguments);
return;
}
var _3e=_3d.split(",");
var _3f=dojo.i18n.normalizeLocale(_3c);
var _40="";
for(var i=0;i<_3e.length;i++){
if(_3f.indexOf(_3e[i])==0){
if(_3e[i].length>_40.length){
_40=_3e[i];
}
}
}
var _42=_40.replace("-","_");
var _43=dojo.getObject([_3a,"nls",_3b].join("."));
if(_43&&_43[_42]){
bundle[_3f.replace("-","_")]=_43[_42];
}else{
var _44=[_3a,(_42||"root"),_3b].join(".");
var _45=dojo._xdBundleMap[_44];
if(!_45){
_45=dojo._xdBundleMap[_44]={};
}
_45[_3f.replace("-","_")]=true;
dojo.require(_3a+".nls"+(_40?"."+_40:"")+"."+_3b);
}
};
dojo._xdRealRequireLocalization=dojo.requireLocalization;
dojo.requireLocalization=function(_46,_47,_48,_49){
var _4a=this.moduleUrl(_46).toString();
if(this._xdIsXDomainPath(_4a)){
return dojo.xdRequireLocalization.apply(dojo,arguments);
}else{
return dojo._xdRealRequireLocalization.apply(dojo,arguments);
}
};
dojo._xdUnpackDependency=function(dep){
var _4c=null;
var _4d=null;
switch(dep[0]){
case "requireIf":
case "requireAfterIf":
if(dep[1]===true){
_4c=[{name:dep[2],content:null}];
}
break;
case "platformRequire":
var _4e=dep[1];
var _4f=_4e["common"]||[];
var _4c=(_4e[dojo.hostenv.name_])?_4f.concat(_4e[dojo.hostenv.name_]||[]):_4f.concat(_4e["default"]||[]);
if(_4c){
for(var i=0;i<_4c.length;i++){
if(_4c[i] instanceof Array){
_4c[i]={name:_4c[i][0],content:null};
}else{
_4c[i]={name:_4c[i],content:null};
}
}
}
break;
case "require":
_4c=[{name:dep[1],content:null}];
break;
case "i18n._preloadLocalizations":
dojo.i18n._preloadLocalizations.apply(dojo.i18n._preloadLocalizations,dep.slice(1));
break;
}
if(dep[0]=="requireAfterIf"||dep[0]=="requireIf"){
_4d=_4c;
_4c=null;
}
return {requires:_4c,requiresAfter:_4d};
};
dojo._xdWalkReqs=function(){
var _51=null;
var req;
for(var i=0;i<this._xdOrderedReqs.length;i++){
req=this._xdOrderedReqs[i];
if(this._xdDepMap[req]){
_51=[req];
_51[req]=true;
this._xdEvalReqs(_51);
}
}
};
dojo._xdEvalReqs=function(_54){
while(_54.length>0){
var req=_54[_54.length-1];
var res=this._xdDepMap[req];
if(res){
var _57=res.requires;
if(_57&&_57.length>0){
var _58;
for(var i=0;i<_57.length;i++){
_58=_57[i].name;
if(_58&&!_54[_58]){
_54.push(_58);
_54[_58]=true;
this._xdEvalReqs(_54);
}
}
}
var _5a=this._xdContents[res.contentIndex];
if(!_5a.isDefined){
var _5b=_5a.content;
_5b["resourceName"]=_5a["resourceName"];
_5b["resourcePath"]=_5a["resourcePath"];
this._xdDefList.push(_5b);
_5a.isDefined=true;
}
this._xdDepMap[req]=null;
var _57=res.requiresAfter;
if(_57&&_57.length>0){
var _58;
for(var i=0;i<_57.length;i++){
_58=_57[i].name;
if(_58&&!_54[_58]){
_54.push(_58);
_54[_58]=true;
this._xdEvalReqs(_54);
}
}
}
}
_54.pop();
}
};
dojo._xdClearInterval=function(){
clearInterval(this._xdTimer);
this._xdTimer=0;
};
dojo._xdWatchInFlight=function(){
var _5c="";
var _5d=(dojo.config.xdWaitSeconds||15)*1000;
var _5e=(this._xdStartTime+_5d)<(new Date()).getTime();
for(var _5f in this._xdInFlight){
if(this._xdInFlight[_5f]===true){
if(_5e){
_5c+=_5f+" ";
}else{
return;
}
}
}
this._xdClearInterval();
if(_5e){
throw "Could not load cross-domain resources: "+_5c;
}
this._xdWalkReqs();
var _60=this._xdDefList.length;
for(var i=0;i<_60;i++){
var _62=dojo._xdDefList[i];
if(dojo.config["debugAtAllCosts"]&&_62["resourceName"]){
if(!this["_xdDebugQueue"]){
this._xdDebugQueue=[];
}
this._xdDebugQueue.push({resourceName:_62.resourceName,resourcePath:_62.resourcePath});
}else{
_62.apply(dojo.global,dojo._scopeArgs);
}
}
for(var i=0;i<this._xdContents.length;i++){
var _63=this._xdContents[i];
if(_63.content&&!_63.isDefined){
_63.content.apply(dojo.global,dojo._scopeArgs);
}
}
this._xdReset();
if(this["_xdDebugQueue"]&&this._xdDebugQueue.length>0){
this._xdDebugFileLoaded();
}else{
this._xdNotifyLoaded();
}
};
dojo._xdNotifyLoaded=function(){
this._inFlightCount=0;
if(this._initFired&&!this._loadNotifying){
this._callLoaded();
}
};
}
