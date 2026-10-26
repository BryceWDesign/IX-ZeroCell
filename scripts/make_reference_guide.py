"""Render the original system wiring and printable assembly manual.

Optional document dependency: reportlab. No vendor drawings are republished.
The JSON BOM/wiring schedule and Markdown procedure remain the editable source.
"""
import json
from pathlib import Path
import re
import subprocess
from xml.sax.saxutils import escape
import reportlab
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (SimpleDocTemplate,Paragraph,Spacer,PageBreak,
                               LongTable,TableStyle,Image,KeepTogether)

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"docs/build"
INK="#173548";TEAL="#087F83";RED="#C94737";BLUE="#286AAB";GOLD="#9B7018"
FONT_DIR=Path(reportlab.__file__).parent/'fonts'
pdfmetrics.registerFont(TTFont('ZSans',str(FONT_DIR/'Vera.ttf')))
pdfmetrics.registerFont(TTFont('ZSansBold',str(FONT_DIR/'VeraBd.ttf')))
pdfmetrics.registerFont(TTFont('ZSansItalic',str(FONT_DIR/'VeraIt.ttf')))
pdfmetrics.registerFont(TTFont('ZSansBoldItalic',str(FONT_DIR/'VeraBI.ttf')))
pdfmetrics.registerFontFamily('ZSans',normal='ZSans',bold='ZSansBold',italic='ZSansItalic',boldItalic='ZSansBoldItalic')


def schematic():
    width,height=1200,850
    pdf=canvas.Canvas(str(OUT/"SYSTEM_WIRING.pdf"),pagesize=(width,height))
    pdf.setTitle("IX-ZeroCell ZC-D10 system wiring")
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
         '<rect width="1200" height="850" fill="white"/>']
    def rect(x,y,w,h,stroke=INK,fill="#F4F8FA"):
        pdf.setStrokeColor(colors.HexColor(stroke));pdf.setFillColor(colors.HexColor(fill))
        pdf.roundRect(x,height-y-h,w,h,8,stroke=1,fill=1)
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" stroke="{stroke}" fill="{fill}"/>')
    def text(x,y,value,size=13,color=INK,bold=False):
        pdf.setFont("ZSansBold" if bold else "ZSans",size)
        pdf.setFillColor(colors.HexColor(color));pdf.drawString(x,height-y,value)
        svg.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" font-weight="{"bold" if bold else "normal"}" fill="{color}">{escape(value)}</text>')
    def line(points,color=RED,width=2):
        pdf.setStrokeColor(colors.HexColor(color));pdf.setLineWidth(width)
        path=pdf.beginPath();path.moveTo(points[0][0],height-points[0][1])
        for x,y in points[1:]:path.lineTo(x,height-y)
        pdf.drawPath(path)
        svg.append(f'<polyline points="{" ".join(str(x)+","+str(y) for x,y in points)}" fill="none" stroke="{color}" stroke-width="{width}"/>')
    def node(x,y,color=RED):
        pdf.setFillColor(colors.HexColor(color));pdf.circle(x,height-y,3,stroke=0,fill=1)
        svg.append(f'<circle cx="{x}" cy="{y}" r="3" fill="{color}"/>')
    text(30,30,"IX-ZeroCell | ZC-D10 system wiring",24,bold=True)
    text(30,53,"Version 0.2.0  |  Original module-level drawing  |  Read the complete terminal schedule before assembly",12)
    rect(30,80,190,130);text(45,106,"PV1  ACOPOWER",14,bold=True)
    text(45,129,"HY050-12M, single panel");text(45,151,"50 W STC; field-dependent")
    text(45,175,"Check polarity / cold Voc <30 V",11)
    rect(265,80,160,130);text(280,106,"F1 + S1",14,bold=True)
    text(280,130,"5 A DC fuse, PV+");text(280,152,"DPST source isolation")
    text(280,175,"Both conductors switched",11)
    rect(475,80,255,160);text(490,106,"U1  Pololu 4095",15,bold=True)
    text(490,129,"D36V50F12, 12 V buck");text(490,151,"VIN / GND  |  VOUT / GND")
    text(490,175,"EN: RUV1/RUV2 divider");text(490,199,"VRP and PG: unconnected",11)
    text(490,222,"Fixed voltage window, not MPPT",11,color=GOLD)
    line([(220,120),(265,120)]);line([(425,120),(475,120)])
    line([(220,185),(265,185)],BLUE);line([(425,185),(475,185)],BLUE)
    text(225,110,"PV+",10,color=RED);text(225,202,"PV-",10,color=BLUE)
    line([(730,120),(785,120),(785,290),(425,290),(425,415),(475,415)])
    text(525,278,"F2  3 A DC | qualified 12 V link",12,color=RED)
    rect(475,365,255,210);text(490,392,"U2  ADI DC1937B",15,bold=True)
    text(490,418,"E1 VIN / E3 VOUT");text(490,442,"E2/E4 returns; JP1 INTVCC")
    text(490,466,"4 x 10 F stock bank, 10 V float")
    text(490,490,"2.5 F equivalent, 2 A input limit")
    text(490,514,"Replace R3: 649k to 715k",13,color=GOLD,bold=True)
    text(490,536,"R4 stays 162k; backup ~6.50 V",12,color=GOLD)
    text(490,558,"E9 VCAP / E10 GND: service",11)
    line([(600,240),(600,325),(445,325),(445,500),(475,500)],BLUE)
    text(458,342,"Power returns follow W08/W10/W14",10,color=BLUE)
    rect(830,365,265,180);text(845,392,"U3  Pololu 4091",15,bold=True)
    text(845,418,"D36V50F5, final 5 V buck")
    text(845,442,"VIN from U2; common return")
    text(845,466,"EN default; VRP/PG unused",11)
    text(845,490,"Use paired power-pad pigtails",11)
    text(845,518,"Thermal/load qualification required",11,color=GOLD)
    line([(730,415),(830,415)]);text(739,402,"E3 VOUT",10,color=RED)
    line([(730,500),(830,500)],BLUE);text(744,519,"E4 GND",10,color=BLUE)
    rect(830,670,265,115);text(845,696,"F3 + S2 / JOUT",15,bold=True)
    text(845,720,"5 A DC fuse / output switch")
    text(845,744,"5 V DC, 10 W design target")
    text(845,768,"20 W only after unit-specific tests",11,color=GOLD)
    line([(1095,415),(1150,415),(1150,710),(1095,710)])
    line([(1095,500),(1170,500),(1170,770),(1095,770)],BLUE)
    text(1110,650,"+",16,color=RED,bold=True);text(1174,745,"-",16,color=BLUE,bold=True)
    rect(30,335,330,235);text(45,360,"U1 enable divider, W15-W18",14,bold=True)
    text(45,382,"VIN",11,color=RED)
    line([(80,390),(220,390),(220,400)],GOLD)
    line([(80,390),(80,400)],GOLD)
    rect(65,400,30,30,GOLD,'#FFFFFF');rect(205,400,30,30,GOLD,'#FFFFFF')
    text(105,420,"RUV1 2.20k",10);text(245,415,"100k",10)
    text(245,429,"internal",9)
    line([(80,430),(80,450),(310,450)],GOLD)
    line([(220,430),(220,450)],GOLD);node(80,450,GOLD)
    text(270,443,"U1 EN",10,color=GOLD)
    line([(80,450),(80,465)],GOLD);rect(65,465,30,25,GOLD,'#FFFFFF')
    text(108,481,"RUV2 191 ohm",11)
    line([(80,490),(80,505)],BLUE)
    line([(65,505),(95,505)],BLUE);line([(70,510),(90,510)],BLUE);line([(75,515),(85,515)],BLUE)
    text(45,538,"Typical on/off: 16.57 / 14.72 V",12,bold=True)
    text(45,559,"Measure actual thresholds on the bench.",10)
    rect(475,655,255,130);text(490,681,"Service branch only",14,bold=True)
    text(490,705,"E9 / F4 2 A / S3 / RDIS")
    text(490,728,"RDIS: 100 ohm / 5 W, to E10")
    text(490,751,"S3 OFF for run; source isolated",11,color=GOLD)
    text(490,774,"Meter bank below 0.5 V before work",11)
    line([(730,545),(765,545),(765,700),(730,700)])
    line([(475,735),(400,735),(400,600),(600,600),(600,575)],BLUE)
    text(30,627,"Stock bank: brief interruption buffer",15,bold=True)
    text(30,650,"Not overnight storage or a 72-hour blackout supply.",11)
    text(30,676,"Red: positive power     Blue: return",12)
    text(30,700,"All grounds above are the same electrical return.",11)
    text(30,724,"No USB-C PD, mains or parallel output bus.",11)
    text(30,748,"Required details: BOM.md, WIRING.md and",11)
    text(30,768,"docs/build/ASSEMBLY_GUIDE.md",11,bold=True)
    text(30,816,"DESIGN REFERENCE / NOT A MEASUREMENT REPORT | Output depends on source, component condition, losses and actual tests.",11,color=GOLD)
    pdf.showPage();pdf.save();svg.append('</svg>')
    (OUT/"SYSTEM_WIRING.svg").write_text('\n'.join(svg))
    subprocess.run(['pdftoppm','-f','1','-singlefile','-scale-to','1800','-png',
                    str(OUT/'SYSTEM_WIRING.pdf'),str(OUT/'SYSTEM_WIRING')],check=True)


def manual():
    styles=getSampleStyleSheet()
    for style in styles.byName.values():
        if getattr(style,'fontName','').startswith('Helvetica'):
            style.fontName='ZSansBold' if 'Bold' in style.fontName else 'ZSans'
    styles.add(ParagraphStyle(name='BodyZ',fontName='ZSans',fontSize=9.3,leading=13.3,
                             textColor=colors.HexColor(INK),spaceAfter=7))
    styles.add(ParagraphStyle(name='SmallZ',parent=styles['BodyZ'],fontSize=8,leading=10.5))
    styles.add(ParagraphStyle(name='HeadingZ',parent=styles['Heading2'],fontName='ZSansBold',
                             fontSize=14,leading=18,textColor=colors.HexColor(TEAL),spaceBefore=12,spaceAfter=8,keepWithNext=True))
    styles.add(ParagraphStyle(name='CellZ',parent=styles['SmallZ'],fontSize=8.2,leading=10.8,wordWrap='CJK',spaceAfter=1))
    def markup(text):
        text=escape(text)
        text=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',text)
        text=re.sub(r'`(.*?)`',r'<font name="Courier">\1</font>',text)
        text=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',r'<link href="\2" color="#087F83">\1</link>',text)
        return text
    def para(text,style='BodyZ'):return Paragraph(markup(text),styles[style])
    story=[Paragraph('IX-ZeroCell',styles['Title']),
           Paragraph('Everyday Power Reference Build',styles['Heading1']),
           para('ZC-D10 | Version 0.2.0 | Bryce Lovell | 25 October 2026'),
           para('**Construction reference:** complete module-level BOM, wiring and assembly. Hardware output has not been measured in this session.'),
           Image(str(OUT/'SYSTEM_WIRING.png'),width=500,height=500*850/1200),
           para('The stock bank buffers brief interruptions. The design target is 5 V / 10 W when the real source supports it; 20 W requires separate qualification. The power path needs no Arduino or computer.'),
           PageBreak()]
    pending_heading=None
    for line in (OUT/'ASSEMBLY_GUIDE.md').read_text().splitlines():
        if not line.strip() or line.startswith('# '):continue
        if line.startswith('## '):
            pending_heading=Paragraph(markup(line[3:]),styles['HeadingZ'])
            continue
        body=para(line)
        if pending_heading is not None:
            story.append(KeepTogether([pending_heading,body]))
            pending_heading=None
        elif re.match(r'^\d+\.',line):story.append(KeepTogether([body]))
        else:story.append(body)
    story += [PageBreak(),Paragraph('Complete assembly BOM',styles['HeadingZ']),
              para('Purchased populated modules include their internal components. Commodity items are fully specified purchase requirements; no current cost or availability is invented.')]
    bom=json.loads((ROOT/'hardware/reference_build/BOM.json').read_text())
    rows=[[para('Ref','CellZ'),para('Qty','CellZ'),para('Part / specification','CellZ'),para('Purpose','CellZ')]]
    for item in bom['parts']:
        part=item['manufacturer']+'; '+item['part_or_purchase_spec']
        if item['source_url']:part+=' [source]('+item['source_url']+')'
        rows.append([para(item['ref'],'CellZ'),para(str(item['quantity']),'CellZ'),
                     para(part,'CellZ'),para(item['function'],'CellZ')])
    table=LongTable(rows,colWidths=[58,24,225,208],repeatRows=1,hAlign='LEFT')
    table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#D9ECEE')),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F5F8FA')]),
        ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),
        ('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),5),
        ('BOTTOMPADDING',(0,0),(-1,-1),5),('LINEBELOW',(0,0),(-1,0),.7,colors.HexColor(TEAL))]))
    story.append(table)
    story += [Spacer(1,12),Paragraph('Required commissioning equipment',styles['HeadingZ'])]
    apparatus=[('Isolated current-limited supply','1','0-25 V, at least 3 A'),
               ('Calibrated DC voltmeters','2','0-30 V, resolve 10 mV'),
               ('Simultaneous input/output power channels','2','0-30 V, 0-5 A, logged acquisition'),
               ('Electronic load','1','Constant power 0-25 W; operates at 5 V'),
               ('Oscilloscope','1','At least two channels, correctly referenced probes'),
               ('Temperature probes','3','One per power module'),
               ('Fine soldering and wire tools','1 set','Magnification and equipment suitable for 0402 rework')]
    for name,qty,spec in apparatus:story.append(para(qty+' x '+name+': '+spec,'SmallZ'))
    story.append(para('Keep test equipment and passive load resistors outside the enclosure. Meter supply/debug power that can enter the assembly. Use the current manufacturer reference for any instrument connections.','SmallZ'))
    story += [PageBreak(),Paragraph('Terminal-by-terminal wiring schedule',styles['HeadingZ'])]
    wiring=json.loads((ROOT/'hardware/reference_build/wiring.json').read_text())
    rows=[[para(t,'CellZ') for t in ['Wire','From','To','AWG','Max mm']]]
    for row in wiring['connections']:
        rows.append([para(str(row[k]),'CellZ') for k in ['wire','from','to','awg','maximum_route_mm']])
    table=LongTable(rows,colWidths=[45,180,180,45,65],repeatRows=1)
    table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#D9ECEE')),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F5F8FA')]),
        ('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
    story += [table,Spacer(1,10),para(wiring['module_power_termination'])]
    story += [PageBreak(),Paragraph('Executed proof of concept',styles['HeadingZ'])]
    story += [para('Six executed circuit screens: five module-level power-path cases and an enable-divider hysteresis run. They are simulations, with no ZeroCell hardware measurement implied.'),
              para('The power-path model starts at the qualified 12 V input to U2. It represents finite capacitor energy, declared conversion losses, source/charge current budgets, priority load delivery, source removal and exhausted-bank cutoff. It is not a vendor switching, thermal, EMI or component-failure macromodel.'),
              para('Reproduce with: `python scripts/run_reference_poc.py` after installing ngspice on PATH. Editable netlists, solver logs and labelled simulated traces are included. Full method: `docs/build/PROOF_OF_CONCEPT.md`.')]
    results=json.loads((ROOT/'results/reference_build/spice_poc.json').read_text())
    rows=[[para(x,'CellZ') for x in ['Simulated case','Input-present regulation','Interruption >=4.75 V']]]
    for case in results['cases']:
        rows.append([para(case['case'].replace('_',' '),'CellZ'),
                     para('yes' if case['input_present_load_in_range'] else 'no, expected control','CellZ'),
                     para(f"{case['interruption_seconds_at_4_75V_or_above']:.3f} s",'CellZ')])
    table=LongTable(rows,colWidths=[230,155,130],repeatRows=1)
    table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#D9ECEE')),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F5F8FA')]),
        ('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
    story += [table,Spacer(1,10),
              para('The zero-input empty-bank case delivers no output; the 25 W overload does not maintain the requested rail. These are required negative controls, not defects hidden from the report.'),
              para('The enable-divider simulation gives about 16.566 V turn-on and 14.724 V turn-off using ideal threshold values. Real thresholds must be measured.'),
              para('The reported 8.4 s / 4.0 s interruption figures depend on assumed efficiency, resistance, leakage, bank state and load. The actual unit must undergo the physical tests in steps 39-56; no simulated duration is a rated backup time.')]
    story += [PageBreak(),Paragraph('Primary sources',styles['HeadingZ'])]
    for line in (OUT/'PRIMARY_SOURCES.md').read_text().splitlines():
        if not line.strip() or line.startswith('# ') or line.startswith('|---'):continue
        if line.startswith('| Source'):continue
        story.append(para(line.strip('| ').replace(' | ',' - ')))
    def decorate(c,doc):
        c.saveState();c.setStrokeColor(colors.HexColor(TEAL));c.line(40,803,555,803)
        c.setFont('ZSans',8);c.setFillColor(colors.HexColor(INK))
        c.drawString(40,813,'IX-ZeroCell | ZC-D10 | Assembly reference')
        c.drawString(40,25,'Version 0.2.0 | Source-dependent power | Hardware measurements outstanding')
        c.drawRightString(555,25,f'{doc.page}')
        c.restoreState()
    doc=SimpleDocTemplate(str(OUT/'ASSEMBLY_AND_BOM.pdf'),pagesize=(595.28,841.89),
                          rightMargin=40,leftMargin=40,topMargin=50,bottomMargin=45,
                          title='IX-ZeroCell ZC-D10 assembly and BOM',author='Bryce Lovell')
    doc.build(story,onFirstPage=decorate,onLaterPages=decorate)


if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    schematic();manual()
    print('Rendered system drawing and printable assembly/BOM guide.')
