/*
	Copyright (c) 2004-2008, The Dojo Foundation
	All Rights Reserved.

	Licensed under the Academic Free License version 2.1 or above OR the
	modified BSD license. For more information on Dojo licensing, see:

		http://dojotoolkit.org/book/dojo-book-0-9/introduction/licensing
*/


if(!dojo._hasResource["dojox.data.jsonPathStore"]){
dojo._hasResource["dojox.data.jsonPathStore"]=true;
dojo.provide("dojox.data.jsonPathStore");
dojo.require("dojox.jsonPath");
dojo.require("dojo.date");
dojo.require("dojo.date.locale");
dojo.require("dojo.date.stamp");
dojox.data.ASYNC_MODE=0;
dojox.data.SYNC_MODE=1;
dojo.declare("dojox.data.jsonPathStore",null,{mode:dojox.data.ASYNC_MODE,metaLabel:"_meta",hideMetaAttributes:false,autoIdPrefix:"_auto_",autoIdentity:true,idAttribute:"_id",indexOnLoad:true,labelAttribute:"",url:"",_replaceRegex:/\'\]/gi,constructor:function(_1){
this.byId=this.fetchItemByIdentity;
if(_1){
dojo.mixin(this,_1);
}
this._dirtyItems=[];
this._autoId=0;
this._referenceId=0;
this._references={};
this._fetchQueue=[];
this.index={};
var _2="("+this.metaLabel+"'])";
this.metaRegex=new RegExp(_2);
if(!this.data&&!this.url){
this.setData({});
}
if(this.data&&!this.url){
this.setData(this.data);
delete this.data;
}
if(this.url){
dojo.xhrGet({url:_1.url,handleAs:"json",load:dojo.hitch(this,"setData"),sync:this.mode});
}
},_loadData:function(_3){
if(this._data){
delete this._data;
}
if(dojo.isString(_3)){
this._data=dojo.fromJson(_3);
}else{
this._data=_3;
}
if(this.indexOnLoad){
this.buildIndex();
}
this._updateMeta(this._data,{path:"$"});
this.onLoadData(this._data);
},onLoadData:function(_4){
while(this._fetchQueue.length>0){
var _5=this._fetchQueue.shift();
this.fetch(_5);
}
},setData:function(_6){
this._loadData(_6);
},buildIndex:function(_7,_8){
if(!this.idAttribute){
throw new Error("buildIndex requires idAttribute for the store");
}
_8=_8||this._data;
var _9=_7;
_7=_7||"$";
_7+="[*]";
var _a=this.fetch({query:_7,mode:dojox.data.SYNC_MODE});
for(var i=0;i<_a.length;i++){
if(dojo.isObject(_a[i])){
var _c=_a[i][this.metaLabel]["path"];
if(_9){
var _d=_9.split("['");
var _e=_d[_d.length-1].replace(this._replaceRegex,"");
if(!dojo.isArray(_a[i])){
this._addReference(_a[i],{parent:_8,attribute:_e});
this.buildIndex(_c,_a[i]);
}else{
this.buildIndex(_c,_8);
}
}else{
var _d=_c.split("['");
var _e=_d[_d.length-1].replace(this._replaceRegex,"");
this._addReference(_a[i],{parent:this._data,attribute:_e});
this.buildIndex(_c,_a[i]);
}
}
}
},_correctReference:function(_f){
if(this.index[_f[this.idAttribute]][this.metaLabel]===_f[this.metaLabel]){
return this.index[_f[this.idAttribute]];
}
return _f;
},getValue:function(_10,_11){
_10=this._correctReference(_10);
return _10[_11];
},getValues:function(_12,_13){
_12=this._correctReference(_12);
return dojo.isArray(_12[_13])?_12[_13]:[_12[_13]];
},getAttributes:function(_14){
_14=this._correctReference(_14);
var res=[];
for(var i in _14){
if(this.hideMetaAttributes&&(i==this.metaLabel)){
continue;
}
res.push(i);
}
return res;
},hasAttribute:function(_17,_18){
_17=this._correctReference(_17);
if(_18 in _17){
return true;
}
return false;
},containsValue:function(_19,_1a,_1b){
_19=this._correctReference(_19);
if(_19[_1a]&&_19[_1a]==_1b){
return true;
}
if(dojo.isObject(_19[_1a])||dojo.isObject(_1b)){
if(this._shallowCompare(_19[_1a],_1b)){
return true;
}
}
return false;
},_shallowCompare:function(a,b){
if((dojo.isObject(a)&&!dojo.isObject(b))||(dojo.isObject(b)&&!dojo.isObject(a))){
return false;
}
if(a["getFullYear"]||b["getFullYear"]){
if((a["getFullYear"]&&!b["getFullYear"])||(b["getFullYear"]&&!a["getFullYear"])){
return false;
}else{
if(!dojo.date.compare(a,b)){
return true;
}
return false;
}
}
for(var i in b){
if(dojo.isObject(b[i])){
if(!a[i]||!dojo.isObject(a[i])){
return false;
}
if(b[i]["getFullYear"]){
if(!a[i]["getFullYear"]){
return false;
}
if(dojo.date.compare(a,b)){
return false;
}
}else{
if(!this._shallowCompare(a[i],b[i])){
return false;
}
}
}else{
if(!b[i]||(a[i]!=b[i])){
return false;
}
}
}
for(var i in a){
if(!b[i]){
return false;
}
}
return true;
},isItem:function(_1f){
if(!dojo.isObject(_1f)||!_1f[this.metaLabel]){
return false;
}
if(this.requireId&&this._hasId&&!_1f[this._id]){
return false;
}
return true;
},isItemLoaded:function(_20){
_20=this._correctReference(_20);
return this.isItem(_20);
},loadItem:function(_21){
return true;
},_updateMeta:function(_22,_23){
if(_22&&_22[this.metaLabel]){
dojo.mixin(_22[this.metaLabel],_23);
return;
}
_22[this.metaLabel]=_23;
},cleanMeta:function(_24,_25){
_24=_24||this._data;
if(_24[this.metaLabel]){
if(_24[this.metaLabel]["autoId"]){
delete _24[this.idAttribute];
}
delete _24[this.metaLabel];
}
if(dojo.isArray(_24)){
for(var i=0;i<_24.length;i++){
if(dojo.isObject(_24[i])||dojo.isArray(_24[i])){
this.cleanMeta(_24[i]);
}
}
}else{
if(dojo.isObject(_24)){
for(var i in _24){
this.cleanMeta(_24[i]);
}
}
}
},fetch:function(_27){
if(!this._data){
this._fetchQueue.push(_27);
return _27;
}
if(dojo.isString(_27)){
_28=_27;
_27={query:_28,mode:dojox.data.SYNC_MODE};
}
var _28;
if(!_27||!_27.query){
if(!_27){
var _27={};
}
if(!_27.query){
_27.query="$..*";
_28=_27.query;
}
}
if(dojo.isObject(_27.query)){
if(_27.query.query){
_28=_27.query.query;
}else{
_28=_27.query="$..*";
}
if(_27.query.queryOptions){
_27.queryOptions=_27.query.queryOptions;
}
}else{
_28=_27.query;
}
if(!_27.mode){
_27.mode=this.mode;
}
if(!_27.queryOptions){
_27.queryOptions={};
}
_27.queryOptions.resultType="BOTH";
var _29=dojox.jsonPath.query(this._data,_28,_27.queryOptions);
var tmp=[];
var _2b=0;
for(var i=0;i<_29.length;i++){
if(_27.start&&i<_27.start){
continue;
}
if(_27.count&&(_2b>=_27.count)){
continue;
}
var _2d=_29[i]["value"];
var _2e=_29[i]["path"];
if(!dojo.isObject(_2d)){
continue;
}
if(this.metaRegex.exec(_2e)){
continue;
}
this._updateMeta(_2d,{path:_29[i].path});
if(this.autoIdentity&&!_2d[this.idAttribute]){
var _2f=this.autoIdPrefix+this._autoId++;
_2d[this.idAttribute]=_2f;
_2d[this.metaLabel]["autoId"]=true;
}
if(_2d[this.idAttribute]){
this.index[_2d[this.idAttribute]]=_2d;
}
_2b++;
tmp.push(_2d);
}
_29=tmp;
var _30=_27.scope||dojo.global;
if("sort" in _27){
console.log("TODO::add support for sorting in the fetch");
}
if(_27.mode==dojox.data.SYNC_MODE){
return _29;
}
if(_27.onBegin){
_27["onBegin"].call(_30,_29.length,_27);
}
if(_27.onItem){
for(var i=0;i<_29.length;i++){
_27["onItem"].call(_30,_29[i],_27);
}
}
if(_27.onComplete){
_27["onComplete"].call(_30,_29,_27);
}
return _27;
},dump:function(_31){
var _31=_31||{};
var d=_31.data||this._data;
if(!_31.suppressExportMeta&&_31.clone){
_33=dojo.clone(d);
if(_33[this.metaLabel]){
_33[this.metaLabel]["clone"]=true;
}
}else{
var _33=d;
}
if(!_31.suppressExportMeta&&_33[this.metaLabel]){
_33[this.metaLabel]["last_export"]=new Date().toString();
}
if(_31.cleanMeta){
this.cleanMeta(_33);
}
switch(_31.type){
case "raw":
return _33;
case "json":
default:
return dojo.toJson(_33);
}
},getFeatures:function(){
return {"dojo.data.api.Read":true,"dojo.data.api.Identity":true,"dojo.data.api.Write":true,"dojo.data.api.Notification":true};
},getLabel:function(_34){
_34=this._correctReference(_34);
var _35="";
if(dojo.isFunction(this.createLabel)){
return this.createLabel(_34);
}
if(this.labelAttribute){
if(dojo.isArray(this.labelAttribute)){
for(var i=0;i<this.labelAttribute.length;i++){
if(i>0){
_35+=" ";
}
_35+=_34[this.labelAttribute[i]];
}
return _35;
}else{
return _34[this.labelAttribute];
}
}
return _34.toString();
},getLabelAttributes:function(_37){
_37=this._correctReference(_37);
return dojo.isArray(this.labelAttribute)?this.labelAttribute:[this.labelAttribute];
},sort:function(a,b){
console.log("TODO::implement default sort algo");
},getIdentity:function(_3a){
if(this.isItem(_3a)){
return _3a[this.idAttribute];
}
throw new Error("Id not found for item");
},getIdentityAttributes:function(_3b){
return [this.idAttribute];
},fetchItemByIdentity:function(_3c){
var id;
if(dojo.isString(_3c)){
id=_3c;
_3c={identity:id,mode:dojox.data.SYNC_MODE};
}else{
if(_3c){
id=_3c["identity"];
}
if(!_3c.mode){
_3c.mode=this.mode;
}
}
if(this.index&&(this.index[id]||this.index["identity"])){
if(_3c.mode==dojox.data.SYNC_MODE){
return this.index[id];
}
if(_3c.onItem){
_3c["onItem"].call(_3c.scope||dojo.global,this.index[id],_3c);
}
return _3c;
}else{
if(_3c.mode==dojox.data.SYNC_MODE){
return false;
}
}
if(_3c.onError){
_3c["onItem"].call(_3c.scope||dojo.global,new Error("Item Not Found: "+id),_3c);
}
return _3c;
},newItem:function(_3e,_3f){
var _40={};
var _41={item:this._data};
if(_3f){
if(_3f.parent){
_3f.item=_3f.parent;
}
dojo.mixin(_41,_3f);
}
if(this.idAttribute&&!_3e[this.idAttribute]){
if(this.requireId){
throw new Error("requireId is enabled, new items must have an id defined to be added");
}
if(this.autoIdentity){
var _42=this.autoIdPrefix+this._autoId++;
_3e[this.idAttribute]=_42;
_40["autoId"]=true;
}
}
if(!_41&&!_41.attribute&&!this.idAttribute&&!_3e[this.idAttribute]){
throw new Error("Adding a new item requires, at a minumum, either the pInfo information, including the pInfo.attribute, or an id on the item in the field identified by idAttribute");
}
if(!_41.attribute){
_41.attribute=_3e[this.idAttribute];
}
_41.oldValue=this._trimItem(_41.item[_41.attribute]);
if(dojo.isArray(_41.item[_41.attribute])){
this._setDirty(_41.item);
_41.item[_41.attribute].push(_3e);
}else{
this._setDirty(_41.item);
_41.item[_41.attribute]=_3e;
}
_41.newValue=_41.item[_41.attribute];
if(_3e[this.idAttribute]){
this.index[_3e[this.idAttribute]]=_3e;
}
this._updateMeta(_3e,_40);
this._addReference(_3e,_41);
this._setDirty(_3e);
this.onNew(_3e,_41);
return _3e;
},_addReference:function(_43,_44){
var rid="_ref_"+this._referenceId++;
if(!_43[this.metaLabel]["referenceIds"]){
_43[this.metaLabel]["referenceIds"]=[];
}
_43[this.metaLabel]["referenceIds"].push(rid);
this._references[rid]=_44;
},deleteItem:function(_46){
_46=this._correctReference(_46);
console.log("Item: ",_46);
if(this.isItem(_46)){
while(_46[this.metaLabel]["referenceIds"].length>0){
console.log("refs map: ",this._references);
console.log("item to delete: ",_46);
var rid=_46[this.metaLabel]["referenceIds"].pop();
var _48=this._references[rid];
console.log("deleteItem(): ",_48,_48.parent);
parentItem=_48.parent;
var _49=_48.attribute;
if(parentItem&&parentItem[_49]&&!dojo.isArray(parentItem[_49])){
this._setDirty(parentItem);
this.unsetAttribute(parentItem,_49);
delete parentItem[_49];
}
if(dojo.isArray(parentItem[_49])){
console.log("Parent is array");
var _4a=this._trimItem(parentItem[_49]);
var _4b=false;
for(var i=0;i<parentItem[_49].length&&!_4b;i++){
if(parentItem[_49][i][this.metaLabel]===_46[this.metaLabel]){
_4b=true;
}
}
if(_4b){
this._setDirty(parentItem);
var del=parentItem[_49].splice(i-1,1);
delete del;
}
var _4e=this._trimItem(parentItem[_49]);
this.onSet(parentItem,_49,_4a,_4e);
}
delete this._references[rid];
}
this.onDelete(_46);
delete _46;
}
},_setDirty:function(_4f){
for(var i=0;i<this._dirtyItems.length;i++){
if(_4f[this.idAttribute]==this._dirtyItems[i][this.idAttribute]){
return;
}
}
this._dirtyItems.push({item:_4f,old:this._trimItem(_4f)});
this._updateMeta(_4f,{isDirty:true});
},setValue:function(_51,_52,_53){
_51=this._correctReference(_51);
this._setDirty(_51);
var old=_51[_52]|undefined;
_51[_52]=_53;
this.onSet(_51,_52,old,_53);
},setValues:function(_55,_56,_57){
_55=this._correctReference(_55);
if(!dojo.isArray(_57)){
throw new Error("setValues expects to be passed an Array object as its value");
}
this._setDirty(_55);
var old=_55[_56]||null;
_55[_56]=_57;
this.onSet(_55,_56,old,_57);
},unsetAttribute:function(_59,_5a){
_59=this._correctReference(_59);
this._setDirty(_59);
var old=_59[_5a];
delete _59[_5a];
this.onSet(_59,_5a,old,null);
},save:function(_5c){
var _5d=[];
if(!_5c){
_5c={};
}
while(this._dirtyItems.length>0){
var _5e=this._dirtyItems.pop()["item"];
var t=this._trimItem(_5e);
var d;
switch(_5c.format){
case "json":
d=dojo.toJson(t);
break;
case "raw":
default:
d=t;
}
_5d.push(d);
this._markClean(_5e);
}
this.onSave(_5d);
},_markClean:function(_61){
if(_61&&_61[this.metaLabel]&&_61[this.metaLabel]["isDirty"]){
delete _61[this.metaLabel]["isDirty"];
}
},revert:function(){
while(this._dirtyItems.length>0){
var d=this._dirtyItems.pop();
this._mixin(d.item,d.old);
}
this.onRevert();
},_mixin:function(_63,_64){
if(dojo.isObject(_64)){
if(dojo.isArray(_64)){
while(_63.length>0){
_63.pop();
}
for(var i=0;i<_64.length;i++){
if(dojo.isObject(_64[i])){
if(dojo.isArray(_64[i])){
var mix=[];
}else{
var mix={};
if(_64[i][this.metaLabel]&&_64[i][this.metaLabel]["type"]&&_64[i][this.metaLabel]["type"]=="reference"){
_63[i]=this.index[_64[i][this.idAttribute]];
continue;
}
}
this._mixin(mix,_64[i]);
_63.push(mix);
}else{
_63.push(_64[i]);
}
}
}else{
for(var i in _63){
if(i in _64){
continue;
}
delete _63[i];
}
for(var i in _64){
if(dojo.isObject(_64[i])){
if(dojo.isArray(_64[i])){
var mix=[];
}else{
if(_64[i][this.metaLabel]&&_64[i][this.metaLabel]["type"]&&_64[i][this.metaLabel]["type"]=="reference"){
_63[i]=this.index[_64[i][this.idAttribute]];
continue;
}
var mix={};
}
this._mixin(mix,_64[i]);
_63[i]=mix;
}else{
_63[i]=_64[i];
}
}
}
}
},isDirty:function(_67){
_67=this._correctReference(_67);
return _67&&_67[this.metaLabel]&&_67[this.metaLabel]["isDirty"];
},_createReference:function(_68){
var obj={};
obj[this.metaLabel]={type:"reference"};
obj[this.idAttribute]=_68[this.idAttribute];
return obj;
},_trimItem:function(_6a){
var _6b;
if(dojo.isArray(_6a)){
_6b=[];
for(var i=0;i<_6a.length;i++){
if(dojo.isArray(_6a[i])){
_6b.push(this._trimItem(_6a[i]));
}else{
if(dojo.isObject(_6a[i])){
if(_6a[i]["getFullYear"]){
_6b.push(dojo.date.stamp.toISOString(_6a[i]));
}else{
if(_6a[i][this.idAttribute]){
_6b.push(this._createReference(_6a[i]));
}else{
_6b.push(this._trimItem(_6a[i]));
}
}
}else{
_6b.push(_6a[i]);
}
}
}
return _6b;
}
if(dojo.isObject(_6a)){
_6b={};
for(var _6d in _6a){
if(!_6a[_6d]){
_6b[_6d]=undefined;
continue;
}
if(dojo.isArray(_6a[_6d])){
_6b[_6d]=this._trimItem(_6a[_6d]);
}else{
if(dojo.isObject(_6a[_6d])){
if(_6a[_6d]["getFullYear"]){
_6b[_6d]=dojo.date.stamp.toISOString(_6a[_6d]);
}else{
if(_6a[_6d][this.idAttribute]){
_6b[_6d]=this._createReference(_6a[_6d]);
}else{
_6b[_6d]=this._trimItem(_6a[_6d]);
}
}
}else{
_6b[_6d]=_6a[_6d];
}
}
}
return _6b;
}
},onSet:function(){
},onNew:function(){
},onDelete:function(){
},onSave:function(_6e){
},onRevert:function(){
}});
dojox.data.jsonPathStore.byId=dojox.data.jsonPathStore.fetchItemByIdentity;
}
