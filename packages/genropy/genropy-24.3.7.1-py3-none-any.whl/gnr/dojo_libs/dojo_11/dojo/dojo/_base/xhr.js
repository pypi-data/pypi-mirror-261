/*
	Copyright (c) 2004-2008, The Dojo Foundation
	All Rights Reserved.

	Licensed under the Academic Free License version 2.1 or above OR the
	modified BSD license. For more information on Dojo licensing, see:

		http://dojotoolkit.org/book/dojo-book-0-9/introduction/licensing
*/


if(!dojo._hasResource["dojo._base.xhr"]){
dojo._hasResource["dojo._base.xhr"]=true;
dojo.provide("dojo._base.xhr");
dojo.require("dojo._base.Deferred");
dojo.require("dojo._base.json");
dojo.require("dojo._base.lang");
dojo.require("dojo._base.query");
(function(){
var _d=dojo;
function setValue(_2,_3,_4){
var _5=_2[_3];
if(_d.isString(_5)){
_2[_3]=[_5,_4];
}else{
if(_d.isArray(_5)){
_5.push(_4);
}else{
_2[_3]=_4;
}
}
};
dojo.formToObject=function(_6){
var _7={};
var iq="input:not([type=file]):not([type=submit]):not([type=image]):not([type=reset]):not([type=button]), select, textarea";
_d.query(iq,_6).filter(function(_9){
return !_9.disabled&&_9.name;
}).forEach(function(_a){
var _b=_a.name;
var _c=(_a.type||"").toLowerCase();
if(_c=="radio"||_c=="checkbox"){
if(_a.checked){
setValue(_7,_b,_a.value);
}
}else{
if(_a.multiple){
_7[_b]=[];
_d.query("option",_a).forEach(function(_d){
if(_d.selected){
setValue(_7,_b,_d.value);
}
});
}else{
setValue(_7,_b,_a.value);
if(_c=="image"){
_7[_b+".x"]=_7[_b+".y"]=_7[_b].x=_7[_b].y=0;
}
}
}
});
return _7;
};
dojo.objectToQuery=function(_e){
var _f=encodeURIComponent;
var _10=[];
var _11={};
for(var _12 in _e){
var _13=_e[_12];
if(_13!=_11[_12]){
var _14=_f(_12)+"=";
if(_d.isArray(_13)){
for(var i=0;i<_13.length;i++){
_10.push(_14+_f(_13[i]));
}
}else{
_10.push(_14+_f(_13));
}
}
}
return _10.join("&");
};
dojo.formToQuery=function(_16){
return _d.objectToQuery(_d.formToObject(_16));
};
dojo.formToJson=function(_17,_18){
return _d.toJson(_d.formToObject(_17),_18);
};
dojo.queryToObject=function(str){
var ret={};
var qp=str.split("&");
var dec=decodeURIComponent;
_d.forEach(qp,function(_1d){
if(_1d.length){
var _1e=_1d.split("=");
var _1f=dec(_1e.shift());
var val=dec(_1e.join("="));
if(_d.isString(ret[_1f])){
ret[_1f]=[ret[_1f]];
}
if(_d.isArray(ret[_1f])){
ret[_1f].push(val);
}else{
ret[_1f]=val;
}
}
});
return ret;
};
dojo._blockAsync=false;
dojo._contentHandlers={"text":function(xhr){
return xhr.responseText;
},"json":function(xhr){
if(!dojo.config.usePlainJson){
console.warn("Consider using mimetype:text/json-comment-filtered"+" to avoid potential security issues with JSON endpoints"+" (use djConfig.usePlainJson=true to turn off this message)");
}
return (xhr.status==204)?undefined:_d.fromJson(xhr.responseText);
},"json-comment-filtered":function(xhr){
var _24=xhr.responseText;
var _25=_24.indexOf("/*");
var _26=_24.lastIndexOf("*/");
if(_25==-1||_26==-1){
throw new Error("JSON was not comment filtered");
}
return (xhr.status==204)?undefined:_d.fromJson(_24.substring(_25+2,_26));
},"javascript":function(xhr){
return _d.eval(xhr.responseText);
},"xml":function(xhr){
var _29=xhr.responseXML;
if(_d.isIE&&(!_29||window.location.protocol=="file:")){
_d.forEach(["MSXML2","Microsoft","MSXML","MSXML3"],function(_2a){
try{
var dom=new ActiveXObject(_2a+".XMLDOM");
dom.async=false;
dom.loadXML(xhr.responseText);
_29=dom;
}
catch(e){
}
});
}
return _29;
}};
dojo._contentHandlers["json-comment-optional"]=function(xhr){
var _2d=_d._contentHandlers;
try{
return _2d["json-comment-filtered"](xhr);
}
catch(e){
return _2d["json"](xhr);
}
};
dojo._ioSetArgs=function(_2e,_2f,_30,_31){
var _32={args:_2e,url:_2e.url};
var _33=null;
if(_2e.form){
var _34=_d.byId(_2e.form);
var _35=_34.getAttributeNode("action");
_32.url=_32.url||(_35?_35.value:null);
_33=_d.formToObject(_34);
}
var _36=[{}];
if(_33){
_36.push(_33);
}
if(_2e.content){
_36.push(_2e.content);
}
if(_2e.preventCache){
_36.push({"dojo.preventCache":new Date().valueOf()});
}
_32.query=_d.objectToQuery(_d.mixin.apply(null,_36));
_32.handleAs=_2e.handleAs||"text";
var d=new _d.Deferred(_2f);
d.addCallbacks(_30,function(_38){
return _31(_38,d);
});
var ld=_2e.load;
if(ld&&_d.isFunction(ld)){
d.addCallback(function(_3a){
return ld.call(_2e,_3a,_32);
});
}
var err=_2e.error;
if(err&&_d.isFunction(err)){
d.addErrback(function(_3c){
return err.call(_2e,_3c,_32);
});
}
var _3d=_2e.handle;
if(_3d&&_d.isFunction(_3d)){
d.addBoth(function(_3e){
return _3d.call(_2e,_3e,_32);
});
}
d.ioArgs=_32;
return d;
};
var _3f=function(dfd){
dfd.canceled=true;
var xhr=dfd.ioArgs.xhr;
var _at=typeof xhr.abort;
if(_at=="function"||_at=="unknown"){
xhr.abort();
}
var err=new Error("xhr cancelled");
err.dojoType="cancel";
return err;
};
var _44=function(dfd){
return _d._contentHandlers[dfd.ioArgs.handleAs](dfd.ioArgs.xhr);
};
var _46=function(_47,dfd){
console.debug(_47);
return _47;
};
var _49=function(_4a){
var dfd=_d._ioSetArgs(_4a,_3f,_44,_46);
dfd.ioArgs.xhr=_d._xhrObj(dfd.ioArgs.args);
return dfd;
};
var _4c=null;
var _4d=[];
var _4e=function(){
var now=(new Date()).getTime();
if(!_d._blockAsync){
for(var i=0,tif;i<_4d.length&&(tif=_4d[i]);i++){
var dfd=tif.dfd;
try{
if(!dfd||dfd.canceled||!tif.validCheck(dfd)){
_4d.splice(i--,1);
}else{
if(tif.ioCheck(dfd)){
_4d.splice(i--,1);
tif.resHandle(dfd);
}else{
if(dfd.startTime){
if(dfd.startTime+(dfd.ioArgs.args.timeout||0)<now){
_4d.splice(i--,1);
var err=new Error("timeout exceeded");
err.dojoType="timeout";
dfd.errback(err);
dfd.cancel();
}
}
}
}
}
catch(e){
console.debug(e);
dfd.errback(new Error("_watchInFlightError!"));
}
}
}
if(!_4d.length){
clearInterval(_4c);
_4c=null;
return;
}
};
dojo._ioCancelAll=function(){
try{
_d.forEach(_4d,function(i){
i.dfd.cancel();
});
}
catch(e){
}
};
if(_d.isIE){
_d.addOnUnload(_d._ioCancelAll);
}
_d._ioWatch=function(dfd,_56,_57,_58){
if(dfd.ioArgs.args.timeout){
dfd.startTime=(new Date()).getTime();
}
_4d.push({dfd:dfd,validCheck:_56,ioCheck:_57,resHandle:_58});
if(!_4c){
_4c=setInterval(_4e,50);
}
_4e();
};
var _59="application/x-www-form-urlencoded";
var _5a=function(dfd){
return dfd.ioArgs.xhr.readyState;
};
var _5c=function(dfd){
return 4==dfd.ioArgs.xhr.readyState;
};
var _5e=function(dfd){
var xhr=dfd.ioArgs.xhr;
if(_d._isDocumentOk(xhr)){
dfd.callback(dfd);
}else{
var err=new Error("Unable to load "+dfd.ioArgs.url+" status:"+xhr.status);
err.status=xhr.status;
err.responseText=xhr.responseText;
dfd.errback(err);
}
};
var _62=function(_63,dfd){
var _65=dfd.ioArgs;
var _66=_65.args;
var xhr=_65.xhr;
xhr.open(_63,_65.url,_66.sync!==true,_66.user||undefined,_66.password||undefined);
if(_66.headers){
for(var hdr in _66.headers){
if(hdr.toLowerCase()==="content-type"&&!_66.contentType){
_66.contentType=_66.headers[hdr];
}else{
xhr.setRequestHeader(hdr,_66.headers[hdr]);
}
}
}
xhr.setRequestHeader("Content-Type",_66.contentType||_59);
if(!_66.headers||!_66.headers["X-Requested-With"]){
xhr.setRequestHeader("X-Requested-With","XMLHttpRequest");
}
try{
xhr.send(_65.query);
}
catch(e){
dfd.cancel();
}
_d._ioWatch(dfd,_5a,_5c,_5e);
xhr=null;
return dfd;
};
dojo._ioAddQueryToUrl=function(_69){
if(_69.query.length){
_69.url+=(_69.url.indexOf("?")==-1?"?":"&")+_69.query;
_69.query=null;
}
};
dojo.xhr=function(_6a,_6b,_6c){
var dfd=_49(_6b);
if(!_6c){
_d._ioAddQueryToUrl(dfd.ioArgs);
}
return _62(_6a,dfd);
};
dojo.xhrGet=function(_6e){
return _d.xhr("GET",_6e);
};
dojo.xhrPost=function(_6f){
return _d.xhr("POST",_6f,true);
};
dojo.rawXhrPost=function(_70){
var dfd=_49(_70);
dfd.ioArgs.query=_70.postData;
return _62("POST",dfd);
};
dojo.xhrPut=function(_72){
return _d.xhr("PUT",_72,true);
};
dojo.rawXhrPut=function(_73){
var dfd=_49(_73);
var _75=dfd.ioArgs;
if(_73.putData){
_75.query=_73.putData;
_73.putData=null;
}
return _62("PUT",dfd);
};
dojo.xhrDelete=function(_76){
return _d.xhr("DELETE",_76);
};
})();
}
