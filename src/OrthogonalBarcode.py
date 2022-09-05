import random
import math
import os
from Bio import SeqIO
from Bio.SeqUtils import GC
from Bio.Restriction import *
from Bio import pairwise2

from Bio.Seq import Seq 

class OrthogonalBarcode:

	def __init__(self):
		self.amount = 1 #amount of barcodes to generate
		self.length = 20 #default barcode length
		self.gc = 50 #gc percentage
		self.ooi_file = None #organism of interest
		self.ooi_homology_threshold = 50 #default maximum barcode homology to any part of the ooi
		self.hamming_distance = 0 #distance between each barcode
		self.avoid_motifs = ["AAAA","TTTT","CGCGCGCG","ATATATAT"]
		self.avoid_start = ["ATATAT"] #avoid starting
		self.avoid_end = ["ATATAT"] #avoid ending
		self.avoid_rs = [] #restriction sites to avoid. (EcoRI,BamHI,NheI,etc...)
		self.barcodes = []

	def generate_random_sequence(self):
		gc_sequence = ''.join(random.choices(['G','C'], k=math.ceil(self.length*(self.gc/100))))
		at_sequence = ''.join(random.choices(['A','T'], k=math.floor(self.length*(1-(self.gc/100)))))
		return self.join_and_shuffle(gc_sequence+at_sequence)

	def join_and_shuffle(self,sequence):
		return ''.join(random.sample(sequence,len(sequence)))

	def calculate_gc_content(self,sequence):
		return GC(sequence)

	def generate_barcodes(self):
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
			elif(self.ooi_file != None and self.filter_ooi_fasta_sequences(sequence) == True):
				pass	
			else:
				self.barcodes.append(sequence)
				print (len(self.barcodes)," of ",self.amount,' created...')

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

	def filter_ooi_fasta_sequences(self,barcode):
		for record in SeqIO.parse(os.path.abspath(self.ooi_file), "fasta"):
			for alignment in pairwise2.align.localms(Seq(barcode),record.seq, 1, -7, -7, -7):
				if ( ((alignment.score/self.length)*100) >= self.ooi_homology_threshold ):
					return True



# Basic Usage
# barcodes = OrthogonalBarcode()
# barcodes.length=25
# barcodes.gc=50
# barcodes.amount=10
# barcodes.hamming_distance=4
# barcodes.ooi_file='tests/test_ooi.fasta'
# barcodes.ooi_homology_threshold = 40
# barcodes.avoid_rs=[EcoRI,BamHI,NheI,XhoI,KasI]
# barcodes.generate_barcodes()
# print(barcodes.barcodes)
