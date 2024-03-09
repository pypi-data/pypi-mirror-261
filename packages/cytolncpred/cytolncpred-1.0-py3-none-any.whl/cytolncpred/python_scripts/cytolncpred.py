from Bio import SeqIO
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import argparse
import numpy as np
import os
import zipfile  
import urllib.request
import warnings

warnings.filterwarnings('ignore')

nf_path = os.path.dirname(os.path.realpath(__file__))

import urllib.request

def download_and_extract(url, target_folder):
    # Check if the target folder exists
    if not os.path.exists(os.path.join(target_folder, "dnabert2_10k")):

        # Download the zip file from the URL
        zip_filename = os.path.join(target_folder, "dnabert2_10k.zip")
        urllib.request.urlretrieve(url, zip_filename)

        # Extract the contents of the zip file
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(target_folder)

        # Remove the zip file after extraction
        os.remove(zip_filename)
        print(f"Folder downloaded and extracted to: {target_folder}")
    else:
        print(f"Folder already exists: {target_folder}")

external_url = "https://webs.iiitd.edu.in/raghava/cytolncpred/downloads/dnabert2_10k.zip"
target_directory = nf_path + "/.."

download_and_extract(external_url, target_directory)


def main():
	print('####################################################################################')
	print('# This program CytoLNCpred is developed for predicting the probability of lncRNA   #')
	print('# localizing to the Cytoplasm, developed by Prof G. P. S. Raghava group.      #')
	print('# Please cite: CytoLNCpred; available at https://webs.iiitd.edu.in/raghava/cytolncpred/ #')
	print('####################################################################################')

	parser = argparse.ArgumentParser(description='Provide the following inputs for a successful run')
	parser.add_argument("-i", "--input", type=str, required=True, help="Input: nucleotide sequence in FASTA format")
	parser.add_argument("-o", "--output",type=str, default="outfile.csv", help="Output: File for saving results; by default outfile.csv")
	parser.add_argument("-t","--threshold", type=float, default=0.5, help="Threshold: Value between 0 to 1; by default 0.5")
	parser.add_argument("-w", "--workdir",type=str, default="./", help="Working directory: Directory where all intermediate and final files will be created; by default .")
	parser.add_argument("-d","--display", type=int, choices = [1,2,3], default=3, help="Display: 1:Cytoplasm-localized, 2: Nucleus-localized, 3: All; by default 3")
	args = parser.parse_args()

	fasta_input = args.input
	output_file = args.output
	model_path = nf_path+"/../dnabert2_10k"
	thr = args.threshold
	wd = args.workdir
	disp = args.display

	sequences = [str(sequence_record.seq) for sequence_record in SeqIO.parse(fasta_input, "fasta")]
	headers = [str(sequence_record.id) for sequence_record in SeqIO.parse(fasta_input, "fasta")]

	tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
	model = AutoModelForSequenceClassification.from_pretrained(model_path, trust_remote_code=True)
	device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

	prob_list = []
	for sequence in sequences:
		inputs = tokenizer(sequence, return_tensors="pt")
		outputs = model(**inputs)
		logits = outputs.logits
		probabilities = torch.nn.functional.softmax(logits, dim=-1)
		prob_list.append(probabilities.detach().numpy().flatten()[1])

	prob_dict={'ID':headers, 'LLM Score':prob_list}

	df1 = pd.DataFrame(data=prob_dict)
	df1['Prediction'] = np.where(df1['LLM Score'] >= thr, 'Cytoplasm', 'Nucleus')

	if disp==1:
		df2 = df1.loc[df1['Prediction']=='Cytoplasm',:]
	elif disp==2:
		df2 = df1.loc[df1['Prediction']=='Nucleus',:]
	else:
		df2=df1

	df2.to_csv(wd+output_file, header=True, index=False)
 
if __name__ == '__main__':
    main()

