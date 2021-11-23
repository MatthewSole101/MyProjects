import java.awt.BorderLayout;
import java.awt.GridLayout;
import javax.swing.*;
import javax.swing.JPanel;
import java.awt.BorderLayout;

public class Interface extends JPanel
{
	JLabel myTurnLabel;
	GamelPanel gamepaanel;
	private Tile[] myTiles = new Tile[9];
    public char myReturn = 'X';
   
    
    public Interface()

    {
    	myTurnLabel = new JLabel();
    	gamepaanel = new GamelPanel(myTurnLabel);

        {
            this.setLayout(new BorderLayout());
            this.add(gamepaanel, BorderLayout.CENTER);
            
            myTurnLabel.setText("Current turn  "+myReturn);
            this.add(myTurnLabel, BorderLayout.NORTH);
            	
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