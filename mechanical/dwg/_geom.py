"""Shared geometry for the Rev 1 drawing package. Single source of truth."""
# overall envelope
OA_W, OA_H, OA_D = 15.370, 28.690, 3.250
T_ACM, T_PLY     = 0.118, 0.500
TUBE_D           = OA_D - T_ACM            # 3.132

# face plate features (from ../fab-rev1/make-cutfiles.py)
WIN_W, WIN_H     = 12.170, 21.240
WIN_X            = (OA_W - WIN_W) / 2      # 1.600
WIN_TOP          = 1.350                   # below the top edge
BTN_CC, BTN_DIA  = 3.500, 1.2008           # 30.5 mm
BTN_TOP          = 25.440                  # button centreline below the top edge
RAIL_TOP         = 23.715                  # cleat row below the top edge
EDGE, HOLE       = 0.625, 0.1875
R_OUT, R_IN      = 0.250, 0.250

# cavity
CAV_W, CAV_H     = OA_W - 2*T_PLY, OA_H - 2*T_PLY     # 14.370 x 27.690

# box parts
SIDE_D, SIDE_H   = TUBE_D, OA_H            # P2  3.132 x 28.690
TOPB_D, TOPB_L   = TUBE_D, CAV_W           # P3  3.132 x 14.370
REAR_W, REAR_H   = 14.270, 27.590          # P4  0.050 clearance all round

# cleats
CL, RC           = 1.000, 0.750
CLV_L            = CAV_H                   # P5  27.690
CLH_L            = CAV_W - 2*CL            # P6  12.370
RAIL_L           = CLH_L                   # P7  12.370
RCV_L            = CAV_H                   # P8  27.690

# internal frame
VESA             = 100/25.4                # 3.937
VR_W, VR_L       = 1.500, CAV_H            # P9  1.500 x 27.690
VR_X             = [OA_W/2 - VESA/2, OA_W/2 + VESA/2]
TRAY_W, TRAY_D   = 4.000, 2.900            # P10

# monitor, nominal 23.8" 16:9 portrait
MON_OW, MON_OH   = 12.870, 21.440
MON_AW, MON_AH   = 11.670, 20.740
MON_T            = 1.800                   # thickest point
MON_TOP          = 1.250                   # outline below the top edge

# depth chain, from the front face
Z = dict(face_f=0.000, face_b=0.118, mon_f=0.218, mon_b=2.018,
         vr_f=2.018, vr_b=2.518, rear_f=2.750, rear_b=3.250)

# placement on the machine
BTN_AFF, KIOSK_BOT, KIOSK_TOP = 38.000, 34.750, 63.440
DOOR_TOP, ADA_LO, ADA_HI      = 71.150, 15.0, 48.0

BOM = [
 (1,'P1','FACE PLATE',                   1,'ACM 3 mm, MATTE BLACK 2 SIDES','15.370 x 28.690','200'),
 (2,'P2','SIDE PANEL',                   2,'BALTIC BIRCH 1/2"','3.132 x 28.690','300'),
 (3,'P3','TOP / BOTTOM PANEL',           2,'BALTIC BIRCH 1/2"','3.132 x 14.370','300'),
 (4,'P4','REAR PANEL',                   1,'BALTIC BIRCH 1/2"','14.270 x 27.590','301'),
 (5,'P5','FRONT CLEAT, VERTICAL',        2,'HARDWOOD 1.00 SQ','27.690','302'),
 (6,'P6','FRONT CLEAT, HORIZONTAL',      2,'HARDWOOD 1.00 SQ','12.370','302'),
 (7,'P7','BUTTON RAIL',                  1,'HARDWOOD 1.00 SQ','12.370','302'),
 (8,'P8','REAR CLEAT, VERTICAL',         2,'HARDWOOD 0.75 SQ','27.690','302'),
 (9,'P9','VESA RAIL',                    2,'BALTIC BIRCH 1/2"','1.500 x 27.690','301'),
 (10,'P10','RASPBERRY PI TRAY',          1,'BALTIC BIRCH 1/2"','4.000 x 2.900','301'),
 (11,'H1','INSERT, THREADED, #8-32, WOOD',21,'BRASS','—','400'),
 (12,'H2','SCREW, #8-32 x 1/2, BUTTON HEAD, PIN-TORX, BLACK',15,'STEEL','—','400'),
 (13,'H3','FASTENER, QUARTER-TURN / CAPTIVE THUMBSCREW #8-32',6,'—','—','400'),
 (14,'H4','BOLT, M4 x 12, + WASHER',      4,'STEEL','VESA 100','400'),
 (15,'H5','SWITCH, PUSHBUTTON, 30 mm ANTI-VANDAL, MOM., SPST-NO',3,'STAINLESS','30.5 CUTOUT','500'),
 (16,'H6','INLET, IEC C14, PANEL MOUNT, FUSED',1,'—','—','500'),
 (17,'H7','SCREW, WOOD, #6 x 1-1/4',     40,'STEEL','—','600'),
 (18,'E1','RASPBERRY PI 4B, 4 GB',        1,'—','—','500'),
 (19,'E2','POWER SUPPLY, 5 V 3 A, USB-C', 1,'—','—','500'),
 (20,'E3','MONITOR, 24" IPS 1080p MATTE, VESA 100',1,'—','SEE NOTE 6','500'),
 (21,'E4','CABLE, HDMI, RIGHT-ANGLE, 3 ft',1,'—','—','500'),
]

# (number, title block, index line) — the title block cell fits about 26 characters
SHEETS = [
 ('000','COVER AND NOTES',      'COVER · DRAWING INDEX · GENERAL NOTES'),
 ('100','GENERAL ARRANGEMENT',  'ASSEMBLY · GENERAL ARRANGEMENT · INSTALLED CONTEXT'),
 ('101','EXPLODED VIEW AND BOM','ASSEMBLY · EXPLODED · BILL OF MATERIALS'),
 ('102','SECTION A-A',          'ASSEMBLY · SECTION A-A · DEPTH CHAIN'),
 ('200','P1 FACE PLATE',        'P1 FACE PLATE · ACM · CUT DRAWING'),
 ('300','P2 / P3 BOX PANELS',   'P2 SIDE PANEL · P3 TOP AND BOTTOM PANEL'),
 ('301','P4 / P9 / P10',        'P4 REAR PANEL · P9 VESA RAIL · P10 PI TRAY'),
 ('302','P5-P8 CLEATS',         'P5 TO P8 CLEATS AND BUTTON RAIL'),
 ('400','HOLE SCHEDULE',        'HOLE AND FASTENER SCHEDULE'),
 ('500','ELECTRICAL',           'ELECTRICAL SCHEMATIC AND WIRING'),
 ('600','ASSEMBLY SEQUENCE',    'ASSEMBLY SEQUENCE'),
 ('700','INSPECTION',           'INSPECTION DIMENSIONS AND SIGN-OFF'),
]
