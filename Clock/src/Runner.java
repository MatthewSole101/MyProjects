import javax.swing.JFrame;
import java.awt.Color;
public class Runner
{

	public static void main(String[] args)
	{
		// TODO Auto-generated method stub
		JFrame window = new JFrame();
		ClockPannel clock = new ClockPannel();
		window.setContentPane(clock);
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		window.setTitle("Clock");
		window.setSize(400,300);
		window.setVisible(true);
		window.setBackground(Color.darkGray);
	
		
	}
	

}
 