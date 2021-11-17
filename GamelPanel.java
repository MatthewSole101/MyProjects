import java.awt.GridLayout;

import javax.swing.JPanel;

public class GamelPanel extends JPanel
{
	private Tile[] myTiles = new Tile[9];
	public char myReturn = 'X';
	
	public GamelPanel()
		
	{
		this.setLayout(new GridLayout (3,3));
		for(int i=0; i<myTiles.length; i++)
		{
			myTiles[i] = new Tile();
			this.add(myTiles[1]);
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

