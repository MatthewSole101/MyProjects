import java.awt.BorderLayout;
import java.awt.Color;
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
    	System.out.println("Welcome to naughts and crosses");
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
                    System.out.println("here");
                    
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
    
    public char checkWinner ()
    {
    	
	    if (myTiles[0][0].getSymbol() == 'X' | myTiles[0][0].getSymbol() == 'O'  )
	    {
		    	if (myTiles[0][0].getSymbol()== myTiles [0][1].getSymbol() &&  myTiles [0][2].getSymbol() == myTiles[0][0].getSymbol() )//row 1
		    	{
		    		
		    		System.out.println("top row winner: "+myTiles[0][0].getSymbol());
		    		return (myTiles[0][0].getSymbol());
		    	}
		    	
		    	if ( myTiles[0][0].getSymbol()== myTiles [1][0].getSymbol() &&  myTiles [2][0].getSymbol() == myTiles[0][0].getSymbol() )// row 3
		    	{
		    		
		    		System.out.println("Left column winner: "+myTiles[2][0].getSymbol());
		    		return (myTiles[0][0].getSymbol());
		    	}
	    
	    }
	    
	    if (myTiles[2][2].getSymbol() == 'X'|myTiles[2][2].getSymbol() == 'O' ) 
	    {
	    	if ( myTiles[2][0].getSymbol()== myTiles [2][1].getSymbol() &&  myTiles [2][2].getSymbol() == myTiles[2][0].getSymbol() )// row 3
	    	{
	    		
	    		System.out.println("Bottom row winner: "+myTiles[2][0].getSymbol());
	    		return (myTiles[2][0].getSymbol());
	    	
	    	}
	    	
	    	
	    	if ( myTiles[0][2].getSymbol()== myTiles [1][2].getSymbol() &&  myTiles [2][2].getSymbol() == myTiles[0][2].getSymbol() )// row 3
	    	{
	    		
	    		System.out.println("Right column winner: "+myTiles[0][2].getSymbol());
	    		return (myTiles[0][2].getSymbol());
	    	}
    	
	    }
	    
	    if (myTiles[1][1].getSymbol() == 'X'| myTiles[1][1].getSymbol() == 'O')
	    {
	    	if (myTiles[0][1].getSymbol() == myTiles[1][1].getSymbol() && myTiles[2][1].getSymbol() == myTiles[0][1].getSymbol() )
	    	{
	    		System.out.println("Top Middle row winner :" +myTiles[0][1].getSymbol());
	    		return(myTiles[0][1].getSymbol());
	    	
	    	}
	    	
		    if (myTiles[1][0].getSymbol()== myTiles [1][1].getSymbol() &&  myTiles [1][2].getSymbol() == myTiles[1][0].getSymbol() )//row 2
	    	{
	    		
	    		System.out.println("Middle row winner!!: "+myTiles[1][0].getSymbol());//Horisontal
	    		return (myTiles[1][0].getSymbol());
	    	)

			if (myTiles[0][2].getSymbol() == myTiles[1][1].getSymbol() && myTiles[2][0].getSymbol() == myTiles[0][2].getSymbol())
			{
				System.out.println("Middle row winner!!: "+myTiles[0][2].getSymbol());//Horisontal
	    		return (myTiles[0][2].getSymbol());

			}
	    }
	    	
	    
	    
	    
	    
	    
	    
	    
	    if (myTiles[1][0].getSymbol() != ' ' &&  myTiles[1][0].getSymbol()== myTiles [1][1].getSymbol() &&  myTiles [1][2].getSymbol() == myTiles[1][0].getSymbol() )//row 2
	    	{
	    		
	    		System.out.println("Middle row winner!!: "+myTiles[1][0].getSymbol());//Horisontal
	    		return (myTiles[1][0].getSymbol());
	    	}
	    	
	    	
	    	if (myTiles[0][2].getSymbol() != ' ' &&  myTiles[0][2].getSymbol()== myTiles [1][2].getSymbol() &&  myTiles [2][2].getSymbol() == myTiles[0][2].getSymbol() )// row 3
	    	{
	    		
	    		System.out.println("Right column winner: "+myTiles[2][0].getSymbol());
	    		return (myTiles[2][0].getSymbol());
	    	}
    	
    	
    	
    	
    	
    	return('b');
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
	   clicked.getCoordinate(); 
	   int [] Cd = clicked.getCoordinate();
	   
	   clicked.setBackground(Color.BLUE);
 	   
	   this.checkWinner();
	   switchTurn();
   }

}