#Import modules used
import pandas as pd
import numpy as np
import math
import os
import pdb

Compostions =['BSE','Komatiite','Basalt','Mercury'] #Define the compostion names
Temperatures =['1500','1995','2505','3000'] #Define the temperature ranges
#temperatures = (0,33,67,100)
temperatures = {'1500': 0, '1995':33 , '2505': 67, '3000':100} #Set up a dictionary where we match the temperature name to the temperature index value
fo2 = ['-2','-1','0','1','2'] #Define the fo2 values used
file_prefix='Vaporock' #Define file name
file_extension = ".dat" #Define file extension
elements =['O', 'Mg', 'Ca' ,'Al' ,'Si','Na','K','Fe' ,'Ti' ,'Cr'] #Define the elements

#create data files
#Import in the BSE molar fraction excel files and store them as panda dataframes
BSE_mol=r'./BSE' 
BSE_mols= os.listdir(BSE_mol)
BSE_mol_files = [file for file in BSE_mols if file.endswith('.xlsx')]
from tkinter import Tcl
BSE_mol_files = Tcl().call('lsort', '-dict', BSE_mol_files)
print(BSE_mol_files)
mol_bse = []
for file in BSE_mol_files:
    BSE_mols = os.path.join(BSE_mol,file)
    df = pd.read_excel(BSE_mols)
    mol_bse.append(df)

#Import in the Komatiite molar fraction excel files and store them as panda dataframes
KOMA_mol=r'./Komatiite'
KOMA_mols= os.listdir(KOMA_mol)
KOMA_mol_files = [file for file in KOMA_mols if file.endswith('.xlsx')]
from tkinter import Tcl
KOMA_mol_files = Tcl().call('lsort', '-dict', KOMA_mol_files)
print(KOMA_mol_files)
mol_koma = []
for file in KOMA_mol_files:
    KOMA_mols = os.path.join(KOMA_mol,file)
    df = pd.read_excel(KOMA_mols)
    mol_koma.append(df)

#Import in the Basalt molar fraction excel files and store them as panda dataframes
BASA_mol=r'./Basalt'
BASA_mols= os.listdir(BASA_mol)
BASA_mol_files = [file for file in BASA_mols if file.endswith('.xlsx')]
from tkinter import Tcl
BASA_mol_files = Tcl().call('lsort', '-dict', BASA_mol_files)
print(BASA_mol_files)
mol_basa = []
for file in BASA_mol_files:
    BASA_mols = os.path.join(BASA_mol,file)
    df = pd.read_excel(BASA_mols)
    mol_basa.append(df)

#Import in the Mercury molar fraction excel files and store them as panda dataframes
Merc_mol=r'./Mercury'
Merc_mols= os.listdir(Merc_mol)
Merc_mol_files = [file for file in Merc_mols if file.endswith('.xlsx')]
from tkinter import Tcl
Merc_mol_files = Tcl().call('lsort', '-dict', Merc_mol_files)
print(Merc_mol_files)
mol_merc = []
for file in KOMA_mol_files:
    Merc_mols = os.path.join(Merc_mol,file)
    df = pd.read_excel(Merc_mols)
    mol_merc.append(df)
Ele = np.zeros((10,4,4,5))
print(mol_merc)


compostions = [mol_bse,mol_koma,mol_basa,mol_merc] #Define the compostion dataframe list
output_directory = "Vaporock datafiles"
 # Construct the file name
for i in range(len(Compostions)):
    for k in range(len(fo2)):
        for l in range(len(Temperatures)):
            j=temperatures[Temperatures[l]]
            file_name = "Vaporock_" + Compostions[i] + "_"+  Temperatures[l] + "_fo2_" + fo2[k] + ".dat"
            
            # Combine the directory path with the file name
            file_path = os.path.join(output_directory, file_name)
            
            Ele=pd.Series.tolist(compostions[i][k].iloc[:,j])
            content=np.log10(Ele)+12 #Change the elemental fractions using the equation given in the FastChem documentation
            #pdb.set_trace()
            print(i,l,k,content)
            if i==2 and l==0 and k==4:
                pdb.set_trace()
            f=open(file_path,'w') #Open file
            f.seek(0)
            f.write(file_name +'\n') #Write the filename on the top line
            f.write('e-  0.00 \n')
            f.close()
            spec_string="-inf"
            #Write each elements abudence
            for m in range(len(content)):
                with open(file_path, "a") as file:
                    file.seek(2)
                    if content[m] != float('-inf') and not math.isinf(content[m]):
                        #pdb.set_trace()
                        file.write(str(elements[m]) + ' ' +  str(content[m]) +'\n')
            
            print(f"Created {file_path}")

