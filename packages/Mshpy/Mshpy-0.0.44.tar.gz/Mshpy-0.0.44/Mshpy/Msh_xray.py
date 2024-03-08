#!/bin/bash
# Written by Jaewoon Jung, on 03/07/2024.
# Some of the code used are based on the code written by Hyunju K. Connor.

#Run example:
#python Msh_xray.py name 3 path jel 30 75 105 1 180 210 1 0 0 1
#will make simulated X-ray emission measurement data observed from 30 Re away from the Earth in 'path'/xray.'name'/data
#and image in 'path'/xray.'name'/ps
#Solar wind condition should be pre-exist as 'SW_cond.txt' as in current directory. 
#Format of the file should be following:
#Year DOY HR MN Bx By Bz Vx Vy Vz n Pd Ma Mm, as in OMNIweb
#e.g. 
#1967 1 0 00 2 -2 -5 -400 0 0 10 2 10 6


import sys
import os

def run_mshpy(RUN, TI, Dout, model_bs, dsc, the1, the2, dthe, phi1, phi2, dphi, XRAYPS, MSHPY, ALL):
    the1_ = the1 - 90
    the2_ = the2 - 90

    ran = f"xray,xray:{phi1}:{phi2}:10:2:{the1_}:{the2_}:10:2"

    if MSHPY == 1:
        PYE = "./xraysc_sight_Msh.py"
        Din = "./modeling"
        Ddata = os.path.join(Dout, f"xray.{RUN}/data")

        if not os.path.exists(Dout):
            os.mkdir(Dout)

        LL = str(TI).zfill(6)
        OP1 = f"-xsc {dsc} -ysc 0 -zsc 0"
        OP2 = "-xlk 0 -ylk -1 -zlk 0"
        OP3 = f"-the1 {the1} -the2 {the2} -dthe {dthe} -phi1 {phi1} -phi2 {phi2} -dphi {dphi}"
        fout = os.path.join(Ddata, f"{RUN}.{LL}")
        cmd = f"python {PYE} -path {Din} {OP1} {OP2} {OP3} -fo {fout} -model {model_bs}"
        print(cmd)
        os.system(cmd)

    if XRAYPS == 1:
        PYE = "./plot_rates_Msh.py"
        Ddata = os.path.join(Dout, f"xray.{RUN}/data")
        Dps = os.path.join(Dout, f"xray.{RUN}/ps")

        if not os.path.exists(Dps):
            os.mkdir(Dps)

        LL = str(TI).zfill(6)
        TT2 = TI + 1
        LL2 = str(TT2).zfill(6)
        fin = f"{Ddata}/{RUN}.sc.{LL}:{Ddata}/{RUN}.sc.{LL2}"
        fbl = "none"
        fmp = "none"
        tash = 0
        cmd = f"python {PYE} {Dps} {fin} {fbl} {fmp} {ran} {tash}"
        print(cmd)
        os.system(cmd)

    if ALL == 1:
        PYE = "./xraysc_sight_Msh.py"
        Din = "./modeling"
        Ddata = os.path.join(Dout, f"xray.{RUN}/data")

        if not os.path.exists(Dout):
            os.mkdir(Dout)

        if not os.path.exists(os.path.join(Dout, f"xray.{RUN}")):
            os.mkdir(os.path.join(Dout, f"xray.{RUN}"))

        if not os.path.exists(Ddata):
            os.mkdir(Ddata)

        LL = str(TI).zfill(6)
        TT2 = TI + 1
        LL2 = str(TT2).zfill(6)

        xsc = 0
        ysc = dsc
        zsc = 0

        xlk = 0
        ylk = -1
        zlk = 0

        ysc2 = 0
        zsc2 = dsc

        ylk2 = 0
        zlk2 = -1

        OP1 = f"-xsc {xsc} -ysc {ysc} -zsc {zsc}"
        OP1_2 = f"-xsc {xsc} -ysc {ysc2} -zsc {zsc2}"

        OP2 = f"-xlk {xlk} -ylk {ylk} -zlk {zlk}"
        OP2_2 = f"-xlk {xlk} -ylk {ylk2} -zlk {zlk2}"

        the1_2 = phi1 - 90
        the2_2 = phi2 - 90
        phi1_2 = the1 + 90
        phi2_2 = the2 + 90

        OP3 = f"-the1 {the1} -the2 {the2} -dthe {dthe} -phi1 {phi1} -phi2 {phi2} -dphi {dphi}"
        OP3_2 = f"-the1 {the1_2} -the2 {the2_2} -dthe {dthe} -phi1 {phi1_2} -phi2 {phi2_2} -dphi {dphi}"

        fout = os.path.join(Ddata, f"{RUN}.sc.{LL}")
        fout_2 = os.path.join(Ddata, f"{RUN}.sc.{LL2}")

        cmd = f"python {PYE} -path {Din} {OP1} {OP2} {OP3} -fo {fout} -model {model_bs}"
        print(cmd)
        os.system(cmd)

        cmd = f"python {PYE} -path {Din} {OP1_2} {OP2_2} {OP3_2} -fo {fout_2} -model {model_bs}"
        print(cmd)
        os.system(cmd)

        PYE = "./plot_rates_Msh.py"
        Ddata = os.path.join(Dout, f"xray.{RUN}/data")
        Dps = os.path.join(Dout, f"xray.{RUN}/ps")

        if not os.path.exists(Dps):
            os.mkdir(Dps)

        fin = f"{Ddata}/{RUN}.sc.{LL}:{Ddata}/{RUN}.sc.{LL2}"
        fbl = "none"
        fmp = "none"        
        tash = 0
        cmd = f"python {PYE} {Dps} {fin} {fbl} {fmp} {ran} {tash}"
        print(cmd)
        os.system(cmd)

if __name__ == "__main__":
    RUN = sys.argv[1]
    TI = int(sys.argv[2])
    Dout = sys.argv[3]
    model_bs = sys.argv[4]
    dsc = float(sys.argv[5])
    the1 = float(sys.argv[6])
    the2 = float(sys.argv[7])
    dthe = float(sys.argv[8])
    phi1 = float(sys.argv[9])
    phi2 = float(sys.argv[10])
    dphi = float(sys.argv[11])
    MSHPY = int(sys.argv[12])
    XRAYPS = int(sys.argv[13])
    ALL = int(sys.argv[14])

    run_mshpy(RUN, TI, Dout, model_bs, dsc, the1, the2, dthe, phi1, phi2, dphi, XRAYPS, MSHPY, ALL)
