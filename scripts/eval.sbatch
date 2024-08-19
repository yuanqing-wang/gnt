#!/bin/bash
#SBATCH --time=0:59:00
#SBATCH --mem=32GB
#SBATCH --job-name=tune
#SBATCH --output=%A.out
#SBATCH --gres=gpu:1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
# #SBATCH --partition nvidia

export TRANSFORMERS_CACHE=/scratch/yw8052/hf/

python eval.py
