import java.awt.BorderLayout;
import java.awt.GridLayout;
import javax.swing.*;
import javax.swing.JPanel;
import java.awt.BorderLayout;

public class Interface extends JPanel
{
	JLabel myTurnLabel;
	GamelPanel gamepaanel;
	//private woah w1 = new woah
    public char myReturn = 'X';
    private JTabbedPane nc;
   
    
    public Interface()

    {
    	myTurnLabel = new JLabel();
    	gamepaanel = new GamelPanel(myTurnLabel);

        {
            this.setLayout(new BorderLayout());
            this.add(gamepaanel, BorderLayout.CENTER);
            
            myTurnLabel.setText("Current turn  "+myReturn);
            this.add(myTurnLabel, BorderLayout.NORTH);
            
            
           // nc = new JTabbedPane(JTabbedPane.TOP, JTabbedPane.WRAP_TAB_LAYOUT);
           // nc.addTab("Richard Tomblin", w1);
            	
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