export PATH=$PATH:/usr/local/bin/kytea
export TOOLS=tools/
export SCRIPTS=${TOOLS}script.segmentation.distribution
export MOSES=${TOOLS}/mosesdecoder/scripts
export KYTEA_MODEL=${TOOLS}/jp-0.4.7-1.mod

export TARGET=$1

echo $TARGET

cat $TARGET \
  | perl -Mencoding=utf8 -pe 's/(.)［[０-９．]+］$/${1}/;' \
  | perl ${SCRIPTS}/h2z-utf8-without-space.pl \
  | kytea -debug 0 -model $KYTEA_MODEL -out tok \
  | perl -pe 's/^ +//; s/ +$//; s/ +/ /g;' \
  | perl -Mencoding=utf8 -pe 'while(s/([０-９]) ([０-９])/$1$2/g){} s/([０-９]) (．) ([０-９])/$1$2$3/g; while(s/([Ａ-Ｚ]) ([Ａ-Ｚａ-ｚ])/$1$2/g){} while(s/([ａ-ｚ]) ([ａ-ｚ])/$1$2/g){}' \
  > $TARGET.tok




