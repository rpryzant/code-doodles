* **3 sum**
  * find triples where sum(triple) = 0 in a list (no dups, triples are uniques, list isn't sorted)
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/3sum/3sum.py
* **word search**
  * play word search with 2d matrix -- stick seeds in queue and keep working until exausted or done
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/word_search/search.py
* **palindrome permutation**
  * use bit vector to track odd/even counts for each character! smart
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/CRACKING/1.4.is_palin_perm.py
* **all lengths**
  * all lengths of diving board -- just iterate 1,...,num_options and use that as a pivot
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/CRACKING/16.11.py
* **linked list palindrome**
  * have nodes know their length, and use a stack to verify 2nd half with 1st half's elems
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/CRACKING/2.6.py
* **get next in-order successor in binary tree (with parent links)**
  * (leftmost on the right) or (first parent that you are the left child of)
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/CRACKING/4.6.py
* **multiply strings (non-negative)**
  * multiply each elem of `b` (in reverse order) with all of `a`, combining products with `10^(len(b) - i - 1)` to recover original index from b
* **simplify unix style path**
  * iterate through `re.findall( "\/(\w+|\.\.)" ` and use a stack
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/simply_path/simplify.py
* **scrambled tree (tell if two binary trees are equal except that their children as swapped)**
  * base case, make sure char distribution matches. then iterate with a pivot, and test for whether both halves are scrambled twice (once for normal sides, then again if the left & right child are swapped)
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/scramble_string/scramble.py
* **kth to last node in linked list**
  * send runner k out, then initialize lagger, then send 'em both until runner hits end
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/CRACKING/2.2.kth_to_last.py
* **partition linked list around pivot**
  * make bigger/smaller lists as you go and attach bigger to end of smaller
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/partition_list/partition.py
* **kth multiple** -- kth multiple of a list of prime factors
  * greedy search through transition space
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/CRACKING/17.9.py
* **one edit away** -- test whether strings are edit distance 1 away
  * find first disagreement, then check for substitution, insertion, deletion
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/CRACKING/1.5_v2.py
* **rank from stream** -- track rank of each number as it comes in from a stream
  * place into binary tree (have nodes track their rank), look up position in tree
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/CRACKING/10.10.py
* **kth smallest in bst**
  * get size of all subtrees, then branch left/right until #left + skipped sofar + 1 (for me) = target
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/k_th_smalest_bst/kthSmallest.py
* **rm dups in-place**  -- rm dups by shrinking array (new len)
  * sort, then move to `[i - repeats]` if not repeat, and `repeats += 1` if repeats
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/remove_duplicates/rem_dups.py
* **implement sqrt**
  * binary search
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/sqrt/sqrt.py
* **validate number**
  * regex up in this bitch
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/valid_number/valid.py
* **swap adjacent nodes in linked list**
  * pretty straightforward, but kick off iteration by tacking on additional root
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/swap_node_pairs/swapper.py
* **swap bits**
  * get even mask, then bring even bits right, then odd bits left
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/CRACKING/5.7.py
* **all subsets**
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/CRACKING/8.4.py
* **delete internal node**
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/CRACKING/2.3.py
* **is balanced bst**
  * in one function, both track height and make sure heights aren't off by more than 1
  * https://github.com/rpryzant/code-doodles/blob/master/interview_problems/CRACKING/4.4.is_balanced_bst.py
