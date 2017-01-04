### Introduction

This is an ARM emulator written for the annual WAVE emulation competition at Williams College. 

All instructions in an ARM-based assembly were decoded and emulated in an x86-based language. 

The space-time tradeoff was taken into account during both both the design and implementation of this emulator. Additionally, this was a team project, and involved collaborating with both a partner and the professor.

My group's emulator broke the all-time speed/time record. It was also the only emulator to pass every test.

### Project files

* [makefile](https://github.com/rpryzant/code-doodles/blob/master/wave/makefile) - builds the emulator.
* [run_all.py](https://github.com/rpryzant/code-doodles/blob/master/wave/run_all.py) - benchmarks the emulator.
* [wave4.is](https://github.com/rpryzant/code-doodles/blob/master/wave/wave4.is) - my group's submission. 
* [wave4.out](https://github.com/rpryzant/code-doodles/blob/master/wave/wave4.out) - sample output.
* [wave4.stats](https://github.com/rpryzant/code-doodles/blob/master/wave/wave4.stats) - sample benchmark output.
* [test/](https://github.com/rpryzant/code-doodles/tree/master/wave/tests) - emulator benchmarks. These are C programs that have been compiled into ARM. They include tasks like solving mazes with DFS.

### Performance

![performance](https://raw.githubusercontent.com/rpryzant/code-doodles/master/wave/performance.png)

The above plot shows some historical performance for this contest. The y-axis shows emulator speed, and the x-axis shows emulator footprint (space). My group's emulator is circled in red. 
