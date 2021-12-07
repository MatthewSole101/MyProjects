import javax.swing.*;

public class Tile extends JButton
{
    private char mySymbol;
    private String setText;
    private boolean isAvailable = false;
    private int y;
    private int x;

    public void setSymbol(char s)
    {
        mySymbol=s;
        this.setText(""+s);
        this.setEnabled(false);
    }

    public char getSymbol()
    {
        return mySymbol;
    }

    public void clear()
    {
        mySymbol = ' ';
        this.setText("");
    }

    public Tile(int x, int y)
    {
    	this.x = x;
    	this.y = y;
    }
    
    public int [] getCoordinate()
    {
    	return new int[]{x, y};
    	
    }
    

}