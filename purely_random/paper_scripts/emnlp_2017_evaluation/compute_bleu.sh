export TOOLS=tools
export MOSES=${TOOLS}/mosesdecoder/scripts

export PREDS=$1
export LABELS=$2


perl ${MOSES}/generic/multi-bleu.perl $LABELS < $PREDS

