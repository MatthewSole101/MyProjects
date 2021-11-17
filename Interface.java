import java.awt.GridLayout;

import javax.swing.JPanel;

public class Interface extends JPanel
{
	private Tile[] myTiles = new Tile[9];
	public char myReturn = 'X';
	
	public Interface()
		
	{
		this.setLayout(new GridLayout (3,3));
		for(int i=0; i<myTiles.length; i++)
		{
			myTiles[i] = new Tile();
			this.add(myTiles[i]);
		}
	}
	
	public void reset()
	{
		for(int i=0; i<myTiles.length; i++)
		{
			myTiles[i].clear();
		}
	}
	
	public char getReturn()
	{
		return myReturn;
	}
	
	public char checkWinner()
	{
		return ' ';
	}
	
}
