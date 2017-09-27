


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


# example config.json for tensorflow.nmt
{
  "attention": "bahdanau",
  "attention_architecture": "standard",
  "batch_size": 128,
  "bpe_delimiter": "@@",
  "colocate_gradients_with_ops": true,
  "decay_factor": 0.5,
  "decay_steps": 9999999999999999,
  "dropout": 0.2,
  "encoder_type": "bi",
  "eos": "</s>",
  "forget_bias": 1.0,
  "infer_batch_size": 32,
  "init_weight": 0.1,
  "learning_rate": 0.0001,
  "max_gradient_norm": 5.0,
  "metrics": ["bleu"],
  "num_buckets": 5,
  "num_layers": 4,
  "num_train_steps": 200000,
  "num_units": 512,
  "optimizer": "adam",
  "residual": false,
  "share_vocab": true,
  "sos": "<s>",
  "source_reverse": true,
  "src_max_len": 50,
  "src_max_len_infer": null,
  "start_decay_step": 99999999999999,
  "steps_per_external_eval": null,
  "steps_per_stats": 100,
  "tgt_max_len": 50,
  "tgt_max_len_infer": null,
  "time_major": true,
  "unit_type": "lstm",
  "beam_width": 10
}





