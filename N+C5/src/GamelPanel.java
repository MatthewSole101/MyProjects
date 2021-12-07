import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.*;

import javax.swing.JLabel;
import javax.swing.JPanel;


public class GamelPanel extends JPanel implements ActionListener
{
    private Tile[][] myTiles = new Tile[3][3];//
    public char myReturn = 'X';
    JLabel mTL;


    public GamelPanel(JLabel tl)

    {
    	System.out.println("ughghgh");
    	this.mTL = tl;
        this.setLayout(new GridLayout (3,3));
        for(int y=0; y<myTiles.length; y++)
        {
   
            
            for (int x=0; x<myTiles[y].length; x++)
            {
                    myTiles[y][x] = new Tile(x, y);
                    this.add(myTiles[y] [x]);
                    myTiles[y] [x].addActionListener((ActionListener) this);
                    myTiles[y] [x].setFocusable(false);
                    
            }
        }
        
        

    }

    public void reset()
    {
        for(int y=0; y<myTiles.length; y++)
        {
           for (int x=0; x<myTiles[y].length; x++)
           {   
        	myTiles[y] [x].clear();
        
           }
        }
    }

    public char getReturn()
    {
        return myReturn;
    }

//    public char checkWinner(int[] coordinates)
//    {
////    	Tile t = myTiles[coordinates [0]] [coordinates [1]];
////    	int [] cw = new int [] {0, 0, 0, 0};//1st Hori 2nd verticle 3rd left diaginal, 4th right diaginal
//    	 
//        
//    	for(int y=0; y<myTiles.length; y++)
//        {
//           for (int x=0; x<myTiles[y].length; x++)
//           {   
//        	  if (myTiles[y][x].getSymbol() == myReturn)
//        	  {
//        		 if (y == t.getCoordinate()[1])
//        		 {
//        			 
//        		 }
//        	  }
//           } 
//        }
//    }
    
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
	   
//	   this.checkWinner(clicked.getCoordinate());
	   switchTurn();
   }

}