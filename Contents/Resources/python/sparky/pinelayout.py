# -----------------------------------------------------------------------------
# Layouts for PINE graph
# -----------------------------------------------------------------------------
#
# Developed by Woonghee Lee
# e-mail: whlee@nmrfam.wisc.edu
# National Magnetic Resonance Facilities at Madison
# Department of Bichemistry, University of Wisconsin at Madison
#
# Last updated: May 10, 2010
# 
# Usage:
#
# 
# -----------------------------------------------------------------------------
pseudo_layout = {
## from here
  'C': {
    'QB':('HB2', 'HB3'),
    },
  'D': {
    'QB':('HB2', 'HB3'),
    },
  'E': {
    'QB':('HB2','HB3'),
    'QG':('HG2','HG3'),
    },
  'F': {
    'QB':('HB2','HB3'),
    'QD':('HD1','HD2'),
    'QE':('HE1','HE2'),
    },
  'G': {
    'QA':('HA2','HA3'),
    },
  'H': {
    'QB':('HB2','HB3'),
    },
  'K': {
    'QB':('HB2','HB3'),
    'QD':('HD2','HD3'),
    'QE':('HE2','HE3'),
    'QG':('HG2','HG3'),
    },
  'L': {
    'QB':('HB2','HB3'),    
    },
  'M': {
    'QB':('HB2','HB3'),
    'QG':('HG2','HG3'),
    },
  'N': {
    'QB':('HB2','HB3'),
    'QD2':('HD21','HD22'),
    },
  'P': {
    'QB':('HB2','HB3'),
    'QD':('HD2','HD3'),
    'QG':('HG2','HG3'),
    },
  'Q': {
    'QB':('HB2','HB3'),
    'QE2':('HE21','HE22'),
    'QG':('HG2','HG3'),
    },
  'R': {
    'QB':('HB2','HB3'),
    'QD':('HD2','HD3'),
    'QG':('HG2','HG3'),
    'QH1':('HH11','HH12'),
    'QH2':('HH21','HH22'),
    },
  'S': {
    'QB':('HB2','HB3'),
    },
  'W': {
    'QB':('HB2','HB3'),
    },
  'Y': {
  #  'CD':('CD1','CD2'),
  #  'CE':('CE1','CE2'),
    'QB':('HB2','HB3'),
    'QD':('HD1','HD2'),
    'QE':('HE1','HE2'),
    },
  'I': {
    'QG1':('HG12','HG13'),
    },
 }
meta_layout = {
  'A': {
    'HB': ('HB1','HB2','HB3')
    },
  'I': {
  #  'CG':('CG1','CG2'),
    'HD1':('HD11','HD12','HD13'),
    'HG2':('HG21','HG22','HG23'),
    },
  'K': {
    'HZ':('HZ1','HZ2','HZ3'),
    },
  'L': {
  #  'CD':('CD1','CD2'),
    'HD1':('HD11','HD12','HD13'),
    'HD2':('HD21','HD22','HD23'),
  #  'HD':('HD1','HD2','HD3','HD11','HD12','HD13','HD21','HD22','HD23'),
    },
  'M': {
    'HE':('HE1','HE2','HE3'),
    },
  'T': {
    'HG2':('HG21','HG22','HG23'),
    },
  'V': {
  #  'CG':('CG1','CG2'),
    'HG1':('HG11','HG12','HG13'),
    'HG2':('HG21','HG22','HG23'),
  #  'HG':('HG1','HG2','HG11','HG12','HG13','HG21','HG22','HG23'),
    },
  }
pine_disabled_layout = {
    'S':('OG', 'HG'),
    'T':('HG1'),
    'C':('SG', 'HG'),
    'M':('CE', 'HE1', 'HE2', 'HE3'),
#    'F':('CG', 'CD1', 'CE1', 'CZ', 'HZ', 'CD2', 'CE2', 'HD11', 'HD12', 'HE11', 'HE12', 'HD21', 'HD22', 'HE21', 'HE22'),
    'F':('CG', 'CD1', 'CE1', 'CZ', 'HZ', 'CD2', 'CE2', 'HD1', 'HE1', 'HD2', 'HE2'),
    'Y':('CG', 'CD1', 'CD2', 'CE1', 'CE2', 'CZ', 'HD11', 'HD12', 'HD21', 'HD22', 'HE11', 'HE12', 'HE21', 'HE22', 'HH', 'OH'),
    'W':('CG', 'CD1', 'CD2', 'NE1', 'CE2', 'CE3', 'CZ2', 'CZ3', 'CH2', 'HD1', 'HD2', 'HE1', 'HE3', 'HZ2', 'HZ3', 'HH2'),
    'H':('CG', 'ND1', 'CD2', 'NE1', 'CE2', 'HD1', 'HD2', 'HE1', 'HE2'),
    'D':('CG2', 'OD1', 'OD2', 'HD2'),
    'E':('CD', 'OD1', 'OD2', 'HD2'),
    'N':('CG', 'OD1', 'ND2', 'HD21', 'HD22'),
    'Q':('CD', 'OE1', 'NE2', 'HE21', 'HE22'),
    #'K':('NZ', 'HZ1', 'HZ2', 'HZ3'),
    'K':('NZ', 'HZ'),
    'R':('NE', 'CZ', 'NH1', 'NH2', 'HE', 'HH11', 'HH12', 'HH21', 'HH22'),                        
    }
pine_layout = {
  'X':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("R",(-1,1)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    },               
  'G':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA2",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("HA3",(-1,1)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    },
  'A':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("HB",(-3,1)),
    'Atom8':("CB",(-1,1)),
    'Atom9':("HB",(1,1)),
    'Atom10':("HB",(-1,3)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    'Bond9':(2,(-2,1)),
    'Bond10':(2,(0,1)),
    'Bond11':(1,(-1,2)),
    },
  'S':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("HB2",(-3,1)),
    'Atom8':("CB",(-1,1)),
    'Atom9':("HB3",(1,1)),
    'Atom10':("OG",(-1,3)),
    'Atom11':("HG",(-1,5)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    'Bond9':(2,(-2,1)),
    'Bond10':(2,(0,1)),
    'Bond11':(1,(-1,2)),
    'Bond12':(1,(-1,4)),
    },
  'T':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("HB",(-3,1)),
    'Atom8':("CB",(-1,1)),
    'Atom9':("OG1",(1,1)),
    'Atom10':("HG1",(3,1)),
    'Atom11':("CG2",(-1,3)),
    'Atom12':("HG2",(-3,3)),
    'Atom13':("HG2",(1,3)),
    'Atom14':("HG2",(-1,5)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    'Bond9':(2,(-2,1)),
    'Bond10':(2,(0,1)),
    'Bond11':(2,(2,1)),
    'Bond12':(1,(-1,2)),
    'Bond13':(2,(-2,3)),
    'Bond14':(2,(0,3)),
    'Bond15':(1,(-1,4)),
    },
  'C':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("HB2",(-3,1)),
    'Atom8':("CB",(-1,1)),
    'Atom9':("HB3",(1,1)),
    'Atom10':("HG",(-1,5)),
    'Atom11':("SG",(-1,3)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    'Bond9':(2,(-2,1)),
    'Bond10':(2,(0,1)),
    'Bond11':(1,(-1,2)),
    'Bond12':(1,(-1,4)),
    },
  'V':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("HG1",(-3,1)),
    'Atom8':("HG2",(1,1)),
    'Atom9':("CB",(-1,2)),
    'Atom10':("HG1",(-5,3)),
    'Atom11':("CG1",(-3,3)),
    'Atom12':("CG2",(1,3)),
    'Atom13':("HG2",(3,3)),
    'Atom14':("HB",(-1,4)),
    'Atom15':("HG1",(-3,5)),
    'Atom16':("HG2",(1,5)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    'Bond9':(1,(-1,1)),
    'Bond10':(1,(-3,2)),
    'Bond11':(1,(1,2)),
    'Bond12':(2,(-4,3)),
    'Bond13':(9,(-2,3)),
    'Bond14':(1,(-1,3)),
    'Bond15':(5,(0,3)),
    'Bond16':(2,(2,3)),
    'Bond17':(1,(-3,4)),
    'Bond18':(1,(1,4)),
    },
  'L':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("HB2",(-3,1)),
    'Atom8':("CB",(-1,1)),
    'Atom9':("HB3",(1,1)),
    'Atom10':("HD1",(-5,3)),
    'Atom11':("HD2",(3,3)),
    'Atom12':("CG",(-1,4)),
    'Atom13':("HD1",(-5,5)),
    'Atom14':("CD1",(-3,5)),
    'Atom15':("CD2",(1,5)),
    'Atom16':("HD2",(3,5)),
    'Atom17':("HG",(-1,6)),
    'Atom18':("HD1",(-5,7)),
    'Atom19':("HD2",(3,7)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    'Bond9':(2,(-2,1)),
    'Bond10':(2,(0,1)),
    'Bond11':(1,(-1,2)),
    'Bond12':(1,(-1,3)),
    'Bond13':(3,(-4,4)),
    'Bond14':(10,(-2,4)),
    'Bond15':(6,(0,4)),
    'Bond16':(4,(2,4)),
    'Bond17':(2,(-4,5)),
    'Bond18':(1,(-1,5)),
    'Bond19':(2,(2,5)),
    'Bond20':(4,(-4,6)),
    'Bond21':(3,(2,6)),
    },
  'I':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("HG2",(-5,1)),
    'Atom8':("CB",(-1,2)),
    'Atom9':("HG2",(-5,3)),
    'Atom10':("CG2",(-3,3)),
    'Atom11':("HG2",(-5,3)),
    'Atom12':("HB",(1,3)),
    'Atom13':("HG2",(-5,5)),
    'Atom14':("CG1",(-1,5)),
    'Atom15':("HG12",(-3,7)),
    'Atom16':("CD1",(-1,7)),
    'Atom17':("HG13",(1,7)),
    'Atom18':("HD1",(-3,9)),
    'Atom19':("HD1",(-1,9)),
    'Atom20':("HD1",(1,9)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    'Bond9':(1,(-1,1)),
    'Bond10':(3,(-4,2)),
    'Bond11':(2,(-4,3)),
    'Bond12':(9,(-2,3)),
    'Bond13':(1,(-1,3)),
    'Bond14':(5,(0,3)),
    'Bond15':(4,(-4,4)),
    'Bond16':(1,(-1,4)),
    'Bond17':(4,(-2,6)),
    'Bond18':(1,(-1,6)),
    'Bond19':(1,(-1,8)),
    'Bond20':(4,(-2,8)),
    'Bond21':(3,(0,8)),
    'Bond22':(3,(0,6)),
    },
  'M':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("HB2",(-3,1)),
    'Atom8':("CB",(-1,1)),
    'Atom9':("HB3",(1,1)),
    'Atom10':("HG2",(-3,3)),
    'Atom11':("CG",(-1,3)),
    'Atom12':("HG3",(1,3)),
    'Atom13':("HE",(-3,7)),
    'Atom14':("CE",(-1,7)),
    'Atom15':("HE",(1,7)),
    'Atom16':("HE",(-1,9)),
    'Atom17':("SD",(-1,5)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    'Bond9':(2,(-2,1)),
    'Bond10':(2,(0,1)),
    'Bond11':(1,(-1,2)),
    'Bond12':(2,(-2,3)),
    'Bond13':(2,(0,3)),
    'Bond14':(1,(-1,4)),
    'Bond15':(1,(-1,6)),
    'Bond16':(2,(-2,7)),
    'Bond17':(2,(0,7)),
    'Bond18':(1,(-1,8)),
    },
  'P':{
    'Atom1':("HA",(-1,-3)),
    'Atom2':("O",(2,-3)),
    'Atom3':("N",(-3,-1)),
    'Atom4':("CA",(-1,-1)),
    'Atom5':("C",(2,-1)),
    'Atom6':("CD",(-4,1)),
    'Atom7':("CB",(0,1)),
    'Atom8':("CG",(-2,3)),
    'Atom9':("HB3",(2,1)),
    'Atom10':("HB2",(2,3)),
    'Atom11':("HG2",(-4,5)),
    'Atom12':("HG3",(0,5)),
    'Atom13':("HD2",(-6,1)),
    'Atom14':("HD3",(-6,3)),
    'Bond1':(1,(-1,-2)),
    'Bond2':(101,(2,-2)),
    'Bond3':(2,(-4,-1)),
    'Bond4':(2,(-2,-1)),
    'Bond5':(2,(0,-1)),
    'Bond6':(2,(1,-1)),
    'Bond7':(11,(-3,0)),
    'Bond8':(8,(-1,0)),
    'Bond9':(3,(-3,2)),
    'Bond10':(4,(-1,2)),
    'Bond11':(2,(1,1)),
    'Bond12':(3,(1,2)),
    'Bond13':(4,(-3,4)),
    'Bond14':(3,(-1,4)),
    'Bond15':(2,(-5,1)),
    'Bond16':(4,(-5,2)),
    },
  'F':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("HB2",(-3,1)),
    'Atom8':("CB",(-1,1)),
    'Atom9':("HB3",(1,1)),
#    'Atom10':("HD11",(-5,2)),
#    'Atom11':("HD21",(3,2)),
    'Atom10':("CG",(-1,3)),
    'Atom11':("HD1",(-5,4)),
    'Atom12':("CD1",(-3,4)),
    'Atom13':("CD2",(1,4)),
    'Atom14':("HD2",(3,4)),
#    'Atom17':("HE11",(-5,6)),
    'Atom15':("CE1",(-3,6)),
    'Atom16':("CE2",(1,6)),
#    'Atom20':("HE21",(3,6)),
    'Atom17':("CZ",(-1,7)),
    'Atom18':("HE1",(-5,8)),
    'Atom19':("HE2",(3,8)),
    'Atom20':("HZ",(-1,9)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    'Bond9':(2,(-2,1)),
    'Bond10':(2,(0,1)),
    'Bond11':(1,(-1,2)),
#    'Bond12':(3,(-4,3)),
#    'Bond13':(4,(2,3)),
    'Bond12':(2,(-4,4)),
    'Bond13':(109,(-2,4)),
    'Bond14':(5,(0,4)),
    'Bond15':(2,(2,4)),
    'Bond16':(1,(-3,5)),
    'Bond17':(101,(1,5)),
#    'Bond20':(2,(-4,6)),
    'Bond18':(106,(-2,6)),
    'Bond19':(10,(0,6)),
#    'Bond23':(2,(2,6)),
    'Bond20':(4,(-4,7)),
    'Bond21':(3,(2,7)),
    'Bond22':(1,(-1,8)),
    },
  'Y':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("HB2",(-3,1)),
    'Atom8':("CB",(-1,1)),
    'Atom9':("HB3",(1,1)),
    'Atom10':("HD11",(-5,2)),
    'Atom11':("HD21",(3,2)),
    'Atom12':("CG",(-1,3)),
    'Atom13':("HD12",(-5,4)),
    'Atom14':("CD1",(-3,4)),
    'Atom15':("CD2",(1,4)),
    'Atom16':("HD22",(3,4)),
    'Atom17':("HE11",(-5,6)),
    'Atom18':("CE1",(-3,6)),
    'Atom19':("CE2",(1,6)),
    'Atom20':("HE21",(3,6)),
    'Atom21':("CZ",(-1,7)),
    'Atom22':("HE12",(-5,8)),
    'Atom23':("HE22",(3,8)),
    'Atom24':("OH",(-1,9)),
    'Atom25':("HH",(-1,11)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    'Bond9':(2,(-2,1)),
    'Bond10':(2,(0,1)),
    'Bond11':(1,(-1,2)),
    'Bond12':(3,(-4,3)),
    'Bond13':(4,(2,3)),
    'Bond14':(2,(-4,4)),
    'Bond15':(109,(-2,4)),
    'Bond16':(5,(0,4)),
    'Bond17':(2,(2,4)),
    'Bond18':(1,(-3,5)),
    'Bond19':(101,(1,5)),
    'Bond20':(2,(-4,6)),
    'Bond21':(106,(-2,6)),
    'Bond22':(10,(0,6)),
    'Bond23':(2,(2,6)),
    'Bond24':(4,(-4,7)),
    'Bond25':(3,(2,7)),
    'Bond26':(1,(-1,8)),
    'Bond27':(1,(-1,10)),
    },
  'W':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("HB2",(-3,1)),
    'Atom8':("CB",(-1,1)),
    'Atom9':("HB3",(1,1)),
    'Atom10':("HD1",(-5,3)),
    'Atom11':("CG",(-1,3)),
    'Atom12':("HD2",(3,3)),
    'Atom13':("CD1",(-3,4)),
    'Atom14':("CD2",(1,4)),
    'Atom15':("HE3",(-6,5)),
    'Atom16':("CE3",(-4,6)),
    'Atom17':("CE2",(-1,6)),
    'Atom18':("NE1",(1,6)),
    'Atom19':("HE1",(3,6)),
    'Atom20':("CZ3",(-4,8)),
    'Atom21':("CZ2",(-1,8)),
    'Atom22':("HZ3",(-6,9)),
    'Atom23':("HZ2",(1,9)),
    'Atom24':("CH2",(-3,10)),
    'Atom25':("HH2",(-3,12)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    'Bond9':(2,(-2,1)),
    'Bond10':(2,(0,1)),
    'Bond11':(1,(-1,2)),
    'Bond12':(5,(-4,4)),
    'Bond13':(9,(-2,4)),
    'Bond14':(105,(0,4)),
    'Bond15':(9,(2,4)),
    'Bond16':(12,(-4,5)),
    'Bond17':(103,(-2,5)),
    'Bond18':(1,(1,5)),
    'Bond19':(5,(-5,6)),
    'Bond20':(2,(0,6)),
    'Bond21':(2,(2,6)),
    'Bond22':(101,(-4,7)),
    'Bond23':(1,(-1,7)),
    'Bond24':(9,(-5,8)),
    'Bond25':(7,(-3,9)),
    'Bond26':(104,(-2,9)),
    'Bond27':(5,(0,9)),
    'Bond28':(1,(-3,11)),
    },
  'D':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("HB2",(-3,1)),
    'Atom8':("CB",(-1,1)),
    'Atom9':("HB3",(1,1)),
    'Atom10':("CG2",(-1,3)),
    'Atom11':("OD1",(-3,5)),
    'Atom12':("OD2",(1,5)),
    'Atom13':("HD2",(2,7)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    'Bond9':(2,(-2,1)),
    'Bond10':(2,(0,1)),
    'Bond11':(1,(-1,2)),
    'Bond12':(4,(-2,4)),
    'Bond13':(3,(0,4)),
    'Bond14':(8,(1,6)),
    },
  'E':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("HB2",(-3,1)),
    'Atom8':("CB",(-1,1)),
    'Atom9':("HB3",(1,1)),
    'Atom10':("HG2",(-3,3)),
    'Atom11':("CG",(-1,3)),
    'Atom12':("HG3",(1,3)),
    'Atom13':("CD",(-1,5)),
    'Atom14':("OD1",(-3,7)),
    'Atom15':("OD2",(1,7)),
    'Atom16':("HD2",(1,9)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    'Bond9':(2,(-2,1)),
    'Bond10':(2,(0,1)),
    'Bond11':(1,(-1,2)),
    'Bond12':(2,(-2,3)),
    'Bond13':(2,(0,3)),
    'Bond14':(1,(-1,4)),
    'Bond15':(4,(-2,6)),
    'Bond16':(3,(0,6)),
    'Bond17':(1,(1,8)),
    },
  'N':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("HB2",(-3,1)),
    'Atom8':("CB",(-1,1)),
    'Atom9':("HB3",(1,1)),
    'Atom10':("CG",(-1,3)),
    'Atom11':("OD1",(-3,5)),
    'Atom12':("ND2",(1,5)),
    'Atom13':("HD21",(-1,7)),
    'Atom14':("HD22",(3,7)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    'Bond9':(2,(-2,1)),
    'Bond10':(2,(0,1)),
    'Bond11':(1,(-1,2)),
    'Bond12':(104,(-2,4)),
    'Bond13':(3,(0,4)),
    'Bond14':(4,(0,6)),
    'Bond15':(3,(2,6)),
    },
  'Q':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("HB2",(-3,1)),
    'Atom8':("CB",(-1,1)),
    'Atom9':("HB3",(1,1)),
    'Atom10':("HG2",(-3,3)),
    'Atom11':("CG",(-1,3)),
    'Atom12':("HG3",(1,3)),
    'Atom13':("CD",(-1,5)),
    'Atom14':("OE1",(-3,7)),
    'Atom15':("NE2",(1,7)),
    'Atom16':("HE21",(-1,9)),
    'Atom17':("HE22",(3,9)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    'Bond9':(2,(-2,1)),
    'Bond10':(2,(0,1)),
    'Bond11':(1,(-1,2)),
    'Bond12':(2,(-2,3)),
    'Bond13':(2,(0,3)),
    'Bond14':(1,(-1,4)),
    'Bond15':(4,(-2,6)),
    'Bond16':(3,(0,6)),
    'Bond17':(4,(0,8)),
    'Bond18':(3,(2,8)),
    },
  'H':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("HB2",(-3,1)),
    'Atom8':("CB",(-1,1)),
    'Atom9':("HB3",(1,1)),
    'Atom10':("HD1",(-5,3)),
    'Atom11':("CG",(-1,3)),
    'Atom12':("HD2",(3,3)),
    'Atom13':("ND1",(-3,4)),
    'Atom14':("CD2",(1,4)),
    'Atom15':("CE2",(-2,6)),
    'Atom16':("NE1",(0,6)),
    'Atom17':("HE2",(-4,7)),
    'Atom18':("HE1",(2,7)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    'Bond9':(2,(-2,1)),
    'Bond10':(2,(0,1)),
    'Bond11':(1,(-1,2)),
    'Bond12':(5,(-4,4)),
    'Bond13':(9,(-2,4)),
    'Bond14':(105,(0,4)),
    'Bond15':(9,(2,4)),
    'Bond16':(7,(-2,5)),
    'Bond17':(12,(0,5)),
    'Bond18':(102,(-1,6)),
    'Bond19':(9,(-3,7)),
    'Bond20':(5,(1,7)),
    },
  'K':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("HB2",(-3,1)),
    'Atom8':("CB",(-1,1)),
    'Atom9':("HB3",(1,1)),
    'Atom10':("HG2",(-3,3)),
    'Atom11':("CG",(-1,3)),
    'Atom12':("HG3",(1,3)),
    'Atom13':("HD2",(-3,5)),
    'Atom14':("CD",(-1,5)),
    'Atom15':("HD3",(1,5)),
    'Atom16':("HE2",(-3,7)),
    'Atom17':("CE",(-1,7)),
    'Atom18':("HE3",(1,7)),
    'Atom19':("HZ",(-3,9)),
    'Atom20':("NZ",(-1,9)),
    'Atom21':("HZ",(1,9)),
    'Atom22':("HZ",(-1,11)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    'Bond9':(2,(-2,1)),
    'Bond10':(2,(0,1)),
    'Bond11':(1,(-1,2)),
    'Bond12':(2,(-2,3)),
    'Bond13':(2,(0,3)),
    'Bond14':(1,(-1,4)),
    'Bond15':(2,(-2,5)),
    'Bond16':(2,(0,5)),
    'Bond17':(1,(-1,6)),
    'Bond18':(2,(-2,7)),
    'Bond19':(2,(0,7)),
    'Bond20':(1,(-1,8)),
    'Bond21':(2,(-2,9)),
    'Bond22':(2,(0,9)),
    'Bond23':(1,(-1,10)),
    },
  'R':{
    'Atom1':("H",(-4,-3)),
    'Atom2':("HA",(-1,-3)),
    'Atom3':("O",(2,-3)),
    'Atom4':("N",(-4,-1)),
    'Atom5':("CA",(-1,-1)),
    'Atom6':("C",(2,-1)),
    'Atom7':("HB2",(-3,1)),
    'Atom8':("CB",(-1,1)),
    'Atom9':("HB3",(1,1)),
    'Atom10':("HG2",(-3,3)),
    'Atom11':("CG",(-1,3)),
    'Atom12':("HG3",(1,3)),
    'Atom13':("HD2",(-3,5)),
    'Atom14':("CD",(-1,5)),
    'Atom15':("HD3",(1,5)),
    'Atom16':("HE",(-3,7)),
    'Atom17':("NE",(-1,7)),
    'Atom18':("CZ",(-1,9)),
    'Atom19':("HH11",(-5,11)),
    'Atom20':("NH1",(-3,11)),
    'Atom21':("NH2",(1,11)),
    'Atom22':("HH22",(3,11)),
    'Atom23':("HH12",(-4,13)),
    'Atom24':("HH21",(2,13)),
    'Bond1':(1,(-4,-2)),
    'Bond2':(1,(-1,-2)),
    'Bond3':(101,(2,-2)),
    'Bond4':(2,(-3,-1)),
    'Bond5':(2,(-2,-1)),
    'Bond6':(2,(0,-1)),
    'Bond7':(2,(1,-1)),
    'Bond8':(1,(-1,0)),
    'Bond9':(2,(-2,1)),
    'Bond10':(2,(0,1)),
    'Bond11':(1,(-1,2)),
    'Bond12':(2,(-2,3)),
    'Bond13':(2,(0,3)),
    'Bond14':(1,(-1,4)),
    'Bond15':(2,(-2,5)),
    'Bond16':(2,(0,5)),
    'Bond17':(1,(-1,6)),
    'Bond18':(2,(-2,7)),
    'Bond19':(1,(-1,8)),
    'Bond20':(4,(-2,10)),
    'Bond21':(3,(0,10)),
    'Bond22':(2,(-4,11)),
    'Bond23':(2,(2,11)),
    'Bond24':(12,(-4,12)),
    'Bond25':(7,(2,12)),
    },
  }
