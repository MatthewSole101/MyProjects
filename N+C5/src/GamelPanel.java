import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.*;

import javax.swing.JLabel;
import javax.swing.JPanel;


public class GamelPanel extends JPanel implements ActionListener
{
    private Tile[] myTiles = new Tile[9];
    public char myReturn = 'X';
    JLabel mTL;


    public GamelPanel(JLabel tl)

    {
    	System.out.println("ughghgh");
    	this.mTL = tl;
        this.setLayout(new GridLayout (3,3));
        for(int i=0; i<myTiles.length; i++)
        {
            myTiles[i] = new Tile();
            this.add(myTiles[i]);
            myTiles[i].addActionListener((ActionListener) this);
            myTiles[i].setFocusable(false);
            
                                                                                                                                                                                                                                                                       
        
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
      return 'a'; //if(myTiles[i+0].getSymbol() != ' ' && myTiles[i+0].getSymbol() == myTiles[i+1] ! )
    }
    private void switchTurn()//switch what symbol shows on tiles once pressed
    {
    	if(myReturn == 'X')
    		myReturn = 'O';
    		//myTurnLabel.setText("Current turn  "+myReturn);
    	else                                                                                                  
    		myReturn = 'X';
    	 	//myTiles[i].setText("Current turn  "+myReturn);
    	mTL.setText("Current turn "+myReturn);
    }                                                                

   public void actionPerformed(ActionEvent a)
   {
	   Tile clicked = (Tile)a.getSource();
	   clicked.setSymbol(myReturn);
	   switchTurn();
   }

}