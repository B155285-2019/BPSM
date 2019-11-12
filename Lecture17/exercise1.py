#!/usr/bin/python3

import pandas as pd

df = pd.read_csv('/localdisk/data/BPSM/Lecture17_AI/eukaryotes.txt', sep="\t")
fungal = df[df['Group'] == 'Fungi']

fungal_100mb = df[(df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100)]
len(fungal_100mb)

group-counts = df['Group'].value_counts()

had_Heli = df.apply(lambda x: x["#Organism/Name"],axis = 1).str.contains("Heliconius")
had_Heli.value_counts()

plants = df[df['Group'] == 'Plants']
plants['Center'].value_counts()


