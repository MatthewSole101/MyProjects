import javax.swing.JButton;

public class Tile extends JButton
{
	private char mySymbol;
	private String setText;
	
	public void setSymbol(char s)
	{
		mySymbol=s;
		this.setText =(""+s);
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
	
	
	
}