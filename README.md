# Orthogonal Barcodes 

A simple Python class for generating custom orthogonal DNA/RNA barcodes.


## Features

- Generate a configurable amount of barcodes.
- Define length of barcodes.
- GC percent filter.
- Hamming distance filter.
- Avoid common and custom restriction sites.
- Custom motifs avoidance from barcodes.
- Start and end sequence avoidance.
- Avoid barcode homology to organism of interest.


## Installation 

```
pip install OrthogonalBarcodes
```


## Quickstart

```python
from OrthogonalBarcodes import OrthogonalBarcode

barcodes = OrthogonalBarcode.OrthogonalBarcode()
barcodes.length=25
barcodes.gc=50
barcodes.amount=10
barcodes.hamming_distance=4
barcodes.generate_barcodes()
print(barcodes.barcodes)

>
>

# Prints the list of barcodes below
['TTAGACGTGCAGTCGTCTTGACCCT', 'CCGTGTGGTCTCCCTCATGGTTAAA', 'GAGCCGGGTGAAACTCAAACTCAAC', 'AGTGGGGACTGTGCTAAGGCAAGAT', 'TGCAGCACCTTTGGTCACCTTTCTC', 'CAGCCGGTCTCCGATTATCTATCTC', 'TATGGGGAAGCTGTCGTGATTGGCT', 'GGCGCCACCAGAATCACTTTAAGTG', 'TACGGTCGATATGGATCCTTCCGTG', 'TGAGTCTCAGGTACGCAAGTTGCCT']

```



## Full Usage

```python
from OrthogonalBarcodes import OrthogonalBarcode

# Instantiate the class and set required/optional properties below.
barcodes = OrthogonalBarcode.OrthogonalBarcode()

# Required — The length of each barcode (Default:20)
barcodes.length=25

# Required — The GC percentage for each barcode generated (Default:50)
barcodes.gc=50

# Required — The amount of barcodes to generate (Default:1)
barcodes.amount=10

# Optional — Hamming distance between all barcodes. (Default:0)
barcodes.hamming_distance=4

# Optional — Fasta file path for organism of interest. (Default:none)
barcodes.ooi_file='tests/test_ooi.fasta'

# Optional — Maximum barcode homology to any part of the oranism of interest file Default:50)
barcodes.ooi_homology_threshold = 40

# Optional — List of restriction sites to avoid when generating barcodes. (Default:none; Accepts Bio.Restriction properties)
barcodes.avoid_rs=[EcoRI,BamHI,NheI,XhoI,KasI] 

# Optional — List of any motifs to filter from barcodes (Default: "AAAA","TTTT","CGCGCGCG","ATATATAT")
barcodes.avoid_motifs=["AAATTTT","TTTTTT","GGGGGGGG"] 

# Optional — List of starting sequences to avoid (Default: "ATATAT")
barcodes.avoid_start=["AAATTTT","TTTTTT","GGGGGGGG"] 

# Optional — List of ending sequences to avoid (Default: "ATATAT")
barcodes.avoid_end=["AAATTTT","TTTTTT","GGGGGGGG"] 

# Generate the barcodes
barcodes.generate_barcodes()

# Print a list of generated barcodes.
print(barcodes.barcodes)

>
>

# Prints the list of barcodes below
['AATCGATCGTGGCATCGTCCCTATC', 'GAAATCGAGACTCCGACCGATGTCT', 'GGTAACTAGTCCTAGATCAGCGAGG', 'AACAGTTCCTGGTGGTGTCTAGGCT', 'TGTTGCGTCCGTACTGTGGCGTAAA', 'CCGATTGATCTGACGTCGTGTCAAG', 'CTAGGACCATTGACTCGGCAACAAG', 'AATACTCACGATGCGATTTCCGCGG', 'TCGGTCTGTAGAGAGAGATACGTGC', 'AGGGTCGTCAGAAACTGAACCTGCT']

```


## Notes
This class uses a brute force method to generate barcodes. The amount of time to generate barcodes increases greatly with the amount of barcodes being generated. Additionally, when filtering against an organism of interest or increasing the hamming distance between barcodes, the class will increase its complexity and barcode generation time will increase. 



