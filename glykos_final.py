# -*- coding: utf-8 -*-
"""Glykos Final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QPfnk0rNQmQyRvXpl-B6qUpQgwMc2Byd
"""

class read_seq:
  def is_sequence(self, seq):
    size = len(seq)
    codon_in = "ATG"
    codon_out1 = "TAA"
    codon_out2 = "TAG"
    codon_out3 = "TGA"
    count = 0
    s_codon = False
    for i in range(size - 2):
      c_codon = seq[i:i+3]
      if c_codon == codon_in:
        start = i
        s_codon = True
      if c_codon in [codon_out1, codon_out2, codon_out3]:
        end = i + 2
        count += 1
    if count == 1 and s_codon == True:
        print("This is a typical prokaryotic transcription sequence.")
        #print(seq[start:end+1])
    elif count!= 0 and s_codon == False:
        print("This is not a typical prokaryotic transcription sequence, there is no entry codon.")
    elif count > 1 and s_codon == False:
        print("This is not a typical prokaryotic transcription sequence, there is no entry codon and:", count, "end codons in total.")
    elif count > 1:
        print("The sequence is not  typical, there are", count, "end codons in total.")
    elif count == 0 and s_codon == False:
        print("This is not a typical prokaryotic transcription sequence, there is no entry or end codon.")


  def is_sequence_rev(self, seq):
    size = len(seq)
    codon_in = "TAC"
    codon_out1 = "ATT"
    codon_out2 = "ATC"
    codon_out3 = "ACT"
    count = 0
    s_codon = False
    for i in range(size - 2):
        c_codon = seq[i:i+3]
        if c_codon == codon_in:
          start = i
          s_codon = True
        if c_codon in [codon_out1, codon_out2, codon_out3]:
          end = i + 2
          count += 1
    if count == 1 and s_codon == True:
          print("This is a typical prokaryotic transcription sequence.")
        #print(seq[start:end+1])
    elif count!= 0 and s_codon == False:
          print("This is not a typical prokaryotic transcription sequence, there is no entry codon.")
    elif count > 1 and s_codon == False:
          print("This is not a typical prokaryotic transcription sequence, there is no entry codon and:", count, "end codons in total.")
    elif count > 1:
          print("The sequence is not  typical, there are", count, "end codons in total.")
    elif count == 0 and s_codon == False:
          print("This is not a typical prokaryotic transcription sequence, there is no entry or end codon.")

direction = ""
test = read_seq()
while direction not in ("A", "B", "a", "b"):
  direction = input("Please enter 'A' if it is a 5' 3' sequence, or 'B' if it is a 3' 5'.")
  if direction == "A" or direction == "a":
    seq = input("Please enter a sequence: ")
    test.is_sequence(seq)
  elif direction == "B" or direction == "b":
    seq = input("Please enter a sequence: ")
    test.is_sequence_rev(seq)