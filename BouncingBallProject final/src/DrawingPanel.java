import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.*;
import java.util.ArrayList;


import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.Timer;

public class DrawingPanel extends JPanel implements ActionListener, KeyListener
{

    //	private Ball myBall;
    private Timer myTimer;
    private boolean isaddBall = false;
    private ArrayList<Ball> myBall = new ArrayList();
    //	private ArrayList<Ball>mySquare = new ArrayList();
    private ArrayList<GravBall>myGravBall = new ArrayList();
    private int countBall;
    private boolean isgravitygame = false;
    private int numball;







    public DrawingPanel()
    {
        int numballs = 1;

//		g2d.setRect()
//		JButton b = new JButton("Add");
//		b.setBounds(50,100,95,30);
        countBall = 10;
        addKeyListener(this);
        setFocusable(true);



        for(int i=0; i < countBall; i++)
        {
            myBall.add (new Ball());
            myBall.get(i).myxpos((int) Math.random()*100);
            myBall.get(i).myypos((int) Math.random()*100);
            myBall.get(i).myxspeed(1);
            myBall.get(i).myyspeed(1);
            myBall.get(i).mySize(15);
            myBall.get(i).myColor(Color.GREEN);

//			mySquare.add(new Ball());
//			mySquare.get(i).myxpos(-800);
//			mySquare.get(i).myypos(-300);

//			mySquare.get(i).mySize(20);
//			mySquare.get(i).myColor(Color.RED);

            myGravBall.add (new GravBall());
            myGravBall.get(i).mygravballxpos(-400);
            myGravBall.get(i).mygravballypos(-400);
            myGravBall.get(i).mygravballxspeed(1);
            myGravBall.get(i).mygravballyspeed(1);
            myGravBall.get(i).mygravballSize(15);
            myGravBall.get(i).mygravballColor(Color.BLUE);
            myGravBall.get(i).myceilingypos(0);


//						this.setVisible(false);

            this.setBackground(new Color(1, 1, 1, 10 ));



            myTimer = new Timer(10, this);
            myTimer.start();

//		JButton button = new JButton();
//		button.setBounds(200, 100, 100, 50);


        }


    }

//    public void numballs()
//    {
////        int numballs = 1;
//        int numball += 1;
//    }



    public  void addBall()
    {
//		(int) (Math.random()*100);


        myBall.add (new Ball());
        myBall.get(countBall).myxpos((int) (Math.random()*100));
        myBall.get(countBall).myypos((int) (Math.random()*100));
        myBall.get(countBall).myxspeed(1);
        myBall.get(countBall).myyspeed(1);
        myBall.get(countBall).mySize(15);
        myBall.get(countBall).myColor(Color.GREEN);


        countBall += 1;


    }

    public void minigame()
    {
        myBall = new ArrayList();

        for(int i=0; i < countBall; i++)
        {
//			mySquare.get(i).myxpos(100);
//			mySquare.get(i).myypos(100);
        }

//		g2d.drawOval
    }

//	public void moveup()
//
//	{
//		for(int i=0; i < 10 ; i++)
//		{
//			mySquare.get(i).myypos(-10);
////			System.out.println("hello world");
//		}
//	}


    public void gravgame()
    {
//		System.out.println("hello world");
        myBall = new ArrayList();

        for(int i=0; i < 10; i++)
        {
            myGravBall.get(i).mygravballxpos(100);
            myGravBall.get(i).mygravballypos(100);
        }
    }


//	public void movedown()
//	{
//		for(int i=0; i < 10; i++)
//		{
//			mySquare.get(i).myypos(+10);
//		}
//	}
//





    public static void prirnt()
    {
        System.out.println("sus");
    }




    public void paintComponent (Graphics g)
    {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D)g;

        if (myBall.size() != 0 )
        {
            for(int i=0; i < countBall; i++)
            {
                g2d.setColor(myBall.get(i).getmyColor());
                g2d.fillOval(myBall.get(i).getmyxpos(), myBall.get(i).getmyypos(), myBall.get(i).getmySize(), myBall.get(i).getmySize());
                g2d.setColor(Color.WHITE);
            }
        }
        if (myGravBall.size() != 0 )
        {
            for(int i=0; i < 10; i++)
            {
                g2d.setColor(Color.RED);
                g2d.fillOval(myGravBall.get(i).getmygravballxpos(), myGravBall.get(i).getmygravballypos(), myGravBall.get(i).getmygravballSize(), myGravBall.get(i).getmygravballSize());


            }

        }

    }





    public void actionPerformed(ActionEvent e)
    {
        if (myBall.size() != 0)
        {
            for(int i=0; i < myBall.size(); i++)
            {

                myBall.get(i).updatePosition(getWidth(), getHeight());


            }//
        }
        else if (myGravBall.size() != 0 )
        {
            for (int i=0; i < 10; i++)
            {
                myGravBall.get(i).updatePosition(getWidth(), getHeight());
            }
        }



        repaint();

    }
//		repaint(




    @Override
    public void keyTyped(KeyEvent e)
    {
        // TODO Auto-generated method stub
//		if (e.getKeyCode() == KeyEvent.VK_W)
//		{
//            System.out.println("up");
//            moveup();
//            repaint();
//		}
//
//		if (e.getKeyChar() == 's')
//		{
//            System.out.println("down");
//            movedown();
//            repaint();
//		}
    }



    @Override
    public void keyPressed(KeyEvent e)
    {
        // TODO Auto-generated method stub
//
//		switch(e.getKeyChar())
//		{
//			case 'w': player1.setLocation(player1.getX(), player1.getY()-1);
//
//		}



//
//			if (e.getKeyChar() == 'w')
//			{
//	            System.out.println("up");
//	            moveup();
//	            repaint();
//			}
//
//			if (e.getKeyChar() == 's')
//			{
//	            System.out.println("down");
//	            movedown();
//	            repaint();
//			}

    }



    @Override
    public void keyReleased(KeyEvent e) {
        // TODO Auto-generated method stub

    }






}



