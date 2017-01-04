#Replace this with the test you want to run
WAVE=wave4
PLA=pla2
TEST=phase2

all:
	waa tests/$(TEST).as
	wia $(WAVE).is
	pa $(PLA).p $(PLA).po
	wii -gs -p $(PLA).po -x $(TEST).o $(WAVE).o
	cat $(WAVE).out