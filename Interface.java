import java.awt.BorderLayout;

import javax.swing.JPanel;

public class Interface extends JPanel
{
	private GamelPanel myGamePanel = new GamelPanel()
	
	public Interface() 
	{
		this.setLayout(new BorderLayout());
		this.add(myGamePanel, BorderLayout.CENTER);
	}
			
	
}
