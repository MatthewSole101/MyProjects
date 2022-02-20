import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;



public class Interface extends JFrame implements ActionListener
{
    DrawingPanel dr = new DrawingPanel(); // made an instance of it interface so can get any method;
    JButton button = new JButton();
    JButton buttongame = new JButton();
    JButton antigrav = new JButton();
    JLabel gamelabel;
    JLabel currentballs = new JLabel();
    private int numball;

    boolean isUp;


    public Interface()
    {
        int numball = 1;

        this.setLayout(new BorderLayout());
        this.add(dr, BorderLayout.CENTER);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(400,300);
        this.setVisible(true);
        this.setBackground(Color.black);
//	    this.addKeyListener(this);

        //make a panel for the buttons
        JPanel buttonPanel = new JPanel(new GridLayout(1,3));
        button.setText("Add");
        buttonPanel.add(button);
        button.setBounds(000, 000, 400, 50);
        button.addActionListener((ActionListener) this);
        button.setFocusable(false);

        buttongame.setText("Mini Game");
        buttongame.setBounds(100, 200, 400, 50);
        buttongame.addActionListener(this);
        buttongame.setFocusable(false);
        buttonPanel.add(buttongame);

        antigrav.setText("Anti Gravity");
        buttonPanel.add(antigrav);
        antigrav.setBounds(150, 200, 400, 50);
        antigrav.addActionListener(this);
        antigrav.setFocusable(false);

        currentballs.setText("The number of balls are: " + numball );

        //add buttonPanel to this panel
        this.add(buttonPanel, BorderLayout.NORTH);
        this.add(currentballs, BorderLayout.SOUTH );

//		gamelabel = new JLabel();
//		gamelabel.setBounds(0, 0, 100, 100);
//		gamelabel.setBackground(Color.RED);
//		gamelabel.setOpaque(true);





    }

    public void ballgame()
    {
        numball +=1;
        currentballs.setText("The number of balls are: " + numball);

    }

    public void actionPerformed(ActionEvent e)
    {

        if(e.getSource() ==  button)
        {

            dr.addBall();
            ballgame();

        }

        if(e.getSource() == buttongame)
        {
            dr.minigame();
        }

        if(e.getSource() == antigrav)
        {
            System.out.println("hello");
            dr.gravgame();
        }
    }






}
