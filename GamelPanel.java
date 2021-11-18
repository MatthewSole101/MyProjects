import java.awt.GridLayout;
import java.awt.event.*;
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
            myTiles[1].addActionListener((ActionListener) this);
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
    private void switchTurn()//switch what symbol shows on tiles once pressed
    {
    	if(myReturn == 'X')
    		myReturn = 'O';
    	else 
    		myReturn = 'X';
    }

   public void actionPerformed(ActionEvent a)
   {
	   Tile clicked = (Tile)a.getSource();
	   clicked.setSymbol(myReturn);
	   switchTurn();
   }

}