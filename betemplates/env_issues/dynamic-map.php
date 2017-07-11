<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml">
	<head>
		<title>Map created by GPS Visualizer</title>
		<base target="_top"></base>
		<meta name="geo.position" content="{{ mapLat }}; {{ mapLong }}" />
		<meta name="ICBM" content="{{ mapLat }}; {{ mapLong }}" />
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

		<style type = "text/css">
		       .indent {text-indent: 10px;
                        font:11px Arial;}
		</style>
		
		<!-- Copyright 2005 Macromedia, Inc. All rights reserved. -->
<title>Supportive Regional Town Centres</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="stylesheet" href="http://www.livable.eng.unsw.edu.au/stylesheets/mm_lodging1.css" type="text/css" />

<link rel="stylesheet" type="text/css" href="http://www.livable.eng.unsw.edu.au/stylesheets/jqueryslidemenu.css" />
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.2.6/jquery.min.js"></script>
<script type="text/javascript" src="http://www.livable.eng.unsw.edu.au/stylesheets/jqueryslidemenu.js"></script>

	</head>
<body bgcolor="#999966">
<table width="100%" border="0" cellspacing="0" cellpadding="0">
	<tr>
	<td width="15" nowrap="nowrap">&nbsp;</td>
	<td height="60" colspan="2" class="logo" nowrap="nowrap"><br />
	   Enhancing livability in town centres</td>
	<td width="100%">&nbsp;</td>
	</tr>

	<tr bgcolor="#ffffff">
	<td colspan="4"><img src="mm_spacer.gif" alt="" width="1" height="1" border="0" /></td>
	</tr>

	<tr bgcolor="#a4c2c2">
	<td width="15" nowrap="nowrap">&nbsp;</td>
	<td height="36"  width="100%" id="navigation" class="navText">
	 <!-- MENU goes here -------------------------------------------- -->
	<!-- Navigation for the sites pages -->
    <div id="myslidemenu" class="jqueryslidemenu">
<ul>
<li><a href="http://www.livable.eng.unsw.edu.au/index.php">HOME</a></li>
</ul>
<br style="clear: left" />

  <!-- MENU above here -------------------------------------------- -->
	</td></tr>

	<tr bgcolor="#ffffff">
	<td colspan="4"><img src="mm_spacer.gif" alt="" width="1" height="1" border="0" /></td>
	</tr>

	<tr bgcolor="#ffffff">
	<td valign="top" width="15"><img src="mm_spacer.gif" alt="" width="50" height="1" border="0" /></td>
	<td width="710" valign="top"><br />
	<table border="0" cellspacing="0" cellpadding="2" width="610">
        <tr>
          <td class="pageName" colspan="3">{{ mySession.name }} - <a href="/built/{{ mySession.id }}">Report</a></td>
        </tr>
       <tr>
         <td width="197" class="subHeader" valign="bottom">Server interface</td>
		 <td width="1" rowspan="2">&nbsp;</td>
		 <td width="400" height="100" rowspan="2">
		 
		<script type="text/javascript">
			// If you put this map on another Web site, you must include your API key or nothing will work!
			var google_api_key = ''; // Your key goes on THIS line; the following line ("if window.location.host...") can be removed.
			if (window.location.host == 'www.gpsvisualizer.com') { google_api_key = 'ABQIAAAAaG9JDbCe6Ra1Og0hKCn2LRRokW_ItEImBo7ewbVEJAzstSsRWhRJ3RMDAWpL55QacGZ2zQF2kLC_eA'; }
			
			document.writeln('<script src="http://maps.google.com/maps?file=api&v=2&sensor=false&key='+google_api_key+'" type="text/javascript"><'+'/'+'script>');
		</script>
<BR><BR>
		<!--
			If you want to transplant this map into another Web page, by far the best method is to
			simply include it in a IFRAME tag (see http://www.gpsvisualizer.com/faq.html#google_html).
			But, if you must paste the code into another page, be sure to include all of these parts:
			   1. The DOCTYPE declaration and the extra attributes in the "html" tag (xmlns:v=...)
			     that allow Internet Explorer for Windows to render polylines (tracks)
			   2. The "div" tags that contain the map and its widgets (below this comment)
			   3. Three sections of JavaScript code:
			      a. Your Google Maps API key and the maps.google.com code (above this comment)
			      b. "gv_options" and the code that calls "functions.js" on maps.gpsvisualizer.com
			      c. The "GV_Map" function, which contains all the geographic info for the map
		-->
		<table style="position:relative; filter:alpha(opacity=95); -moz-opacity:0.95; opacity:0.95; background:#ffffff;" cellpadding="5" cellspacing="0" border="0"><tr valign="top"><td>
		<div style="width:800px; margin-left:0px; margin-right:0px; margin-top:0px; margin-bottom:0px;">
			<div id="gmap_div" style="width:800px; height:700px; margin:0px; margin-right:12px; background-color:#F0F0F0; float:left; overflow:hidden;">
				<p align="center" style="font:10px Arial;">This map was created using <a target="_blank" href="http://www.gpsvisualizer.com/">GPS Visualizer</a>'s do-it-yourself geographic utilities.<br /><br />Please wait while the map data loads...</p>
			</div>

			<div id="gv_legend_container" style="display:none;"><table id="gv_legend_table" style="position:relative; filter:alpha(opacity=95); -moz-opacity:0.95; opacity:0.95; background:#ffffff;" cellpadding="0" cellspacing="0" border="0"><tr><td><div id="gv_legend_handle" align="center" style="height:6px; max-height:6px; background:#CCCCCC; border-left:1px solid #999999; border-top:1px solid #EEEEEE; border-right:1px solid #999999; padding:0px; cursor:move;"><!-- --></div>
				<div id="gv_legend" align="left" style="line-height:13px; border:solid #000000 1px; background:#FFFFFF; padding:4px;max-width:400px; font:11px Arial; ">
                     <!-- floating box inside of map -->
				</div>
			</td></tr></table></div>



			<!-- the following is the "floating" marker list; the "static" version is below -->
			<div id="gv_marker_list_container" style="display:none;"><table id="gv_marker_list_table" style="position:relative; filter:alpha(opacity=95); -moz-opacity:0.95; opacity:0.95;" cellspacing="0" cellpadding="0" border="0">
            <tr><td>
				<div id="gv_marker_list_handle" align="center" style="height:6px; max-height:6px; background:#CCCCCC; border-left:1px solid #999999; border-top:1px solid #EEEEEE; border-right:1px solid #999999; padding:0px; cursor:move;"><!-- --></div>
				<div id="gv_marker_list" align="left" class="gv_marker_list" style="overflow:auto; background:#FFFFFF; border:solid #666666 1px; padding:4px;"></div>
			</td></tr></table></div>
			</td><td>
			<div id="gv_marker_list_static" align="left" class="gv_marker_list" style="width:300px; overflow:auto; float:left; display:none;"></div>
            <div id="gv_clear_margins" style="height:0px; clear:both;"><!-- clear the "float" --></div> </td><td>
            <!-- %here% -->
            
            </td></tr></table>
		</div>


		<!-- begin GPS Visualizer setup script (must come after maps.google.com code) -->
		<script type="text/javascript">
			/* Global variables used by the GPS Visualizer functions (1329985719): */
			gv_options = [];
				// important variable names:
				gv_options.map_div = 'gmap_div';  // the name of the HTML "div" tag containing the map itself; usually 'gmap_div'

				// basic map parameters:
                gv_options.width = 800;  // width of the map, in pixels
				gv_options.height = 700;  // height of the map, in pixels
				gv_options.full_screen = false;  // true|false: should the map fill the entire page (or frame)?
				gv_options.center = [{{ mapLat }}, {{ mapLong }}];  // [latitude,longitude] - be sure to keep the square brackets
				gv_options.zoom = 16;  // higher number means closer view; can also be 'auto'
				gv_options.map_opacity = 1;  // number from 0 to 1
				gv_options.map_type = 'G_NORMAL_MAP';  // popular map_type choices are 'G_NORMAL_MAP', 'G_SATELLITE_MAP', 'G_HYBRID_MAP', 'G_PHYSICAL_MAP', 'MYTOPO_TILES'
				gv_options.doubleclick_zoom = false;  // true|false: zoom in when mouse is double-clicked?
				gv_options.mousewheel_zoom = true; // true|false; or 'reverse' for down=in and up=out
				gv_options.centering_options = { 'open_info_window':true, 'partial_match':true, 'center_key':'center', 'default_zoom':null } // URL-based centering (e.g., ?center=name_of_marker&zoom=14)

				// widgets on the map:
				gv_options.zoom_control = 'large'; // 'large'|'small'|'3d'|'none'
				gv_options.scale_control = true; // true|false
				gv_options.center_coordinates = true;  // true|false: show a "center coordinates" box and crosshair?
				gv_options.crosshair_hidden = true;  // true|false: hide the crosshair initially?
				gv_options.map_opacity_control = true;  // true|false
				gv_options.map_type_control = [];  // widget to change the background map
				  gv_options.map_type_control.style = 'menu';  // 'menu'|'list'|'none'|'google'
				  gv_options.map_type_control.filter = true;  // true|false: when map loads, are irrelevant maps ignored?
				  gv_options.map_type_control.excluded = ['G_SATELLITE_3D_MAP'];  // comma-separated list of map types that will never show in the list ('included' also works)
				gv_options.legend_options = []; // options for a floating legend box (id="gv_legend"), which can contain anything
				  gv_options.legend_options.legend = true;  // true|false: enable or disable the legend altogether
				  gv_options.legend_options.position = ['G_ANCHOR_TOP_LEFT',70,6];  // [Google anchor name, relative x, relative y]
				  gv_options.legend_options.draggable = true;  // true|false: can it be moved around the screen?
				  gv_options.legend_options.collapsible = true;  // true|false: can it be collapsed by double-clicking its top bar?
				gv_options.measurement_tools = { visible:false, distance_color:'', area_color:'', position:[] };


				// marker-related options:
				gv_options.default_marker = { color:'green',icon:'googlemini' }; // icon can be a URL, but be sure to also include size:[w,h] and optionally anchor:[x,y]
				gv_options.shadows = true; // true|false: do the standard markers have "shadows" behind them?
				gv_options.marker_link_target = '_blank'; // the name of the window or frame into which markers' URLs will load
				gv_options.info_window_width = 250;  // in pixels, the width of the markers' pop-up info "bubbles" (can be overridden by 'window_width' in individual markers)
				gv_options.thumbnail_width = 0;  // in pixels, the width of the markers' thumbnails (can be overridden by 'thumbnail_width' in individual markers)
				gv_options.photo_size = [0,0];  // in pixels, the size of the photos in info windows (can be overridden by 'photo_width' or 'photo_size' in individual markers)
				gv_options.hide_labels = false;  // true|false: hide labels when map first loads?
				gv_options.label_offset = [0,0];  // [x,y]: shift all markers' labels (positive numbers are right and down)
				gv_options.label_centered = false;  // true|false: center labels with respect to their markers?  (label_left is also a valid option.)
				gv_options.driving_directions = false;  // put a small "driving directions" form in each marker's pop-up window? (override with dd:true or dd:false in a marker's options)
				gv_options.garmin_icon_set = 'gpsmap'; // 'gpsmap' are the small 16x16 icons; change it to '24x24' for larger icons
				gv_options.marker_list_options = [];  // options for a dynamically-created list of markers
				  gv_options.marker_list_options.list = true;  // true|false: enable or disable the marker list altogether
				  gv_options.marker_list_options.floating = false;  // is the list a floating box inside the map itself?
				  gv_options.marker_list_options.id_static = 'gv_marker_list_static';  // id of a DIV that holds a non-floating list
				  gv_options.marker_list_options.id_floating = 'gv_marker_list';  // id of a DIV tag that holds a floating list (other associated DIVs -- _handle, _table, _container -- must be similarly named)
				  gv_options.marker_list_options.width = 250;  // floating list only: width, in pixels
				  gv_options.marker_list_options.height = 596;  // floating list only: height, in pixels
				  gv_options.marker_list_options.position = ['G_ANCHOR_BOTTOM_RIGHT',6,38];  // floating list only: position within map
				  gv_options.marker_list_options.draggable = true;  // true|false, floating list only: can it be moved around the screen?
				  gv_options.marker_list_options.collapsible = true;  // true|false, floating list only: can it be collapsed by double-clicking its top bar?
				  gv_options.marker_list_options.include_tickmarks = false;  // true|false: are distance/time tickmarks included in the list?
				  gv_options.marker_list_options.include_trackpoints = false;  // true|false: are "trackpoint" markers included in the list?
				  gv_options.marker_list_options.dividers = false;  // true|false: will a thin line be drawn between each item in the list?
				  gv_options.marker_list_options.desc = true;  // true|false: will the markers' descriptions be shown below their names in the list?
				  gv_options.marker_list_options.icons = true;  // true|false: should the markers' icons appear to the left of their names in the list?
				  gv_options.marker_list_options.thumbnails = false;  // true|false: should markers' thumbnails be shown in the list?
				  gv_options.marker_list_options.folders_collapsed = false;  // true|false: do folders in the list start out in a collapsed state?
				  gv_options.marker_list_options.wrap_names = true;  // true|false: should marker's names be allowed to wrap onto more than one line?
				  gv_options.marker_list_options.unnamed = '[unnamed]';  // what 'name' should be assigned to  unnamed markers in the list?
				  gv_options.marker_list_options.colors = false;  // true|false: should the names/descs of the points in the list be colorized the same as their markers?
				  gv_options.marker_list_options.default_color = '';  // default HTML color code for the names/descs in the list
				  gv_options.marker_list_options.limit = 0;  // how many markers to show in the list; 0 for no limit
				  gv_options.marker_list_options.center = false;  // true|false: does the map center upon a marker when you click its name in the list?
				  gv_options.marker_list_options.zoom = false;  // true|false: does the map zoom to a certain level when you click on a marker's name in the list?
				  gv_options.marker_list_options.zoom_level = 17;  // if 'zoom' is true, what level should the map zoom to?
				  gv_options.marker_list_options.info_window = true;  // true|false: do info windows pop up when the markers' names are clicked in the list?
				  gv_options.marker_list_options.url_links = false;  // true|false: do the names in the list become instant links to the markers' URLs?
				  gv_options.marker_list_options.toggle = false;  // true|false: does a marker disappear if you click on its name in the list?
				  gv_options.marker_list_options.help_tooltips = false;  // true|false: do "tooltips" appear on marker names that tell you what happens when you click?
				  gv_options.marker_list_options.header = ''; // HTML code; be sure to put backslashes in front of any single quotes, and don't include any line breaks
				  gv_options.marker_list_options.footer = ''; // HTML code; be sure to put backslashes in front of any single quotes, and don't include any line breaks
				gv_options.marker_filter_options = [];  // options for removing waypoints that are out of the current view
				  gv_options.marker_filter_options.filter = false;  // true|false: should out-of-range markers be removed?
				  gv_options.marker_filter_options.movement_threshold = 8;  // in pixels, how far the map has to move to trigger filtering
				  gv_options.marker_filter_options.limit = 0;  // maximum number of markers to display on the map; 0 for no limit
				  gv_options.marker_filter_options.update_list = true;  // true|false: should the marker list be updated with only the filtered markers?
				  gv_options.marker_filter_options.sort_list_by_distance = false;  // true|false: should the marker list be sorted by distance from the center of the map?
				  gv_options.marker_filter_options.min_zoom = 0;  // below this zoom level, don't show any markers at all
				  gv_options.marker_filter_options.zoom_message = '';  // message to put in the marker list if the map is below the min_zoom threshold
				

			// Load GPS Visualizer's Google Maps functions (this must be loaded AFTER gv_options are set):
			document.writeln('<script src="http://maps.gpsvisualizer.com/google_maps/functions.js" type="text/javascript"><'+'/'+'script>');
		</script>

		<style type="text/css">
			/* Put any custom style definitions here (e.g., .gv_marker_info_window, .gv_marker_list_item, .gv_tooltip, .gv_label, etc.) */
			.gv_label {
				filter:alpha(opacity=80); -moz-opacity:0.8; opacity:0.8;
				background:#333333; border:1px solid black; padding:1px;
				font:9px Verdana,sans-serif; color:white; font-weight:normal;
			}

		</style>

		<!-- end GPSV setup script and styles; begin map-drawing script (they must be separate) -->
		<script type="text/javascript">
			function GV_Map() {
			
				var scoreWords = new Array();
				scoreWords[0] = "N/A"; 
				scoreWords[1] = "Very bad";
				scoreWords[2] = "Bad";
				scoreWords[3] = "Neutral";
				scoreWords[4] = "Good";
				scoreWords[5] = "Very good";
				
				var scoreColors = new Array();
				scoreColors[0]	= 'FFFFFF';
				scoreColors[5]	= '458B00'; // very good green (chartuse)
				scoreColors[4]	= 'CAFF70'; // good is olive
				scoreColors[3]	= 'FFFF00'; // neutral yellow
				scoreColors[2]	= 'FF7F24'; // bad is orange
				scoreColors[1]	= 'FF0000'; // very bad = red
				
				
			
				if (GBrowserIsCompatible()) {
					if (gv_options.full_screen) { GV_Fill_Window_With_Map(gv_options.map_div); }
					gmap = new GMap2(document.getElementById(gv_options.map_div)); // create map
					GV_Setup_Map(gv_options);
					

					{% for myObj in   spaceAuditList %}

                    GV_Draw_Marker({lat:{{ myObj.owner.latitude }},lon: {{ myObj.owner.longitude }} ,name:'{{ myObj.owner.name }}',desc:'<br>{% if myObj.photo %}<a onclick="window.open(\'http://livable.eng.unsw.edu.au/media/{{ myObj.photo }}\')"><img src="http://livable.eng.unsw.edu.au/media/thumbs/{{ myObj.photo }}" width=82 height=110 align="left" style="padding-right:10px"></a>{% endif %}<b>Obj ID:</b> {{ myObj.owner.id }}  <b>Aud ID:</b>  {{ myObj.id }}<br> {% if myObj.score %}<b>Score:</b> '+ scoreWords[{{ myObj.score }}]+'{% else %}<b>Description{% endif %}<br> {{ myObj.notes }}',color:scoreColors[{% if myObj.score %}{{ myObj.score }}{% else %}0{% endif %}], folder:'space'});
                    
					{% endfor %}	
					
					
					{% for myObj in linkAuditList %}

                    GV_Draw_Marker({lat:{{ myObj.owner.latitude }},lon: {{ myObj.owner.longitude }} ,name:'{{ myObj.owner.name }}',desc:'<br>{% if myObj.photo %}<a onclick="window.open(\'http://livable.eng.unsw.edu.au/media/{{ myObj.photo }}\')"><img src="http://livable.eng.unsw.edu.au/media/thumbs/{{ myObj.photo }}" width=82 height=110 align="left" style="padding-right:10px"></a>{% endif %}<b>Obj ID:</b> {{ myObj.owner.id }}  <b>Aud ID:</b>  {{ myObj.id }}<br> {% if myObj.score %}<b>Score:</b> '+ scoreWords[{{ myObj.score }}]+'{% else %}<b>Description{% endif %}<br> {{ myObj.notes }}',color:scoreColors[{% if myObj.score %}{{ myObj.score }}{% else %}0{% endif %}], folder:'link'});
                    
					{% endfor %}	
					
					{% for myObj in accesspointAuditList %}

                    GV_Draw_Marker({lat:{{ myObj.owner.latitude }},lon: {{ myObj.owner.longitude }} ,name:'{{ myObj.owner.name }}',desc:'<br>{% if myObj.photo %}<a onclick="window.open(\'http://livable.eng.unsw.edu.au/media/{{ myObj.photo }}\')"><img src="http://livable.eng.unsw.edu.au/media/thumbs/{{ myObj.photo }}" width=82 height=110 align="left" style="padding-right:10px"></a>{% endif %}<b>Obj ID:</b> {{ myObj.owner.id }}  <b>Aud ID:</b>  {{ myObj.id }}<br> {% if myObj.score %}<b>Score:</b> '+ scoreWords[{{ myObj.score }}]+'{% else %}<b>Description{% endif %}<br> {{ myObj.notes }}',color:scoreColors[{% if myObj.score %}{{ myObj.score }}{% else %}0{% endif %}], folder:'accesspoint'});
                    
					{% endfor %}	
					
					{% for myObj in serviceAuditList %}

                    GV_Draw_Marker({lat:{{ myObj.owner.latitude }},lon: {{ myObj.owner.longitude }} ,name:'{{ myObj.owner.name }}',desc:'<br>{% if myObj.photo %}<a onclick="window.open(\'http://livable.eng.unsw.edu.au/media/{{ myObj.photo }}\')"><img src="http://livable.eng.unsw.edu.au/media/thumbs/{{ myObj.photo }}" width=82 height=110 align="left" style="padding-right:10px"></a>{% endif %}<b>Obj ID:</b> {{ myObj.owner.id }}  <b>Aud ID:</b>  {{ myObj.id }}<br> {% if myObj.score %}<b>Score:</b> '+ scoreWords[{{ myObj.score }}]+'{% else %}<b>Description{% endif %}<br> {{ myObj.notes }}',color:scoreColors[{% if myObj.score %}{{ myObj.score }}{% else %}0{% endif %}], folder:'service'});
                    
					{% endfor %}	
					
					
                    GV_Finish_Map(gv_options);

				} else {
					document.getElementById('gmap_div').style.backgroundColor = '#DDDDDD';
					document.getElementById('gmap_div').innerHTML = 'Sorry, your Google Map cannot be displayed.';
				}
			}

			function boxclick(box,category,find) {
                if (box == Allbox) {
                    walk0box.checked = 1;
                    walk1box.checked = 1;
                    walk2box.checked = 1;
                    spacebox.checked = 1;
                    linkbox.checked = 1;
                    accessbox.checked = 1;
                    servicebox.checked = 1;
                    Vpoorbox.checked = 1;
                    Poorbox.checked = 1;
                    Neutralbox.checked = 1;
                    Goodbox.checked = 1;
                    Vgoodbox.checked = 1;
                    Allbox.checked = 0;
                    GV_Toggle_Markers_With_Text( {show:true, field:category,pattern:find} );
                } else {
                    if (box.checked) {
                        //GV_Toggle_Markers_With_Text( {show:true, field:category,pattern:find} );
                        box.checked = 0;
                    } else {
                        GV_Toggle_Markers_With_Text( {show:false, field:category,pattern:find} );
                    }
                }
            }

			GV_Map(); // execute the above code
		</script>    </td>
            </tr>
        <tr>
          <td valign="top" class="bodyText"><p class="style1">Audits can be visualised on a google map</p>		  </td>
        </tr>
      </table>
	  &nbsp;<br />
	  &nbsp;<br />	</td>
	</tr>

	<tr>
	<td width="15">&nbsp;</td>
    <td width="35">&nbsp;</td>
    <td width="710">&nbsp;</td>
	<td width="100%">&nbsp;</td></tr>
</table>			
					
	</body>

</html>