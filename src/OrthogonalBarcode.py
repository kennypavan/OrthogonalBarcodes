import random
import math
from Bio.SeqUtils import GC
from Bio.Restriction import *

class OrthogonalBarcode:

	def __init__(self):
		self.amount = 2 #amount of barcodes to generate
		self.length = 20 #default barcode length
		self.gc = 50 #gc percentage
		self.ooi = None #organism of interest
		self.ooi_homology_threshold = 50 #max homology to the ooi
		self.hamming_distance = 0 #distance of each barcode
		self.self_dimer = 10 #self-dimerization free energy
		self.avoid_motifs = ["AAAA","TTTT","CGCGCGCG","ATATATAT"]
		self.avoid_start = ["ATATAT"] #avoid starting
		self.avoid_end = ["ATATAT"] #avoid ending
		self.avoid_rs = [] #restriction sites to avoid. (EcoRI,BamHI,NheI,etc...)
		self.barcodes = []

	def generate_random_sequence(self):
		"""Generate a random sequence of defined length"""
		gc_sequence = ''.join(random.choices(['G','C'], k=math.ceil(self.length*(self.gc/100))))
		at_sequence = ''.join(random.choices(['A','T'], k=math.floor(self.length*(1-(self.gc/100)))))
		return self.join_and_shuffle(gc_sequence+at_sequence)

	def join_and_shuffle(self,sequence):
		"""Join and randomly suffle two balanced AT and GC strings"""
		return ''.join(random.sample(sequence,len(sequence)))

	def calculate_gc_content(self,sequence):
		return GC(sequence)

	def generate_sequences(self):
		while len(self.barcodes) < self.amount:
			sequence = self.generate_random_sequence()
			if(self.motif_check(sequence) == True):
				pass
			elif(self.restriction_site_check(sequence) == True):
				pass
			elif(self.start_check(sequence) == True):
				pass
			elif(self.end_check(sequence) == True):
				pass
			elif(self.hamming_distance_check(sequence) == True):
				pass
			else:
				self.barcodes.append(sequence)

	def motif_check(self,sequence):
		res = [ele for ele in self.avoid_motifs if(ele in sequence)]
		return bool(res)

	def restriction_site_check(self,sequence):
		res = [ele for ele in self.avoid_rs if(ele.site in sequence)]
		return bool(res)

	def start_check(self, sequence):
		res = [ele for ele in self.avoid_start if(ele == sequence[0:len(ele)])]
		return bool(res)

	def end_check(self, sequence):
		res = [ele for ele in self.avoid_end if(ele == sequence[-len(ele)])]
		return bool(res)

	def hamming_distance_compare(self,sequence_a,sequence_b):
		i = 0
		count = 0
		while(i < len(sequence_a)):
			if(sequence_a[i] != sequence_b[i]):
				count += 1
			i += 1
		return count

	def hamming_distance_check(self,sequence):
		for barcode in self.barcodes:
			if(self.hamming_distance_compare(sequence,barcode) < self.hamming_distance):
				return True
		return False


# Testing
barcodes = OrthogonalBarcode()
barcodes.length=50
barcodes.gc=60
barcodes.amount=5
barcodes.hamming_distance=5
barcodes.avoid_rs=[EcoRI,BamHI,NheI,XhoI,KasI]
barcodes.generate_sequences()
print(barcodes.barcodes)
