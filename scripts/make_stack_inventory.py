"""Regenerate assembly-scope inventory and power routes; resets open gate register."""
import json,csv,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R))
from ix_zerocell.stack import StackDesign
D=StackDesign();rows=[]
def add(ref,q,spec,role,status='specified_component',source='',scope='channel'):
 rows.append(dict(ref=ref,quantity_per_scope=q,scope=scope,stack_quantity=q*(20 if scope=='channel' else 1),part_or_purchase_spec=spec,role=role,selection_status=status,source=source))
adi='https://www.analog.com/media/en/technical-documentation/user-guides/dc1924afa.pdf'
eaton='https://www.eaton.com/content/dam/eaton/products/electronic-components/resources/data-sheet/eaton-xlr-48-supercapacitor-module-data-sheet.pdf'
add('PV1-PV3',3,'REC420AA PURE-R, 420 W','Parallel solar source; no series connection',source='https://www.recgroup.com/sites/default/files/2025-01/Web_DS_REC_Alpha_Pure-R_EN.pdf')
add('A1-A4',4,'ADI DC1924A populated board','Direct, two charging, output converter; modifications required',source=adi)
add('C01-C60',60,'Eaton XLR-48R6167-R, 166 F, 48.6 V','Storage module; individually characterized',source=eaton)
add('RC01-RC60',60,'TE HSC2002R2J, 2.2 ohm 200 W 5%','Module fault-current limiting; pulse coordination outstanding',source='https://www.te.com/en/product-1-1630019-6.html')
add('FC01-FC60',60,'Littelfuse KLKD, 2 A DC fuse','Module positive-terminal protection','coordination_pending')
add('HC01-HC60',60,'Finger-safe fuse holder matched to KLKD 10x38 mm; >=100 VDC and bank fault duty','Module fuse holders','installation_selection')
add('D1-D5',5,'STPS10H100CFP; join both anodes; common cathode','Direct, chargers, storage, and output reverse blocking',source='https://www.st.com/resource/en/datasheet/stps10h100c.pdf')
add('HD1-HD5',5,'Insulated mounting/heat sink assembly for TO-220FP diode; validate junction temperature at measured loss','Diode cooling','thermal_selection')
add('RB',1,'1.2 ohm, 1%, >=50 W aluminium-housed wirewound resistor; voltage and pulse rating coordinated with fuses','Passive output sharing','purchase_specification')
add('FPV1-FPV3',3,'Littelfuse KLKD, 15 A DC','PV parallel-branch fuse','coordination_pending')
add('FPVMAIN',1,'Littelfuse KLKD, 30 A DC','PV combiner fuse','coordination_pending')
add('FA1',1,'Littelfuse KLKD, 5 A DC','Direct board input fuse','coordination_pending')
add('FA2-FA3',2,'Littelfuse KLKD, 10 A DC','Charge board input fuses','coordination_pending')
add('FBANK',1,'Littelfuse KLKD, 15 A DC','Bank trunk fuse','coordination_pending')
add('FGATE',1,'Littelfuse KLKD, 5 A DC','Bank gate load branch','coordination_pending')
add('FA4',1,'Littelfuse KLKD, 5 A DC','Output converter input branch','coordination_pending')
add('FOUT_LOCAL-FOUT_BUS',2,'Littelfuse KLKD, 2 A DC','Feeder protection at source and combiner ends','coordination_pending')
add('HF',12,'DC fuse holders matching non-module KLKD fuses above; verify interrupt duty','Other specified channel fuse holders','installation_selection')
add('K1',1,'TE EV200AAANA, normally open; coil fed only from PV auxiliary','Source disconnect','driver_coordination_pending','https://www.te.com/en/product-1618002-7.html')
add('AUX12',1,'Traco TEN 60-7212WIR, 36–160 V input, 12 V output','PV-only coil and auxiliary feed',source='https://www.tracopower.com/ten60wir-datasheet')
add('AUX5P-AUX5B',2,'RECOM R-78HB5.0-0.5, 9–72 V input, 5 V output','PV-side and bank-side logic supply',source='https://recom-power.com/en/products/switching-regulators/switching-regulators-sip/rec-p-R-78HB5.0-0.5.html')
add('AUXPROTECT',1,'Dedicated PV/bank auxiliary branch fuses, output OR diodes, decoupling and pickup-current allowance','Auxiliary protection assembly','G01_unreleased')
add('A5',1,'LM5069-1 based gate; CSD19536KTT candidate pass FET; independent UVLO/OVLO option','Bank gate, SOA/inrush redesign for revised input load','G01_unreleased','https://www.ti.com/lit/ds/symlink/lm5069.pdf')
add('OVCTRL',1,'TLV1702 + LM4040A25; nominal charge divider 178 kohm/10 kohm; latched independent cutoff','OV comparator and fault-priority latch/driver assembly','G01_unreleased')
add('TS01-TS60',60,'Normally closed, calibrated 45 C body-temperature switch with supervised open-circuit wiring','Thermal fault sensing','G01_unreleased')
add('ALARM',1,'60-module open-collector alarm and supervised continuity harness; <=5 mA sink per module','Eaton alarm aggregation; not a direct MCU substitute','G01_unreleased')
add('R49_A1',1,'86.6 kohm, 0.1%, 0603','A1 output current resistor')
add('R49_A2_A3',2,'34.8 kohm, 0.1%, 0603','Charger output current resistors')
add('R49_A4',1,'143 kohm, 0.1%, 0603 plus 10 kohm sealed multi-turn trim','Calibrated A4 current; two physical parts')
add('R13_A1_A4',2,'392 kohm, 0.1%, 0603 plus 20 kohm sealed multi-turn trim','Output divider; each set has two physical parts')
add('R13_A2_A3',2,'374 kohm, 0.1%, 0603 plus 5 kohm sealed multi-turn trim','Charger divider; each set has two physical parts')
add('R16_A1_A4',4,'10.0 kohm, 0.1%, 0603','Divider bottoms; existing board part may be retained after inspection')
add('R53_A1',1,'590 kohm, 0.1%, 0603','Direct source regulation')
add('R53_A2_A3',2,'649 kohm, 0.1%, 0603','Charging source regulation')
add('R54_A1_A3',3,'20.0 kohm, 0.1%, 0603','Source-regulation bottoms')
add('R11_A1_A3',3,'590 kohm, 0.1%, 0603','PV input UVLO top')
add('R11_A4',1,'294 kohm, 0.1%, 0603','Output stage input UVLO top')
add('R14_A1_A4',4,'20.0 kohm, 0.1%, 0603','UVLO bottoms; existing board part must meet target tolerance')
add('ISOLATORS',1,'Lockable DC-rated PV/bank service isolation set; ratings derived from complete fault study','Service isolation; opening is not discharge','G03_G06_unreleased')
add('RACK',4,'Anchored rack >=300 kg rated load, fifteen modules per rack, insulated covers and individual restraints','Storage mechanics','G06_unreleased')
add('CHANNEL_HARNESS',1,'Equal-length module branches; 2.5 mm2 copper reference, trunk 6 mm2 reference, >=100 V insulation; final lengths/ampacity site-designed','Lugs, strain relief, labels, wiring, busbar guards and supports','G06_unreleased')
add('SECTION',4,'Five-channel busbar/return with covered terminals, rated section disconnect/protection','Section combining','G05_unreleased',scope='stack')
add('MAIN',1,'Main DC disconnect, load protection, independent output OV/UV shutdown and precharge','Common output protection and startup','G05_unreleased',scope='stack')
add('CENTRAL',1,'Metering and optional supervisory logger within total 50 W common loss budget','No final acquisition/actuation hardware selected','G05_unreleased',scope='stack')
add('SITE',1,'PV mounting, matched connectors, conductor routing, bonding, enclosures, cooling and structural plan','Installation engineering inventory','G06_unreleased',scope='stack')
add('TEST',1,'Calibrated 80 V current-limited supply; >=1.5 kW 60 V DC load; synchronized meters; differential probes; temperature logging; limited-energy fault fixture','Test equipment, not installed operating source','equipment_specification',scope='stack')
data={'version':'0.2.0','profile':'ZC-S1000-B','hardware_measured':False,'procurement_released':False,
      'scope':'Assembly-scope inventory, not a closed component-level BOM for unreleased control/protection assemblies',
      'internal_board_parts':'A1-A4 purchased populated; vendor board BOM covers unchanged parts; rework is enumerated separately',
      'parts':rows}
p=R/'hardware/stack1000';(p/'BOM.json').write_text(json.dumps(data,indent=2)+'\n')
with (p/'BOM.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
s=['# ZC-S1000 assembly-scope BOM','',data['scope']+'. **Procurement release: NO.** Rows marked Gxx require completed design before purchase/energization. No unselected assembly is represented as a ready-made product. A populated board includes its manufacturer internal BOM; replacement parts are additional. All quantities exclude spares. Prices and availability are not asserted.','','| Ref | Per scope | Stack quantity | Part or purchase specification | Status |','|---|---:|---:|---|---|']
for x in rows:s.append(f"| {x['ref']} | {x['quantity_per_scope']} / {x['scope']} | {x['stack_quantity']} | {x['part_or_purchase_spec']} | {x['selection_status']} |")
(p/'BOM.md').write_text('\n'.join(s)+'\n')
gates=[{'id':f'G{i:02}','status':'open','hardware_release_blocker':True} for i in range(1,8)]
(p/'release_gates.json').write_text(json.dumps({'version':'0.2.0','construction_released':False,'hardware_validated':False,'gates':gates},indent=2)+'\n')
(p/'design.json').write_text(json.dumps(D.bounds(),indent=2)+'\n')
# Connection IDs identify actual board terminals; protection assemblies remain explicitly logical interfaces.
wires=[]
def wire(ch,a,b,kind='power',status='design_route'):
 wires.append({'id':f'W{len(wires)+1:05}','channel':ch,'from':a,'to':b,'class':kind,'status':status})
for i in range(1,21):
 ch=f'CH{i:02}';n=lambda x:ch+'.'+x
 for j in range(1,61):
  wire(ch,n(f'C{j:02}.positive'),n(f'FC{j:02}.in'));wire(ch,n(f'FC{j:02}.out'),n(f'RC{j:02}.in'))
  wire(ch,n(f'RC{j:02}.out'),n('CB+'));wire(ch,n(f'C{j:02}.negative'),n('B0'))
 for j in range(1,4):
  wire(ch,n(f'PV{j}.positive'),n(f'FPV{j}.in'));wire(ch,n(f'FPV{j}.out'),n('PV_COMBINER+'));wire(ch,n(f'PV{j}.negative'),n('B0'))
 for a,b in [('PV_COMBINER+','FPVMAIN.in'),('FPVMAIN.out','K1.contact_in'),('K1.contact_out','PV_SWITCHED+')]:wire(ch,n(a),n(b))
 for j in range(1,4):
  wire(ch,n('PV_SWITCHED+'),n(f'FA{j}.in'));wire(ch,n(f'FA{j}.out'),n(f'A{j}.TP1'));wire(ch,n(f'A{j}.TP3'),n('B0'));wire(ch,n(f'A{j}.TP4'),n('B0'))
  wire(ch,n(f'A{j}.TP2'),n(f'D{j}.anodes'));wire(ch,n(f'D{j}.cathode'),n('SUPPLY+' if j==1 else 'CB+'))
 for a,b in [('CB+','FBANK.in'),('FBANK.out','FGATE.in'),('FGATE.out','A5.IN'),('A5.OUT','D4.anodes'),('D4.cathode','SUPPLY+'),('SUPPLY+','FA4.in'),('FA4.out','A4.TP1'),('A4.TP3','B0'),('A4.TP4','B0'),('A4.TP2','RB.in'),('RB.out','D5.anodes'),('D5.cathode','FOUT_LOCAL.in'),('FOUT_LOCAL.out','FOUT_BUS.in')]:wire(ch,n(a),n(b),status='G01_interface' if 'A5' in a+b else 'design_route')
 section=(i-1)//5+1
 wire(ch,n('FOUT_BUS.out'),f'SECTION{section}.positive',status='G05_interface');wire(ch,n('B0'),f'SECTION{section}.return',status='G05_interface')
 for j in range(1,5):wire(ch,n('OVCTRL.inhibit_A'+str(j)),n(f'A{j}.TP5'),kind='control',status='G01_unreleased_logical_interface')
for i in range(1,5):
 wire('COMMON',f'SECTION{i}.positive','MAIN.input+',status='G05_interface');wire('COMMON',f'SECTION{i}.return','MAIN.return',status='G05_interface')
wire('COMMON','MAIN.protected_output+','LOAD.positive',status='G05_interface');wire('COMMON','MAIN.return','LOAD.negative',status='G05_interface')
with (p/'WIRING.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=wires[0].keys());w.writeheader();w.writerows(wires)
(p/'WIRING.md').write_text('# Stack connection schedule\n\n`WIRING.csv` enumerates '+str(len(wires))+' power/control routes with unique IDs. It is a power-topology schedule, not a complete harness fabrication drawing. G01/G05 interfaces are logical unreleased assemblies; their labels do not pretend to be physical connector pinouts. Auxiliary, thermal and alarm harness fabrication is blocked by G01. See DESIGN.md and ASSEMBLY.md before using any route.\n\nDC1924A terminal mapping: TP1 VIN, TP3 input PGND, TP2 VOUT, TP4 output PGND, TP5 /SHDN. Diode anodes join; cathode faces destination bus. No series-connected capacitor modules or panels.\n')
print(len(rows),'BOM rows;',len(wires),'routes')
