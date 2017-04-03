#!/usr/bin/bash

data_dir='../data/squad'
sent_size_th=400
para_size_th=256
dump_answer=True
use_char_emb=True
device_type=gpu

python3 -m basic.cli \
	--data_dir $data_dir \
	--sent_size_th $sent_size_th \
	--para_size_th $para_size_th \
	--dump_answer $dump_answer \
	--use_char_emb $use_char_emb \
	--device_type $device_type
