/*
	Copyright (c) 2004-2008, The Dojo Foundation
	All Rights Reserved.

	Licensed under the Academic Free License version 2.1 or above OR the
	modified BSD license. For more information on Dojo licensing, see:

		http://dojotoolkit.org/book/dojo-book-0-9/introduction/licensing
*/


if(!dojo._hasResource["dojox.charting.plot2d.MarkersOnly"]){dojo._hasResource["dojox.charting.plot2d.MarkersOnly"]=true;dojo.provide("dojox.charting.plot2d.MarkersOnly");dojo.require("dojox.charting.plot2d.Default");dojo.declare("dojox.charting.plot2d.MarkersOnly",dojox.charting.plot2d.Default,{constructor:function(){this.opt.lines=false;this.opt.markers=true;}});}