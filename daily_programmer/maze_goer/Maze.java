import java.lang.*;
import java.util.*;
import java.nio.file.*;
import java.nio.charset.*;
import java.io.*;

public class Maze {

    private char[][] map; 
    private Coord exit;
    private Coord loc;
    private int m;
    private int n;

    public Maze(String rawMaze) {
	this.map = convertToMatrix(rawMaze);
	this.m = this.map.length;
	this.n = this.map[0].length;
	this.exit = findExit();
	this.loc = initLocation();
    }

    public Boolean hasWon() {
	return exit.equals(loc);
    }

    public Boolean makeMove(char move) {
	switch(move) {
            case 'w':
		if (!(map[loc.r-1][loc.c] == '#')) {
		    loc.r--;
		    return true;
		}
		else {
		    return false;
		}
	    case 's':
		if (!(map[loc.r+1][loc.c] == '#')) {
		    loc.r++;
		    return true;
		}
		else {
		    return false;
		}
    	    case 'a':
		if (!(map[loc.r][loc.c-1] == '#')) {
		    loc.c--;
		    return true;
		}
		else {
		    return false;
		}
	    case 'd':
		if (!(map[loc.r][loc.c+1] == '#')) {
		    loc.c++;
		    return true;
		}
		else {
		    return false;
		}
	}
	return false;
    }

    private class Coord {
	public int r;
	public int c;
	public Coord(int r, int c) {
	    this.r = r;
	    this.c = c;
	}
	public Boolean equals(Coord other) {
	    return (r == other.r && c == other.c);
	}
    }



    private Coord initLocation() {
	int lR, lC;
	Random r = new Random();
	while (true) {
	    lR = r.nextInt(m);
	    lC = r.nextInt(n);
	    if (map[lR][lC] == ' ') {
		return new Coord(lR, lC);
	    }
	}
    }

    private Coord findExit() {
	for (int i = 0; i < map.length; i++) {
	    for (int j = 0; j < map[0].length; j++) {
		if (map[i][j] == 'X') {
		    return new Coord(i, j);
		}
	    }
	}
	return null;
    }

    /* converts an m x n maze string into an m x n matrix of characters
     *
     */
    private char[][] convertToMatrix(String rawMaze) {
	String[] rows = rawMaze.split("\n");
	char[][] m = new char[rows.length][rows[0].length()];	
	for (int i = 0; i < rows.length; i++) {
	    for (int j = 0; j < rows[0].length(); j++) {
		m[i][j] = rows[i].charAt(j);
	    }
	}
	return m;
    }

    private static String readFile(String path) throws IOException {
	byte[] encoded = Files.readAllBytes(Paths.get(path));
	return new String(encoded, StandardCharsets.UTF_8);
    }


    public String toString() {
	StringBuilder s = new StringBuilder();
	for (int i = 0; i < map.length; i++) {
	    for (int j = 0; j < map[0].length; j++) {
		if (i == loc.r && j == loc.c) 
		    s.append('O');
		else
		    s.append(map[i][j]);
	    }
	    s.append('\n');
	}
	return s.toString();
    }


    public static void main(String[] args) {
	String rawMaze;
	try {
	    rawMaze  = readFile(args[0]);
	} catch (IOException e) {
	    throw new RuntimeException(e);
	}
	Maze m = new Maze(rawMaze);
	System.out.println(m);
	Scanner scan = new Scanner(System.in);
	char input;
	while (!m.hasWon()) {
	    System.out.println("Make a move: ");
	    input = scan.next().charAt(0);
	    m.makeMove(input);
	    System.out.println(m);
	}
	System.out.println("You won!");
    }

}