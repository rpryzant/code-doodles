TOOD: project to auto convert latex documents to mathjax appropriate for web view



=====  CONVERSIONS I'VE NOTICED SO FAR:

\bm \bf
\intercal T
\] $$
\[ $$
\bm{x} {\bf x}
\it{x}  $x$

==== DON'T FORGET ABOUT BIBS
bibliography/references

==== PICTURES TOO
<img src="figs/mlp.jpg" alt="Mountain View" style="width:75%;">
TO
\begin{figure}[H]
  \centering
  \includegraphics[width=5in]{figures/chap3/mlp_unit}
  \caption{An MLP unit with a popular nonlinear activation function known as the sigmoid. We've labeled the value of $\bm{w}^\interca\
l \bm{x}$ as $net$.}
\end{figure}
