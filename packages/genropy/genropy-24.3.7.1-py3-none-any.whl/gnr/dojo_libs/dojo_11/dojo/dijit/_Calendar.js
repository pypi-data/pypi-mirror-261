/*
	Copyright (c) 2004-2008, The Dojo Foundation
	All Rights Reserved.

	Licensed under the Academic Free License version 2.1 or above OR the
	modified BSD license. For more information on Dojo licensing, see:

		http://dojotoolkit.org/book/dojo-book-0-9/introduction/licensing
*/


if(!dojo._hasResource["dijit._Calendar"]){
dojo._hasResource["dijit._Calendar"]=true;
dojo.provide("dijit._Calendar");
dojo.require("dojo.cldr.supplemental");
dojo.require("dojo.date");
dojo.require("dojo.date.locale");
dojo.require("dijit._Widget");
dojo.require("dijit._Templated");
dojo.declare("dijit._Calendar",[dijit._Widget,dijit._Templated],{templateString:"<table cellspacing=\"0\" cellpadding=\"0\" class=\"dijitCalendarContainer\">\n\t<thead>\n\t\t<tr class=\"dijitReset dijitCalendarMonthContainer\" valign=\"top\">\n\t\t\t<th class='dijitReset' dojoAttachPoint=\"decrementMonth\">\n\t\t\t\t<div class=\"dijitInline dijitCalendarIncrementControl dijitCalendarDecrease\"><span dojoAttachPoint=\"decreaseArrowNode\" class=\"dijitA11ySideArrow dijitCalendarIncrementControl dijitCalendarDecreaseInner\">-</span></div>\n\t\t\t</th>\n\t\t\t<th class='dijitReset' colspan=\"5\">\n\t\t\t\t<div dojoAttachPoint=\"monthLabelSpacer\" class=\"dijitCalendarMonthLabelSpacer\"></div>\n\t\t\t\t<div dojoAttachPoint=\"monthLabelNode\" class=\"dijitCalendarMonthLabel\"></div>\n\t\t\t</th>\n\t\t\t<th class='dijitReset' dojoAttachPoint=\"incrementMonth\">\n\t\t\t\t<div class=\"dijitInline dijitCalendarIncrementControl dijitCalendarIncrease\"><span dojoAttachPoint=\"increaseArrowNode\" class=\"dijitA11ySideArrow dijitCalendarIncrementControl dijitCalendarIncreaseInner\">+</span></div>\n\t\t\t</th>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<th class=\"dijitReset dijitCalendarDayLabelTemplate\"><span class=\"dijitCalendarDayLabel\"></span></th>\n\t\t</tr>\n\t</thead>\n\t<tbody dojoAttachEvent=\"onclick: _onDayClick\" class=\"dijitReset dijitCalendarBodyContainer\">\n\t\t<tr class=\"dijitReset dijitCalendarWeekTemplate\">\n\t\t\t<td class=\"dijitReset dijitCalendarDateTemplate\"><span class=\"dijitCalendarDateLabel\"></span></td>\n\t\t</tr>\n\t</tbody>\n\t<tfoot class=\"dijitReset dijitCalendarYearContainer\">\n\t\t<tr>\n\t\t\t<td class='dijitReset' valign=\"top\" colspan=\"7\">\n\t\t\t\t<h3 class=\"dijitCalendarYearLabel\">\n\t\t\t\t\t<span dojoAttachPoint=\"previousYearLabelNode\" class=\"dijitInline dijitCalendarPreviousYear\"></span>\n\t\t\t\t\t<span dojoAttachPoint=\"currentYearLabelNode\" class=\"dijitInline dijitCalendarSelectedYear\"></span>\n\t\t\t\t\t<span dojoAttachPoint=\"nextYearLabelNode\" class=\"dijitInline dijitCalendarNextYear\"></span>\n\t\t\t\t</h3>\n\t\t\t</td>\n\t\t</tr>\n\t</tfoot>\n</table>\t\n",value:new Date(),dayWidth:"narrow",setValue:function(_1){
if(!this.value||dojo.date.compare(_1,this.value)){
_1=new Date(_1);
this.displayMonth=new Date(_1);
if(!this.isDisabledDate(_1,this.lang)){
this.value=_1;
this.value.setHours(0,0,0,0);
this.onChange(this.value);
}
this._populateGrid();
}
},_setText:function(_2,_3){
while(_2.firstChild){
_2.removeChild(_2.firstChild);
}
_2.appendChild(dojo.doc.createTextNode(_3));
},_populateGrid:function(){
var _4=this.displayMonth;
_4.setDate(1);
var _5=_4.getDay();
var _6=dojo.date.getDaysInMonth(_4);
var _7=dojo.date.getDaysInMonth(dojo.date.add(_4,"month",-1));
var _8=new Date();
var _9=this.value;
var _a=dojo.cldr.supplemental.getFirstDayOfWeek(this.lang);
if(_a>_5){
_a-=7;
}
dojo.query(".dijitCalendarDateTemplate",this.domNode).forEach(function(_b,i){
i+=_a;
var _d=new Date(_4);
var _e,_f="dijitCalendar",adj=0;
if(i<_5){
_e=_7-_5+i+1;
adj=-1;
_f+="Previous";
}else{
if(i>=(_5+_6)){
_e=i-_5-_6+1;
adj=1;
_f+="Next";
}else{
_e=i-_5+1;
_f+="Current";
}
}
if(adj){
_d=dojo.date.add(_d,"month",adj);
}
_d.setDate(_e);
if(!dojo.date.compare(_d,_8,"date")){
_f="dijitCalendarCurrentDate "+_f;
}
if(!dojo.date.compare(_d,_9,"date")){
_f="dijitCalendarSelectedDate "+_f;
}
if(this.isDisabledDate(_d,this.lang)){
_f="dijitCalendarDisabledDate "+_f;
}
var _11=this.getClassForDate(_d,this.lang);
if(_11){
_f+=_11+" "+_f;
}
_b.className=_f+"Month dijitCalendarDateTemplate";
_b.dijitDateValue=_d.valueOf();
var _12=dojo.query(".dijitCalendarDateLabel",_b)[0];
this._setText(_12,_d.getDate());
},this);
var _13=dojo.date.locale.getNames("months","wide","standAlone",this.lang);
this._setText(this.monthLabelNode,_13[_4.getMonth()]);
var y=_4.getFullYear()-1;
var d=new Date();
dojo.forEach(["previous","current","next"],function(_16){
d.setFullYear(y++);
this._setText(this[_16+"YearLabelNode"],dojo.date.locale.format(d,{selector:"year",locale:this.lang}));
},this);
var _17=this;
var _18=function(_19,_1a,adj){
dijit.typematic.addMouseListener(_17[_19],_17,function(_1c){
if(_1c>=0){
_17._adjustDisplay(_1a,adj);
}
},0.8,500);
};
_18("incrementMonth","month",1);
_18("decrementMonth","month",-1);
_18("nextYearLabelNode","year",1);
_18("previousYearLabelNode","year",-1);
},goToToday:function(){
this.setValue(new Date());
},postCreate:function(){
this.inherited(arguments);
var _1d=dojo.hitch(this,function(_1e,n){
var _20=dojo.query(_1e,this.domNode)[0];
for(var i=0;i<n;i++){
_20.parentNode.appendChild(_20.cloneNode(true));
}
});
_1d(".dijitCalendarDayLabelTemplate",6);
_1d(".dijitCalendarDateTemplate",6);
_1d(".dijitCalendarWeekTemplate",5);
var _22=dojo.date.locale.getNames("days",this.dayWidth,"standAlone",this.lang);
var _23=dojo.cldr.supplemental.getFirstDayOfWeek(this.lang);
dojo.query(".dijitCalendarDayLabel",this.domNode).forEach(function(_24,i){
this._setText(_24,_22[(i+_23)%7]);
},this);
var _26=dojo.date.locale.getNames("months","wide","standAlone",this.lang);
dojo.forEach(_26,function(_27){
var _28=dojo.doc.createElement("div");
this._setText(_28,_27);
this.monthLabelSpacer.appendChild(_28);
},this);
this.value=null;
this.setValue(new Date());
},_adjustDisplay:function(_29,_2a){
this.displayMonth=dojo.date.add(this.displayMonth,_29,_2a);
this._populateGrid();
},_onDayClick:function(evt){
var _2c=evt.target;
dojo.stopEvent(evt);
while(!_2c.dijitDateValue){
_2c=_2c.parentNode;
}
if(!dojo.hasClass(_2c,"dijitCalendarDisabledDate")){
this.setValue(_2c.dijitDateValue);
this.onValueSelected(this.value);
}
},onValueSelected:function(_2d){
},onChange:function(_2e){
},isDisabledDate:function(_2f,_30){
},getClassForDate:function(_31,_32){
}});
}
