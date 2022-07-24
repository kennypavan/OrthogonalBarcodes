import random
import math
from Bio.SeqUtils import GC

class OrthogonalBarcode:

	def __init__(self):
		self.amount = 2
		self.length = 20
		self.gc = 50
		self.ooi = None #organism of interest
		self.ooi_homology_threshold = 50
		self.hamming_distance = 0 
		self.self_dimer = 10 #self-dimerization free energy
		self.avoid_motifs = ["AAAA","TTTT","CGCGCGCG","ATATATAT"]
		self.avoid_start = ["ATATAT"] #avoid starting
		self.avoid_end = ["ATATAT"] #avoid ending
		self.avoid_rs = [] #restriction sites to avoid
		self.barcodes = []

	def generate_random_sequence(self):
		"""Generate a random sequence of defined length"""
		gc_sequence = ''.join(random.choices(['G','C'], k=math.ceil(self.length*(self.gc/100))))
		at_sequence = ''.join(random.choices(['A','T'], k=math.floor(self.length*(1-(self.gc/100)))))
		sequence = self.join_and_shuffle(gc_sequence+at_sequence)
		if(self.motif_check(sequence) == True):
			return self.generate_random_sequence()
		else:
			return sequence

	def join_and_shuffle(self,sequence):
		"""Join and randomly suffle two balanced AT and GC strings"""
		return ''.join(random.sample(sequence,len(sequence)))

	def calculate_gc_content(self,sequence):
		return GC(sequence)

	def generate_sequences(self):
		for i in range(self.amount):
			self.barcodes.append(self.generate_random_sequence())

	def motif_check(self,sequence):
		res = [ele for ele in self.avoid_motifs if(ele in sequence)]
		return bool(res)



# Testing
barcodes = OrthogonalBarcode()
barcodes.length=30
barcodes.gc=60
barcodes.amount=50
barcodes.generate_sequences()
print(barcodes.barcodes)
