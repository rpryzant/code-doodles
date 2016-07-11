import java.lang.Integer;

public class GameOfThree {

    public static void main(String[] args) {
	int current = Integer.parseInt(args[0]);
	int modifier = 0;
	while (current != 1) {
	    if (current % 3 == 0) {
		System.out.println(current + " 0");
	    } else if ((current + 1) % 3 == 0) {
		System.out.println(current + " 1");
		current = current + 1;
	    } else if ((current - 1) % 3 == 0) {
		System.out.println(current + " -1");
		current = current - 1;
	    }
	    current /= 3;
	}
	System.out.println(current);
    }
}