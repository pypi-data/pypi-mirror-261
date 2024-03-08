/*
	Copyright (c) 2004-2008, The Dojo Foundation
	All Rights Reserved.

	Licensed under the Academic Free License version 2.1 or above OR the
	modified BSD license. For more information on Dojo licensing, see:

		http://dojotoolkit.org/book/dojo-book-0-9/introduction/licensing
*/


if(!dojo._hasResource["dojox.data.SnapLogicStore"]){
dojo._hasResource["dojox.data.SnapLogicStore"]=true;
dojo.provide("dojox.data.SnapLogicStore");
dojo.require("dojo.io.script");
dojo.require("dojo.data.util.sorter");
dojo.declare("dojox.data.SnapLogicStore",null,{Parts:{DATA:"data",COUNT:"count"},url:"",constructor:function(_1){
if(_1.url){
this.url=_1.url;
}
this._parameters=_1.parameters;
},_assertIsItem:function(_2){
if(!this.isItem(_2)){
throw new Error("dojox.data.SnapLogicStore: a function was passed an item argument that was not an item");
}
},_assertIsAttribute:function(_3){
if(typeof _3!=="string"){
throw new Error("dojox.data.SnapLogicStore: a function was passed an attribute argument that was not an attribute name string");
}
},getFeatures:function(){
return {"dojo.data.api.Read":true};
},getValue:function(_4,_5){
this._assertIsItem(_4);
this._assertIsAttribute(_5);
i=dojo.indexOf(_4.attributes,_5);
if(i!==-1){
return _4.values[i];
}
return undefined;
},getAttributes:function(_6){
this._assertIsItem(_6);
return _6.attributes;
},hasAttribute:function(_7,_8){
this._assertIsItem(_7);
this._assertIsAttribute(_8);
for(var i=0;i<_7.attributes.length;++i){
if(_8==_7.attributes[i]){
return true;
}
}
return false;
},isItemLoaded:function(_a){
return this.isItem(_a);
},loadItem:function(_b){
},getLabel:function(_c){
return undefined;
},getLabelAttributes:function(_d){
return null;
},containsValue:function(_e,_f,_10){
return this.getValue(_e,_f)===_10;
},getValues:function(_11,_12){
this._assertIsItem(_11);
this._assertIsAttribute(_12);
i=dojo.indexOf(_11.attributes,_12);
if(i!==-1){
return [_11.values[i]];
}
return undefined;
},isItem:function(_13){
if(_13&&_13._store===this){
return true;
}
return false;
},close:function(_14){
},_fetchHandler:function(_15){
var _16=_15.scope||dojo.global;
if(_15.onBegin){
_15.onBegin.call(_16,_15._countResponse[0],_15);
}
if(_15.onItem||_15.onComplete){
response=_15._dataResponse;
if(!response.length){
_15.onError.call(_16,new Error("dojox.data.SnapLogicStore: invalid response of length 0"),_15);
return;
}else{
if(_15.query!="record count"){
field_names=response.shift();
var _17=[];
for(var i=0;i<response.length;++i){
if(_15._aborted){
break;
}
_17.push({attributes:field_names,values:response[i],_store:this});
}
if(_15.sort&&!_15._aborted){
_17.sort(dojo.data.util.sorter.createSortFunction(_15.sort,self));
}
}else{
_17=[({attributes:["count"],values:response,_store:this})];
}
}
if(_15.onItem){
for(var i=0;i<_17.length;++i){
if(_15._aborted){
break;
}
_15.onItem.call(_16,_17[i],_15);
}
_17=null;
}
if(_15.onComplete&&!_15._aborted){
_15.onComplete.call(_16,_17,_15);
}
}
},_partHandler:function(_19,_1a,_1b){
if(_1b instanceof Error){
if(_1a==this.Parts.DATA){
_19._dataHandle=null;
}else{
_19._countHandle=null;
}
_19._aborted=true;
if(_19.onError){
_19.onError.call(_19.scope,_1b,_19);
}
}else{
if(_19._aborted){
return;
}
if(_1a==this.Parts.DATA){
_19._dataResponse=_1b;
}else{
_19._countResponse=_1b;
}
if((!_19._dataHandle||_19._dataResponse!==null)&&(!_19._countHandle||_19._countResponse!==null)){
this._fetchHandler(_19);
}
}
},fetch:function(_1c){
_1c._countResponse=null;
_1c._dataResponse=null;
_1c._aborted=false;
_1c.abort=function(){
if(!_1c._aborted){
_1c._aborted=true;
if(_1c._dataHandle&&_1c._dataHandle.cancel){
_1c._dataHandle.cancel();
}
if(_1c._countHandle&&_1c._countHandle.cancel){
_1c._countHandle.cancel();
}
}
};
if(_1c.onItem||_1c.onComplete){
var _1d=this._parameters||{};
if(_1c.start){
if(_1c.start<0){
throw new Error("dojox.data.SnapLogicStore: request start value must be 0 or greater");
}
_1d["sn.start"]=_1c.start+1;
}
if(_1c.count){
if(_1c.count<0){
throw new Error("dojox.data.SnapLogicStore: request count value 0 or greater");
}
_1d["sn.limit"]=_1c.count;
}
_1d["sn.content_type"]="application/javascript";
var _1e=this;
var _1f=function(_20,_21){
if(_20 instanceof Error){
_1e._fetchHandler(_20,_1c);
}
};
var _22={url:this.url,content:_1d,timeout:60000,callbackParamName:"sn.stream_header",handle:dojo.hitch(this,"_partHandler",_1c,this.Parts.DATA)};
_1c._dataHandle=dojo.io.script.get(_22);
}
if(_1c.onBegin){
var _1d={};
_1d["sn.count"]="records";
_1d["sn.content_type"]="application/javascript";
var _22={url:this.url,content:_1d,timeout:60000,callbackParamName:"sn.stream_header",handle:dojo.hitch(this,"_partHandler",_1c,this.Parts.COUNT)};
_1c._countHandle=dojo.io.script.get(_22);
}
return _1c;
}});
}
