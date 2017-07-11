##################################################################
FileName		= 'JTreportlabCharts.py'
# By:			Jason Thorne
# Date:			23-06-2013
# Description: 	This is an include file of standard classes to use 
# for my reportlab charts.
##################################################################
from reportlab.lib.colors import HexColor 

from reportlab.lib.colors import Color, blue, red
from reportlab.graphics.charts.legends import Legend, TotalAnnotator
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from reportlab.lib.validators import Auto
from reportlab.graphics.charts.barcharts import VerticalBarChart

from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.colors import black, red, purple, green, maroon, brown, pink, white, HexColor
from reportlab.graphics.charts.legends import Legend
from reportlab.lib.colors import HexColor, black

"""pdf_chart_colors = [ HexColor("#0000e5"), HexColor("#1f1feb"), HexColor("#5757f0"), \
HexColor("#8f8ff5"), HexColor("#c7c7fa"), HexColor("#f5c2c2"), HexColor("#eb8585"), \
HexColor("#e04747"), HexColor("#d60a0a"), HexColor("#cc0000"), HexColor("#ff0000"), ] 
"""
pdf_chart_colors = [
		HexColor("#0000e5"),\
		HexColor("#1f1feb"),\
		HexColor("#5757f0"),\
		HexColor("#8f8ff5"),\
		HexColor("#c7c7fa"),\
		HexColor("#f5c2c2"),\
		HexColor("#eb8585"),\
		HexColor("#e04747"),\
		HexColor("#d60a0a"),\
		HexColor("#cc0000"),\
		HexColor("#ff0000"),\
		]
##################################################################
class JRTpieDrawing(_DrawingEditorMixin,Drawing):

	def __init__(self,width=400,height=200,*args,**kw):
		apply(Drawing.__init__,(self,width,height)+args,kw)
		# adding a pie chart to the drawing 
		self._add(self, Pie(), name='pie', validate=None, desc=None)
		self.pie.width					= 150
		self.pie.height					= self.pie.width
		self.pie.x						= 20
		self.pie.y						= (height-self.pie.height)/2
		
		self.pie.simpleLabels			= 1
		self.pie.slices.label_visible	= 0
		self.pie.slices.fontColor		= None
		self.pie.slices.strokeColor		= white
		self.pie.slices.strokeWidth		= 1
		
		# adding legend
		self._add(self,Legend(),name='legend',validate=None,desc=None)
		self.legend.x					= 200
		self.legend.y					= height/2
		self.legend.dx					= 8
		self.legend.dy					= 8
		self.legend.fontName			= 'Helvetica'
		self.legend.fontSize			= 7
		self.legend.boxAnchor			= 'w'
		self.legend.columnMaximum		= 10
		self.legend.strokeWidth			= 1
		self.legend.strokeColor			= black
		self.legend.deltax				= 75
		self.legend.deltay				= 10
		self.legend.autoXPadding		= 5
		self.legend.yGap				= 0
		self.legend.dxTextSpace			= 5
		self.legend.alignment			= 'right'
		self.legend.dividerLines		= 1|2|4
		self.legend.dividerOffsY		= 4.5
		self.legend.subCols.rpad		= 30
	# end __init__
# end BreakdownPieDrawing
		
##################################################################
class JTVBar(_DrawingEditorMixin,Drawing):
	def __init__(self,width=400,height=200,*args,**kw):
		apply(Drawing.__init__,(self,width,height)+args,kw)
		self._add(self,VerticalBarChart(),name='bar',validate=None,desc=None)
		self.bar.data			 = [[4.22], [4.12], [3.65], [3.56], [3.49], [3.44], [3.07], \
		[2.84], [2.76], [1.09]]
		self.bar.categoryAxis.categoryNames = ['Financials','Energy','Health Care','Telecoms',\
		'Consumer','Consumer 2','Industrials','Materials','Other','Liquid Assets']
		self.bar.categoryAxis.labels.fillColor = None
		self.bar.width					= 200
		self.bar.height					= 150
		self.bar.x						= 30
		self.bar.y						= 15
		self.bar.barSpacing				= 5
		self.bar.groupSpacing			= 5
		self.bar.valueAxis.labels.fontName	= 'Helvetica'
		self.bar.valueAxis.labels.fontSize	= 8
		self.bar.valueAxis.forceZero	= 1
		self.bar.valueAxis.rangeRound	= 'both'
		self.bar.valueAxis.valueMax		= None#10#
		self.bar.categoryAxis.visible	= 1
		self.bar.categoryAxis.visibleTicks	= 0
		self.bar.barLabels.fontSize		= 6
		self.bar.valueAxis.labels.fontSize	= 6
		self.bar.strokeWidth			= 0.1
		self.bar.bars.strokeWidth		= 0.5
		n								= len(self.bar.data)
		setItems(n,self.bar.bars,'fillColor',pdf_chart_colors)
		#add and set up legend
		self._add(self,Legend(),name='legend',validate=None,desc=None)
		_ = ['Vodafone Group', 'UBS', 'British Petroleum', 'Royal bk of Scotland', \
		'HSBC Holdings', 'Total Elf Fina', 'Repsol', 'Novartis', 'BNP Paribas', 'Schneider Electric' ]
		self.legend.colorNamePairs  = [(Auto(chart=self.bar),(t,'%.2f'% d[0])) \
		for t,d in zip(_,self.bar.data)]
		self.legend.columnMaximum   = 10
		self.legend.fontName		= 'Helvetica'
		self.legend.fontSize		= 5.5
		self.legend.boxAnchor		= 'w'
		self.legend.x				= 260
		self.legend.y				= self.height/2
		self.legend.dx				= 8
		self.legend.dy				= 8
		self.legend.alignment		= 'right'
		self.legend.yGap			= 0
		self.legend.deltay			= 11
		self.legend.dividerLines	= 1|2|4
		self.legend.subCols.rpad	= 10
		self.legend.dxTextSpace		= 5
		self.legend.strokeWidth		= 0
		self.legend.dividerOffsY	= 6
		self.legend.colEndCallout   = TotalAnnotator(rText='%.2f'%sum([x[0] \
		for x in self.bar.data]), fontName='Helvetica-Bold', fontSize=self.legend.fontSize*1.1)
		self.legend.colorNamePairs  = [(self.bar.bars[i].fillColor, \
		(self.bar.categoryAxis.categoryNames[i][0:20], '%0.2f' % self.bar.data[i][0])) \
		for i in range(len(self.bar.data))]
	# end __init__
# end FactSheetHoldingsVBar

##################################################################		
def setItems(n, obj, attr, values): 
	m = len(values) 
	i = m // n 
	
	for j in xrange(n): 
		setattr(obj[j],attr,values[j*i % m]) 
	# next j
# end setItems

##################################################################
def pieExample(): #NORUNTESTS
	drawing = BreakdownPieDrawing()
	drawing.pie.data 					= [26.90,13.30,11.10,9.40,8.50,7.80,7.00,6.20,8.80,1.00]
	drawing.pie.labels = ['Financials','Energy','Health Care','Telecoms','Consumer',\
		'Consumer 2','Industrials','Materials','Other','Liquid Assets']
	n = len(drawing.pie.data)
	setItems(n, drawing.pie.slices,'fillColor', pdf_chart_colors)
	drawing.legend.colorNamePairs = [(drawing.pie.slices[i].fillColor, (drawing.pie.labels[i][0:20],\
	'%0.2f' % drawing.pie.data[i])) for i in xrange(n)]
	
	# the drawing will be saved as pdf and png below, you could do other things with it obviously.
	drawing.save(formats=['pdf',],outDir='.',fnRoot=None)
# end pieExample

##################################################################

