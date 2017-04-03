#!/usr/bin/bash


data_dir='../data/squad'
mode=train
batch_size=60
load=False
num_steps=20000
sent_size_th=400
para_size_th=256
dump_eval=True
dump_answer=False
dump_pickle=False
use_char_emb=True
device_type=gpu

python3 -m basic.cli \
	--data_dir $data_dir \
	--mode $mode \
	--load $load \
	--batch_size $batch_size \
	--num_steps $num_steps \
	--sent_size_th $sent_size_th \
	--para_size_th $para_size_th \
	--dump_eval $dump_eval \
	--dump_answer $dump_answer \
	--dump_pickle $dump_pickle \
	--use_char_emb $use_char_emb \
	--device_type $device_type
	#--debug
	#--cluster \
	#--noload \


# Training
#
# python3 -m basic.cli --mode train --device_type cpu --cluster --noload
#
# python3 -m basic.cli --mode train --noload --debug

# 
# python3 -m squad.prepro --mode full --glove_vec_size 300


# Testing
#
# python3 -m basic.cli --device_type cpu --data_dir '../data/squad'
#
# python3 -m basic.cli --device_type cpu --len_opt --cluster


#
# grep -rnH --include='*.py' "load_step"


#
# TensorBoard
#
# python3 -m tensorflow.tensorboard --logdir=/home/kuohsin/Downloads/ADL2016/Final/bi-att-flow/out/basic/00/log
#
# /home/kuohsin/Downloads/ADL2016/Final/out_128_256_0108_2/basic/00/log 
# /home/kuohsin/Downloads/ADL2016/Final/out_0104_14000/basic/00/log
#
# /home/kuohsin/Downloads/ADL2016/Final/bi-att-flow/out/basic/00/log

