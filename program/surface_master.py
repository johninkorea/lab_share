import os
import argparse
from pymatgen.io.lammps.data import LammpsData
from pymatgen.core.structure import Structure

def tuple_type(strings):
    mapped_int = map(int, strings.split(","))
    return tuple(mapped_int)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-in', '--input_file', required=True, type=str,
                        help="write the name of input structure. (can be cif or POSCAR format)")
    
    parser.add_argument('-M', '--miller_index', required=False, default=(0,0,1), type=tuple_type,
                        help="Miller index of plane parallel to surface. Note that this is referenced to the input structure. If you need this to be based on the conventional cell, you should supply the conventional structure.")
    parser.add_argument('-S', '--slab', required=False, default=10,type=float,
                        help="min size of slab in Angstroms")
    parser.add_argument('-V', '--vacuum', required=False, default=10,type=float,
                        help="min vacuum size in Angstroms")
    parser.add_argument('-SC', '--supercell', required=False, default=(1,1,1),type=tuple_type,
                        help="make primitive cell to Supercell")
    parser.add_argument('-R', '--result', required=False, default="l",type=str,
                        help='result format ("p" for POSCAR or "l" for Lammps)')
    parser.add_argument('-B', '--bottom', required=False, default=1, type=int,
                        help="Ture or False move stucture to bottom.")
    # parser.add_argument('-', '--', required=False, 
    #                     help="")

    args = parser.parse_args()

# read file
print("[read structure start]\n ...")
ma=Structure.from_file(args.input_file)
print("[read structure done]\n"+"="*60+"\n")

# Generator Slab
print("[Generator Slab start]")
from asd import slab
slabs, qwe=slab.slabgen(ma, args.miller_index, args.slab, args.vacuum)
print("[Generator Slab done]\n"+"="*60+"\n")

# move to bottom
print("[position move start]")
from asd.move import mv2bottom
## get slabs data
data=[]
z=0
while z<len(qwe):
    print(z)
    old=slabs[qwe[z]]
    old.to(filename=f"POSCAR", fmt="POSCAR")
    ma=Structure.from_file("POSCAR")
    os.system("rm POSCAR")
    if args.bottom==1:
        ma=mv2bottom(ma)
    else: print("do not thing")
    data.append(ma)
    z+=1
print("[position move done]\n"+"="*60+"\n")

# primitive cell to Supercell
print("[Supercell start]")
if args.supercell==(1,1,1): print(" do not thing")
else:
    z=0
    while z<len(data):
        data[z].make_supercell(args.supercell)
        z+=1
print("[Supercell done]\n"+"="*60+"\n")

# export data to file
print("[export start]")
if args.result=="p":
    z=0
    while z<len(data):
        print(f"export {qwe[z]}")
        data[z].to(filename=f"POSCAR_{qwe[z]}", fmt="POSCAR")
        z+=1
elif args.result=="l":
    z=0
    while z<len(data):
        print(f"export {qwe[z]}")
        LammpsData.from_structure(data[z]).write_file(f"position_{qwe[z]}")
        z+=1
else:
    print("l or p only")
print("[export done]\n"+"="*60+"\n")