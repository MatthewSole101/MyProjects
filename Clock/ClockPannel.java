import java.awt.*;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;

public class ClockPannel extends JPanel implements ActionListener// implement actionlistener

{
	private JButton start;
	private Clock myclock = new Clock();
	private JLabel time = new JLabel(myclock.getTime());
	private JButton reset;
	private JButton stop;
	
	private Timer myTimer = new Timer(1, this);//as it is in milliseconds
	public ClockPannel()
	{
		myTimer.start();// starts timer
		
		this.setLayout(new GridLayout(2,2));
		
		JPanel buttonPanel = new JPanel();
		buttonPanel.setLayout(new GridLayout(1,3));
		
		
		time.setFont(new Font("Tahoma", Font.BOLD, 100));
		this.add(time, BorderLayout.CENTER);
		time.setHorizontalAlignment(SwingConstants.CENTER);//Overidding default alignment from the left as I put CENTER
		
		
		
		start = new JButton("Start");
		start.addActionListener(this);
		start.setBackground(Color.RED);
		buttonPanel.add(start);
		start.setFocusable(false);
		
		stop = new JButton("Stop");
		stop.addActionListener(this);
		stop.setBackground(Color.BLUE);
		buttonPanel.add(stop);
		stop.setFocusable(false);

		
		reset = new JButton("Reset");
		reset.addActionListener(this);
		reset.setBackground(Color.CYAN);
		buttonPanel.add(reset);
		reset.setFocusable(false);

		
		
		this.add(buttonPanel, BorderLayout.SOUTH);
		
		
		
	}//flow layout

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource() == start)
		{
			System.out.println("Welcome");
			//myclock.increment(1);
			myTimer.start();
			start.setBackground(Color.GRAY);
		}
		else if (e.getSource() == stop)
		{
			System.out.println("Clock has stopped");
			stop.setBackground(Color.GRAY);
			myTimer.stop();
		}
		else if (e.getSource() == reset)
		{
			start.setBackground(Color.RED);
			stop.setBackground(Color.BLUE);
			myTimer.stop();
			myclock.setTime(0,  0, 0, 0);


			
		}
		else if(e.getSource() == time );
		{
			myclock.increment(1);
			time.setText(myclock.getTime());
		}
	}
	
	
	
}