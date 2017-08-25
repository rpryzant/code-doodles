


# run inference with tensorflow.nmt
python -m nmt.nmt \
    --src=ja --tgt=en \
    --ckpt=4_1/output/best_bleu/translate.ckpt-90000 \
    --hparams_path=params.json \
    --out_dir=INFERENCE_OUTPUT \
    --vocab_prefix=4_1/vocab \
    --inference_input_file=4_1/test.ja \
    --inference_output_file=INFERENCE_OUTPUT/trans \
    --inference_ref_file=4_1/test.en


# run training with tensorflow.nmt
python -m nmt.nmt \
    --src=ja --tgt=en \
    --hparams_path=params.json \
    --out_dir=jesc/output/ \
    --vocab_prefix=jesc/vocab \
    --train_prefix=jesc/train \
    --dev_prefix=jesc/val \
    --test_prefix=jesc/test






